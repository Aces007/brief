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
# 1st Step: These two will ask for your current money
PeraNaMeronKa, MagkanoApples = Survey()


MansanasYouAcquired, SukliMoAy = calculations()


MagkanoLahatNgNagastosKo()