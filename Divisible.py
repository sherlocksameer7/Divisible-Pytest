def divisible_by_5(x):
    if x % 5 == 0:
        return True
    else:
        return False

def divisible_by_7(x):
    if x % 7 == 0:
        return True
    else:
        return False

def divisible_by_9(x):
    if x % 9 == 0:
        return True
    else:
        return False

def divisible_by_10(x):
    if x % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":

    x = int(input("Enter a Number to Check Divisible or Not: "))


    Result1 = divisible_by_5(x)
    if Result1 == True:
        print(x, "is Divisible by 5")
    else:
        print(x, "is Not Divisible by 5")


    Result2 = divisible_by_7(x)
    if Result2 == True:
        print(x, "is Divisible by 7")
    else:
        print(x, "is Not Divisible by 7")


    Result3 = divisible_by_9(x)
    if Result3 == True:
        print(x, "is Divisible by 9")
    else:
        print(x, "is Not Divisible by 9")

        
    Result4 = divisible_by_10(x)
    if Result4 == True:
        print(x, "is Divisible by 10")
    else:
        print(x, "is Not Divisible by 10")