test_string = "(+ (* 3 5) (* 3 4))"
test_string1 = "(+ 1 (+ 1 (+ 1 1)))"
test_string2 = "(* 3 5)"


def temp_func(string):
    elements = []
    paran_count = 0
    start_index = 1
    # stop_index = 0
    for i, item in enumerate(string.split(' ')):
        if paran_count == 1:
            elements.append(string[start_index:i+1])
            start_index = i+1
        if item.count('(') > 0:
            paran_count += 1
        if item.count(')') < 0:
            paran_count -= 1
    print(elements)

temp_func(test_string)
temp_func(test_string1)
temp_func(test_string2)

