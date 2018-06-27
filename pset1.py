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
    result = False

    if bears == 42:
        return True
    if bears % 2 == 0:
        result = is_reachable(bears // 2)
    if (bears % 3 == 0 or bears % 4 == 0) and bears // 10 % 10 != 0 \
            and bears % 10 != 0 and bears > 42:
        result = is_reachable(bears - (bears // 10 % 10) * (bears % 10))
    if bears % 5 == 0 and bears > 42:
        result = is_reachable(bears - 42)

    return result


