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


PeraNaMeronKa, MagkanoApples = Survey()


MansanasYouAcquired, SukliMoAy = calculations()


MagkanoLahatNgNagastosKo()