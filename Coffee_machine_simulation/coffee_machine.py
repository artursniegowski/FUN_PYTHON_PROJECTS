coffee_type =    { 
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }}

class ResourcesManagment:
    """Manging the resources of the coffee machine"""
    # Starting resources
    def __init__(self, remaining_water_ml: int = 300, \
        remaining_milk_ml: int = 200, \
            remaining_coffee_g: int = 100):
        self._remaining_water_ml = remaining_water_ml # 300 ml
        self._remaining_milk_ml = remaining_milk_ml # 200 ml
        self._remaining_coffee_g = remaining_coffee_g # 100 g


    @property
    def _remaining_water_ml(self) -> int:
        return self.__remaining_water_ml

    @_remaining_water_ml.setter
    def _remaining_water_ml(self, value: int) -> None:
        if value < 0:
            print("watter has to be a positive value in ml")
            raise ValueError("water cant be nagative !!")
        else:
            self.__remaining_water_ml = value

    @property
    def _remaining_milk_ml(self) -> int:
        return self.__remaining_milk_ml

    @_remaining_milk_ml.setter
    def _remaining_milk_ml(self, value: int) -> None:
        if value < 0:
            print("milk has to be a positive value in ml")
            raise ValueError("milk cant be nagative !!")
        else:
            self.__remaining_milk_ml = value

    @property
    def _remaining_coffee_g(self) -> int:
        return self.__remaining_coffee_g

    @_remaining_coffee_g.setter
    def _remaining_coffee_g(self, value: int) -> None:
        if value < 0:
            print("coffee has to be a positive value in g")
            raise ValueError("coffee cant be nagative !!")
        else:
            self.__remaining_coffee_g = value


    def check_resources(self, water_needed: int = 0, \
        milk_needed: int = 0, coffee_needed: int = 0) -> bool:
        """Checking if enough resources in the coffee machine to make the coffee
        with set parameters
        """
        if water_needed:
            if water_needed > self._remaining_water_ml:
                print(f"Not enough water! Coffeemachine: {self._remaining_water_ml}ml < needed: {water_needed} ml")
                return False

        if milk_needed:
            if milk_needed > self._remaining_milk_ml:
                print(f"Not enough milk! Coffeemachine: {self._remaining_milk_ml}ml < needed: {milk_needed} ml")
                return False

        if coffee_needed:
            if coffee_needed > self._remaining_coffee_g:
                print(f"Not enough coffee! Coffeemachine: {self._remaining_coffee_g}g < needed: {coffee_needed} g")
                return False

        return True

    def deduct_resources(self, water_needed: int = 0, \
        milk_needed: int = 0, coffee_needed: int = 0) -> bool :
        """Checking if enough resources in the coffee machine to make the coffee
        with set parameters, if yes deduct them and return True if successful,
        otherwise false 
        """
        if self.check_resources(water_needed,milk_needed,coffee_needed):

            self._remaining_water_ml -= water_needed
            self._remaining_milk_ml -= milk_needed
            self._remaining_coffee_g -= coffee_needed
            return True
        else :
            return False


