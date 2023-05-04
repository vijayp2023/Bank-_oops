class Account:
    def __init__(self, bankname, acc_no, branch, holdername):
        self.bankname = bankname
        self.branch = branch
        self.acc_no = acc_no
        self.holdername = holdername

    def acc_details(self):
        print(self.bankname)
        print(self.branch)
        print(self.acc_no)
        print(self.holdername)
