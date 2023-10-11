def findAinB(sir1, sir2):
    #functia count este o metoda a obiectului string care cauta un sir intr-un al sit si numara aparitiile
    count=sir2.count(sir1)
    return count

def main():
    sir1=input("Introduceti primul sir: ")
    sir2=input("Introduceti al doilea sir: ")
    result=findAinB(sir1, sir2)
    print(f"Primul sir se gaseste de {result} ori in al doilea sir")

main()