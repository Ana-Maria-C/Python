def isPalindrom(number):
    ok=True
    sir=str(number)
    n=len(sir)
    for i in range(0,n//2):
        if sir[i] != sir[-i-1]:
            ok=False
            break
    return ok

def main():
    number=input("Introduceti numarul: ")
    result=isPalindrom(number)
    if result==True:
        print("Numarul este palindrom")
    else:
        print("Numarul nu este palindrom")

main()