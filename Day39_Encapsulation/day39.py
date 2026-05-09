class BankAccount:
    def __init__(self, balance):
        # Private variable (__ lagane se bahar access nahi hota)
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposit ho gaya! ✅")

    def show_balance(self):
        # Bahar se balance sirf is method ke zariye dikhega
        print(f"Current Balance: {self.__balance}")

# Object banana
acc = BankAccount(1000)

# 1. Direct access try karna (Ye error dega ya kaam nahi karega)
# print(acc.__balance) 

# 2. Method ke zariye access karna
acc.deposit(500)
acc.show_balance()