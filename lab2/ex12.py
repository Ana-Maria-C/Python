def find_rhyme(list_of_words):
    list_of_list = []
    i = 0
    while i < len(list_of_words):
        my_list = [list_of_words[i]]
        j = i + 1
        while j < len(list_of_words):
            if list_of_words[i][-2] == list_of_words[j][-2]:
                my_list.append(list_of_words[j])
                del list_of_words[j]
            j += 1
        list_of_list.append(my_list)
        i += 1

    return list_of_list


def main():
    list_of_words = ['ana', 'banana', 'carte', 'arme', 'parte']
    result = find_rhyme(list_of_words)
    print(f"Listele rimate sunt: {result}")


main()
