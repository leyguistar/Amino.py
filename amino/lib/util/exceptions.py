# These are placeholders

class FailedLogin(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 100
class UnsupportedService(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 102 (API_STD_ERR_ENTITY_TOO_LARGE_RAW)
class FileTooLarge(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 103, 104
class InvalidRequest(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 105
class InvalidSession(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 106
class AccessDenied(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 107
class UnexistentData(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 113
# Be more specific, please.
class MessageNeeded(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 200
class InvalidAccountOrPassword(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 200
class EmailAlreadyRegistered(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 213
class InvalidEmail(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 214
class InvalidPassword(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 219
class AccountLimitReached(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 219
class TooManyRequests(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 221
class CantFollowYourself(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 225
class UserUnavailable(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 229
class YouAreBanned(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 230
class UserNotMemberOfCommunity(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 240
class ReachedTitleLength(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 246
class AccountDeleted(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 262
class ReachedMaxTitles(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 270
class VerificationRequired(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 291
# Whoa there! You've done too much too quickly. Take a break and try again later.
class CommandCooldown(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 300
class BadImage(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

 # AMINO ERROR 313
class InvalidThemepack(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 314
class InvalidVoiceNote(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 551
# This post type is restricted to members with a level X ranking and above.
class InsufficientLevel(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 702
class WallCommentingDisabled(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 805
class CommunityNameAlreadyTaken(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 801
# This Community no longer exists.
class CommunityNoLongerExists(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 802
# Sorry, this code or link is invalid.
class InvalidCodeOrLink(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 833
# This Community has been deleted.
class CommunityDeleted(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 1605
class ChatFull(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 1661
class LevelFiveRequiredToEnableProps(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 1663
class ChatViewOnly(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 2601
class AlreadyCheckedIn(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 2001
# Sorry, you have already submitted a membership request.
class AlreadyRequested(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 2611
class AlreadyUsedMonthlyRepair(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 2800
class AccountAlreadyRestored(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 4300
class NotEnoughCoins(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 4400
class AlreadyPlayedLottery(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

# AMINO ERROR 4500, 4501
class CannotSendCoins(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class SpecifyType(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnknownResponse(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class UnsupportedFileExtension(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NotLoggedIn(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NoCommunity(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NoChatThread(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class ChatRequestsBlocked(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class NoImageSource(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)

class CannotFetchImage(Exception):
    def __init__(*args, **kwargs):
        Exception.__init__(*args, **kwargs)
