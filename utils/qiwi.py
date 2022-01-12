import pyqiwi
import random
import datetime
import json

class Payment():
    amount: int = None
    comment: str = None
    type: str = None
    nickname: str = None
    number: str = None
    token: str = None
    wallet: pyqiwi.Wallet = None

    def create(self, amount: int, type: str):
        try:
            self.amount = amount
            self.comment = str(random.randint(100000, 999999))
            self.type = type
            with open('data/config.json') as json_file:
                config = json.load(json_file)
            self.nickname = config['Bot_Data']['Qiwi_Wallet']['Nickname']
            self.number = config['Bot_Data']['Qiwi_Wallet']['Number']
            self.token = config['Bot_Data']['Qiwi_Wallet']['Token']
        except:
            raise Exception('Qiwi wallet is banned')

    def invoice(self):
        link = f'''https://qiwi.com/payment/form/99999?amountInteger={str(self.amount)}&amountFraction=0&currency=643&extra%5B%27comment%27%5D={str(self.comment)}&extra%5B%27account%27%5D={str(self.nickname)}&blocked%5B0%5D=comment&blocked%5B1%5D=account&blocked%5B2%5D=sum&0%5Bextra%5B%27accountType%27%5D%5D=nickname'''
        return link

    def check_payment(self):
        self.wallet = pyqiwi.Wallet(self.token, self.number)
        start_date = datetime.datetime.now() - datetime.timedelta(minutes=15)
        transactions = self.wallet.history(start_date=start_date, operation='IN').get('transactions')
        for transaction in transactions:
            if (transaction.comment == self.comment) and (transaction.sum.amount == self.amount) and (transaction.sum.currency == 643):
                return True
        return False

def get_balance():
    with open('data/config.json') as json_file:
        config = json.load(json_file)
    number = config['Bot_Data']['Qiwi_Wallet']['Number']
    token = config['Bot_Data']['Qiwi_Wallet']['Token']
    wallet = pyqiwi.Wallet(token, number)
    balance = wallet.balance()
    return balance