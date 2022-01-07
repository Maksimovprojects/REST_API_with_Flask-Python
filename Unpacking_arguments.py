# example 1
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total


print(multiply(1, 2, 3, 4, (1, 2, 3, 4, 5)))
print(multiply(-1))
print("# ------------------------------------")


def apply(*args, operator):
    if operator == "*":
        print(args)
        return multiply(args)
    elif operator == "+":
        print(args)
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 9, 90, 100, operator="+"))

print("# ------------------------------------")


# example 2
def add(x, y):
    return x + y


nums = [3, 5]
print(add(*nums))

dic_num = {"x": 3, "y": 7}
print(add(**dic_num))
print("# **kwards_examples ------------------------------------")


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 5, 7, name="Bob", age=25)




print("# mix examples ------------------------")
mix = [1, 3, 5, {"name": "Bob", "age": 25}, [1, 2, 3]]

(both(mix))
