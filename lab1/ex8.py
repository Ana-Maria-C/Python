def tenToTwo(number):
    result="0"
    while number>0:
        bin=number%2
        result =str(bin)+ result
        number= number//2
    return result

def countOne(sir):
    count=0
    for ch in sir:
        if ch=='1':
            count+=1
    return count

def main():
    number=24
    binar=tenToTwo(number)
    result=countOne(binar)
    print(f"Numarul de biti de 1 este: {result}")

main()