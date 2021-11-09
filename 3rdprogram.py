def Survey():
    PeraNaMeronkaNgayon = int(input("How much money do you currently have?:"))
    MagkanoBaYungMansanas = int(input("How much does the apple cost?:"))
    return PeraNaMeronkaNgayon, MagkanoBaYungMansanas


def calculations():
    ApplesNaMabibiliMo = int(PeraNaMeronKa) // (MagkanoApples)
    MagkanoMatitiraSaPeraMo = int(PeraNaMeronKa) % (MagkanoApples)
    return ApplesNaMabibiliMo, MagkanoMatitiraSaPeraMo


def MagkanoLahatNgNagastosKo():
    print(f"You can buy {MansanasYouAcquired} apples and your change is {SukliMoAy}")

# So, the last program I did these user inputs are separated, now for a more simpler presentation of the progam these were mixed together.
# 1st Step: These two will ask for your current money, and the prices given for the apples you're willing to buy.
PeraNaMeronKa, MagkanoApples = Survey()

# 2ndStep: Then these will perform the calculations of the number of apples that you can buy with your money and 
# as a result the prorgam will present you the amount of change you will get.
MansanasYouAcquired, SukliMoAy = calculations()

# Last Step: Lastly I decided to separate the print function from the calculations and user inputs to not cause confusion.
# This will present you the apples you can buy with the money you currently have and the change you will receive from the expenses.
MagkanoLahatNgNagastosKo()