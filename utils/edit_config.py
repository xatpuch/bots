import json

def edit_vk_token(token: str):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Vk_Token'] = token

    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def edit_subscription_required(value: bool):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Subscription_Required'] = value

    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def edit_channel_link(link: str):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Channel_Link'] = link

    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def edit_help_username(username: str):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Help_Username'] = username

    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def edit_referal_percentage(percentage: float):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Referal_Percentage'] = percentage

    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def add_admin(user_id: int):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Admins'].append(user_id)
    
    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def delete_admin(user_id: int):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
        config['Bot_Data']['Admins'].remove(user_id)
    
    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def edit_qiwi(number: str, token: str, nickname: str):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
    config['Bot_Data']['Qiwi_Wallet']['Nickname'] = nickname
    config['Bot_Data']['Qiwi_Wallet']['Number'] = number
    config['Bot_Data']['Qiwi_Wallet']['Token'] = token
    
    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file)

def edit_yoo(yid):
    with open('data/config.json', 'r') as json_file:
        config = json.load(json_file)
    config['Yoomoney_reciver'] = yid

    with open('data/config.json', 'w') as json_file:
        json.dump(config, json_file, indent=4)