y=input()
print(len(y))
val = 0
for x in y:
    print(x)
    if x == "א":
        val += 1
        print("Letra Alef")
    elif x == "ב":
        val += 2
        print("Letra Bet")
    elif x == "ג":
        val += 3
        print("Letra Gimel")
    elif x == "ד":
        val += 4
        print("Letra Dalet")
    elif x == "ה":
        val += 5
        print("Letra He")
    elif x == "ו":
        val += 6
        print("Letra Vav")
    elif x == "ז":
        val += 7
        print("Letra Zayin")
    elif x == "ח":
        val += 8
        print("Letra Het")
    elif x == "ט":
        val += 9
        print("Letra Tet")
    elif x == "י":
        val += 10
        print("Letra Yod")
    elif x == "כ":
        val += 20
        print("Letra Kaf")
    elif x == "ך" or x == "כ" or x == "ךּ":
        val += 20  # Letra Kaf final
        print("Letra Kaf final")
    elif x == "ל":
        val += 30
        print("Letra Lamed")
    elif x == "מ":
        val += 40
        print("Letra Mem")
    elif x == "ם":
        val += 40  # Letra Mem final
        print("Letra Mem final")
    elif x == "נ":
        val += 50
        print("Letra Nun")
    elif x == "ן" or x == "נ" or x == "ןּ":
        val += 50  # Letra Nun final
        print("Letra Nun final")
    elif x == "ס":
        val += 60
        print("Letra Samekh")
    elif x == "ע":
        val += 70
        print("Letra Ayin")
    elif x == "פ":
        val += 80
        print("Letra Pe")
    elif x == "ף" or x == "פ" or x == "ףּ":
        val += 80  # Letra Pe final
        print("Letra Pe final")
    elif x == "צ":
        val += 90
        print("Letra Tsadi")
    elif x == "ץ" or x == "צ" or x == "ץּ":
        val += 90  # Letra Tsadi final
        print("Letra Tsadi final")
    elif x == "ק":
        val += 100
        print("Letra Qof")
    elif x == "ר":
        val += 200
        print("Letra Resh")
    elif x == "ש":
        val += 300
        print("Letra Shin")
    elif x == "ת":
        val += 400
        print("Letra Tav")
    else:
        pass
print(f"Total: {val}")