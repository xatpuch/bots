import random

def generate_phone_number():
    codes = ['915', '916', '925', '903', '968', '999', '901', '919']
    number = '+7' + random.choice(codes)
    for _ in range(7):
        number = number + str(random.randint(0, 9))
    return number

def get_random_archive():
    with open('data/archives.txt') as text:
        archives = text.readlines()
    choice = random.choice(archives)
    return choice

def get_random_photo():
    with open('data/photos.txt') as text:
        photos = text.readlines()
    choice = random.choice(photos)
    return choice

def get_random_messages():
    with open('data/messages.txt') as text:
        messages = text.readlines()
    choice = random.choice(messages)
    return choice

def get_random_friends():
    with open('data/friends.txt') as text:
        friends = text.readlines()
    choice = random.choice(friends)
    return choice