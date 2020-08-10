class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    _new_deposit = {}
    _new_deposit["amount"] = amount
    _new_deposit["description"] = description
    self.ledger.append(_new_deposit)

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      for key, value in item.items():
        if key == "amount":
          balance += value
    return balance

  def check_funds(self, amount):
    _current_balance = self.get_balance()
    if amount < _current_balance:
      return False
    else:
      return True

  def withdraw(self, amount, description):
    _is_available = self.check_funds(amount)
    if _is_available:
      _new_withdrawal = {}
      _new_withdrawal[amount] = -amount
      _new_withdrawal["description"] = description
      self.ledger.append(_new_withdrawal)
      return True
    else:
      return False

  def transfer(self, amount, category):
    pass

def create_spend_chart(categories):
  pass