import requests
import error_lib
import json


class BoxmateAPI:
    def __init__(self, api_token: str):
        self.api_session = requests.session()
        self.api_root_page = "https://api.boxmateapp.co.uk"
        self.api_token = api_token

    def api_call(self, endpoint: str) -> dict:
        """ Standard API call with correct token payload """
        api_call = self.api_root_page + endpoint
        print(api_call)
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
        api_endpoint = f"/exercise/{exercise_id}/scores"
        r = self.api_call(api_endpoint)
        return r


if __name__ == '__main__':
    with open("token_config.json", 'r') as token_file:
        token_json = json.load(token_file)
        API_TOKEN = token_json['token']
    tester = BoxmateAPI(API_TOKEN)
    tester.exercise_scores(217)
