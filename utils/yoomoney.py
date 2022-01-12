from yookassa import Configuration, Payment
import json
import uuid

import datetime
from yoomoney import Client, Quickpay

class PaymentYoo():
    type: str = None
    link: str = None
    amount = None
    code: str = None

    with open('data/config.json') as json_file:
        config = json.load(json_file)
    client = Client(config['Yoomoney_Key'])

    def create(self, amount: int, type: str):
        self.code = str(uuid.uuid4())
        self.type = type
        self.amount = amount
        pay = Quickpay(self.client.account_info().account, 'shop', 'Oplata', 'SB', amount, label=self.code)
        self.link = pay.base_url

    def invoice(self):
        return self.link

    def check_payment(self):
        start_date = datetime.datetime.now() - datetime.timedelta(minutes=15)
        for operation in self.client.operation_history(label=self.code, from_date=start_date).operations:
            if operation.status == 'success':
                return True
            else:
                return False