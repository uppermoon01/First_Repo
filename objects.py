from abc import abstractmethod
from constants_store import *

class Categories:
  @abstractmethod
  def return_discount(self):
    pass
  @abstractmethod
  def __init__(self, vehicle, fastag_balance):
    pass


class Truck(Categories):
  
  __category = HEAVY
  __price = PRICE_HEAVY
  
  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO
    

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    

  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY


  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category

  def get_price(self):
    return self.__price

  def get_discount(self):
    return self.__discount
  
  def get_trip(self):
    return self.__trip
    
  
class Bus(Categories):

  __category = HEAVY
  __price = PRICE_HEAVY

  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    
  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY


  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category

  def get_price(self):
    return self.__price

  def get_discount(self):
    return self.__discount

  def get_trip(self):
    return self.__trip
    
    
class Van(Categories):
   
  __category = LIGHT
  __price = PRICE_LIGHT
  
  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    
  
  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY

  
  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category  

  def get_price(self):
    return self.__price
  
  def get_discount(self):
    return self.__discount
  
  def get_trip(self):
    return self.__trip
    
    
    
class Car(Categories):

  __category = LIGHT
  __price = PRICE_LIGHT

  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO

  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category

  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY


  def get_price(self):
    return self.__price

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    

  def get_discount(self):
    return self.__discount

  def get_trip(self):
    return self.__trip
    


class Rikshaw(Categories):

  __category = LIGHT
  __price = PRICE_LIGHT

  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    

  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY


  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category

  def get_price(self):
    return self.__price

  def get_discount(self):
    return self.__discount

  def get_trip(self):
    return self.__trip
    


class Scooter(Categories):

  __category = TWOWHEELER
  __price = PRICE_TWOWHEELER

  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    

  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY

  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category

  def get_price(self):
    return self.__price

  def get_discount(self):
    return self.__discount

  def get_trip(self):
    return self.__trip
    


class Motorbike(Categories):

  __category = TWOWHEELER
  __price = PRICE_TWOWHEELER

  def __init__(self, vehicle, fastag_balance):
    self.__vehicle = vehicle
    self.__fastag_balance = fastag_balance
    self.__cash = ZERO
    self.__discount = ZERO
    self.__trip = ZERO

  def get_vehicle(self):
    return self.__vehicle

  def add_trip(self):
    self.__trip += ONE
    

  def get_cash(self):
    return self.__cash

  def set_cash(self, remaining):
    self.__cash += remaining + PENALTY


  def get_fastag_balance(self):
    return self.__fastag_balance

  def set_fastag_balance(self):
    self.__fastag_balance -= self.__price

  def get_category(self):
    return self.__category

  def get_price(self):
    return self.__price

  def get_discount(self):
    return self.__discount

  def get_trip(self):
    return self.__trip
    


