import random as r

hp = 0
coins = 0
damage = 0

def InitGame(InitHp, InitCoins, InitDamage):
    global hp
    global coins
    global damage

    hp = InitHp
    coins = InitCoins
    damage = InitDamage

    print('Здравия желаю, салага! Судьба у тебя не лёгкая, у тебя вечно проблемы. И мне всегда приходится прикрывать твою задницу. В этот раз ты отправился в долгое путешествие. Надеюсь хоть там у тебя не будет проблем. В общем удачной дороги.')
InitGame(1, 1, 1)