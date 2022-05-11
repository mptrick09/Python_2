

from turtle import position


my_wort={}
wort=input("Gib ein wort ein: ")
Alpbet_dict={
    "a":{"position":1},"b":{"position":2}, "c":{"position":3}, "d":{"position":4} ,
    "e":{"position":5}, "f":{"position":6},"g":{"position":7}, "h":{"position":8}, "i":{"position":9},"j":{"position":10},
    "k":{"position":11},"l":{"position":12}, "m":{"position":13}, "n":{"position":14},"o":{"position":15},
    "p":{"position":16},"q":{"position":17}, "r":{"position":18}, "s":{"position":19},"t":{"position":20},
    "u":{"position":21},"v":{"position":22}, "w":{"position":23}, "x":{"position":4},"y":{"position":25}, "z":{"position":26}
}
for i in wort:
    my_wort[i] = Alpbet_dict[i]["position"]
print(my_wort)



