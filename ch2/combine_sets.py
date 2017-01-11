# -*- coding: utf-8 -*-

def card ():
    card = []
    rang = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    mast = ["C", "D", "H", "S"]
    for i in range(4):
        for j in range(13):
            card.append(mast[i]+rang[j])
    return card
print "Колода карт:", card()

def numbers():
    number = []
    letters = ["A","B","E","I","K","M","H","O","P","C","T","X"]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(len(letters)):
                        for n in range(len(letters)):
                            number.append(str(i)+str(j)+str(k)+str(l)+letters[m]+letters[n])
    return number
       
def dice ():
    s = 0 
    dice = []
    first = ["1", "2", "3", "4", "5", "6"]
    second = ["1", "2", "3", "4", "5", "6"]
    for i in range(6):
        for j in range(6):
            dice.append(first[i] + "," + second[j])
    for i in range(6):
        for j in range(6):
            if int(first[i])+int(second[j]) == 7:
                s += 1
    return dice, s
dice, s = dice()

print "Все возможные комбинации: ", dice
print "Кол-во комбинаций = 7:", s

