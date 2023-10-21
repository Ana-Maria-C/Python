def my_function(*args):
    args_l = len(args)
    list_of_tuples = []
    each_arg_l = 0
    for arg in args:
        if len(arg)>each_arg_l:
            each_arg_l=len(arg)
    for i in range(0, each_arg_l):
        each_list = []
        for arg in args:
            if i<len(arg):
                each_list.append(arg[i])
            else:
                each_list.append(None)
        each_tuple = tuple(each_list)
        list_of_tuples.append(each_tuple)
    return tuple(list_of_tuples)


def main():
    result = my_function([1, 2, 3], [5, 6, 7], ["a", "b", "c"])
    print(f"Tuple rezultate sunt {result}")


main()
