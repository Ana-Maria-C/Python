def my_function(*args, **keyword_args):
    values_of_keyword_args = keyword_args.values()
    count = 0
    for each_arg in args:
        if each_arg in values_of_keyword_args:
            count += 1
    return count


def main():
    result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
    print(result)


main()
