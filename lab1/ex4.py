def fromUtoL(sir):
    newsir=""
    for ch in sir:
        if ch.isupper():
            newsir+='_'
            newsir+=ch.lower()
        else:
            newsir+=ch
    return newsir

def main():
    sir=input("Introduceti sirul: ")
    result=fromUtoL(sir)
    print(f"Noul sir este {result}")

main()