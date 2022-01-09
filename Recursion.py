def fact(num):
    if num == 0:
        return 1
    print(num)
    return num*fact(num-1)


print(fact(4))

