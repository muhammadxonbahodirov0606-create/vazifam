shaharlar = {"Toshkent": 3000000, "Fargona": 300000, "Samarqand": 600000}

print("500 000 dan kop:")

for shahar, aholi in shaharlar.items():
    if aholi > 500000:
        print(shahar, end=", ")

eng_kop = max(shaharlar, key=shaharlar.get)

print("\nEng kop aholi:", eng_kop)