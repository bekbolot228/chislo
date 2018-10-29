class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"You have {self.amount} {self.currency} "
    def convert(self):
        if currency == 'KGS':
            res = self.amount * 69
            print(f'Money ({self.amount} {self.currency}) = ' + str(res) + ' USD' )
        else:
            res = self.amount/69
            print(f'Money({self.amount} {self.currency}) = ' + str(res) + ' KGZ')

amount = float(input('Введите сумму денег: '))
currency = float(input('Введите фалюту USD или KGS:'))
som = Money(amount, currency)
print(som)
som.convert()