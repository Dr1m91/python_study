
from HeroOfDonbass import *

#================================MAIN======================
myhero1 = HeroOfDonbass('Solider', 5, "Russian")
myhero2 = HeroOfDonbass('Pilot', 4, "KaZah")

myhero1.show_hero()
myhero1.move()
myhero1.level_up()
myhero2.show_hero()
myhero2.level_up()
myhero2.set_health(60)
myhero2.show_hero()