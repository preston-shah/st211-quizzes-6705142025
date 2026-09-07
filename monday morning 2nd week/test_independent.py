from bank import BankAccount

def test_deposite_independant():
    account = BankAccount(balance=100)
    account.deposite(50)
    assert new_balance == 150

 def test_withdraw_indepependent():
    account = BankAccount (100)
    account.withdraw(50)
    assert account.balance == 50   