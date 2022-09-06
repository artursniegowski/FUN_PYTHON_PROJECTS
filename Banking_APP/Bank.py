# banking class
import datetime

#################################
############## Bank class #######
#################################

class Bank:
    """
    class for handling all the bank transactions
    """

    bank_name = 'Santander'
    branch_name = 'nr.I branch in Warsaw'

    def __init__(self, balance: float = 0.0) -> None:
        self._balance = balance

    @property
    def _balance(self):
        return round(self.__balance,2)

    @_balance.setter
    def _balance(self, value: float):
        if value < 0.0:
            print("Balance cant be negative")
            raise ValueError("Balance cant be nagative !!")
        else:
            self.__balance = round(value,2)

    # Managing the account
    def deposit(self, value: float = 0.0) -> bool:
        """depositing money"""
        if value > 0:
            self._balance += value
            print(f"Deposited ${value:.2f} to your account")
            return True
        else:
            print("amount should be a positive value and greater than 0")
            return False

    def withdraw(self, value: float = 0.0) -> bool:
        """withdrawing money"""
        if value > 0:
            if self._balance - value >= 0:
                self._balance -= value
                print(f"${value:.2f} deducted from your account")
                return True
            else:
                print("Not enough funds on the account")
        else:
            print("amount should be a positive value and greater than 0")
        
        return False


    def check_balance(self) -> float:
        """checking the balance"""
        return self._balance


############################################
########### TransactionsLog class ##########
############################################

class TransactionsLog:
    """
    class for handling all the writing to file actions
    """
    
    def __init__(self, file_name: str ='transactions.txt') -> None:
        self.__file_name = file_name
        self.trans_number = 0

    @property
    def __file_name(self):
        return self.__file_name_full

    @__file_name.setter
    def __file_name(self, value: str):
        if isinstance(value,str):
            if '.txt' in value:
                self.__file_name_full = value
            else:
                print(f"{value} should have a .txt extension")
        else:
            print("The file name has to be a string !!")
    
    def generator_transaction_nr(self) -> int:
        """generator function for returning the transaction number"""
        while True:
            self.trans_number += 1
            yield self.trans_number


    def get_time(self) -> str:
        """returning current time from your system"""
        current_time = datetime.datetime.now()
        return f'Transaction nr.{next(self.generator_transaction_nr())} on : {current_time.day:02d}/{current_time.month:02d}/{current_time.year}  {current_time.hour:02d}:{current_time.minute:02d}:{current_time.second:02d}'

    def log_transaction(self, transaction: list[str]) -> None:
        """writing transaction to a file"""
        try:
            transaction = ['\n' + self.get_time()+'\n'] + transaction
            with open(self.__file_name,'a') as f:
                f.writelines(transaction)
        except Exception as e:
            print(f"Exception {e} was caught while writing the transaction")
            print(type(e))
        else : # if no exception caught
            print("Wrtiting transaction successful")
            

#######################################
############### User class ############
#######################################

class User(Bank,TransactionsLog):
    """
    class for handling the user data
    """

    def __init__(self, first_name: str ='', last_name: str='', balance: float = 0.0) -> None:
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        Bank.__init__(self,balance)
        TransactionsLog.__init__(self,file_name ='transactions.txt')

  # decorator function
    def transactionlogger(inner_func) :           
        def outer_func(self,value) :
            if inner_func(self,value):
                log_message = []
                log_message.append(f'Client: {self.first_name} {self.last_name} \n')
                transaction_type = 'not_defined' 
                if inner_func.__name__ == 'deposit':
                    transaction_type = 'deposited'
                elif inner_func.__name__ == 'withdraw':
                    transaction_type = 'withdrew'
                log_message.append(f'Transaction = {transaction_type}: ${value:.2f} , Balance Total: ${self.check_balance():.2f} \n')
                self.log_transaction(log_message)
        return outer_func
  
    @transactionlogger
    def deposit(self, value: float = 0.0) -> bool:
        return Bank.deposit(self,value)

    @transactionlogger
    def withdraw(self, value: float = 0.0) -> bool:
        return Bank.withdraw(self,value)


    def __str__(self) -> str:
        return ( 
            f"""\nBank: {self.bank_name} \nClient: {self.first_name} {self.last_name} \nBalance: {self.check_balance():.2f}$ \n""")