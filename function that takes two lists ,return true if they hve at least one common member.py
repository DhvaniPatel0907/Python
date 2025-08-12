def fun1(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False


list_a = [1, 2, 3, 4]
list_b = [5, 6, 3, 8]

result = fun1(list_a, list_b)
print("Do they have a common member?", result)
