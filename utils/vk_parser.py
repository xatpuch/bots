import vk_api
import json

with open('data/config.json') as json_file:
    config = json.load(json_file)
    VK_TOKEN = config['Bot_Data']['Vk_Token']

session = vk_api.VkApi(token=VK_TOKEN)
vk = session.get_api()

def get_user_data(user_id: str) -> dict:
    data = session.method('users.get', {'user_ids': user_id, 'fields': 'sex, photo_max'})
    data_dict = {'id': 0, 'first_name': '', 'last_name': '', 'sex': 0, 'photo': ''}
    data_dict['id'] = data[0]['id']
    data_dict['first_name'] = data[0]['first_name']
    data_dict['last_name'] = data[0]['last_name']
    data_dict['sex'] = data[0]['sex']
    data_dict['photo'] = data[0]['photo_max']
    return data_dict