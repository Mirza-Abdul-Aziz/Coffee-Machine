class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposeable_cups = 9
    money = 550

    def __init__(self, water, milk, coffee_beans, disposeable_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposeable_cups = disposeable_cups
        self.money = money
    
    def buy(self):
        while True:
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
            #global water, milk, coffee_beans, disposeable_cups, money
            if choice == '1':
                if self.water >= 250 and self.coffee_beans >= 16 and self.disposeable_cups != 0:
                    print("I have enough resources, making you a coffee!")
                    self.water -= 250
                    self.coffee_beans -= 16
                    self.disposeable_cups -= 1
                    self.money += 4
                    break
                else:
                    if self.water < 250:
                        print("Sorry, not enough water!")
                        break
                    else:
                        if self.coffee_beans < 16:
                            print("Sorry, not enough coffee beans!")
                            break
                        else:
                            if self.disposeable_cups == 0:
                                print("Sorry, not enough disposeable cups!")
                                break
            else:
                if choice == '2':
                    if self.water >= 350 and self.milk >=75 and self.coffee_beans >= 20 and self.disposeable_cups != 0:
                        print("I have enough resources, making you a coffee!")
                        self.water -= 350
                        self.milk -= 75
                        self.coffee_beans -= 20
                        self.disposeable_cups -= 1
                        self.money += 7
                        break
                    else:
                        if self.water < 350:
                            print("Sorry, not enough water!")
                            break
                        else:
                            if self.milk < 75:
                                print("Sorry, not enough milk!")
                                break
                            else:
                                if self.coffee_beans < 20:
                                    print("Sorry, not enough coffee beans!")
                                    break
                                else:
                                    if self.disposeable_cups == 0:
                                        print("Sorry, not enough disposeable cups!")
                                        break
            
                else:
                    if choice == '3':
                        if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12 and self.disposeable_cups != 0:
                            print("I have enough resources, making you a coffee!")
                            self.water -= 200
                            self.milk -= 100
                            self.coffee_beans -= 12
                            self.disposeable_cups -= 1
                            self.money += 6
                            break
                        else:
                            if self.water < 2000:
                                print("Sorry, not enough water!")
                                break
                            else:
                                if self.milk < 100:
                                    print("Sorry, not enough milk!")
                                    break
                                else:
                                    if self.coffee_beans < 12:
                                        print("Sorry, not enough coffee beans!")
                                        break
                                    else:
                                        if self.disposeable_cups == 0:
                                            print("Sorry, not enough disposeable cups!")
                                            break
                    else:
                        if choice == "back":
                            break
    def fill(self):
        update_water = int(input("Write how many ml of water do you want to add:\n"))
        update_milk = int(input("Write how many ml of milk do you want to add:\n"))
        update_coffee_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        update_disposeable_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        #global water
        self.water += update_water
        #global milk
        self.milk += update_milk
        #global coffee_beans
        self.coffee_beans += update_coffee_beans
        #global disposeable_cups
        self.disposeable_cups += update_disposeable_cups
    def take(self):    
        #global money
        print("I gave you $" + str(self.money))
        self.money = self.money * 0
    def remaining(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.coffee_beans, "of coffee beans")
        print(self.disposeable_cups, "of disposeable cups")
        print(self.money, "of money")
    
    def action(self):
        while True:
            action = str(input("Write action (buy, fill, take, remaining, exit):\n"))
            if action == "buy":
                CoffeeMachine.buy(self)
            else:
                if action == "fill":
                    CoffeeMachine.fill(self)
                else:
                    if action == "take":
                        CoffeeMachine.take(self)
                    else:
                        if action == "remaining":
                            CoffeeMachine.remaining(self)
                        else:
                            if action == "exit":
                                break
coffeemachine1 = CoffeeMachine(400, 540, 120, 9, 550)
coffeemachine1.action()
