import math
import random

#Pokemon Damage Calculator

#A Lv. 90 Charizard (Fire/Flying, Sp. Atk: 205) attacks a Lv. 95
#Feraligatr (Water, Sp. Def: 188) with Fire Blast, a Fire-type move
#with a Power of 110 and gains a same-type attack bonus.. It hits
#the target normally but deals a not very effective damage. The
#weather on the field is normal. Given the following conditions,
#determine how much damage Charizard’s attack will deal.

pkm = {
    "level":90,  "attack":205, "defense":188, "power":110}

poke_modif = {
    "target":1,
    "weather":1,
    "badge":1,
    "critical":1,
    "random":random.randint(85,100)/100,
    "stab1":1.5,
    "type1":0.5,
    "burn1":1,
    "misc1":1
}
modifier = math.prod(poke_modif.values())
dmg = ((((((2*pkm["level"])/5)+2)*pkm["power"]*pkm["attack"]/pkm["defense"])/50)+2)*modifier
print ("\nCharizard's Damage to Feraligatr is : ",round(dmg,2))