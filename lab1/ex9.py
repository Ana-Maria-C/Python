def findMaxCount(sir):
    newSir=[]
    count=[]
    for ch in sir:
        if ch in newSir:
            count[newSir.index(ch)]+=1
        else:
            newSir.append(ch)
            count.append(1)
    maxCount=max(count)
    chMaxIndex = count.index(maxCount)
    chMax = newSir[chMaxIndex]
    return (chMax,maxCount)

def main():
    sir="Ana are mere si are pere"
    chMax, maxCount=findMaxCount(sir)
    print(f"Cel mai intalnit caracter este {chMax} cu numarul de aparitii {maxCount}")

main()