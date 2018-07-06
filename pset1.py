# Name:             Zhoushuai (Andrew) Wu
# Course:           CPE 202
# Instructor:       Daniel Kauffman
# Assignment:       Problem Set 1: Recursion
# Term:             Summer 2018

def permute(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        result = []
        for i in string:
            p_string = permute(string.replace(i, ""))
            for j in p_string:
                result.append(i + j)
        return result


def is_reachable(bears):
    
    forty_two = 42
    hundred = 100
    
    digi_0 = bears % 10
    digi_1 = (bears % hundred) // 10


    if bears < forty_two:
        return False
    if bears == forty_two:
        return True
    if bears % 2 == 0 and is_reachable(bears // 2):
        return True
    if (bears % 4 == 0 or bears % 3 == 0) and digi_0 * digi_1 != 0:         
        if is_reachable(bears - digi_0 * digi_1):
            return True
    if bears % 5 == 0 and is_reachable(bears - forty_two):
        return True
    
    return False


