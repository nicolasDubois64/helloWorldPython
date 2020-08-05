###########Varaible permutation
pA = "A"
pB = "B"
#print("pA => " + " " + pA + " et pB => " + pB)
pA, pB = pB, pA
#print("pA => " + " " + pA + " et pB => " + pB + "\n")

###########type() is the new instanceof"
type("OSS117")

###########the importance of indentation in the python
age = 62
ageLegalPourBoire = 18
msg = ""
if age >= ageLegalPourBoire:
    msg = "Félicitation tu es assez vieux pour boire"
else:
    msg = "Too bad, pas de Get27 pour toi"

########## Définition d'une fonction
#In python the signature of a function is based only on the name, so no override
def getUserMsg(name, age=10):
    return name + " a " + str(age) + " ans."

########## Call function
getUserMsg("Jean Hubert", 62)
#Use default value
getUserMsg("Toto") 

########## Lambdas
f = lambda x, y : x + y
#print(str(f(40,2)))

########## Tests import
degre = -7

# with 'import' we are loading the entire math library
#import math 
#absDegre = math.fabs(degre)

#we only load the fabs function in the main namespace (so no need to do math.fabs)
from math import fabs 
absDegre = fabs(degre)
#from math import * => on importe tout dans la namespace principal

########## to pause the program
#import os
#os.system("pause")

########## we test the modularity of python
from helloWorldPython.src.features.DateUtils import isLeapYear
myYear = 2020
leapYearMsg = str(myYear)
if isLeapYear(myYear): leapYearMsg + " est  bien bissextile"
else: leapYearMsg + " n'est  pas bissextile"

########## we test python class
from helloWorldPython.src.models.PokeMonster import PokeMonster
raMomo = PokeMonster("Ramoloss", "eau")
raMomo.printInfos()






