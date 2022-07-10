from abc import ABC, abstractmethod

class IBank(ABC):
    def __init__(self, bank) -> None:
        super().__init__()
        self.bank = bank

    @abstractmethod
    def flatRate(self):
        pass


class Bank(IBank):
    def __init__(self, bank, loanAmount, loanYear, loanRate) -> None:
        super().__init__(bank)
        self.loanAmount = loanAmount
        self.loanYear = loanYear
        self.loanRate = loanRate
        self.loanRate = loanRate

    def flatRate(self):
        super().flatRate()
        self.interest = self.loanAmount * (self.loanRate/100) * self.loanYear
        self.monthlypay = (self.loanAmount + self.interest) / (self.loanYear * 12)

    def displayInterest(self):
        print(f"***** {self.bank} Loan Info *****")
        print(f"Loan: {self.loanAmount} Baht")
        print(f"Rate: {self.loanRate} %")
        print(f"Year: {self.loanYear}")
        print(f"-- Interest --")
        print(f"Interest: {self.interest} Baht")
        print(f"Monthly Repayment: {self.monthlypay} Baht")


loand = Bank("SCB", 100000, 2, 3.0)
loand.flatRate()
loand.displayInterest()
