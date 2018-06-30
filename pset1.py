# Name:             Zhoushuai (Andrew) Wu
# Course:           CPE 202
# Instructor:       Daniel Kauffman
# Assignment:       Problem Set 1: Recursion
# Term:             Summer 2018

def permute(string):
    if len(string) == 0:
        return [""]
    elif len(string) == 1:
        return string
    else:
        result = []
        for i in string:
            p_string = permute(string.replace(i, ""))
            for j in p_string:
                result.append(i + j)
        return result


def is_reachable(bears):
    
    forty_two = 42
    two = 2
    three = 3
    four = 4
    five = 5
    ten = 10
    hundred = 100

    if bears < forty_two:
        return False
    if bears == forty_two:
        return True
    if bears % two == 0 and is_reachable(bears // two):
        return True
    if bears % four == 0 or bears % three == 0:
        digi_0 = bears % ten
        digi_1 = (bears % hundred) // ten
        return digi_0 * digi_1 != 0 and is_reachable(bears - digi_0 * digi_1)
    if bears % five == 0 and is_reachable(bears - forty_two):
        return True
    return False


