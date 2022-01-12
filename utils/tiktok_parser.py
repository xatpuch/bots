import requests
from bs4 import BeautifulSoup
import json
from random import choice

def get_profile_picture(username: str):
  url = f'https://tiktok.com/@{username}'  
  user_agents = [
    'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36',
    'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
  ]
  headers = {'User-Agent': choice(user_agents)}
  cookies = {
    'ttwid': '1%7CG_zi7Vrdki_18V0zGX_fqlU3s_cvWOntCt93eUjVbcQ%7C1632522289%7C48ff39b577059861d63fcebba8e118f618fdae17a5e12c07fef4822712e8d13c',
    'tt_webid': '7011629615140537857',
    's_v_web_id': 'verify_ktyxm3eu_9C3I3vSX_y9YG_4jOT_B0tp_EV6KdKcOD2Ng',
    'msToken': 'rpwgHWd5nNH5O8XsGd0f1FR9tMx-yaToMOpYMY_oH2D_WRy6UZNnh-bBN8OOCl_rtK5tKu5i8JI09avqA37MzZSBjmJCD2ER8NDBLk8dgPk9WGUzN5NqcuvLNOonjQkiT1pN06g=',
    'tt_csrf_token': 'kmXAOf-v9YIs_jEAn7Xdav2r',
    'tt_webid_v2': '7011629615140537857'
  }
  # r = requests.get(url, headers=headers, cookies=cookies)
  # soup = BeautifulSoup(r.text, 'html.parser')
  # content = soup.find_all("script", attrs={"type":"application/json", "crossorigin":"anonymous"})
  # content = json.loads(content[0].contents[0])
  # profile_picture = content["props"]["pageProps"]["userInfo"]["user"]["avatarLarger"]
  return 0