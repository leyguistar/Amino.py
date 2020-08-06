import json
import base64
import ffmpeg
import requests
from time import timezone
from time import time as timestamp
from locale import getdefaultlocale as locale
from typing import BinaryIO

from .lib.util import exceptions, headers, device, objects
from .socket import Callbacks, SocketHandler

device = device.DeviceGenerator()
clientId = None

class Client:
    def __init__(self, callback=Callbacks, socket_trace=False):
        self.api = "https://service.narvii.com/api/v1"
        self.authenticated = False
        self.configured = False
        self.user_agent = device.user_agent
        self.device_id = device.device_id
        self.device_id_sig = device.device_id_sig
        self.socket = SocketHandler(self, socket_trace=socket_trace)
        self.callbacks = callback(self)

        self.json = None
        self.sid = None
        self.userId = None
        self.account = None
        self.profile = None

        self.client_config()

    def login(self, email: str, password: str):
        data = json.dumps({
            "email": email,
            "v": 2,
            "secret": f"0 {password}",
            "deviceID": self.device_id,
            "clientType": 100,
            "action": "normal",
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/auth/login", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 200: raise exceptions.InvalidAccountOrPassword
            if response["api:statuscode"] == 213: raise exceptions.InvalidEmail
            if response["api:statuscode"] == 214: raise exceptions.InvalidPassword
            if response["api:statuscode"] == 246: raise exceptions.AccountDeleted
            if response["api:statuscode"] == 270: raise exceptions.VerificationRequired
            else: return response

        else:
            self.authenticated = True
            self.json = json.loads(response.text)
            self.sid = self.json["sid"]
            self.userId = self.json["auid"]
            self.account = objects.userProfile(self.json["account"]).userProfile
            self.profile = objects.userProfile(self.json["userProfile"]).userProfile
            headers.sid = self.sid
            self.socket.start()
            return response.status_code

    def register(self, nickname: str, email: str, password: str, deviceId: str = device.device_id):
        data = json.dumps({
            "secret": f"0 {password}",
            "deviceID": deviceId,
            "email": email,
            "clientType": 100,
            "nickname": nickname,
            "latitude": 0,
            "longitude": 0,
            "address": None,
            "clientCallbackURL": "narviiapp://relogin",
            "type": 1,
            "identity": email,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/auth/register", data=data, headers=headers.Headers(data=data).headers)
        if response.status_code == 200: return response.status_code
        else: return json.loads(response.text)

    def restore(self, email: str, password: str):
        data = json.dumps({
            "secret": f"0 {password}",
            "deviceID": device.device_id,
            "email": email,
            "timestamp": int(timestamp() * 1000)

        })

        response = requests.post(f"{self.api}/g/s/account/delete-request/cancel", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 200: raise exceptions.InvalidAccountOrPassword
            if response["api:statuscode"] == 213: raise exceptions.InvalidEmail
            if response["api:statuscode"] == 214: raise exceptions.InvalidPassword
            if response["api:statuscode"] == 270: raise exceptions.VerificationRequired
            if response["api:statuscode"] == 2800: raise exceptions.AccountAlreadyRestored
            else: return response

        else: return response.status_code

    #@property
    def logout(self):
        data = json.dumps({
            "deviceID": self.device_id,
            "clientType": 100,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/auth/logout", headers=headers.Headers(data=data).headers, data=data)
        self.authenticated = False
        self.socket.close()
        return response.status_code

    def configure(self, age: int, gender: str):
        """
        :param age: Age of Account (Min: 13)
        :param gender: 'Male', 'Female' or 'Non-Binary'
        :return:
        """

        if gender.lower() == "male": gender = 1
        elif gender.lower() == "female": gender = 2
        elif gender.lower() == "non-binary": gender = 255

        data = json.dumps({
            "age": age,
            "gender": gender,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/persona/profile/basic", data=data, headers=headers.Headers(data=data).headers)
        if response.status_code == 200: return response.status_code
        else: return json.loads(response.text)

    def verify(self, email: str):
        data = json.dumps({
            "identity": email,
            "type": 1,
            "deviceID": device.device_id
        })

        response = requests.post(f"{self.api}/g/s/auth/request-security-validation", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 213: raise exceptions.InvalidEmail
            if response["api:statuscode"] == 219: raise exceptions.TooManyRequests
            else: return response

        else: return response.status_code

    def client_config(self):
        data = json.dumps({
            "deviceID": self.device_id,
            "bundleID": "com.narvii.amino.master",
            "clientType": 100,
            "timezone": -timezone // 1000,
            "systemPushEnabled": True,
            "locale": locale()[0],
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/device", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code == 200: self.configured = True

    def upload_media(self, file: BinaryIO = None,data=None):
        if(data==None):
            data = file.read()
        response = requests.post(f"{self.api}/g/s/media/upload", data=data, headers=headers.Headers(type=f"image/jpg", data=data).headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 300: raise exceptions.BadImage
            else: return response

        else: return json.loads(response.text)["mediaValue"]

    def handle_socket_message(self, data):
        return self.callbacks.resolve(data)

    @property
    def sub_clients(self, start: int = 0, size: int = 25):
        if not self.authenticated: raise exceptions.NotLoggedIn
        response = requests.get(f"{self.api}/g/s/community/joined?v=1&start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.communityList(json.loads(response.text)["communityList"]).communityList

    def get_user_info(self, userId: str,save=True):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}", headers=headers.Headers().headers)
        if(save):
            print("Writting user info")
            print('user_' + userId +  '.json')
            with open('user_' + userId +  '.json', 'w') as handler:
                handler.write(response.text)

        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 100: raise exceptions.UnsupportedService
            elif response["api:statuscode"] == 225: raise exceptions.UserUnavailable
            else: return response

        else: return objects.userProfile(json.loads(response.text)["userProfile"]).userProfile

    def get_chat_threads(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/chat/thread?type=joined-me&start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        return objects.threadList(json.loads(response.text)["threadList"]).threadList

    def get_chat_thread(self, chatId: str):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        return objects.thread(json.loads(response.text)["thread"]).thread

    def get_chat_messages(self, chatId: str, size: int = 25):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}/message?v=2&pagingType=t&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        return objects.messageList(json.loads(response.text)["messageList"]).messageList

    def get_message_info(self, chatId: str, messageId: str):
        response = requests.get(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        return objects.message(json.loads(response.text)["message"]).message

    def get_community_info(self, comId: str):
        response = requests.get(f"{self.api}/g/s-x{comId}/community/info?withInfluencerList=1&withTopicList=true&influencerListOrderStrategy=fansCount", headers=headers.Headers().headers)
        with open('comunnity.json', 'w') as handler:
                handler.write(response.text)
        
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 801: raise exceptions.CommunityNoLongerExists
            elif response["api:statuscode"] == 833: raise exceptions.CommunityDeleted
            else: return response


        else: return objects.community(json.loads(response.text)["community"]).community

    def get_user_following(self, userId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/joined?start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 100: raise exceptions.UnsupportedService
            elif response["api:statuscode"] == 225: raise exceptions.UserUnavailable
            else: return response

        else: return objects.userProfileList(json.loads(response.text)["userProfileList"]).userProfileList

    def get_user_followers(self, userId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/member?start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 100: raise exceptions.UnsupportedService
            elif response["api:statuscode"] == 225: raise exceptions.UserUnavailable
            else: return response

        else: return objects.userProfileList(json.loads(response.text)["userProfileList"]).userProfileList

    def get_user_visitors(self, userId: str, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/visitors?start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 100: raise exceptions.UnsupportedService
            elif response["api:statuscode"] == 225: raise exceptions.UserUnavailable
            else: return response

        else: return objects.visitorsList(json.loads(response.text)).visitorsList

    @property
    def get_blocked_users(self, start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/block?start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.userProfileList(json.loads(response.text)["userProfileList"]).userProfileList

    @property
    def get_blocker_users(self):
        response = requests.get(f"{self.api}/g/s/block/full-list", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["blockerUidList"]

    def get_wall_comments(self, userId: str, sorting: str = "newest", start: int = 0, size: int = 25):
        if sorting == "newest": sorting = "newest"
        elif sorting == "oldest": sorting = "oldest"
        elif sorting == "top": sorting = "vote"
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/g-comment?sort={sorting}&start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.commentList(json.loads(response.text)["commentList"]).commentList

    def flag(self, reason: str, flagType: int, userId: str = None, blogId: str = None, asGuest: bool = False):
        data = {
            "flagType": flagType,
            "message": reason,
            "timestamp": int(timestamp() * 1000)
        }

        if userId:
            data["objectId"] = userId
            data["objectType"] = 0

        if userId:
            data["objectId"] = blogId
            data["objectType"] = 1

        if asGuest: flg = "g-flag"
        else: flg = "flag"

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/{flg}", data=data, headers=headers.Headers(data=data).headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def send_message(self, chatId: str, message: str = None, messageType: int = 0, filePath = None, replyTo: str = None, mentionUserIds: list = None, stickerId: str = None, embedId: str = None, embedType: int = None, embedLink: str = None, embedTitle: str = None, embedContent: str = None, embedImage: BinaryIO = None):
        audio_types = ["mp3", "aac", "wav", "ogg", "mkv"]
        image_types = ["png", "jpg", "jpeg", "gif"]
        mentions = []
        if mentionUserIds:
            for mention_uid in mentionUserIds:
                mentions.append({"uid": mention_uid})

        if embedImage:
            embedImage = [[100, self.upload_media(embedImage), None]]

        data = {
            "type": messageType,
            "content": message,
            "clientRefId": int(timestamp() / 10 % 1000000000),
            "attachedObject": {
                "objectId": embedId,
                "objectType": embedType,
                "link": embedLink,
                "title": embedTitle,
                "content": embedContent,
                "mediaList": embedImage
            },
            "extensions": {"mentionedArray": mentions},
            "timestamp": int(timestamp() * 1000)
        }

        if replyTo: data["replyMessageId"] = replyTo

        if stickerId:
            data["content"] = None
            data["stickerId"] = stickerId
            data["type"] = 3

        if filePath:
            data["content"] = None

            with open(filePath, "rb") as file:
                if filePath.split('.')[-1] in audio_types:
                    if filePath.split('.')[-1] != "aac":
                        process = (ffmpeg
                                   .input(filePath)
                                   .output(f"{filePath}.aac", audio_bitrate="320k")
                                   .overwrite_output()
                                   .run_async(pipe_stdout=True)
                                   )

                        process.wait()
                        file = open(f"{filePath}.aac", "rb")

                    data["type"] = 2
                    data["mediaType"] = 110

                elif filePath.split('.')[-1] in image_types:
                    data["mediaType"] = 100
                    data["mediaUploadValueContentType"] = f"image/{filePath.split('.')[-1]}"
                    data["mediaUhqEnabled"] = True

                else: raise exceptions.UnsupportedFileExtension

                data["mediaUploadValue"] = base64.b64encode(file.read()).decode()

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/message", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def delete_message(self, chatId: str, messageId: str, asStaff: bool = False, reason: str = None):
        data = {
            "adminOpName": 102,
            "adminOpNote": {"content": reason},
            "timestamp": int(timestamp() * 1000)
        }

        data = json.dumps(data)
        if not asStaff: response = requests.delete(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}", headers=headers.Headers().headers)
        else: response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/message/{messageId}/admin", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def mark_as_read(self, chatId: str, messageId: str):
        data = json.dumps({
            "messageId": messageId,
            "timestamp": int(timestamp() * 1000)
        })
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/mark-as-read", headers=headers.Headers().headers, data=data)

        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def edit_chat(self, chatId: str, doNotDisturb: bool = None, pinChat: bool = None, title: str = None, icon: str = None, backgroundImage: str = None, content: str = None, announcement: str = None, coHosts: list = None, keywords: list = None, pinAnnouncement: bool = None, publishToGlobal: bool = None, canTip: bool = None, viewOnly: bool = None, canInvite: bool = None, fansOnly: bool = None):
        data = {
            "type": 1,
            "timestamp": int(timestamp() * 1000)
        }

        if title: data["title"] = title
        if content: data["content"] = content
        if icon: data["icon"] = icon
        if keywords: data["keywords"] = keywords
        if announcement: data["extensions"] = {"announcement": announcement}
        if pinAnnouncement: data["extensions"] = {"pinAnnouncement": pinAnnouncement}
        if fansOnly: data["extensions"] = {"fansOnly": fansOnly}

        if publishToGlobal: data["publishToGlobal"] = 0
        if not publishToGlobal: data["publishToGlobal"] = 1

        if doNotDisturb:
            data = json.dumps({"alertOption": 2, "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.profile.id}/alert", data=data, headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if not doNotDisturb:
            data = json.dumps({"alertOption": 1, "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.profile.id}/alert", data=data, headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if pinChat:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/pin", headers=headers.Headers().headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if not pinChat:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/unpin", headers=headers.Headers().headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if backgroundImage:
            data = json.dumps({"media": [100, backgroundImage, None], "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/member/{self.profile.id}/background", data=data, headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if coHosts:
            data = json.dumps({"uidList": coHosts, "timestamp": int(timestamp() * 1000)})
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/co-host", data=data, headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if not viewOnly:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/view-only/disable", headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if viewOnly:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/view-only/enable", headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if not canInvite:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/members-can-invite/disable", headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if canInvite:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/members-can-invite/enable", headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if not canTip:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/tipping-perm-status/disable", headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        if canTip:
            response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}/tipping-perm-status/enable", headers=headers.Headers(data=data).headers)
            if response.status_code != 200: return json.loads(response.text)
            else: pass

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/chat/thread/{chatId}", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def visit(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}?action=visit", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def follow(self, userId: str):
        response = requests.post(f"{self.api}/g/s/user-profile/{userId}/member", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unfollow(self, userId: str):
        response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/member/{self.userId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def block(self, userId: str):
        response = requests.post(f"{self.api}/g/s/block/{userId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unblock(self, userId: str):
        response = requests.delete(f"{self.api}/g/s/block/{userId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def join_community(self, comId: str, invitationId: str = None):
        data = {"timestamp": int(timestamp() * 1000)}
        if invitationId: data["invitationId"] = invitationId

        data = json.dumps(data)
        response = requests.post(f"{self.api}/x{comId}/s/community/join", data=data, headers=headers.Headers(data=data).headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 229: raise exceptions.YouAreBanned
            else: return response
        else: return response.status_code

    def request_join_community(self, comId: str, message: str = None):
        data = json.dumps({"message": message, "timestamp": int(timestamp() * 1000)})
        response = requests.post(f"{self.api}/x{comId}/s/community/membership-request", data=data, headers=headers.Headers(data=data).headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 229: raise exceptions.YouAreBanned
            if response["api:statuscode"] == 2001: raise exceptions.AlreadyRequested
            else: return response
        else: return response.status_code

    def leave_community(self, comId: str):
        response = requests.post(f"{self.api}/x{comId}/s/community/leave", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def flag_community(self, comId: str, reason: str, flagType: int, isGuest: bool = False):
        data = json.dumps({
            "objectId": comId,
            "objectType": 16,
            "flagType": flagType,
            "message": reason,
            "timestamp": int(timestamp() * 1000)
        })

        if isGuest: flg = "g-flag"
        else: flg = "flag"

        response = requests.post(f"{self.api}/x{comId}/s/{flg}", data=data, headers=headers.Headers(data=data).headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def edit_profile(self, nickname: str = None, content: str = None, icon: str = None, backgroundColor: str = None, backgroundImage: str = None):
        data = {
            "address": None,
            "latitude": 0,
            "longitude": 0,
            "mediaList": None,
            "eventSource": "UserProfileView",
            "timestamp": int(timestamp() * 1000)
        }

        if nickname: data["nickname"] = nickname
        if icon: data["icon"] = icon
        if content: data["content"] = content
        if backgroundColor: data["extensions"] = {"style": {"backgroundColor": backgroundColor}}
        if backgroundImage: data["extensions"] = {"style": {"backgroundMediaList": [[100, backgroundImage, None, None, None]]}}

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def set_privacy_status(self, isAnonymous: bool = False, getNotifications: bool = False):
        data = {"timestamp": int(timestamp() * 1000)}

        if not isAnonymous: data["privacyMode"] = 1
        if isAnonymous: data["privacyMode"] = 2
        if not getNotifications: data["notificationStatus"] = 2
        if getNotifications: data["privacyMode"] = 1

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/account/visit-settings", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def set_amino_id(self, aminoId: str):
        data = json.dumps({"aminoId": aminoId, "timestamp": int(timestamp() * 1000)})
        response = requests.post(f"{self.api}/g/s/account/change-amino-id", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    @property
    def get_linked_communities(self):
        response = requests.get(f"{self.api}/g/s/user-profile/{self.userId}/linked-community", headers=headers.Headers().headers)
        return json.loads(response.text)

    def reorder_linked_community(self, comIds: list):
        data = json.dumps({"ndcIds": comIds, "timestamp": int(timestamp() * 1000)})
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}/linked-community/reorder", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def add_linked_community(self, comId: str):
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}/linked-community/{comId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def remove_linked_community(self, comId: str):
        response = requests.delete(f"{self.api}/g/s/user-profile/{self.userId}/linked-community/{comId}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def comment(self, message: str, userId: str = None, blogId: str = None, wikiId: str = None, replyTo: str = None):
        data = {
            "content": message,
            "stickerId": None,
            "type": 0,
            "timestamp": int(timestamp() * 1000)
        }

        if replyTo: data["respondTo"] = replyTo

        if userId:
            data["eventSource"] = "UserProfileView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/user-profile/{userId}/g-comment", headers=headers.Headers(data=data).headers, data=data)

        elif blogId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/blog/{blogId}/g-comment", headers=headers.Headers(data=data).headers, data=data)

        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/item/{wikiId}/g-comment", headers=headers.Headers(data=data).headers, data=data)

        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def delete_comment(self, commentId: str, userId: str = None, blogId: str = None, wikiId: str = None):
        if userId: response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/g-comment/{commentId}", headers=headers.Headers().headers)
        elif blogId: response = requests.delete(f"{self.api}/g/s/blog/{blogId}/g-comment/{commentId}", headers=headers.Headers().headers)
        elif wikiId: response = requests.delete(f"{self.api}/g/s/item/{wikiId}/g-comment/{commentId}", headers=headers.Headers().headers)

        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def like_blog(self, blogId: str = None, wikiId: str = None):
        data = {
            "value": 4,
            "timestamp": int(timestamp() * 1000)
        }

        if blogId:
            data["eventSource"] = "UserProfileView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/blog/{blogId}/g-vote?cv=1.2", headers=headers.Headers(data=data).headers, data=data)

        elif wikiId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/item/{wikiId}/g-vote?cv=1.2", headers=headers.Headers(data=data).headers, data=data)

        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def like_blogs(self, blogIds: list):
        data = json.dumps({
            "value": 4,
            "targetIdList": blogIds,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/feed/g-vote", headers=headers.Headers(data=data).headers, data=data)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unlike_blog(self, blogId: str = None, wikiId: str = None):
        if blogId: response = requests.delete(f"{self.api}/g/s/blog/{blogId}/g-vote?eventSource=UserProfileView", headers=headers.Headers().headers)
        elif wikiId: response = requests.delete(f"{self.api}/g/s/item/{wikiId}/g-vote?eventSource=PostDetailView", headers=headers.Headers().headers)
        else: raise exceptions.SpecifyType

        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def like_comment(self, commentId: str, userId: str = None, blogId: str = None):
        data = {
            "value": 4,
            "timestamp": int(timestamp() * 1000)
        }

        if blogId:
            data["eventSource"] = "PostDetailView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/blog/{blogId}/comment/{commentId}/g-vote?cv=1.2&value=1", headers=headers.Headers(data=data).headers, data=data)
        elif userId:
            data["eventSource"] = "UserProfileView"
            data = json.dumps(data)
            response = requests.post(f"{self.api}/g/s/user-profile/{userId}/comment/{commentId}/g-vote?cv=1.2&value=1", headers=headers.Headers(data=data).headers, data=data)

        else: raise exceptions.SpecifyType
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unlike_comment(self, blogId: str, commentId: str):
        response = requests.delete(f"{self.api}/g/s/blog/{blogId}/comment/{commentId}/g-vote?eventSource=PostDetailView", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    @property
    def get_membership_info(self):
        response = requests.get(f"{self.api}/g/s/membership?force=true", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.membership(json.loads(response.text)).membership

    def get_ta_announcements(self, language: str = "en", start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/announcement?language={language}&start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.blogList(json.loads(response.text)["blogList"]).blogList

    @property
    def get_wallet_info(self):
        response = requests.get(f"{self.api}/g/s/wallet", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.walletInfo(json.loads(response.text)["wallet"]).walletInfo

    def get_from_code(self, code: str,save=False):
        response = requests.get(f"{self.api}/g/s/link-resolution?q={code}", headers=headers.Headers().headers)
        if(save):
            with open('logs/from_code.json','w') as h:
                h.write(response.text)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 107: raise exceptions.UnexistentData
            else: return response

        else: return objects.fromCode(json.loads(response.text)["linkInfoV2"]).fromCode

    @property
    def punishmentTypes(self):
        punishments = ["0 - Bullying",
                       "1 - Inappropriate Content"
                       "2 - Spam",
                       "3 - Art Theft",
                       "4 - Off-Topic",
                       "5 - Trolling",
                       "100 - Sexually Explicit",
                       "101 - Extreme Violence",
                       "102 - Inappropriate Requests",
                       "106 - Violence, Graphic Content or Dangerous Activity",
                       "107 - Hate Speech & Bigotry",
                       "108 - Self-Injury & Suicide",
                       "109 - Harassment & Trolling",
                       "110 - Nudity & Pornography",
                       "104, 105, 200 - Others"]

        return punishments
