from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

me=Menu()
comak=CoffeeMaker()
moma=MoneyMachine()


end=True
while end:
  options= me.get_items()
  a=input(f"What would you like? {options}☕: ").lower()
  if a=="off":
    end=False
  
  elif a=="report":
    comak.report()
    moma.report()

  elif a=="espresso" or "cappuccino" or "latte":
    drink=me.find_drink(a)
    if comak.is_resource_sufficient(drink) :
      if moma.make_payment(drink.cost) :
        comak.make_coffee(drink)



