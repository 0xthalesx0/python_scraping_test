from bs4 import BeautifulSoup as bs
import requests


def get_login_token(raw_resp):
    soup = bs(raw_resp.text, 'lxml')
    token = [n.get('value', '') for n in soup.find_all('input')
             if n.get('name', '') == 'wpLoginToken']
    return token[0]


class Website:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        payload = self.create_payload()

        with requests.session() as s:
            resp = s.get('https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Curitiba')
            payload['wpLoginToken'] = get_login_token(resp)

            response_post = s.post(
                'https://en.wikipedia.org/w/index.php?title=Special:UserLogin&returnto=Curitiba',
                data=payload)
            return response_post.text

    def create_payload(self):
        return {
            'wpName': f'{self.username}',
            'wpPassword': f'{self.password}',
            'wploginattempt': 'Log in',
            'wpEditToken': "+\\",
            'title': "Special:UserLogin",
            'authAction': "login",
            'force': "",
            'wpForceHttps': "1",
            'wpFromhttp': "1",
            # 'wpLoginToken': '',
        }
