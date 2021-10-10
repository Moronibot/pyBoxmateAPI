import requests
import error_lib
import json

class BoxmateAPI:
    def __init__(self, api_token: str):
        self.api_session = requests.session()
        self.api_root_page = "https://api.boxmateapp.co.uk"
        self.api_token = api_token

    @staticmethod
    def keep_list_items(big_list, items_to_keep):
        """ Only keeps keys you want from a list of dicts """
        set_items_to_keep = set(items_to_keep)
        list_to_ret = []
        for n_dict in big_list:
            filter_dict = {key: value for (key, value) in n_dict.items() if key in set_items_to_keep}
            list_to_ret.append(filter_dict)
        return list_to_ret

    def api_call(self, endpoint: str) -> dict:
        """ Standard API call with correct token payload """
        api_call = self.api_root_page + endpoint
        r = self.api_session.post(api_call, data={'member_token': self.api_token})
        return r

    def daily_update(self) -> dict:
        api_endpoint = '/members/activity'
        r = self.api_call(api_endpoint)
        return r

    def lookup_member(self, user_id: int) -> dict:
        """ Pulls recent activity of member """
        api_endpoint = f'/members/activity/{user_id}'
        r = self.api_call(api_endpoint)
        return r

    def exercise_scores(self, exercise_id: int) -> dict:
        api_endpoint = f"/exercise/{exercise_id}/"
        r = self.api_call(api_endpoint)
        print(r)

    def check_scores(self, exercise_id: int, m_or_f: str) -> list:
        """ Pulls up the leaderboard for an exercise """
        api_endpoint = f"/exercise/{exercise_id}/scores"
        score = self.api_call(api_endpoint)
        leaderboard = []
        for entries in score['leaderboard_results']:
            if entries['score_member_gender'] == m_or_f:
                leaderboard.append(entries)
        name_score = ['score_member_name', 'score']
        short_leaderboard = self.keep_list_items(leaderboard, name_score)
        return short_leaderboard


if __name__ == '__main__':
    with open("token_config.json", 'r') as token_file:
        token_json = json.load(token_file)
        API_TOKEN = token_json['token']
    tester = BoxmateAPI(API_TOKEN)
    tester.exercise_scores(57)
