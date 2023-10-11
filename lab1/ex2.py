vowels="aeiou"
def findVowels(sir):
    numbersOfVowels=0
    for character in sir:
        if character in vowels:
            numbersOfVowels=numbersOfVowels+1
    return numbersOfVowels
def main():
    sir=input("Intruduceti un sir de carcatere: ")
    print(f"Numarul de vocale este: {findVowels(sir)}")

main()
