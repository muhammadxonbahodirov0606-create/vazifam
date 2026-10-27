matematika = {"Ali", "Vali", "Madina", "Jasur", "Aziza"}
ingliz = {"Madina", "Jasur", "Sardor", "Aziza", "Malika"}

ikkala_kurs = matematika & ingliz
faqat_bitta_kurs = matematika ^ ingliz

print("Ikkala kursda:", ", ".join(sorted(ikkala_kurs)))
print("Faqat bitta kursda:", ", ".join(sorted(faqat_bitta_kurs)))
