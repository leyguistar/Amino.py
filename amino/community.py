import requests, json
from time import time
from amino.lib.util import exceptions
from urllib.request import urlopen

class Community:
    def __init__(self, ndcid: str):
        self.api = "https://service.narvii.com/api/v1"
        community_data = json.loads(requests.get(f"{self.api}/g/s-x{ndcid}/community/info").text)
        self.json = community_data["community"]
        self.name = community_data["community"]["name"]
        self.endpoint = community_data["community"]["endpoint"]
        self.url = community_data["community"]["link"]
        self.id = community_data["community"]["ndcId"]
        self.searchable = community_data["community"]["searchable"]
        self.user_added_topic_list = community_data["community"]["userAddedTopicList"]
        self.is_standalone_app_deprecated = community_data["community"]["isStandaloneAppDeprecated"]
        self.is_standalone_app_monetization_enabled = community_data["community"]["isStandaloneAppMonetizationEnabled"]
        self.listed_status = community_data["community"]["listedStatus"]
        self.probation_status = community_data["community"]["probationStatus"]
        self.keywords = community_data["community"]["keywords"]
        self.language = community_data["community"]["primaryLanguage"]
        self.heat = community_data["community"]["communityHeat"]
        self.content = community_data["community"]["content"]
        self.tagline = community_data["community"]["tagline"]
        self.icon = community_data["community"]["icon"]
        self.join_type = community_data["community"]["joinType"]
        self.status = community_data["community"]["status"]
        self.template_id = community_data["community"]["templateId"]
        self.created_at = community_data["community"]["createdTime"]
        self.modified_at = community_data["community"]["modifiedTime"]
        self.member_count = community_data["community"]["membersCount"]
        self.media = community_data["community"]["mediaList"]
        self.default_ranking_type_in_leaderboard = community_data["community"]["advancedSettings"]["defaultRankingTypeInLeaderboard"]
        self.front_page_layout = community_data["community"]["advancedSettings"]["frontPageLayout"]
        self.has_pending_review_request = community_data["community"]["advancedSettings"]["hasPendingReviewRequest"]
        self.welcome_message = community_data["community"]["advancedSettings"]["welcomeMessageEnabled"]
        self.welcome_message_content = community_data["community"]["advancedSettings"]["welcomeMessageText"]
        self.poll_min_full_bar_count = community_data["community"]["advancedSettings"]["pollMinFullBarVoteCount"]
        self.is_catalog_enabled = community_data["community"]["advancedSettings"]["catalogEnabled"]
        self.rank_table = community_data["community"]["advancedSettings"]["rankingTable"]
        self.only_allow_official_tag = community_data["community"]["configuration"]["general"]["onlyAllowOfficialTag"]
        self.video_upload_policy = community_data["community"]["configuration"]["general"]["videoUploadPolicy"]
        self.invite_permission = community_data["community"]["configuration"]["general"]["invitePermission"]
        self.disable_live_layer_visible = community_data["community"]["configuration"]["general"]["disableLiveLayerVisible"]
        self.premium_features = community_data["community"]["configuration"]["general"]["premiumFeatureEnabled"]
        self.guidelines = json.loads(requests.get(f"{self.api}/x{ndcid}/s/community/guideline").text)['communityGuideline']

        try: self.aliases = community_data["community"]["extensions"]["communityNameAliases"]
        except TypeError: return

    def __repr__(self):
        return f"{self.name}"

class Agent:
    def __init__(self, ndcid):
        self.api = "https://service.narvii.com/api/v1"
        community_data = json.loads(urlopen(f"{self.api}/g/s-x{ndcid}/community/info").read())
        self.json = community_data["community"]["agent"]
        self.name = community_data["community"]["agent"]["nickname"]
        self.uid = community_data["community"]["agent"]["uid"]
        self.level = community_data["community"]["agent"]["level"]
        self.following_status = community_data["community"]["agent"]["followingStatus"]
        self.account_membership_status = community_data["community"]["agent"]["accountMembershipStatus"]
        self.membership_status = community_data["community"]["agent"]["membershipStatus"]
        self.reputation = community_data["community"]["agent"]["reputation"]
        self.followers = community_data["community"]["agent"]["membersCount"]
        self.is_global = community_data["community"]["agent"]["isGlobal"]
        self.is_verified = community_data["community"]["agent"]["isNicknameVerified"]
        self.role = "Agent"

    def __repr__(self):
        return self.name

class Theme:
    def __init__(self, ndcid):
        self.api = "https://service.narvii.com/api/v1"
        community_data = json.loads(urlopen(f"{self.api}/g/s-x{ndcid}/community/info").read())
        self.json = community_data["community"]
        self.color = community_data["community"]["themePack"]["themeColor"]
        self.hash = community_data["community"]["themePack"]["themePackHash"]
        self.version = community_data["community"]["themePack"]["themePackRevision"]
        self.url = community_data["community"]["themePack"]["themePackUrl"]
        self.home_page_appearance = community_data["community"]["configuration"]["appearance"]["homePage"]["navigation"]
        self.left_side_panel_top = community_data["community"]["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level1"]
        self.left_side_panel_bottom = community_data["community"]["configuration"]["appearance"]["leftSidePanel"]["navigation"]["level2"]
        self.left_side_panel_color = community_data["community"]["configuration"]["appearance"]["leftSidePanel"]["style"]["iconColor"]
        self.custom_list = community_data["community"]["configuration"]["page"]["customList"]