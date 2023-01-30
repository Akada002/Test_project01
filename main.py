'''importing numToString from numToString'''
from numToString import numToString

if __name__ == "__main__":
    integer = int(input())
    numToStringObj=numToString()
    p=numToStringObj.int2str(integer)
    print(p)