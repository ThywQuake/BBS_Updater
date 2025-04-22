import requests
from bs4 import BeautifulSoup
from utils.basic import get_config, derive_data, validate_post
from time import sleep

config = get_config()

class Authenticate:
    def __init__(self):
        self.username = config['AUTHENTICATE']['account']['username']
        self.password_md5 = config['AUTHENTICATE']['account']['password_md5']
        self.url = config['AUTHENTICATE']['url']
        self.headers = config['AUTHENTICATE']['headers']
        
    def login(self):
        data = {
            'username': self.username,
            'password1': self.password_md5
        }
        response = requests.post(self.url, headers=self.headers, data=data)
        if response.status_code != 200:
            print("Failed to login")
            raise Exception("Failed to login")
        else:
            # print("Successfully logged in")
            return response.cookies

class Get:
    def __init__(self):
        self.url = config["GET"]["url"]
        self.headers = config["GET"]["headers"]
        self.cookies = Authenticate().login()
        self.headers["Cookie"] = "token=" + self.cookies.get_dict()['token']
        self.soup = self._soup()
        
    def _soup(self):
        response = requests.get(self.url, headers=self.headers)
        if response.status_code != 200:
            print("Failed to fetch the page")
            raise Exception("Failed to fetch the page")
        print("Successfully fetched the page")
        soup = BeautifulSoup(response.text, "html.parser")
        return soup
    
    @property
    def main_floor(self):
        return self.soup.find_all("div", class_="textblock", id="floor0")[0]
    
    @property
    def tables(self):
        return self.soup.find_all("table", class_="contenttable")
    
    @property
    def table1(self):
        return derive_data(self.tables[0], "temp/table1.csv")
    
    @property
    def table2(self):
        return derive_data(self.tables[1], "temp/table2.csv")

class Post:
    def __init__(self):
        self.url = config["POST"]["url"]
        self.headers = config["POST"]["headers"]
        self.cookies = Authenticate().login()
        self.headers["Cookie"] = "token=" + self.cookies.get_dict()['token']
        
    def post(self, data):
        print("Check twice! Is the page you want to post correctly?")
        sleep(2) # wait 2 second
        validate_post(data)
        if input("Do you want to post the page? (y/N) ") in ['y', 'Y', 'yes', 'Yes']:
            print('Updating...')
        else:
            raise Exception('Update canceled.')
            
        response = requests.post(self.url, headers=self.headers, data=data)
        if response.status_code != 200:
            print("Failed to update the page")
            raise Exception("Failed to update the page")
        else:
            print("Successfully updated the page")
    

if __name__ == "__main__":
    print(Get().table1, Get().table2)