baholar = {"Ali": 85, "Vali": 72, "Madina": 96, "Jasur": 68}

print("Yuqori ball olganlar:")

for ism, ball in baholar.items():
    if ball >= 90:
        print(ism, "—", ball)

ortacha = sum(baholar.values()) / len(baholar)

print("O‘rtacha ball:", ortacha)