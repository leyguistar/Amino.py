import requests
import json
from locale import getdefaultlocale as locale
from time import time as timestamp
from time import timezone
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

    @property
    def logout(self):
        data = json.dumps({
            "deviceID": self.device_id,
            "clientType": 100,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/auth/logout", headers=headers.Headers(data=data).headers, data=data)
        self.authenticated = False
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

    def upload_media(self, file: BinaryIO):
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
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.communityList(json.loads(response.text)["communityList"]).communityList

    def get_user_info(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}", headers=headers.Headers().headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 100: raise exceptions.UnsupportedService
            elif response["api:statuscode"] == 225: raise exceptions.UserUnavailable
            else: return response

        else: return objects.userProfile(json.loads(response.text)["userProfile"]).userProfile

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
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.userProfileList(json.loads(response.text)["userProfileList"]).userProfileList

    @property
    def get_blocker_users(self):
        response = requests.get(f"{self.api}/g/s/block/full-list", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return json.loads(response.text)["blockerUidList"]

    def get_wall_comments(self, userId: str, sorting: str = "newest", start: int = 0, size: int = 25):
        if sorting == "newest": sorting = "newest"
        elif sorting == "oldest": sorting = "oldest"
        elif sorting == "top": sorting = "vote"
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}/g-comment?sort={sorting}&start={start}&size={size}", headers=headers.Headers().headers)
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.commentList(json.loads(response.text)["commentList"]).commentList

    def visit(self, userId: str):
        response = requests.get(f"{self.api}/g/s/user-profile/{userId}?action=visit", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def follow(self, userId: str):
        response = requests.post(f"{self.api}/g/s/user-profile/{userId}/member", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unfollow(self, userId: str):
        response = requests.delete(f"{self.api}/g/s/user-profile/{userId}/member/{self.userId}", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def block(self, userId: str):
        response = requests.post(f"{self.api}/g/s/block/{userId}", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def unblock(self, userId: str):
        response = requests.delete(f"{self.api}/g/s/block/{userId}", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def join_community(self, comId: str, invitationId: str = None):
        data = {"timestamp": int(timestamp() * 1000)}
        if invitationId: data["invitationId"] = invitationId

        data = json.dumps(data)
        response = requests.post(f"{self.api}/x{comId}/s/community/join", data=data, headers=headers.Headers(data=data).headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def leave_community(self, comId: str):
        response = requests.post(f"{self.api}/x{comId}/s/community/leave", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def create_community(self, name: str, tagline: str, icon: BinaryIO, themeColor: str, joinType: str = 0):
        data = json.dumps({
            "icon": {
                "height": 512.0,
                "imageMatrix": [1.6875, 0.0, 108.0, 0.0, 1.6875, 497.0, 0.0, 0.0, 1.0],
                "path": self.upload_media(icon),
                "width": 512.0,
                "x": 0.0,
                "y": 0.0
            },
            "joinType": joinType,
            "name": name,
            "primaryLanguage": "en",
            "tagline": tagline,
            "templateId": 9,
            "themeColor": themeColor,
            "timestamp": int(timestamp() * 1000)
        })

        response = requests.post(f"{self.api}/g/s/community", headers=headers.Headers(data=data).headers, data=data)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 805: raise exceptions.CommunityNameAlreadyTaken
            if response["api:statuscode"] == 2800: raise exceptions.AccountAlreadyRestored
            else: return response

        else: return response.status_code

    def edit_profile(self, nickname: str = None, content: str = None, icon: str = None, backgroundImage: str = None):
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
        if backgroundImage: data["extensions"] = {"style": {"backgroundMediaList": [[100, backgroundImage, None, None, None]]}}

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/user-profile/{self.userId}", headers=headers.Headers(data=data).headers, data=data)
        if self.authenticated is False: raise exceptions.NotLoggedIn
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
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    def set_amino_id(self, aminoId: str):
        data = {
            "aminoId": aminoId,
            "timestamp": int(timestamp() * 1000)
        }

        data = json.dumps(data)
        response = requests.post(f"{self.api}/g/s/account/change-amino-id", headers=headers.Headers(data=data).headers, data=data)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return response.status_code

    @property
    def get_membership_info(self):
        response = requests.get(f"{self.api}/g/s/membership?force=true", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.membership(json.loads(response.text)).membership

    def get_ta_announcements(self, language: str = "en", start: int = 0, size: int = 25):
        response = requests.get(f"{self.api}/g/s/announcement?language={language}&start={start}&size={size}", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.blogList(json.loads(response.text)["blogList"]).blogList

    @property
    def get_wallet_info(self):
        response = requests.get(f"{self.api}/g/s/wallet", headers=headers.Headers().headers)
        if self.authenticated is False: raise exceptions.NotLoggedIn
        if response.status_code != 200: return json.loads(response.text)
        else: return objects.walletInfo(json.loads(response.text)["wallet"]).walletInfo

    def get_from_code(self, code: str):
        response = requests.get(f"{self.api}/g/s/link-resolution?q={code}", headers=headers.Headers().headers)
        if response.status_code != 200:
            response = json.loads(response.text)
            if response["api:statuscode"] == 107: raise exceptions.UnexistentData
            else: return response

        else: return objects.fromCode(json.loads(response.text)["linkInfoV2"]).fromCode

    @property
    def punishmentTypes(self):
        punishments = ["0 - Bullying",
                       "2 - Spam",
                       "4 - Off-Topic",
                       "100 - Sexually Explicit",
                       "101 - Extreme Violence",
                       "102 - Inappropriate Requests",
                       "106 - Violence, Graphic Content or Dangerous Activity",
                       "107 - Hate Speech & Bigotry",
                       "108 - Self-Injury & Suicide",
                       "109 - Harassment & Trolling",
                       "110 - Nudity & Pornography",
                       "200 - Other"]

        return punishments
