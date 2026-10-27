ovozlar = {
    "Ali": "Python",
    "Vali": "JavaScript",
    "Madina": "Python",
    "Jasur": "C++",
    "Aziza": "Python",
    "Sardor": "JavaScript"
}

sanash = {}

for til in ovozlar.values():
    if til in sanash:
        sanash[til] += 1
    else:
        sanash[til] = 1

for til, son in sanash.items():
    print(f"{til}: {son} ta ovoz")

golib = max(sanash, key=sanash.get)
print("Golib:", golib)