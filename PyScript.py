#script by Fauske
import random
import math


def rand_num(*args):
    num = "145689876543"
    four_digits = ""
    for i in range(4):
        four_digits = four_digits+ num[math.floor(random.random()*10)]
    PyScript.write("thebuttonid", "New number", print(four_digits))


rand_num()

