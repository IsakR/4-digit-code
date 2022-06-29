import random
import math

def randomnum(*args):
    num = "145689876543"
    four_digits = ""
    for i in range(4):
        four_digits = four_digits+ num[math.floor(random.random()*10)]
    PyScript.write("thebuttonid", "New number")
    console.log(four_digits) 
    document.getElementById("demo").innerHTML = four_digits
randomnum()

