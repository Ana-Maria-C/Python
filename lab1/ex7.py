def extractNumber(sir):
    n=len(sir)
    number=0
    for i in range(0,n):
        if sir[i] in "0123456789":
            while i<n and sir[i] in "0123456789":
                number=number*10+int(sir[i])
                i+=1
            return number

def main():
    sir="ana 123 ghjdk 46"
    result=extractNumber(sir)
    print(f"Numarul extras este: {result}")

main()