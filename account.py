class Account:
    '''
    class that represents bank account
    '''
    def __init__(self, name: str) -> None:
        '''
        constructor to create initial state of account object
        sets account balance to 0 for each object
        :param name: account first name
        '''
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: int) -> bool:
        '''
        function that deposits money into __account_balance.
        :param amount: amount to deposit
        :return: true if successful. false if unsuccessful
        '''
        if amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def withdraw(self, amount: int) -> str:
        '''
        function that withdraws money from __account_balance.
        :param amount: amount to withdraw
        :return: true if successful. false if unsuccessful
        '''
        if (amount <= 0) or (amount > self.__account_balance):
            return False
        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> str:
        '''
        function to access account balance
        :return: account's balance
        '''
        return self.__account_balance

    def get_name(self):
        ''''
        function to access account name
        :return: account's name
        '''
        return self.__account_name
