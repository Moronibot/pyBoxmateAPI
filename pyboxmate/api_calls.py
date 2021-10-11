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
        r = self.api_session.post(api_call, data={'member_token': self.api_token})
        return r

    def daily_update(self) -> dict:
        api_endpoint = '/members/activity'
        r = self.api_call(api_endpoint)
        return r

    def lookup_member_details(self, user_id: int):
        api_endpoint = f'/members/details/{user_id}'
        r = self.api_call(api_endpoint)
        return r

    def lookup_member_activity(self, user_id: int):
        """ Pulls recent activity of member """
        api_endpoint = f'/members/activity/{user_id}'
        r = self.api_call(api_endpoint)
        return r

    def lookup_member_month(self, user_id: int):
        api_endpoint = f"/member/insights/this%20month/{user_id}"
        r = self.api_call(api_endpoint)
        print(len(r.json()))

    def exercise_scores(self, exercise_id: int) -> dict:
        api_endpoint = f"/exercise/{exercise_id}/scores"
        r = self.api_call(api_endpoint)
        return r

    def box_info(self):
        api_endpoint = "/member/home/main"
        r = self.api_call(api_endpoint)
        return r

    def check_notifications(self):
        api_endpoint = "/member/notifications"
        r = self.api_call(api_endpoint)
        return r

    # Class handling
    def get_timetable(self, year_month_day: str):
        api_endpoint = f"/teamup/customer/events/{year_month_day}"
        r = self.api_call(api_endpoint)
        return r

    def check_class_eligible(self, event_id: int):
        api_endpoint = f"/teamup/customer/events/{event_id}/eligibility"
        r = self.api_call(api_endpoint)
        return r

    def book_class(self, event_id: int):
        api_endpoint = f"/teamup/customer/events/{event_id}/register"
        r = self.api_call(api_endpoint)
        return r

    def cancel_class(self, event_id: int):
        api_endpoint = f"/teamup/customer/events/{event_id}/cancel"
        r = self.api_call(api_endpoint)
        return r

    def recent_attendances(self):
        api_endpoint = "/teamup/customer/attendances"
        r = self.api_call(api_endpoint)
        return r

if __name__ == '__main__':
    with open("token_config.json", 'r') as token_file:
        token_json = json.load(token_file)
        API_TOKEN = token_json['token']
    tester = BoxmateAPI(API_TOKEN)
    benedict = 40511
    me = 40535
    tester.lookup_member_month(me)