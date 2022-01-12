import requests 
from bs4 import BeautifulSoup as bs 
import fake_useragent
import json

def get_profile_photo(username):
    url = f'https://www.instagram.com/{username}/'
    ua = fake_useragent.UserAgent()
    headers = {'User-Agent': ua.random}
    cookies = {
        'sessionid': '48676036471%3Agfmoh1d0SJYMcq%3A15',
        'mid': 'YUoZtgALAAEkOM_i4xlegMYAprL7',
        'csrftoken': 'EGTIAdksljli2sd6B2Tzg3mtjqU2Won7',
        'ds_user_id': '48676036471',
        'ig_did': '41610527-88B5-4EA6-AE4C-DC59390DA079'
    }
    #response = requests.get(url, headers=headers, cookies=cookies).text
    soup = bs(response, features='lxml')
    #script = soup.find_all('script', {'type': 'text/javascript'})[3]
    #script_to_json = str(script).replace('<script type="text/javascript">window._sharedData = ', '')
    #script_to_json = script_to_json.replace(';</script>', '')
    #json_data = json.loads(script_to_json)
    #photo_url = json_data['entry_data']['ProfilePage'][0]['graphql']['user']['profile_pic_url_hd']
    return 0