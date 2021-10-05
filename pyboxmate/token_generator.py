"""
Token generator tool.
"""
import requests


def generate_api_token(email: str, password: str) -> str:
    """ Generates an API token. This token does not expire. """
    api_root_page = "https://api.boxmateapp.co.uk"
    api_session = requests.session()
    login_url = api_root_page + "/member/authenticate"
    login_packet = {"Member_Email": email, "Member_Password": password}
    login_post = api_session.post(login_url, login_packet)
    if login_post.json()['success']:
        return login_post.json()['member_token']
    else:
        raise RuntimeError
