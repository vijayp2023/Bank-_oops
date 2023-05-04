class SavingAccount(Account):
    def __init__(self, acc_balance, debitcard_number):
        self.acc_balance = acc_balance
        self.debitcard_number = debitcard_number
        super()._init_("SBI",  "CHENNIMALAI", 20298711731, "VIJAY")


    def saving_acc(self, deposite, withdraw):
        deposite  = deposite + self.acc_balance
        withdraw  = deposite - withdraw
        print("Bank Name: ", self.bankname)
        print("Branch Name: ", self.branch)
        print("Account Number :", self.acc_no)
        print("Customer Name :", self.holdername)
        print("Balance :", self.acc_balance)
        print("Deposite :", deposite)
        print("After Deposit :", deposite)
        print("Withdraw :", withdraw)
        print("After Withdraw :", withdraw)
