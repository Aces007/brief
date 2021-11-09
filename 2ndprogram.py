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

# 1st Step: For the more refined version of my last program, these values(Val1, Val2) represents the answer you will provide for the questions
# above. They will ask for the oranges and apples you would buy respectively.
Val1, Val2 =  IlanBaKailanganMo()

# Last Step: This last step compared to my last program, is more simple and complete in terms of calculating your total expenses
# I utilized the values from "PresyoNgMgaPrutas" respectively with their positions whilst using the values as well in "IlanBaKailanganMo".
# These will then calculate the total expenses you commited to and provide you the summary at the same time.
MagkanoLahatNgPrutas = fruits()