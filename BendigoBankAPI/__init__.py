import requests
from bs4 import BeautifulSoup
import re
import json

class BendigoBankAPI:

    loginEndpoint = "https://banking.bendigobank.com.au/Logon/login.page"
    userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"

    username = None
    password = None
    securityToken = None

    accounts = []

    loginSession = None

    def login(self):
        r = self.loginSession.get(self.loginEndpoint)
        soup = BeautifulSoup(r.text, 'html.parser')
        viewstate = soup.find("input", {"name": "javax.faces.ViewState"})['value']
        # Login to the website URL
        loginPostData = {
            'loginForm:username': self.username,
            'loginForm:password': self.password,
            'loginForm:authenticationkey': '',
            'loginForm_SUBMIT': 1,
            'javax.faces.ViewState': viewstate,
            'tempPin': 'false',
            'loginForm:_idcl': 'loginForm:logon'
        }
        self.loginSession.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
        loginResponse = self.loginSession.post(self.loginEndpoint, data=loginPostData, allow_redirects=True)
        soup = BeautifulSoup(loginResponse.text, 'html.parser')
        if soup.find("input", {"name": "loginForm:username"}) is not None:
            raise AuthenticationError

        account_data = soup.find('script', {'id': 'data'})
        account_data_m = re.search('window\.__DATA__ = (.*);', account_data.text)
        accounts = json.loads(account_data_m.group(1))
        for account_json in accounts['accounts']:
            a = BBAccount(account_json['id'], account_json['name'],
                          account_json['accountNumber'], account_json['availableBalance'], account_json['bsb'])
            self.accounts.append(a)

    def get_accounts(self):
        return self.accounts

    def get_account_by_name(self, name):
        for account in self.accounts:
            if account.get_name().lower() == name.lower():
                return account

        return None

    def __init__(self, username, password):
        self.loginSession = requests.session()
        self.loginSession.headers.update({'User-Agent': self.userAgent})
        self.username = username
        self.password = password

        # Login to the API
        self.login()

class BBAccount:

    def __init__(self, id, name, number, available_balance, bsb):
        self.name = name
        self.number = number
        self.available_balance = available_balance
        self.bsb = bsb

    def get_account_number(self):
        return self.number

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.available_balance

    def get_bsb(self):
        return self.bsb

class AuthenticationError(Exception):
    def __init__(self, msg=None):
        if msg is None:
            msg = "Invalid credentials"

        super(AuthenticationError, self).__init__(msg)
