# Створіть наступні класи:
#  CreditCardPayment – атрибути currency
#  PayPalPayment – атрибути currency
#  CryptoPayment – атрибути currency
# Методи:
#  pay(amount) – виводить повідомлення
# o CreditCardPayment – оплата карткою {amount}{currency}
# o PayPalPayment – оплата PayPal {amount}{currency}
# o CryptoPayment – оплата криптогаманцем {amount}{currency}
# Напишіть функцію create_payment() яка запитує у
# користувача тип рахунку та потрібні атрибути і повертає
# об’єкт.


class CreditCardPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
       print(f"оплата карткою {amount} {self.currency}")


class PayPalPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата PayPal  {amount} {self.currency}")


class CryptoPayment:
    def __init__(self, currency):
        self.currency = currency

    def pay(self, amount):
        print(f"оплата криптогаманцем {amount} {self.currency}")


def create_payment():
    print("тип рахунку: creditcard, paypal, crypto")
    payment_type = input("Введіть тип рахунку: ").lower()
    currency = input("Введіть валюту: ")

    if  payment_type == "creditcard":
        return CreditCardPayment(currency)
    elif payment_type == "paypal":
        return PayPalPayment(currency)
    elif payment_type == "crypto":
        return CryptoPayment(currency)
    else:
        print("Помилка! тип рахунку: creditcard, paypal, crypto")

# Створіть декілька рахунків, добавте їх у список та для
# кожної викличте відповідні методи.

payments = []
for _ in range(3):
    payment = create_payment()
    if payment is not None:
        payments.append(payment)

for payment in payments:
    payment.pay(int(input("Введіть сумму: ")))