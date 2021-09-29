def twoBigNumbers(x, y):
    if x > 10 and y > 10:
        return True
    else:
        return False
print(twoBigNumbers(30, 40))

def twoSmallNumbers(x, y):
    if x < 10 or y < 10:
        return True
    else:
        return False
print(twoSmallNumbers(2, 3))

def twoBigNumberss(x, y):
    if x > 10 or not y > 10:
        return True
    else:
        return False
print(twoBigNumberss(30, 40))