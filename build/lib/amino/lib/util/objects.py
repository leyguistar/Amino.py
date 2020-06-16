# You don't even know how long this shit took
from contextlib import suppress

class userProfile:
    def __init__(self, data):
        self.json = data
        self.defaultBubbleId = None
        self.email = None
        self.age = None
        self.gender = None
        self.race = None
        self.dateOfBirth = None
        self.securityLevel = None
        self.phoneNumber = None
        self.aminoIdEditable = None
        self.facebookId = None
        self.googleId = None
        self.activation = None
        self.avatarFrame = None
        self.avatarFrameId = None
        self.createdTime = None
        self.visitPrivacy = None
        self.storiesCount = None
        self.blogsCount = None
        self.extensions = None
        self.isMemberOfTeamAmino = None
        self.twitterId = None
        self.appleId = None
        self.aminoId = None
        self.role = None
        self.commentsCount = None
        self.followingCount = None
        self.content = None
        self.membershipStatus = None
        self.pushEnabled = None
        self.notificationSubscriptionStatus = None
        self.level = None
        self.isNicknameVerified = None
        self.mood = None
        self.followersCount = None
        self.postsCount = None
        self.reputation = None
        self.onlineStatus2 = None
        self.accountMembershipStatus = None
        self.isGlobal = None
        self.onlineStatus = None
        self.followingStatus = None
        self.modifiedTime = None
        self.itemsCount = None
        self.moodSticker = None
        self.visitorsCount = None
        self.status = None
        self.id = None
        self.icon = None
        self.nickname = None
        self.privilegeOfCommentOnUserProfile = None
        self.privilegeOfChatInviteRequest = None
        self.coverAnimation = None
        self.backgroundColor = None
        self.disabledStatus = None
        self.disabledLevel = None
        self.disabledTime = None
        self.staffInfo = None
        self.strikeCount = None
        self.lastWarningTime = None
        self.warningCount = None
        self.globalStrikeCount = None
        self.lastStrikeTime = None

    @property
    def userProfile(self):
        with suppress(KeyError, TypeError):
            self.nickname = self.json["nickname"]
            self.icon = self.json["icon"]
            self.id = self.json["uid"]
            self.status = self.json["status"]
            self.visitorsCount = self.json["visitorsCount"]
            self.moodSticker = self.json["moodSticker"]
            self.itemsCount = self.json["itemsCount"]
            self.modifiedTime = self.json["modifiedTime"]
            self.followingStatus = self.json["followingStatus"]
            self.onlineStatus = self.json["onlineStatus"]
            self.onlineStatus2 = self.json["settings"]["onlineStatus"]
            self.accountMembershipStatus = self.json["accountMembershipStatus"]
            self.isGlobal = self.json["isGlobal"]
            self.reputation = self.json["reputation"]
            self.postsCount = self.json["postsCount"]
            self.followersCount = self.json["membersCount"]
            self.isNicknameVerified = self.json["isNicknameVerified"]
            self.mood = self.json["mood"]
            self.level = self.json["level"]
            self.notificationSubscriptionStatus = self.json["notificationSubscriptionStatus"]
            self.pushEnabled = self.json["pushEnabled"]
            self.membershipStatus = self.json["membershipStatus"]
            self.content = self.json["content"]
            self.followingCount = self.json["joinedCount"]
            self.role = self.json["role"]
            self.commentsCount = self.json["commentsCount"]
            self.aminoId = self.json["aminoId"]
            self.createdTime = self.json["createdTime"]
            self.visitPrivacy = self.json["visitPrivacy"]
            self.storiesCount = self.json["storiesCount"]
            self.blogsCount = self.json["blogsCount"]
            self.extensions = self.json["extensions"]
            self.avatarFrame = self.json["avatarFrame"]
            self.avatarFrameId = self.json["avatarFrameId"]
            self.twitterId = self.json["twitterID"]
            self.appleId = self.json["appleID"]
            self.facebookId = self.json["facebookID"]
            self.googleId = self.json["googleID"]
            self.activation = self.json["activation"]
            self.securityLevel = self.json["securityLevel"]
            self.phoneNumber = self.json["phoneNumber"]
            self.aminoIdEditable = self.json["aminoIdEditable"]
            self.email = self.json["email"]
            self.age = self.json["age"]
            self.gender = self.json["gender"]
            self.race = self.json["race"]
            self.dateOfBirth = self.json["dateOfBirth"]
            self.staffInfo = self.json["adminInfo"]
            self.strikeCount = self.json["adminInfo"]["strikeCount"]
            self.lastWarningTime = self.json["adminInfo"]["lastWarningTime"]
            self.warningCount = self.json["adminInfo"]["warningCount"]
            self.globalStrikeCount = self.json["adminInfo"]["globalStrikeCount"]
            self.lastStrikeTime = self.json["adminInfo"]["lastStrikeTime"]
            self.coverAnimation = self.json["extensions"]["coverAnimation"]
            self.backgroundColor = self.json["extensions"]["style"]["coverAnimation"]
            self.privilegeOfCommentOnUserProfile = self.json["extensions"]["privilegeOfCommentOnUserProfile"]
            self.defaultBubbleId = self.json["extensions"]["defaultBubbleId"]
            self.privilegeOfChatInviteRequest = self.json["extensions"]["privilegeOfChatInviteRequest"]
            self.isMemberOfTeamAmino = self.json["extensions"]["isMemberOfTeamAmino"]
            self.disabledStatus = self.json["extensions"]["__disabledStatus__"]
            self.disabledLevel = self.json["extensions"]["__disabledLevel__"]
            self.disabledTime = self.json["extensions"]["__disabledTime__"]

        return self

