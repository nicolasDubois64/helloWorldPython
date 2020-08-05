import numpy as np
from typing import Any, Set
from helloWorldPython.src.features.DateUtils import isLeapYear

def myConcat(strA, strB="biere"):
    return strA + strB

def functionThatCallsMyConcat(s1, s2):
    tmp = myConcat(s1, s2) + "!"
    return tmp

def getIsLeapYearMsg(year):
    leapYear = isLeapYear(year)
    msg= str(year)
    if leapYear:
        msg = msg + " est bien une année bissextile!"
    else:
        msg = msg + " n'est pas une année bissextile!"
    return msg

def uniformize(str_to_uniform: str) -> str:
    uniformed_str = str_to_uniform.lower().replace('(', '') \
        .replace(')', '').replace('.', '')
    return uniformed_str

def distance(s1: Set[Any], s2: Set[Any]) -> float:
    inter_len = len(s1.intersection(s2))
    jaccard = inter_len / len(s1.union(s2))
    cosinus = inter_len / np.sqrt(len(s1)*len(s2))
    return (jaccard + cosinus) / 2

#For debug only
if __name__ == "__main__":
    print(getIsLeapYearMsg(2020))
    