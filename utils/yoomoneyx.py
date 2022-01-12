import sqlite3
import json
import random

import datetime
from yoomoney import Client, Quickpay

con = sqlite3.connect('payments.db')
cur = con.cursor()

class PaymentYoo():
    type: str = None
    link: str = None
    amount = None
    code: str = None
    checks: int = 0

    def create(self, amount: int, type: str):
        self.code = random.randint(100000, 999999)
        self.amount = amount
        self.type = type
        cur.execute(f'INSERT INTO yoomoney VALUES (0, "{self.amount}", "{self.code}", 0)')
        con.commit()

    def invoice(self):
        with open('data/config.json') as file:
            config = json.load(file)
        account = config['Yoomoney_reciver']
        pay = Quickpay(account, 'shop', 'oplata', 'SB', self.amount * 1.02, label=self.code)
        return pay.base_url

    def check_payment(self):
        completed = cur.execute(f'SELECT completed FROM yoomoney WHERE comment = "{self.code}"').fetchone()[0]
        if str(completed) == '1':
            self.checks += 1
            if self.checks == 1:
                return True
            elif self.checks == 2:
                cur.execute(f'DELETE FROM yoomoney WHERE comment = "{self.code}"')
                con.commit()
                return True
        else:
            return False