class MoneyManagment:
    """Managing the money system of the coffee machine"""
    def __init__(self, money: float = 0.00) -> None:
        self._money = money
        self._money_coins_count = {'penny': 0, 'nickel': 0, 'dime': 0, 'quarter': 0}


    def add_coin(self, amount: int, coin_name :str) -> None:
        """base for adding a coins"""
        if amount >= 0:
            self._money_coins_count[coin_name] += amount 
        else:
            print(f"number of {coin_name} coins has to be grater than 0")
            raise ValueError(f"number of {coin_name} coins has to be grater than 0 !!")

    def add_penny(self, amount: int, coin_name :str = 'penny') -> None:
        """Adding pennies to the Cofee-machine """
        self.add_coin(amount,coin_name)

    def add_nickel(self, amount: int, coin_name :str = 'nickel') -> None:
        """Adding nickels to the Cofeemachine """
        self.add_coin(amount,coin_name)

    def add_dime(self, amount: int, coin_name :str = 'dime') -> None:
        """Adding dime to the Cofeemachine """
        self.add_coin(amount,coin_name)

    def add_quarter(self, amount: int, coin_name :str = 'quarter') -> None:
        """Adding quarters to the Cofeemachine """
        self.add_coin(amount,coin_name)

    @property
    def _money(self) -> float:
        return round(self.__money,2)

    @_money.setter
    def _money(self, value: float) -> None:
        if value < 0.00:
            print("money cant be negative")
            raise ValueError("money cant be nagative !!")
        else:
            self.__money = round(float(int(value*100)/100),2)


    def calculate_coins(self) -> float:
        """Return the value of inserted coins"""
        total_inserted = 0.00 
        for key, value in self._money_coins_count.items():
            if key == 'penny':
                total_inserted += 0.01 * value
            elif key == 'nickel':
                total_inserted += 0.05 * value
            elif key == 'dime':
                total_inserted += 0.10 * value
            elif key == 'quarter':
                total_inserted += 0.25 * value
        return total_inserted
    
    def reset_coins_inseted(self) -> None:
        """Reseting the coins inserted"""
        self._money_coins_count = {key:0 for key in self._money_coins_count }
    
    def take_money(self, price: float) -> None:
        """coffee machine takes the money for the coffee"""
        self._money += price

    def insert_coin(self, message: str) -> int: 
        """retriving the numbers of coins inserted"""
        coins_amount = input(f"How many {message}?: ")
        coins_amount = coins_amount.strip()
        try: 
            coins_amount = int(coins_amount)
        except ValueError:
            print(f"{coins_amount} This is not a valid number > 0 !! TRY AGAIN !")
            coins_amount = self.insert_coin(message)
        except Exception as e:
            print(f"Exception {e} was caught")
            print(type(e))
            raise Exception
        else: 
            if coins_amount < 0:
                print(f"{coins_amount} This is not a valid number > 0 !! TRY AGAIN !")
                coins_amount = self.insert_coin(message)

        return coins_amount

    def insert_coin_penny(self) -> None:
        """Adding the amount of pennies coins into the machine"""
        self.add_penny(self.insert_coin('pennies'))
    
    def insert_coin_nickel(self) -> None:
        """Adding the amount of nickels coins into the machine"""
        self.add_nickel(self.insert_coin('nickels'))

    def insert_coin_dime(self) -> None:
        """Adding the amount of dimes coins into the machine"""
        self.add_dime(self.insert_coin('dimes'))

    def insert_coin_quarter(self) -> None:
        """Adding the amount of quarters coins into the machine"""
        self.add_quarter(self.insert_coin('quarters'))



class CoffeeMachine(MoneyManagment, ResourcesManagment):
    """Managing coffee machine"""
    def __init__(self) -> None:
        MoneyManagment.__init__(self)
        ResourcesManagment.__init__(self)

    def shutting_down_maintenance(self) -> None:
        """shutting down for maintenance"""
        print("Shutting down for maintenance !!")

    def order_coffee(self, coffee: str) -> None:
        """Ordering coffee"""
        water = coffee_type[coffee]['ingredients'].get("water",0)
        milk = coffee_type[coffee]['ingredients'].get("milk",0)
        coffee_g = coffee_type[coffee]['ingredients'].get("coffee",0)
        coffee_cost = coffee_type[coffee].get("cost",0)
        if self.check_resources(water,milk,coffee_g) :
            self.insert_coin_quarter()
            self.insert_coin_dime()
            self.insert_coin_nickel()
            self.insert_coin_penny()
            
            total_inserted_coins = self.calculate_coins()
            if total_inserted_coins >= coffee_cost:
                self.take_money(coffee_cost)
                total_inserted_coins -= coffee_cost
                self.deduct_resources(water,milk,coffee_g)

                total_inserted_coins = round(float(int(total_inserted_coins*100)/100),2)
                print(f"Here is ${total_inserted_coins:.2f} in change!")
                print(f"Enjoy your {coffee} Enjoy!")
            else:
                total_inserted_coins = round(float(int(total_inserted_coins*100)/100),2)
                print(f"Coffee {coffee} costs ${coffee_cost}. You have inserted only: {total_inserted_coins:.2f}")
                print("Try again")
            
            self.reset_coins_inseted()

        
    def make_report(self) -> None:
        """Printing the status of the coffee machine"""
        print(self)

    def __str__(self) -> str:
        """changing the priniting view"""
        return ( 
            f"\nWater: {self._remaining_water_ml}ml \
            \nMilk: {self._remaining_milk_ml}ml \
            \nCoffee: {self._remaining_coffee_g}g \
            \nMoney: ${self._money}" 
            )