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
    if amount <= _current_balance:
      return True
    else:
      return False

  def withdraw(self, amount, description=""):
    _is_available = self.check_funds(amount)
    if _is_available:
      _new_withdrawal = {}
      _new_withdrawal["amount"] = -amount
      _new_withdrawal["description"] = description
      self.ledger.append(_new_withdrawal)
      return True
    else:
      return False

  def transfer(self, amount, category):
    _is_available = self.check_funds(amount)
    if _is_available:
      _withdraw_description = f"Transfer to {category.name}"
      _transfer_desc = f"Transfer from {self.name}"
      self.withdraw(amount, _withdraw_description)
      category.deposit(amount, _transfer_desc)
      return True
    else:
      return False

  # def make_decimal(self, amount):
  #   _two_places = Decimal(10) ** -2
  #   _decimal_amount = Decimal(amount).quantize(_two_places)
  #   return _decimal_amount

  def __str__(self):
    _no_of_asterix = 30 - len(self.name)
    _title = ""
    _each_row = ""
    if _no_of_asterix % 2 == 0:
      _asterix = _no_of_asterix / 2
      _title += f'*' * int(_asterix)
      _title += self.name
      _title += f'*' * int(_asterix)
    else:
      _asterix = _no_of_asterix // 2
      _title += f'*' * int(_asterix)
      _title += self.name
      _title += f'"*" * {(int(_asterix) + 1)}'
    #return _title

    for item in self.ledger:
      _string_amount = f'{item["amount"]:.2f}'
      _description = item["description"]
      _amount_lenght = len(_string_amount)
      _description_len = len(_description)

      if _amount_lenght > 7:
        _string_amount = _string_amount[:8]
    
      if _description_len > 23:
        _description = _description[:23]
      _spaces = f' ' * (30 - (len(_string_amount) + len(_description)))
      _each_row += f'\n{_description}{_spaces}{_string_amount}'
    
    _total = self.get_balance()
    _total = f'{_total:.2f}'
    _each_row +=f'\nTotal: {_total}'
    _each_row = _title + _each_row
    
    return _each_row

def create_spend_chart(categories):
  chart = f'Percentage spent by category\n'
  cat_names = []
  spendings = []
  #calculate percentages based on withdrawal
  for category in categories:
    cat_names.append(category.name)
    for transaction in category.ledger:
      withdrawals = 0
      if transaction["amount"] < 0:
        withdrawals += transaction["amount"]
    spendings.append(-withdrawals)
  total_spending = sum(spendings)
  spendings = [(spent/total_spending)*100 for spent in spendings]  
  #each category name should have same length as longest
  longest = len(max(cat_names, key=len))
  cat_names = [name + " " * (longest - len(name)) for name in cat_names]
  #plot chart
  #start with the y-axis
  plot = ""
  for i in range(100, -10, -10):
    vertical_axis = str(i).rjust(3) + "|"
    row_entry = " "
    for percentage in spendings:
      if percentage >= i:
        row_entry += "o  " 
      else:
        row_entry += "   "
    vertical_axis += row_entry
    plot += vertical_axis + "\n"
    #print(plot)
  #generate x-axis
  horizontal_axis = "    " + "-" * (len(cat_names) *3) + "-" + "\n"
  #generate x-axis labels
  labels = "     "
  for i in range(0, longest):
    for cat in cat_names:
      labels += cat[i] + "  "
    if i < longest-1:
      labels += "\n     "
  
  plot = chart + plot + horizontal_axis + labels
  return plot
  
    

  
  
