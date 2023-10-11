# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# ex 1

def findGCD(*listOfNumbers):
    # functia math.gcd returneaza cmmdc a doua numere si face parte din libraria math pe care am importat o
    result=listOfNumbers[0]
    for i in listOfNumbers:
        result=math.gcd(int(result),int(i))
    return result

def main():
    n = int(input("Introduceti numarul de variabile: "))
    listOfNumebers=[]
    for i in range(0,n):
        listOfNumebers.append(input("Introduceti o noua variabila: "))
    result=findGCD(*listOfNumebers)
    print(f"Cel mai mare divizor comun este: {result}")

main()