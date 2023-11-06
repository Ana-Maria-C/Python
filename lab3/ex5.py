def rules_dict(rules, my_dict):
    for key, value in my_dict.items():
        if key not in [rule[0] for rule in rules]:
            return False
        for rule in rules:
            if rule[0] == key:
                prefix, middle, suffix = rule[1], rule[2], rule[3]
                if (prefix != "" and not value.startswith(prefix)) or (suffix != "" and not value.endswith(suffix)):
                    return False
                if middle != "" and prefix != "" and suffix != "" and middle not in value[1:-1] \
                    or middle != "" and prefix != "" and middle not in value[1:] \
                    or middle != "" and suffix != "" and middle not in value[:-1]:
                    return False
    return True


def main():
    result = rules_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
                        {"key1": "come inside, it's too cold out", "key3": "this is not valid"})
    print(result)


main()