class userProfileList:
    def __init__(self, data):
        self.json = data
        self.avatarFrame = []
        self.membershipStatus = []
        self.pushEnabled = []
        self.notificationSubscriptionStatus = []
        self.level = []
        self.mood = []
        self.isNicknameVerified = []
        self.mediaList = []
        self.postsCount = []
        self.reputation = []
        self.isGlobal = []
        self.accountMembershipStatus = []
        self.onlineStatus = []
        self.followingStatus = []
        self.icon = []
        self.status = []
        self.followersCount = []
        self.id = []
        self.itemsCount = []
        self.modifiedTime = []
        self.moodSticker = []
        self.blogsCount = []
        self.storiesCount = []
        self.extensions = []
        self.aminoId = []
        self.commentsCount = []
        self.role = []
        self.followingCount = []
        self.content = []
        self.createdTime = []
        self.avatarFrameId = []
        self.defaultBubbleId = []
        self.isMemberOfTeamAmino = []
        self.nickname = []
        self.privilegeOfCommentOnUserProfile = []
        self.privilegeOfChatInviteRequest = []
        self.coverAnimation = []
        self.backgroundColor = []
        self.backgroundColor = []
        self.staffInfo = []
        self.disabledStatus = []
        self.disabledLevel = []
        self.disabledTime = []
        self.strikeCount = []
        self.lastWarningTime = []
        self.warningCount = []
        self.globalStrikeCount = []
        self.lastStrikeTime = []

    @property
    def userProfileList(self):
        for x in self.json:
            try: self.nickname.append(x["nickname"])
            except (KeyError, TypeError): self.nickname.append(None)
            try: self.id.append(x["uid"])
            except (KeyError, TypeError): self.id.append(None)
            try: self.followersCount.append(x["membersCount"])
            except (KeyError, TypeError): self.followersCount.append(None)
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.icon.append(x["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.followingStatus.append(x["followingStatus"])
            except (KeyError, TypeError): self.followingStatus.append(None)
            try: self.onlineStatus.append(x["onlineStatus"])
            except (KeyError, TypeError): self.onlineStatus.append(None)
            try: self.accountMembershipStatus.append(x["accountMembershipStatus"])
            except (KeyError, TypeError): self.accountMembershipStatus.append(None)
            try: self.isGlobal.append(x["isGlobal"])
            except (KeyError, TypeError): self.isGlobal.append(None)
            try: self.reputation.append(x["reputation"])
            except (KeyError, TypeError): self.reputation.append(None)
            try: self.postsCount.append(x["postsCount"])
            except (KeyError, TypeError): self.postsCount.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.isNicknameVerified.append(x["isNicknameVerified"])
            except (KeyError, TypeError): self.isNicknameVerified.append(None)
            try: self.mood.append(x["mood"])
            except (KeyError, TypeError): self.mood.append(None)
            try: self.level.append(x["level"])
            except (KeyError, TypeError): self.level.append(None)
            try: self.notificationSubscriptionStatus.append(x["notificationSubscriptionStatus"])
            except (KeyError, TypeError): self.notificationSubscriptionStatus.append(None)
            try: self.pushEnabled.append(x["pushEnabled"])
            except (KeyError, TypeError): self.pushEnabled.append(None)
            try: self.membershipStatus.append(x["membershipStatus"])
            except (KeyError, TypeError): self.membershipStatus.append(None)
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.followingCount.append(x["joinedCount"])
            except (KeyError, TypeError): self.followingCount.append(None)
            try: self.role.append(x["role"])
            except (KeyError, TypeError): self.role.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except (KeyError, TypeError): self.commentsCount.append(None)
            try: self.aminoId.append(x["aminoId"])
            except (KeyError, TypeError): self.aminoId.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.storiesCount.append(x["storiesCount"])
            except (KeyError, TypeError): self.storiesCount.append(None)
            try: self.blogsCount.append(x["blogsCount"])
            except (KeyError, TypeError): self.blogsCount.append(None)
            try: self.moodSticker.append(x["moodSticker"])
            except (KeyError, TypeError): self.moodSticker.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.itemsCount.append(x["itemsCount"])
            except (KeyError, TypeError): self.itemsCount.append(None)
            try: self.avatarFrame.append(x["avatarFrame"])
            except (KeyError, TypeError): self.avatarFrame.append(None)
            try: self.avatarFrameId.append(x["avatarFrameId"])
            except (KeyError, TypeError): self.avatarFrameId.append(None)
            try: self.staffInfo.append(x["adminInfo"])
            except (KeyError, TypeError): self.staffInfo.append(None)
            try: self.strikeCount.append(x["adminInfo"]["strikeCount"])
            except (KeyError, TypeError): self.strikeCount.append(None)
            try: self.lastWarningTime.append(x["adminInfo"]["lastWarningTime"])
            except (KeyError, TypeError): self.lastWarningTime.append(None)
            try: self.warningCount.append(x["adminInfo"]["warningCount"])
            except (KeyError, TypeError): self.warningCount.append(None)
            try: self.globalStrikeCount.append(x["adminInfo"]["globalStrikeCount"])
            except (KeyError, TypeError): self.globalStrikeCount.append(None)
            try: self.lastStrikeTime.append(x["adminInfo"]["lastStrikeTime"])
            except (KeyError, TypeError): self.lastStrikeTime.append(None)
            try: self.disabledLevel.append(self.json["extensions"]["__disabledLevel__"])
            except (KeyError, TypeError): self.disabledLevel.append(None)
            try: self.disabledStatus.append(self.json["extensions"]["__disabledStatus__"])
            except (KeyError, TypeError): self.disabledStatus.append(None)
            try: self.disabledTime.append(self.json["extensions"]["__disabledTime__"])
            except (KeyError, TypeError): self.disabledTime.append(None)
            try: self.defaultBubbleId.append(self.json["extensions"]["defaultBubbleId"])
            except (KeyError, TypeError): self.defaultBubbleId.append(None)
            try: self.isMemberOfTeamAmino.append(self.json["extensions"]["isMemberOfTeamAmino"])
            except (KeyError, TypeError): self.isMemberOfTeamAmino.append(None)
            try: self.privilegeOfCommentOnUserProfile.append(self.json["extensions"]["privilegeOfCommentOnUserProfile"])
            except (KeyError, TypeError): self.privilegeOfCommentOnUserProfile.append(None)
            try: self.privilegeOfChatInviteRequest.append(self.json["extensions"]["privilegeOfChatInviteRequest"])
            except (KeyError, TypeError): self.privilegeOfChatInviteRequest.append(None)
            try: self.coverAnimation.append(self.json["extensions"]["coverAnimation"])
            except (KeyError, TypeError): self.coverAnimation.append(None)
            try: self.backgroundColor.append(self.json["extensions"]["style"]["backgroundColor"])
            except (KeyError, TypeError): self.backgroundColor.append(None)

        return self

class blogList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([blg["author"] for blg in data]).userProfileList
        self.createdTime = []
        self.globalVotesCount = []
        self.globalVotedValue = []
        self.keywords = []
        self.mediaList = []
        self.style = []
        self.totalQuizPlayCount = []
        self.title = []
        self.tipInfo = []
        self.tippersCount = []
        self.tippable = []
        self.tippedCoins = []
        self.contentRating = []
        self.needHidden = []
        self.guestVotesCount = []
        self.type = []
        self.status = []
        self.globalCommentsCount = []
        self.modifiedTime = []
        self.widgetDisplayInterval = []
        self.totalPollVoteCount = []
        self.blogId = []
        self.viewCount = []
        self.fansOnly = []
        self.backgroundColor = []
        self.votesCount = []
        self.endTime = []
        self.refObjectId = []
        self.refObject = []
        self.votedValue = []
        self.extensions = []
        self.commentsCount = []
        self.content = []
        self.featuredType = []
        self.shareUrl = []
        self.disabledTime = []

    @property
    def blogList(self):
        for x in self.json:
            try: self.globalVotesCount.append(x["globalVotesCount"])
            except (KeyError, TypeError): self.globalVotesCount.append(None)
            try: self.globalVotedValue.append(x["globalVotedValue"])
            except (KeyError, TypeError): self.globalVotedValue.append(None)
            try: self.keywords.append(x["keywords"])
            except (KeyError, TypeError): self.keywords.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.style.append(x["style"])
            except (KeyError, TypeError): self.style.append(None)
            try: self.totalQuizPlayCount.append(x["totalQuizPlayCount"])
            except (KeyError, TypeError): self.totalQuizPlayCount.append(None)
            try: self.title.append(x["title"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.tipInfo.append(x["tipInfo"])
            except (KeyError, TypeError): self.tipInfo.append(None)
            try: self.tippersCount.append(x["tipInfo"]["tippersCount"])
            except (KeyError, TypeError): self.tippersCount.append(None)
            try: self.tippable.append(x["tipInfo"]["tippable"])
            except (KeyError, TypeError): self.tippable.append(None)
            try: self.tippedCoins.append(x["tipInfo"]["tippedCoins"])
            except (KeyError, TypeError): self.tippedCoins.append(None)
            try: self.contentRating.append(x["contentRating"])
            except (KeyError, TypeError): self.contentRating.append(None)
            try: self.needHidden.append(x["needHidden"])
            except (KeyError, TypeError): self.needHidden.append(None)
            try: self.guestVotesCount.append(x["guestVotesCount"])
            except (KeyError, TypeError): self.guestVotesCount.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.globalCommentsCount.append(x["globalCommentsCount"])
            except (KeyError, TypeError): self.globalCommentsCount.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.widgetDisplayInterval.append(x["widgetDisplayInterval"])
            except (KeyError, TypeError): self.widgetDisplayInterval.append(None)
            try: self.totalPollVoteCount.append(x["totalPollVoteCount"])
            except (KeyError, TypeError): self.totalPollVoteCount.append(None)
            try: self.blogId.append(x["blogId"])
            except (KeyError, TypeError): self.blogId.append(None)
            try: self.viewCount.append(x["viewCount"])
            except (KeyError, TypeError): self.viewCount.append(None)
            try: self.fansOnly.append(x["extensions"]["fansOnly"])
            except (KeyError, TypeError): self.fansOnly.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except (KeyError, TypeError): self.backgroundColor.append(None)
            try: self.votesCount.append(x["votesCount"])
            except (KeyError, TypeError): self.votesCount.append(None)
            try: self.endTime.append(x["endTime"])
            except (KeyError, TypeError): self.endTime.append(None)
            try: self.refObjectId.append(x["refObjectId"])
            except (KeyError, TypeError): self.refObjectId.append(None)
            try: self.refObject.append(x["refObject"])
            except (KeyError, TypeError): self.refObject.append(None)
            try: self.votedValue.append(x["votedValue"])
            except (KeyError, TypeError): self.votedValue.append(None)
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.shareUrl.append(x["shareURLFullPath"])
            except (KeyError, TypeError): self.shareUrl.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except (KeyError, TypeError): self.commentsCount.append(None)
            try: self.featuredType.append(x["extensions"]["featuredType"])
            except (KeyError, TypeError): self.featuredType.append(None)
            try: self.disabledTime.append(x["extensions"]["__disabledTime__"])
            except (KeyError, TypeError): self.disabledTime.append(None)

        return self

class blogCategoryList:
    def __init__(self, data):
        self.json = data
        self.status = []
        self.modifiedTime = []
        self.icon = []
        self.style = []
        self.title = []
        self.content = []
        self.createdTime = []
        self.position = []
        self.type = []
        self.categoryId = []
        self.blogsCount = []

    @property
    def blogCategoryList(self):
        for x in self.json:
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.icon.append(x["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.style.append(x["style"])
            except (KeyError, TypeError): self.style.append(None)
            try: self.title.append(x["label"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.position.append(x["position"])
            except (KeyError, TypeError): self.position.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.categoryId.append(x["categoryId"])
            except (KeyError, TypeError): self.categoryId.append(None)
            try: self.blogsCount.append(x["blogsCount"])
            except (KeyError, TypeError): self.blogsCount.append(None)

        return self

class blog:
    def __init__(self, data):
        self.json = data
        self.createdTime = None
        self.globalVotesCount = None
        self.globalVotedValue = None
        self.keywords = None
        self.mediaList = None
        self.style = None
        self.totalQuizPlayCount = None
        self.title = None
        self.tipInfo = None
        self.tippersCount = None
        self.tippable = None
        self.tippedCoins = None
        self.contentRating = None
        self.needHidden = None
        self.guestVotesCount = None
        self.type = None
        self.status = None
        self.globalCommentsCount = None
        self.modifiedTime = None
        self.widgetDisplayInterval = None
        self.totalPollVoteCount = None
        self.blogId = None
        self.comId = None
        self.viewCount = None
        self.author = None
        self.fansOnly = None
        self.backgroundColor = None
        self.votesCount = None
        self.endTime = None
        self.refObjectId = None
        self.refObject = None
        self.votedValue = None
        self.extensions = None
        self.commentsCount = None
        self.content = None
        self.featuredType = None
        self.shareUrl = None
        self.disabledTime = None

    @property
    def blog(self):
        with suppress(KeyError, TypeError):
            self.globalVotesCount = self.json["globalVotesCount"]
            self.globalVotedValue = self.json["globalVotedValue"]
            self.keywords = self.json["keywords"]
            self.mediaList = self.json["mediaList"]
            self.style = self.json["style"]
            self.totalQuizPlayCount = self.json["totalQuizPlayCount"]
            self.title = self.json["title"]
            self.tipInfo = self.json["tipInfo"]
            self.tippersCount = self.json["tipInfo"]["tippersCount"]
            self.tippable = self.json["tipInfo"]["tippable"]
            self.tippedCoins = self.json["tipInfo"]["tippedCoins"]
            self.contentRating = self.json["contentRating"]
            self.needHidden = self.json["needHidden"]
            self.guestVotesCount = self.json["guestVotesCount"]
            self.type = self.json["type"]
            self.status = self.json["status"]
            self.globalCommentsCount = self.json["globalCommentsCount"]
            self.modifiedTime = self.json["modifiedTime"]
            self.widgetDisplayInterval = self.json["widgetDisplayInterval"]
            self.totalPollVoteCount = self.json["totalPollVoteCount"]
            self.blogId = self.json["blogId"]
            self.comId = self.json["ndcId"]
            self.viewCount = self.json["viewCount"]
            self.shareUrl = self.json["shareURLFullPath"]
            self.author = userProfile(self.json).userProfile
            self.fansOnly = self.json["extensions"]["fansOnly"]
            self.backgroundColor = self.json["extensions"]["style"]["backgroundColor"]
            self.votesCount = self.json["votesCount"]
            self.endTime = self.json["endTime"]
            self.refObjectId = self.json["refObjectId"]
            self.refObject = self.json["refObject"]
            self.votedValue = self.json["votedValue"]
            self.content = self.json["content"]
            self.createdTime = self.json["createdTime"]
            self.extensions = self.json["extensions"]
            self.commentsCount = self.json["commentsCount"]
            self.featuredType = self.json["extensions"]["featuredType"]
            self.disabledTime = self.json["extensions"]["__disabledTime__"]

        return self

class wiki:
    def __init__(self, data):
        self.json = data
        self.createdTime = None
        self.modifiedTime = None
        self.wikiId = None
        self.status = None
        self.style = None
        self.globalCommentsCount = None
        self.votedValue = None
        self.globalVotesCount = None
        self.globalVotedValue = None
        self.contentRating = None
        self.author = None
        self.title = None
        self.content = None
        self.keywords = None
        self.needHidden = None
        self.guestVotesCount = None
        self.extensions = None
        self.backgroundColor = None
        self.fansOnly = None
        self.knowledgeBase = None
        self.originalWikiId = None
        self.version = None
        self.contributors = None
        self.labels = None
        self.votesCount = None
        self.comId = None
        self.createdTime = None
        self.mediaList = None
        self.commentsCount = None

    @property
    def wiki(self):
        with suppress(KeyError, TypeError):
            self.author = userProfile(self.json["author"]).userProfile
            self.createdTime = self.json["createdTime"]
            self.wikiId = self.json["itemId"]
            self.status = self.json["status"]
            self.style = self.json["style"]
            self.globalCommentsCount = self.json["globalCommentsCount"]
            self.modifiedTime = self.json["modifiedTime"]
            self.votedValue = self.json["votedValue"]
            self.globalVotesCount = self.json["globalVotesCount"]
            self.globalVotedValue = self.json["globalVotedValue"]
            self.contentRating = self.json["contentRating"]
            self.contentRating = self.json["contentRating"]
            self.title = self.json["label"]
            self.content = self.json["content"]
            self.keywords = self.json["keywords"]
            self.needHidden = self.json["needHidden"]
            self.guestVotesCount = self.json["guestVotesCount"]
            self.extensions = self.json["extensions"]
            self.votesCount = self.json["votesCount"]
            self.comId = self.json["ndcId"]
            self.createdTime = self.json["createdTime"]
            self.mediaList = self.json["mediaList"]
            self.commentsCount = self.json["commentsCount"]
            self.backgroundColor = self.json["extensions"]["style"]["backgroundColor"]
            self.fansOnly = self.json["extensions"]["fansOnly"]
            self.knowledgeBase = self.json["extensions"]["knowledgeBase"]
            self.labels = wikiLabelList(self.json["extensions"]["props"]).wikiLabelList
            self.version = self.json["extensions"]["knowledgeBase"]["version"]
            self.originalWikiId = self.json["extensions"]["knowledgeBase"]["originalItemId"]
            self.contributors = self.json["extensions"]["knowledgeBase"]["contributors"]

        return self

class wikiList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([wk["author"] for wk in data]).userProfileList
        self.createdTime = []
        self.modifiedTime = []
        self.wikiId = []
        self.status = []
        self.style = []
        self.globalCommentsCount = []
        self.votedValue = []
        self.globalVotesCount = []
        self.globalVotedValue = []
        self.contentRating = []
        self.title = []
        self.content = []
        self.keywords = []
        self.needHidden = []
        self.guestVotesCount = []
        self.extensions = []
        self.backgroundColor = []
        self.fansOnly = []
        self.knowledgeBase = []
        self.originalWikiId = []
        self.version = []
        self.contributors = []
        self.labels = []
        self.votesCount = []
        self.comId = []
        self.createdTime = []
        self.mediaList = []
        self.commentsCount = []

    @property
    def wikiList(self):
        for x in self.json:
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.wikiId.append(x["itemId"])
            except (KeyError, TypeError): self.wikiId.append(None)
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.style.append(x["style"])
            except (KeyError, TypeError): self.style.append(None)
            try: self.globalCommentsCount.append(x["globalCommentsCount"])
            except (KeyError, TypeError): self.globalCommentsCount.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.votedValue.append(x["votedValue"])
            except (KeyError, TypeError): self.votedValue.append(None)
            try: self.globalVotesCount.append(x["globalVotesCount"])
            except (KeyError, TypeError): self.globalVotesCount.append(None)
            try: self.globalVotedValue.append(x["globalVotedValue"])
            except (KeyError, TypeError): self.globalVotedValue.append(None)
            try: self.contentRating.append(x["contentRating"])
            except (KeyError, TypeError): self.contentRating.append(None)
            try: self.contentRating.append(x["contentRating"])
            except (KeyError, TypeError): self.contentRating.append(None)
            try: self.title.append(x["label"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.keywords.append(x["keywords"])
            except (KeyError, TypeError): self.keywords.append(None)
            try: self.needHidden.append(x["needHidden"])
            except (KeyError, TypeError): self.needHidden.append(None)
            try: self.guestVotesCount.append(x["guestVotesCount"])
            except (KeyError, TypeError): self.guestVotesCount.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.votesCount.append(x["votesCount"])
            except (KeyError, TypeError): self.votesCount.append(None)
            try: self.comId.append(x["ndcId"])
            except (KeyError, TypeError): self.comId.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.commentsCount.append(x["commentsCount"])
            except (KeyError, TypeError): self.commentsCount.append(None)
            try: self.backgroundColor.append(x["extensions"]["style"]["backgroundColor"])
            except (KeyError, TypeError): self.backgroundColor.append(None)
            try: self.fansOnly.append(x["extensions"]["fansOnly"])
            except (KeyError, TypeError): self.fansOnly.append(None)
            try: self.knowledgeBase.append(x["extensions"]["knowledgeBase"])
            except (KeyError, TypeError): self.knowledgeBase.append(None)
            try: self.labels.append(wikiLabelList(x["extensions"]["props"]).wikiLabelList)
            except (KeyError, TypeError): self.labels.append(None)
            try: self.version.append(x["extensions"]["knowledgeBase"]["version"])
            except (KeyError, TypeError): self.version.append(None)
            try: self.originalWikiId.append(x["extensions"]["knowledgeBase"]["originalItemId"])
            except (KeyError, TypeError): self.originalWikiId.append(None)
            try: self.contributors.append(x["extensions"]["knowledgeBase"]["contributors"])
            except (KeyError, TypeError): self.contributors.append(None)

        return self


class wikiLabelList:
    def __init__(self, data):
        self.json = data
        self.title = []
        self.content = []
        self.type = []

    @property
    def wikiLabelList(self):
        for x in self.json:
            try: self.title.append(x["title"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.content.append(x["value"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)

        return self

class rankingTableList:
    def __init__(self, data):
        self.json = data
        self.title = []
        self.level = []
        self.reputation = []
        self.id = []

    def rankingTableList(self):
        for x in self.json:
            try: self.title.append(x["title"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.level.append(x["level"])
            except (KeyError, TypeError): self.level.append(None)
            try: self.reputation.append(x["reputation"])
            except (KeyError, TypeError): self.reputation.append(None)
            try: self.id.append(x["id"])
            except (KeyError, TypeError): self.id.append(None)

        return self

class community:
    def __init__(self, data):
        self.json = data
        self.usersCount = None
        self.agent = None
        self.createdTime = None
        self.aminoId = None
        self.icon = None
        self.link = None
        self.comId = None
        self.modifiedTime = None
        self.status = None
        self.joinType = None
        self.tagline = None
        self.primaryLanguage = None
        self.heat = None
        self.themePack = None
        self.probationStatus = None
        self.listedStatus = None
        self.userAddedTopicList = None
        self.name = None
        self.isStandaloneAppDeprecated = None
        self.searchable = None
        self.influencerList = None
        self.keywords = None
        self.mediaList = None
        self.description = None
        self.isStandaloneAppMonetizationEnabled = None
        self.advancedSettings = None
        self.activeInfo = None
        self.configuration = None
        self.extensions = None
        self.nameAliases = None
        self.templateId = None
        self.promotionalMediaList = None
        self.defaultRankingTypeInLeaderboard = None
        self.rankingTable = None
        self.joinedBaselineCollectionIdList = None
        self.newsfeedPages = None
        self.catalogEnabled = None
        self.pollMinFullBarVoteCount = None
        self.leaderboardStyle = None
        self.facebookAppIdList = None
        self.welcomeMessage = None
        self.welcomeMessageEnabled = None
        self.hasPendingReviewRequest = None
        self.frontPageLayout = None

    @property
    def community(self):
        with suppress(KeyError, TypeError):
            self.name = self.json["name"]
            self.usersCount = self.json["membersCount"]
            self.agent = userProfile(self.json["agent"].userProfile)
            self.createdTime = self.json["createdTime"]
            self.aminoId = self.json["endpoint"]
            self.icon = self.json["icon"]
            self.link = self.json["link"]
            self.comId = self.json["ndcId"]
            self.modifiedTime = self.json["modifiedTime"]
            self.status = self.json["status"]
            self.joinType = self.json["joinType"]
            self.primaryLanguage = self.json["primaryLanguage"]
            self.heat = self.json["communityHeat"]
            self.userAddedTopicList = self.json["userAddedTopicList"]
            self.probationStatus = self.json["probationStatus"]
            self.listedStatus = self.json["listedStatus"]
            self.themePack = self.json["themePack"]
            self.tagline = self.json["tagline"]
            self.searchable = self.json["searchable"]
            self.isStandaloneAppDeprecated = self.json["isStandaloneAppDeprecated"]
            self.influencerList = self.json["influencerList"]
            self.keywords = self.json["keywords"]
            self.mediaList = self.json["mediaList"]
            self.description = self.json["content"]
            self.isStandaloneAppMonetizationEnabled = self.json["isStandaloneAppMonetizationEnabled"]
            self.advancedSettings = self.json["advancedSettings"]
            self.defaultRankingTypeInLeaderboard = self.json["advancedSettings"]["defaultRankingTypeInLeaderboard"]
            self.frontPageLayout = self.json["advancedSettings"]["frontPageLayout"]
            self.hasPendingReviewRequest = self.json["advancedSettings"]["hasPendingReviewRequest"]
            self.welcomeMessageEnabled = self.json["advancedSettings"]["welcomeMessageEnabled"]
            self.welcomeMessage = self.json["advancedSettings"]["welcomeMessageText"]
            self.pollMinFullBarVoteCount = self.json["advancedSettings"]["pollMinFullBarVoteCount"]
            self.catalogEnabled = self.json["advancedSettings"]["catalogEnabled"]
            self.leaderboardStyle = self.json["advancedSettings"]["leaderboardStyle"]
            self.facebookAppIdList = self.json["advancedSettings"]["facebookAppIdList"]
            self.newsfeedPages = self.json["advancedSettings"]["newsfeedPages"]
            self.rankingTable = rankingTableList(self.json["advancedSettings"]["rankingTable"].rankingTableList)
            self.joinedBaselineCollectionIdList = self.json["advancedSettings"]["joinedBaselineCollectionIdList"]
            self.activeInfo = self.json["activeInfo"]
            self.configuration = self.json["configuration"]
            self.extensions = self.json["extensions"]
            self.nameAliases = self.json["extensions"]["communityNameAliases"]
            self.templateId = self.json["templateId"]
            self.promotionalMediaList = self.json["promotionalMediaList"]
        return self

class communityList:
    def __init__(self, data):
        self.json = data
        self.usersCount = []
        self.agent = userProfileList([cmnt["agent"] for cmnt in data]).userProfileList
        self.createdTime = []
        self.aminoId = []
        self.icon = []
        self.link = []
        self.comId = []
        self.modifiedTime = []
        self.status = []
        self.joinType = []
        self.tagline = []
        self.primaryLanguage = []
        self.heat = []
        self.themePack = []
        self.probationStatus = []
        self.listedStatus = []
        self.userAddedTopicList = []
        self.name = []
        self.isStandaloneAppDeprecated = []
        self.searchable = []
        self.influencerList = []
        self.keywords = []
        self.mediaList = []
        self.description = []
        self.isStandaloneAppMonetizationEnabled = []
        self.advancedSettings = []
        self.activeInfo = []
        self.configuration = []
        self.extensions = []
        self.nameAliases = []
        self.templateId = []
        self.promotionalMediaList = []
        self.defaultRankingTypeInLeaderboard = []
        self.rankingTable = []
        self.joinedBaselineCollectionIdList = []
        self.newsfeedPages = []
        self.catalogEnabled = []
        self.pollMinFullBarVoteCount = []
        self.leaderboardStyle = []
        self.facebookAppIdList = []
        self.welcomeMessage = []
        self.welcomeMessageEnabled = []
        self.hasPendingReviewRequest = []
        self.frontPageLayout = []

    @property
    def communityList(self):
        for x in self.json:
            try: self.name.append(x["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.usersCount.append(x["membersCount"])
            except (KeyError, TypeError): self.usersCount.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.aminoId.append(x["endpoint"])
            except (KeyError, TypeError): self.aminoId.append(None)
            try: self.icon.append(x["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.link.append(x["link"])
            except (KeyError, TypeError): self.link.append(None)
            try: self.comId.append(x["ndcId"])
            except (KeyError, TypeError): self.comId.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.joinType.append(x["joinType"])
            except (KeyError, TypeError): self.joinType.append(None)
            try: self.primaryLanguage.append(x["primaryLanguage"])
            except (KeyError, TypeError): self.primaryLanguage.append(None)
            try: self.heat.append(x["communityHeat"])
            except (KeyError, TypeError): self.heat.append(None)
            try: self.userAddedTopicList.append(x["userAddedTopicList"])
            except (KeyError, TypeError): self.userAddedTopicList.append(None)
            try: self.probationStatus.append(x["probationStatus"])
            except (KeyError, TypeError): self.probationStatus.append(None)
            try: self.listedStatus.append(x["listedStatus"])
            except (KeyError, TypeError): self.listedStatus.append(None)
            try: self.themePack.append(x["themePack"])
            except (KeyError, TypeError): self.themePack.append(None)
            try: self.tagline.append(x["tagline"])
            except (KeyError, TypeError): self.tagline.append(None)
            try: self.searchable.append(x["searchable"])
            except (KeyError, TypeError): self.searchable.append(None)
            try: self.isStandaloneAppDeprecated.append(x["isStandaloneAppDeprecated"])
            except (KeyError, TypeError): self.isStandaloneAppDeprecated.append(None)
            try: self.influencerList.append(x["influencerList"])
            except (KeyError, TypeError): self.influencerList.append(None)
            try: self.keywords.append(x["keywords"])
            except (KeyError, TypeError): self.keywords.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.description.append(x["content"])
            except (KeyError, TypeError): self.description.append(None)
            try: self.isStandaloneAppMonetizationEnabled.append(x["isStandaloneAppMonetizationEnabled"])
            except (KeyError, TypeError): self.isStandaloneAppMonetizationEnabled.append(None)
            try: self.advancedSettings.append(x["advancedSettings"])
            except (KeyError, TypeError): self.advancedSettings.append(None)
            try: self.defaultRankingTypeInLeaderboard.append(x["advancedSettings"]["defaultRankingTypeInLeaderboard"])
            except (KeyError, TypeError): self.defaultRankingTypeInLeaderboard.append(None)
            try: self.frontPageLayout.append(x["advancedSettings"]["frontPageLayout"])
            except (KeyError, TypeError): self.frontPageLayout.append(None)
            try: self.hasPendingReviewRequest.append(x["advancedSettings"]["hasPendingReviewRequest"])
            except (KeyError, TypeError): self.hasPendingReviewRequest.append(None)
            try: self.welcomeMessageEnabled.append(x["advancedSettings"]["welcomeMessageEnabled"])
            except (KeyError, TypeError): self.welcomeMessageEnabled.append(None)
            try: self.welcomeMessage.append(x["advancedSettings"]["welcomeMessageText"])
            except (KeyError, TypeError): self.welcomeMessage.append(None)
            try: self.pollMinFullBarVoteCount.append(x["advancedSettings"]["pollMinFullBarVoteCount"])
            except (KeyError, TypeError): self.pollMinFullBarVoteCount.append(None)
            try: self.catalogEnabled.append(x["advancedSettings"]["catalogEnabled"])
            except (KeyError, TypeError): self.catalogEnabled.append(None)
            try: self.leaderboardStyle.append(x["advancedSettings"]["leaderboardStyle"])
            except (KeyError, TypeError): self.leaderboardStyle.append(None)
            try: self.facebookAppIdList.append(x["advancedSettings"]["facebookAppIdList"])
            except (KeyError, TypeError): self.facebookAppIdList.append(None)
            try: self.newsfeedPages.append(x["advancedSettings"]["newsfeedPages"])
            except (KeyError, TypeError): self.newsfeedPages.append(None)
            try: self.rankingTable.append(rankingTableList(x["advancedSettings"]["rankingTable"]).rankingTableList)
            except (KeyError, TypeError): self.rankingTable.append(None)
            try: self.joinedBaselineCollectionIdList.append(x["advancedSettings"]["joinedBaselineCollectionIdList"])
            except (KeyError, TypeError): self.joinedBaselineCollectionIdList.append(None)
            try: self.activeInfo.append(x["activeInfo"])
            except (KeyError, TypeError): self.activeInfo.append(None)
            try: self.configuration.append(x["configuration"])
            except (KeyError, TypeError): self.configuration.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.nameAliases.append(x["extensions"]["communityNameAliases"])
            except (KeyError, TypeError): self.nameAliases.append(None)
            try: self.templateId.append(x["templateId"])
            except (KeyError, TypeError): self.templateId.append(None)
            try: self.promotionalMediaList.append(x["promotionalMediaList"])
            except (KeyError, TypeError): self.promotionalMediaList.append(None)

        return self

class visitorsList:
    def __init__(self, data):
        self.json = data
        self.visitors = None
        self.lastCheckTime = None
        self.visitorsCapacity = None
        self.visitorsCount = None
        self.ownerPrivacyMode = []
        self.visitorPrivacyMode = []
        self.visitTime = []
        self.profile = userProfileList([x["profile"] for x in data["visitors"]]).userProfileList

    @property
    def visitorsList(self):
        with suppress(KeyError, TypeError):
            self.visitors = self.json["visitors"]
            self.lastCheckTime = self.json["lastCheckTime"]
            self.visitorsCapacity = self.json["capacity"]
            self.visitorsCount = self.json["visitorsCount"]

        for x in self.json["visitors"]:
            try: self.ownerPrivacyMode.append(x["ownerPrivacyMode"])
            except (KeyError, TypeError): self.ownerPrivacyMode.append(None)
            try: self.visitorPrivacyMode.append(x["visitorPrivacyMode"])
            except (KeyError, TypeError): self.visitorPrivacyMode.append(None)
            try: self.visitTime.append(x["visitTime"])
            except (KeyError, TypeError): self.visitTime.append(None)

        return self

class commentList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([cmnt["author"] for cmnt in data]).userProfileList
        self.votesSum = []
        self.votedValue = []
        self.mediaList = []
        self.parentComId = []
        self.parentId = []
        self.parentType = []
        self.content = []
        self.extensions = []
        self.comId = []
        self.modifiedTime = []
        self.createdTime = []
        self.commentId = []
        self.subcommentsCount = []
        self.type = []

    @property
    def commentList(self):
        for x in self.json:
            try: self.votesSum.append(x["votesSum"])
            except (KeyError, TypeError): self.votesSum.append(None)
            try: self.votedValue.append(x["votedValue"])
            except (KeyError, TypeError): self.votedValue.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.parentComId.append(x["parentNdcId"])
            except (KeyError, TypeError): self.parentComId.append(None)
            try: self.parentId.append(x["parentId"])
            except (KeyError, TypeError): self.parentId.append(None)
            try: self.parentType.append(x["parentType"])
            except (KeyError, TypeError): self.parentType.append(None)
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.comId.append(x["ndcId"])
            except (KeyError, TypeError): self.comId.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.commentId.append(x["commentId"])
            except (KeyError, TypeError): self.commentId.append(None)
            try: self.subcommentsCount.append(x["subcommentsCount"])
            except (KeyError, TypeError): self.subcommentsCount.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)

        return self

class membership:
    def __init__(self, data):
        self.json = data
        self.premiumFeature = None
        self.hasAnyAndroidSubscription = None
        self.hasAnyAppleSubscription = None
        self.accountMembership = None
        self.paymentType = None
        self.membershipStatus = None
        self.isAutoRenew = None
        self.createdTime = None
        self.modifiedTime = None
        self.renewedTime = None
        self.expiredTime = None

    @property
    def membership(self):
        with suppress(KeyError, TypeError):
            self.premiumFeature = self.json["premiumFeatureEnabled"]
            self.hasAnyAndroidSubscription = self.json["hasAnyAndroidSubscription"]
            self.hasAnyAppleSubscription = self.json["hasAnyAppleSubscription"]
            self.accountMembership = self.json["accountMembershipEnabled"]
            self.paymentType = self.json["paymentType"]
            self.membershipStatus = self.json["membership"]["membershipStatus"]
            self.isAutoRenew = self.json["membership"]["isAutoRenew"]
            self.createdTime = self.json["membership"]["createdTime"]
            self.modifiedTime = self.json["membership"]["modifiedTime"]
            self.renewedTime = self.json["membership"]["renewedTime"]
            self.expiredTime = self.json["membership"]["expiredTime"]

        return self

class fromCode:
    def __init__(self, data):
        self.json = data
        self.path = None
        self.objectType = None
        self.shortCode = None
        self.fullPath = None
        self.targetCode = None
        self.objectId = None

    @property
    def fromCode(self):
        with suppress(KeyError, TypeError):
            self.path = self.json["path"]
            self.objectType = self.json["extensions"]["linkInfo"]["objectType"]
            self.shortCode = self.json["extensions"]["linkInfo"]["shortCode"]
            self.fullPath = self.json["extensions"]["linkInfo"]["fullPath"]
            self.targetCode = self.json["extensions"]["linkInfo"]["targetCode"]
            self.objectId = self.json["extensions"]["linkInfo"]["objectId"]

        return self

class userProfileCountList:
    def __init__(self, data):
        self.json = data
        self.profile = userProfileList([cht for cht in data["userProfileList"]]).userProfileList
        self.userProfileCount = None

    @property
    def userProfileCountList(self):
        with suppress(KeyError, TypeError):
            self.userProfileCount = self.json["userProfileCount"]

        return self

class userCheckIns:
    def __init__(self, data):
        self.json = data
        self.hasAnyCheckIn = None
        self.brokenStreaks = None
        self.consecutiveCheckInDays = None

    @property
    def userCheckIns(self):
        with suppress(KeyError, TypeError):
            self.hasAnyCheckIn = self.json["hasAnyCheckIn"]
            self.brokenStreaks = self.json["brokenStreaks"]
            self.consecutiveCheckInDays = self.json["consecutiveCheckInDays"]

        return self

class walletInfo:
    def __init__(self, data):
        self.json = data
        self.totalCoinsFloat = None
        self.adsEnabled = None
        self.adsVideoStats = None
        self.adsFlags = None
        self.totalCoins = None
        self.businessCoinsEnabled = None
        self.totalBusinessCoins = None
        self.totalBusinessCoinsFloat = None

    @property
    def walletInfo(self):
        with suppress(KeyError, TypeError):
            self.totalCoinsFloat = self.json["totalCoinsFloat"]
            self.adsEnabled = self.json["adsEnabled"]
            self.adsVideoStats = self.json["adsVideoStats"]
            self.adsFlags = self.json["adsFlags"]
            self.totalCoins = self.json["totalCoins"]
            self.businessCoinsEnabled = self.json["businessCoinsEnabled"]
            self.totalBusinessCoins = self.json["totalBusinessCoins"]
            self.totalBusinessCoinsFloat = self.json["totalBusinessCoinsFloat"]

        return self


class userAchievements:
    def __init__(self, data):
        self.json = data
        self.secondsSpentOfLast24Hours = None
        self.secondsSpentOfLast7Days = None
        self.numberOfFollowersCount = None
        self.numberOfPostsCreated = None

    @property
    def userAchievements(self):
        with suppress(KeyError, TypeError):
            self.secondsSpentOfLast24Hours = self.json["secondsSpentOfLast24Hours"]
            self.secondsSpentOfLast7Days = self.json["secondsSpentOfLast7Days"]
            self.numberOfFollowersCount = self.json["numberOfMembersCount"]
            self.numberOfPostsCreated = self.json["numberOfPostsCreated"]

        return self

class userSavedBlogs:
    def __init__(self, data):
        self.json = data
        self.objectType = []
        self.bookmarkedTime = []
        self.objectId = []
        self.objectJson = []
        self.object = []

    @property
    def userSavedBlogs(self):
        for x in self.json:
            try: self.objectType.append(x["refObjectType"])
            except (KeyError, TypeError): self.objectType.append(None)
            try: self.bookmarkedTime.append(x["bookmarkedTime"])
            except (KeyError, TypeError): self.bookmarkedTime.append(None)
            try: self.objectId.append(x["refObjectId"])
            except (KeyError, TypeError): self.objectId.append(None)
            try: self.objectJson.append(x["refObject"])
            except (KeyError, TypeError): self.objectJson.append(None)

            if x["refObjectType"] == 1:
                try: self.object.append(blog(x["refObject"]).blog)
                except (KeyError, TypeError): self.object.append(None)

            elif x["refObjectType"] == 2:
                try: self.object.append(wiki(x["refObject"]).wiki)
                except (KeyError, TypeError): self.object.append(None)

            else: self.object.append(x["refObject"])

        return self

class getWikiInfo:
    def __init__(self, data):
        self.json = data
        self.inMyFavorites = None
        self.isBookmarked = None
        self.wiki = None

    @property
    def getWikiInfo(self):
        with suppress(KeyError, TypeError):
            self.inMyFavorites = self.json["inMyFavorites"]
            self.isBookmarked = self.json["isBookmarked"]
            self.wiki = wiki(self.json["item"]).wiki

        return self

class getBlogInfo:
    def __init__(self, data):
        self.json = data
        self.isBookmarked = None
        self.blog = None

    @property
    def getBlogInfo(self):
        with suppress(KeyError, TypeError):
            self.isBookmarked = self.json["isBookmarked"]
            self.blog = blog(self.json["blog"]).blog

        return self

class wikiCategoryList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([wk["author"] for wk in data]).userProfileList
        self.itemsCount = []
        self.parentCategoryId = []
        self.categoryId = []
        self.content = []
        self.extensions = []
        self.createdTime = []
        self.subcategoriesCount = []
        self.title = []
        self.mediaList = []
        self.icon = []

    @property
    def wikiCategoryList(self):
        for x in self.json:
            try: self.itemsCount.append(x["itemsCount"])
            except (KeyError, TypeError): self.itemsCount.append(None)
            try: self.parentCategoryId.append(x["parentCategoryId"])
            except (KeyError, TypeError): self.parentCategoryId.append(None)
            try: self.categoryId.append(x["categoryId"])
            except (KeyError, TypeError): self.categoryId.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.title.append(x["label"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.mediaList.append(x["mediaList"])
            except (KeyError, TypeError): self.mediaList.append(None)
            try: self.icon.append(x["icon"])
            except (KeyError, TypeError): self.icon.append(None)

        return self

class wikiCategory:
    def __init__(self, data):
        self.json = data
        self.itemsCount = None
        self.parentCategoryId = None
        self.parentType = None
        self.author = None
        self.categoryId = None
        self.content = None
        self.extensions = None
        self.createdTime = None
        self.subcategoriesCount = None
        self.title = None
        self.mediaList = None
        self.icon = None
        self.subCategory = None

    @property
    def wikiCategory(self):
        with suppress(KeyError, TypeError):
            self.itemsCount = self.json["itemCategory"]["itemsCount"]
            self.parentCategoryId = self.json["itemCategory"]["parentCategoryId"]
            self.author = userProfile(self.json["itemCategory"]["author"]).userProfile
            self.categoryId = self.json["itemCategory"]["categoryId"]
            self.extensions = self.json["itemCategory"]["extensions"]
            self.createdTime = self.json["itemCategory"]["createdTime"]
            self.title = self.json["itemCategory"]["label"]
            self.mediaList = self.json["itemCategory"]["mediaList"]
            self.icon = self.json["itemCategory"]["icon"]
            self.parentType = self.json["childrenWrapper"]["type"]
            self.subCategory = wikiCategoryList(self.json["childrenWrapper"]["itemCategoryList"]).wikiCategoryList

        return self

class tippedUsersSummary:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([tpd["tipper"] for tpd in data["tippedUserList"]]).userProfileList
        self.tipSummary = None
        self.totalCoins = None
        self.tippersCount = None
        self.globalTipSummary = None
        self.globalTippersCount = None
        self.globalTotalCoins = None
        self.lastTippedTime = []
        self.totalTippedCoins = []
        self.lastThankedTime = []

    @property
    def tippedUsersSummary(self):
        with suppress(KeyError, TypeError):
            self.tipSummary = self.json["tipSummary"]
            self.totalCoins = self.json["tipSummary"]["totalCoins"]
            self.tippersCount = self.json["tipSummary"]["tippersCount"]
            self.globalTipSummary = self.json["globalTipSummary"]
            self.globalTippersCount = self.json["globalTipSummary"]["tippersCount"]
            self.globalTotalCoins = self.json["globalTipSummary"]["totalCoins"]

        for tippedUserList in self.json["tippedUserList"]:
            try: self.lastTippedTime.append(tippedUserList["lastTippedTime"])
            except (KeyError, TypeError): self.lastTippedTime.append(None)
            try: self.totalTippedCoins.append(tippedUserList["totalTippedCoins"])
            except (KeyError, TypeError): self.totalTippedCoins.append(None)
            try: self.lastThankedTime.append(tippedUserList["lastThankedTime"])
            except (KeyError, TypeError): self.lastThankedTime.append(None)

        return self

class thread:
    def __init__(self, data):
        self.json = data
        self.userAddedTopicList = None
        self.membersQuota = None
        self.membersSummary = None
        self.chatId = None
        self.keywords = None
        self.membersCount = None
        self.isPinned = None
        self.title = None
        self.membershipStatus = None
        self.content = None
        self.needHidden = None
        self.alertOption = None
        self.lastReadTime = None
        self.type = None
        self.status = None
        self.publishToGlobal = None
        self.modifiedTime = None
        self.condition = None
        self.icon = None
        self.latestActivityTime = None
        self.author = None
        self.extensions = None
        self.viewOnly = None
        self.coHosts = None
        self.membersCanInvite = None
        self.announcement = None
        self.language = None
        self.lastMembersSummaryUpdateTime = None
        self.backgroundImage = None
        self.channelType = None
        self.comId = None
        self.createdTime = None
        self.creatorId = None
        self.bannedUsers = None
        self.tippingPermStatus = None
        self.visibility = None
        self.fansOnly = None
        self.pinAnnouncement = None
        self.vvChatJoinType = None
        self.screeningRoomHostId = None
        self.screeningRoomPermission = None
        self.disabledTime = None

    @property
    def thread(self):
        with suppress(KeyError, TypeError):
            self.userAddedTopicList = self.json["userAddedTopicList"]
            self.membersQuota = self.json["membersQuota"]
            self.membersSummary = self.json["membersSummary"]
            self.chatId = self.json["threadId"]
            self.keywords = self.json["keywords"]
            self.membersCount = self.json["membersCount"]
            self.isPinned = self.json["isPinned"]
            self.title = self.json["title"]
            self.content = self.json["content"]
            self.needHidden = self.json["needHidden"]
            self.alertOption = self.json["alertOption"]
            self.lastReadTime = self.json["lastReadTime"]
            self.type = self.json["type"]
            self.status = self.json["status"]
            self.publishToGlobal = self.json["publishToGlobal"]
            self.modifiedTime = self.json["modifiedTime"]
            self.condition = self.json["condition"]
            self.icon = self.json["icon"]
            self.latestActivityTime = self.json["latestActivityTime"]
            self.comId = self.json["ndcId"]
            self.createdTime = self.json["createdTime"]
            self.extensions = self.json["extensions"]
            self.viewOnly = self.json["extensions"]["viewOnly"]
            self.coHosts = self.json["extensions"]["coHost"]
            self.membersCanInvite = self.json["extensions"]["membersCanInvite"]
            self.language = self.json["extensions"]["language"]
            self.announcement = self.json["extensions"]["announcement"]
            self.backgroundImage = self.json["extensions"]["bm"][1]
            self.lastMembersSummaryUpdateTime = self.json["extensions"]["lastMembersSummaryUpdateTime"]
            self.channelType = self.json["extensions"]["channelType"]
            self.creatorId = self.json["extensions"]["creatorUid"]
            self.bannedUsers = self.json["extensions"]["bannedMemberUidList"]
            self.visibility = self.json["extensions"]["visibility"]
            self.fansOnly = self.json["extensions"]["fansOnly"]
            self.pinAnnouncement = self.json["extensions"]["pinAnnouncement"]
            self.vvChatJoinType = self.json["extensions"]["vvChatJoinType"]
            self.disabledTime = self.json["extensions"]["__disabledTime__"]
            self.tippingPermStatus = self.json["extensions"]["tippingPermStatus"]
            self.screeningRoomHostId = self.json["extensions"]["screeningRoomHostUid"]
            self.screeningRoomPermission = self.json["extensions"]["screeningRoomPermission"]["action"]
            self.author = userProfile(self.json["author"]).userProfile

        return self

class threadList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([cht["author"] for cht in data]).userProfileList
        self.userAddedTopicList = []
        self.membersQuota = []
        self.membersSummary = []
        self.chatId = []
        self.keywords = []
        self.membersCount = []
        self.isPinned = []
        self.title = []
        self.membershipStatus = []
        self.content = []
        self.needHidden = []
        self.alertOption = []
        self.lastReadTime = []
        self.type = []
        self.status = []
        self.publishToGlobal = []
        self.modifiedTime = []
        self.condition = []
        self.icon = []
        self.latestActivityTime = []
        self.extensions = []
        self.viewOnly = []
        self.coHosts = []
        self.membersCanInvite = []
        self.announcement = []
        self.language = []
        self.lastMembersSummaryUpdateTime = []
        self.backgroundImage = []
        self.channelType = []
        self.comId = []
        self.createdTime = []
        self.creatorId = []
        self.bannedUsers = []
        self.tippingPermStatus = []
        self.visibility = []
        self.fansOnly = []
        self.pinAnnouncement = []
        self.vvChatJoinType = []
        self.screeningRoomHostId = []
        self.screeningRoomPermission = []
        self.disabledTime = []

    @property
    def threadList(self):
        for chat in self.json:
            try: self.userAddedTopicList.append(chat["userAddedTopicList"])
            except (KeyError, TypeError): self.userAddedTopicList.append(None)
            try: self.membersQuota.append(chat["membersQuota"])
            except (KeyError, TypeError): self.membersQuota.append(None)
            try: self.membersSummary.append(chat["membersSummary"])
            except (KeyError, TypeError): self.membersSummary.append(None)
            try: self.chatId.append(chat["threadId"])
            except (KeyError, TypeError): self.chatId.append(None)
            try: self.keywords.append(chat["keywords"])
            except (KeyError, TypeError): self.keywords.append(None)
            try: self.membersCount.append(chat["membersCount"])
            except (KeyError, TypeError): self.membersCount.append(None)
            try: self.isPinned.append(chat["isPinned"])
            except (KeyError, TypeError): self.isPinned.append(None)
            try: self.title.append(chat["title"])
            except (KeyError, TypeError): self.title.append(None)
            try: self.content.append(chat["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.needHidden.append(chat["needHidden"])
            except (KeyError, TypeError): self.needHidden.append(None)
            try: self.alertOption.append(chat["alertOption"])
            except (KeyError, TypeError): self.alertOption.append(None)
            try: self.lastReadTime.append(chat["lastReadTime"])
            except (KeyError, TypeError): self.lastReadTime.append(None)
            try: self.type.append(chat["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.status.append(chat["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.publishToGlobal.append(chat["publishToGlobal"])
            except (KeyError, TypeError): self.publishToGlobal.append(None)
            try: self.modifiedTime.append(chat["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.condition.append(chat["condition"])
            except (KeyError, TypeError): self.condition.append(None)
            try: self.icon.append(chat["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.latestActivityTime.append(chat["latestActivityTime"])
            except (KeyError, TypeError): self.latestActivityTime.append(None)
            try: self.comId.append(chat["ndcId"])
            except (KeyError, TypeError): self.comId.append(None)
            try: self.createdTime.append(chat["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try:  self.extensions.append(chat["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try:  self.viewOnly.append(chat["extensions"]["viewOnly"])
            except (KeyError, TypeError): self.viewOnly.append(None)
            try:  self.coHosts.append(chat["extensions"]["coHost"])
            except (KeyError, TypeError): self.coHosts.append(None)
            try:  self.membersCanInvite.append(chat["extensions"]["membersCanInvite"])
            except (KeyError, TypeError): self.membersCanInvite.append(None)
            try:  self.language.append(chat["extensions"]["language"])
            except (KeyError, TypeError): self.language.append(None)
            try:  self.announcement.append(chat["extensions"]["announcement"])
            except (KeyError, TypeError): self.announcement.append(None)
            try:  self.backgroundImage.append(chat["extensions"]["bm"][1])
            except (KeyError, TypeError): self.backgroundImage.append(None)
            try:  self.lastMembersSummaryUpdateTime.append(chat["extensions"]["lastMembersSummaryUpdateTime"])
            except (KeyError, TypeError): self.lastMembersSummaryUpdateTime.append(None)
            try:  self.channelType.append(chat["extensions"]["channelType"])
            except (KeyError, TypeError): self.channelType.append(None)
            try:  self.creatorId.append(chat["extensions"]["creatorUid"])
            except (KeyError, TypeError): self.creatorId.append(None)
            try:  self.bannedUsers.append(chat["extensions"]["bannedMemberUidList"])
            except (KeyError, TypeError): self.bannedUsers.append(None)
            try:  self.visibility.append(chat["extensions"]["visibility"])
            except (KeyError, TypeError): self.visibility.append(None)
            try:  self.fansOnly.append(chat["extensions"]["fansOnly"])
            except (KeyError, TypeError): self.fansOnly.append(None)
            try:  self.pinAnnouncement.append(chat["extensions"]["pinAnnouncement"])
            except (KeyError, TypeError): self.pinAnnouncement.append(None)
            try:  self.vvChatJoinType.append(chat["extensions"]["vvChatJoinType"])
            except (KeyError, TypeError): self.vvChatJoinType.append(None)
            try:  self.tippingPermStatus.append(chat["extensions"]["tippingPermStatus"])
            except (KeyError, TypeError): self.tippingPermStatus.append(None)
            try:  self.screeningRoomHostId.append(chat["extensions"]["screeningRoomHostUid"])
            except (KeyError, TypeError): self.screeningRoomHostId.append(None)
            try:  self.disabledTime.append(chat["extensions"]["__disabledTime__"])
            except (KeyError, TypeError): self.disabledTime.append(None)
            try:  self.screeningRoomPermission.append(chat["extensions"]["screeningRoomPermission"]["action"])
            except (KeyError, TypeError): self.screeningRoomPermission.append(None)

        return self

class sticker:
    def __init__(self, data):
        self.json = data
        self.status = None
        self.icon = None
        self.iconV2 = None
        self.name = None
        self.stickerId = None
        self.smallIcon = None
        self.smallIconV2 = None
        self.stickerCollectionId = None
        self.mediumIcon = None
        self.mediumIconV2 = None
        self.extensions = None
        self.usedCount = None
        self.createdTime = None
        self.collection = None

    @property
    def sticker(self):
        with suppress(KeyError, TypeError):
            self.status = self.json["status"]
            self.icon = self.json["icon"]
            self.iconV2 = self.json["iconV2"]
            self.name = self.json["name"]
            self.stickerId = self.json["stickerId"]
            self.smallIcon = self.json["smallIcon"]
            self.smallIconV2 = self.json["smallIconV2"]
            self.stickerCollectionId = self.json["stickerCollectionId"]
            self.mediumIcon = self.json["mediumIcon"]
            self.mediumIconV2 = self.json["mediumIconV2"]
            self.extensions = self.json["extensions"]
            self.usedCount = self.json["extensions"]
            self.createdTime = self.json["createdTime"]
            self.collection = stickerCollection(self.json["stickerCollectionSummary"]).stickerCollection

        return self

class stickerCollection:
    def __init__(self, data):
        self.json = data
        self.author = None
        self.status = None
        self.collectionType = None
        self.modifiedTime = None
        self.bannerUrl = None
        self.smallIcon = None
        self.stickersCount = None
        self.usedCount = None
        self.icon = None
        self.title = None
        self.collectionId = None
        self.extensions = None
        self.isActivated = None
        self.ownershipStatus = None
        self.isNew = None
        self.availableComIds = None
        self.description = None
        self.iconSourceStickerId = None
        self.originalAuthor = None
        self.originalCommunity = None
        self.restrictionInfo = None
        self.discountValue = None
        self.discountStatus = None
        self.ownerId = None
        self.ownerType = None
        self.restrictType = None
        self.restrictValue = None
        self.availableDuration = None

    @property
    def stickerCollection(self):
        with suppress(KeyError, TypeError):
            self.author = userProfile(self.json["author"]).userProfile
            self.status = self.json["status"]
            self.collectionType = self.json["collectionType"]
            self.modifiedTime = self.json["modifiedTime"]
            self.bannerUrl = self.json["bannerUrl"]
            self.smallIcon = self.json["smallIcon"]
            self.stickersCount = self.json["stickersCount"]
            self.usedCount = self.json["usedCount"]
            self.icon = self.json["icon"]
            self.title = self.json["name"]
            self.collectionId = self.json["collectionId"]
            self.extensions = self.json["extensions"]
            self.iconSourceStickerId = self.json["extensions"]["iconSourceStickerId"]
            self.originalAuthor = userProfile(self.json["extensions"]["originalAuthor"]).userProfile
            self.originalCommunity = community(self.json["extensions"]["originalCommunity"]).community
            self.isActivated = self.json["isActivated"]
            self.ownershipStatus = self.json["ownershipStatus"]
            self.isNew = self.json["isNew"]
            self.availableComIds = self.json["availableNdcIds"]
            self.description = self.json["description"]
            self.restrictionInfo = self.json["restrictionInfo"]
            self.discountStatus = self.json["restrictionInfo"]["discountStatus"]
            self.discountValue = self.json["restrictionInfo"]["discountValue"]
            self.ownerId = self.json["restrictionInfo"]["ownerUid"]
            self.ownerType = self.json["restrictionInfo"]["ownerType"]
            self.restrictType = self.json["restrictionInfo"]["restrictType"]
            self.restrictValue = self.json["restrictionInfo"]["restrictValue"]
            self.availableDuration = self.json["restrictionInfo"]["availableDuration"]

        return self

class stickerCollectionList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([stk["author"] for stk in data]).userProfileList
        self.status = []
        self.collectionType = []
        self.modifiedTime = []
        self.bannerUrl = []
        self.smallIcon = []
        self.stickersCount = []
        self.usedCount = []
        self.icon = []
        self.name = []
        self.collectionId = []
        self.extensions = []
        self.isActivated = []
        self.ownershipStatus = []
        self.isNew = []
        self.availableComIds = []
        self.description = []
        self.iconSourceStickerId = []
        self.originalAuthor = []
        self.originalCommunity = []
        self.restrictionInfo = []
        self.discountValue = []
        self.discountStatus = []
        self.ownerId = []
        self.ownerType = []
        self.restrictType = []
        self.restrictValue = []
        self.availableDuration = []

    @property
    def stickerCollectionList(self):
        for x in self.json:
            try: self.status.append(x["status"])
            except (KeyError, TypeError): self.status.append(None)
            try: self.collectionType.append(x["collectionType"])
            except (KeyError, TypeError): self.collectionType.append(None)
            try: self.modifiedTime.append(x["modifiedTime"])
            except (KeyError, TypeError): self.modifiedTime.append(None)
            try: self.bannerUrl.append(x["bannerUrl"])
            except (KeyError, TypeError): self.bannerUrl.append(None)
            try: self.smallIcon.append(x["smallIcon"])
            except (KeyError, TypeError): self.smallIcon.append(None)
            try: self.stickersCount.append(x["stickersCount"])
            except (KeyError, TypeError): self.stickersCount.append(None)
            try: self.usedCount.append(x["usedCount"])
            except (KeyError, TypeError): self.usedCount.append(None)
            try: self.icon.append(x["icon"])
            except (KeyError, TypeError): self.icon.append(None)
            try: self.name.append(x["name"])
            except (KeyError, TypeError): self.name.append(None)
            try: self.collectionId.append(x["collectionId"])
            except (KeyError, TypeError): self.collectionId.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.iconSourceStickerId.append(x["extensions"]["iconSourceStickerId"])
            except (KeyError, TypeError): self.iconSourceStickerId.append(None)
            try: self.originalAuthor.append(userProfile(x["extensions"]["originalAuthor"]).userProfile)
            except (KeyError, TypeError): self.originalAuthor.append(None)
            try: self.originalCommunity.append(community(x["extensions"]["originalCommunity"]).community)
            except (KeyError, TypeError): self.originalCommunity.append(None)
            try: self.isActivated.append(x["isActivated"])
            except (KeyError, TypeError): self.isActivated.append(None)
            try: self.ownershipStatus.append(x["ownershipStatus"])
            except (KeyError, TypeError): self.ownershipStatus.append(None)
            try: self.isNew.append(x["isNew"])
            except (KeyError, TypeError): self.isNew.append(None)
            try: self.availableComIds.append(x["availableNdcIds"])
            except (KeyError, TypeError): self.availableComIds.append(None)
            try: self.description.append(x["description"])
            except (KeyError, TypeError): self.description.append(None)
            try: self.restrictionInfo.append(x["restrictionInfo"])
            except (KeyError, TypeError): self.restrictionInfo.append(None)
            try: self.discountStatus.append(x["restrictionInfo"]["discountStatus"])
            except (KeyError, TypeError): self.discountStatus.append(None)
            try: self.discountValue.append(x["restrictionInfo"]["discountValue"])
            except (KeyError, TypeError): self.discountValue.append(None)
            try: self.ownerId.append(x["restrictionInfo"]["ownerUid"])
            except (KeyError, TypeError): self.ownerId.append(None)
            try: self.ownerType.append(x["restrictionInfo"]["ownerType"])
            except (KeyError, TypeError): self.ownerType.append(None)
            try: self.restrictType.append(x["restrictionInfo"]["restrictType"])
            except (KeyError, TypeError): self.restrictType.append(None)
            try: self.restrictValue.append(x["restrictionInfo"]["restrictValue"])
            except (KeyError, TypeError): self.restrictValue.append(None)
            try: self.availableDuration.append(x["restrictionInfo"]["availableDuration"])
            except (KeyError, TypeError): self.availableDuration.append(None)

        return self

class message:
    def __init__(self, data):
        self.json = data
        self.author = None
        self.content = None
        self.includedInSummary = None
        self.isHidden = None
        self.messageId = None
        self.mediaType = None
        self.mediaValue = None
        self.chatBubbleId = None
        self.clientRefId = None
        self.chatId = None
        self.createdTime = None
        self.chatBubbleVersion = None
        self.type = None
        self.extensions = None
        self.sticker = None
        self.duration = None
        self.originalStickerId = None

    @property
    def message(self):
        with suppress(KeyError, TypeError):
            self.content = self.json["content"]
            self.includedInSummary = self.json["includedInSummary"]
            self.isHidden = self.json["isHidden"]
            self.messageId = self.json["messageId"]
            self.mediaType = self.json["mediaType"]
            self.chatBubbleId = self.json["chatBubbleId"]
            self.clientRefId = self.json["clientRefId"]
            self.chatId = self.json["threadId"]
            self.createdTime = self.json["createdTime"]
            self.chatBubbleVersion = self.json["chatBubbleVersion"]
            self.type = self.json["type"]
            self.mediaValue = self.json["mediaValue"]
            self.extensions = self.json["extensions"]
            self.duration = self.json["extensions"]["duration"]
            self.originalStickerId = self.json["extensions"]["originalStickerId"]
            self.sticker = sticker(self.json["extensions"]["sticker"]).sticker
            self.author = userProfile(self.json["author"]).userProfile

        return self

class messageList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([msg["author"] for msg in data]).userProfileList
        self.content = []
        self.includedInSummary = []
        self.isHidden = []
        self.messageId = []
        self.mediaType = []
        self.mediaValue = []
        self.chatBubbleId = []
        self.clientRefId = []
        self.chatId = []
        self.createdTime = []
        self.chatBubbleVersion = []
        self.type = []
        self.extensions = []
        self.sticker = []
        self.duration = []
        self.originalStickerId = []

    @property
    def messageList(self):
        for x in self.json:
            try: self.content.append(x["content"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.includedInSummary.append(x["includedInSummary"])
            except (KeyError, TypeError): self.includedInSummary.append(None)
            try: self.isHidden.append(x["isHidden"])
            except (KeyError, TypeError): self.isHidden.append(None)
            try: self.messageId.append(x["messageId"])
            except (KeyError, TypeError): self.messageId.append(None)
            try: self.mediaType.append(x["mediaType"])
            except (KeyError, TypeError): self.mediaType.append(None)
            try: self.chatBubbleId.append(x["chatBubbleId"])
            except (KeyError, TypeError): self.chatBubbleId.append(None)
            try: self.clientRefId.append(x["clientRefId"])
            except (KeyError, TypeError): self.clientRefId.append(None)
            try: self.chatId.append(x["threadId"])
            except (KeyError, TypeError): self.chatId.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.chatBubbleVersion.append(x["chatBubbleVersion"])
            except (KeyError, TypeError): self.chatBubbleVersion.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.mediaValue.append(x["mediaValue"])
            except (KeyError, TypeError): self.mediaValue.append(None)
            try: self.extensions.append(x["extensions"])
            except (KeyError, TypeError): self.extensions.append(None)
            try: self.duration.append(x["extensions"]["duration"])
            except (KeyError, TypeError): self.duration.append(None)
            try: self.originalStickerId.append(x["extensions"]["originalStickerId"])
            except (KeyError, TypeError): self.originalStickerId.append(None)
            try: self.sticker.append(sticker(self.json["extensions"]["sticker"]).sticker)
            except (KeyError, TypeError): self.sticker.append(None)

        return self

class communityStickerCollection:
    def __init__(self, data):
        self.json = data
        self.stickerCollectionCount = None
        self.sticker = None

    def communityStickerCollection(self):
        with suppress(KeyError, TypeError):
            self.stickerCollectionCount = self.json["stickerCollectionCount"]
            self.sticker = stickerCollectionList(self.json["stickerCollectionList"]).stickerCollectionList

        return self

class notificationList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([notf["author"] for notf in data]).userProfileList
        self.contextComId = []
        self.objectText = []
        self.objectType = []
        self.contextValue = []
        self.comId = []
        self.notificationId = []
        self.objectSubtype = []
        self.parentType = []
        self.createdTime = []
        self.parentId = []
        self.type = []
        self.contextText = []
        self.objectId = []
        self.parentText = []

    @property
    def notificationList(self):
        for x in self.json:
            try: self.parentText.append(x["parentText"])
            except (KeyError, TypeError): self.parentText.append(None)
            try: self.objectId.append(x["objectId"])
            except (KeyError, TypeError): self.objectId.append(None)
            try: self.contextText.append(x["contextText"])
            except (KeyError, TypeError): self.contextText.append(None)
            try: self.type.append(x["type"])
            except (KeyError, TypeError): self.type.append(None)
            try: self.parentId.append(x["parentId"])
            except (KeyError, TypeError): self.parentId.append(None)
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.parentType.append(x["parentType"])
            except (KeyError, TypeError): self.parentType.append(None)
            try: self.objectSubtype.append(x["objectSubtype"])
            except (KeyError, TypeError): self.objectSubtype.append(None)
            try: self.comId.append(x["ndcId"])
            except (KeyError, TypeError): self.comId.append(None)
            try: self.notificationId.append(x["notificationId"])
            except (KeyError, TypeError): self.notificationId.append(None)
            try: self.objectText.append(x["objectText"])
            except (KeyError, TypeError): self.objectText.append(None)
            try: self.contextValue.append(x["contextValue"])
            except (KeyError, TypeError): self.contextValue.append(None)
            try: self.contextComId.append(x["contextNdcId"])
            except (KeyError, TypeError): self.contextComId.append(None)
            try: self.objectType.append(x["objectType"])
            except (KeyError, TypeError): self.objectType.append(None)

        return self

class adminLogList:
    def __init__(self, data):
        self.json = data
        self.author = userProfileList([adm["author"] for adm in data]).userProfileList
        self.createdTime = []
        self.objectType = []
        self.operationName = []
        self.comId = []
        self.referTicketId = []
        self.extData = []
        self.operationDetail = []
        self.operationLevel = []
        self.moderationLevel = []
        self.operation = []
        self.objectId = []
        self.logId = []
        self.objectUrl = []
        self.content = []
        self.value = []

    @property
    def adminLogList(self):
        for x in self.json:
            try: self.createdTime.append(x["createdTime"])
            except (KeyError, TypeError): self.createdTime.append(None)
            try: self.objectType.append(x["objectType"])
            except (KeyError, TypeError): self.objectType.append(None)
            try: self.operationName.append(x["operationName"])
            except (KeyError, TypeError): self.operationName.append(None)
            try: self.comId.append(x["ndcId"])
            except (KeyError, TypeError): self.comId.append(None)
            try: self.referTicketId.append(x["referTicketId"])
            except (KeyError, TypeError): self.referTicketId.append(None)
            try: self.extData.append(x["extData"])
            except (KeyError, TypeError): self.extData.append(None)
            try: self.content.append(x["extData"]["note"])
            except (KeyError, TypeError): self.content.append(None)
            try: self.value.append(x["extData"]["value"])
            except (KeyError, TypeError): self.value.append(None)
            try: self.operationDetail.append(x["operationDetail"])
            except (KeyError, TypeError): self.operationDetail.append(None)
            try: self.operationLevel.append(x["operationLevel"])
            except (KeyError, TypeError): self.operationLevel.append(None)
            try: self.moderationLevel.append(x["moderationLevel"])
            except (KeyError, TypeError): self.moderationLevel.append(None)
            try: self.operation.append(x["operation"])
            except (KeyError, TypeError): self.operation.append(None)
            try: self.objectId.append(x["objectId"])
            except (KeyError, TypeError): self.objectId.append(None)
            try: self.logId.append(x["logId"])
            except (KeyError, TypeError): self.logId.append(None)
            try: self.objectUrl.append(x["objectUrl"])
            except (KeyError, TypeError): self.objectUrl.append(None)

        return self

class lotteryLog:
    def __init__(self, data):
        self.json = data
        self.awardValue = None
        self.parentId = None
        self.parentType = None
        self.objectId = None
        self.objectType = None
        self.createdTime = None
        self.awardType = None
        self.refObject = None

    @property
    def lotteryLog(self):
        with suppress(KeyError, TypeError):
            self.awardValue = self.json["awardValue"]
            self.parentId = self.json["parentId"]
            self.parentType = self.json["parentType"]
            self.objectId = self.json["objectId"]
            self.objectType = self.json["objectType"]
            self.createdTime = self.json["createdTime"]
            self.awardType = self.json["awardType"]
            self.refObject = self.json["refObject"]

        return self