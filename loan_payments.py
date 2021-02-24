class Loan:
    def __init__(self, principal, interest_rate, name):
        self.principal = principal
        self.interest_rate = interest_rate
        self.name = name

    def accrue(self):
        accrual = self.principal * self.interest_rate / 365
        self.principal += accrual

    def make_payment(self, amount):
        self.principal -= amount
        if self.principal < 0:
            return abs(self.principal)
        else:
            return 0

    def get_name(self):
        return self.name


def main():
    loanf = Loan(9000, 0.05990, "fixed")
    loanv = Loan(27000, 0.0274, "variable")


if __name__ == "__main__":
    main()
