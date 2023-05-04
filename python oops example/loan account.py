class LoanAccount(Account):
    def _init_(self, principal_amount, instalment):
        self.principal_amount = principal_amount
        self.instalment = instalment
        super()._init_("SBI",  "CHENNIMALAI", 20298711731, "VIJAY")

    def loan(self):
        print("Bank Name: ", self.bankname)
        print("Branch Name: ", self.branch)
        print("Account Number :", self.acc_no)
        print("Customer Name :", self.holdername)
        print("Principal Amount :", self.principal_amount)
        print("Paid instalment: ", self.instalment)
        paid = int(input("enter instalment: "))
        a = self.principal_amount
        b = self.instalment
        for i in range(paid):
            a = a - b

            print(f"Paid instalment :{self.instalment}")
            print("Remaining Amount :", a)
            print()
