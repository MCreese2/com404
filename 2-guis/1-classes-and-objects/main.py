from Bot import Bot
from SuperBot import SuperBot
from FlyingBot import FlyingBot

#Creates an object "walle" with parameters of the bot class
walle = Bot("Wall-E", 15, 25, 20)

superwalle = SuperBot("Super Walle-E", 20, 30, 25, 15)

flyingsuperwalle = FlyingBot("Flying Super Walle-E", 25, 35, 30, 20, 5)

#Invoked the methods on the bot class
walle.display_name()
walle.display_age()
walle.display_energy()
walle.display_shield()

superwalle.display_name()
superwalle.display_age()
superwalle.display_energy()
superwalle.display_shield()
#invokes the superbot method
superwalle.display_super_power_level()

flyingsuperwalle.display_name()
flyingsuperwalle.display_age()
flyingsuperwalle.display_energy()
flyingsuperwalle.display_shield()
flyingsuperwalle.display_super_power_level()
#invokes the flying bot method
flyingsuperwalle.display_hover()

