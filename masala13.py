ali = {"komediya", "sarguzasht", "fantastika"}
vali = {"fantastika", "drama", "komediya"}

umumiy = ali & vali
bitta = ali ^ vali

print("Umumiy janrlar:", ", ".join(umumiy))
print("Faqat bittasiga yoqadi:", ", ".join(bitta))