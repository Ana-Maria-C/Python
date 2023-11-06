def link(tag, content, **my_dict):
    my_link = '"<'
    my_link += tag
    for key, value in my_dict.items():
        my_link += f' {key}="{value}\\"'  # \ este caracter de escape, motiv pentru care l am dublat pentru a-l include in sir
    my_link += f'>{content}"'
    return my_link


def main():
    result = link("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid ")
    print(f"Rezultatul obtinut este \n {result}")


main()
