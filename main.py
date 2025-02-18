

##BANK###

# Напишіть клас Банківський рахунок з атрибутами:
#  ім'я клієнта
#  баланс
#  валюта
#  словник з курсом валют(однаковий для всіх)
# Додайте методи:
#  вивід загальної інформації
#  перевірка чи відома валюта(якщо ні, викликати
# ValueError)
#  перевести гроші з однієї валюти в іншу(ця операція
# часто використовується, тому зрочно реалізувати
# окремим методом)
#  зміна валюти
#  поповнення балансу(валюта та сама)
#  зняття грошей з балансу(валюта та сама).


class BankAccount:
    # словник курсів валют (однаковий для всіх)
    exchange_rates = {
        "UAH": 1,  # базова валюта
        "USD": 40,  # 1 USD = 40 UAH
        "EUR": 44,  # 1 EUR = 44 UAH
        "GBP": 50  # 1 GBP = 50 UAH
    }

    def __init__(self, client_name, balance, currency):
        self.client_name = client_name
        self.balance = balance
        self.currency = currency.upper()
        self.check_currency(self.currency)  # Перевірка, чи валюта відома

    def check_currency(self, currency):
        """Перевіряє, чи вказана валюта присутня у словнику курсів."""
        if currency.upper() not in BankAccount.exchange_rates:
            raise ValueError(f"Невідома валюта: {currency}.")
        #return True

    def display_info(self):

        print(f"клієнт: {self.client_name}")
        print(f"Баланс: {self.balance:.2f} {self.currency}")
        print("Курси валют (до базової, UAH):")

        for curr, rate in BankAccount.exchange_rates.items():
            print(f"  {curr}: {rate}")


    def convert(self, amount, from_currency, to_currency):
        """
        Переводить суму з однієї валюти в іншу.
        Формула: amount * (rate_from / rate_to)
        """
        from_curr = from_currency.upper()
        to_curr = to_currency.upper()
        # Перевірка валют
        if from_curr not in BankAccount.exchange_rates or to_curr not in BankAccount.exchange_rates:
            raise ValueError("1 або 2 валюти невідомі")


        rate_from = BankAccount.exchange_rates[from_curr]
        rate_to = BankAccount.exchange_rates[to_curr]

        amount_in_base = amount * rate_from
        converted_amount = amount_in_base / rate_to
        return converted_amount

    def change_currency(self, new_currency):

        new_currency = new_currency.upper()
        self.check_currency(new_currency)

        if new_currency == self.currency:
            print("Нова валюта співпадає з поточною. Зміни не потрібні.")
        else:
            # Перераховуємо баланс у нову валюту
            new_balance = self.convert(self.balance, self.currency, new_currency)
            print(f"Зміна валюти з {self.currency} на {new_currency}.")
            print(f"Баланс: {self.balance:.2f} {self.currency} -> {new_balance:.2f} {new_currency}")
            self.balance = new_balance
            self.currency = new_currency

    def deposit(self, amount):

        if amount <= 0:
            print("Сума для поповнення має бути позитивною.")
        else:
            self.balance += amount
            print(f"Поповнення на {amount:.2f} {self.currency}. Новий баланс: {self.balance:.2f} {self.currency}")

    def withdraw(self, amount):

        if amount <= 0:
            print("Сума для зняття має бути позитивною.")
        elif amount > self.balance:
            print("Недостатньо коштів для зняття.")
        else:
            self.balance -= amount
            print(f"Зняття {amount:.2f} {self.currency}. Залишок: {self.balance:.2f} {self.currency}")


# Приклад :
try:
    account = BankAccount("Anna", 10030, "USD")
    account.display_info()

    print("\nПоповнення рахунку:")
    account.deposit(2000)

    print("\nЗняття коштів:")
    account.withdraw(1530)

    print("\nПеревід валюти:")
    account.change_currency("EUR")

    print("\nСпроба з невідомою валютою:")
    account.change_currency("ABC")  # ValueError

except ValueError as ve:
    print(f"Помилка: {ve}")

