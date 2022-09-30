"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        if self.commission==None:
            return self.contract.get_contractPay()
        else:
            return self.commission.get_commisionPay()+self.contract.get_contractPay()
    def __str__(self):
        str = f"{self.name} works on {self.contract}"
        if self.commission!= None:
            str +=  f" {self.commission}"
        return str+f".  Their total pay is {self.get_pay()}."
class Contract:
    def __init__(self,pay,hour=1):
        self.pay = pay
        self.hour = hour

    def get_contractPay(self):
        return self.pay*self.hour

    def __str__(self):
        if self.hour==1:
            return f"a monthly salary of {self.get_contractPay()}"
        else:
            return f"a contract of {self.hour} hours at {self.pay}/hour"

class Commision:
    def __init__(self, bonus, contracts=1):
        self.contracts = contracts
        self.bonus = bonus

    def get_commisionPay(self):
        return self.contracts*self.bonus

    def __str__(self):
        str = "and receives a "
        if self.contracts==1:
            str+= f"bonus commission of {self.bonus}"
        else:
            str+= f"commission for {self.contracts} contract(s) at {self.bonus}/contract"
        return str
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Contract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',Contract(25,100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',Contract(3000),Commision(200,4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',Contract(25,150),Commision(220,3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',Contract(2000),Commision(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',Contract(30,120),Commision(600))
