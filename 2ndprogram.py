def IlanBaKailanganMo():
    Oranges = int(input("Oranges you wish to buy?: "))
    Apples = int(input("Apples you wish to buy?: "))
    return Oranges, Apples


def fruits():
    total = Val1*PresyoNgMgaPrutas[0] + Val2*PresyoNgMgaPrutas[1] 
    print(f"The total amount is {total}")


# These here are the prices provided for the oranges and apples respectively.
# They are utilized for the function fruits() above, necessary for calculating the total expenses.  
PresyoNgMgaPrutas = [25, 20]

# 1st Step:s
Val1, Val2 =  IlanBaKailanganMo()


MagkanoLahatNgPrutas = fruits()