def splitTheWords(sir):
    words=sir.split()
    return len(words)

def main():
    sir="Acesta este  un sir pe care l-am introdus"
    result=splitTheWords(sir)
    print(f"Numarul de cuvinte al sirului introdus este: {result}")

main()