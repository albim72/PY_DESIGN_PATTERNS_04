from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress','queue preparation baking ready')
PizzaDough = Enum('PizzaDough','thin thick')
PizzaSauce = Enum('PizzaSauce','tomato garlic')
PizzaTopping = Enum('PizzaTopping','mozarella double_mozarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3

