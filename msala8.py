harorat = (18, 20, 17, 23, 25, 21, 19)
yuqori_harorat = []

for qiymat in harorat:
	if qiymat > 20:
		yuqori_harorat.append(qiymat)

natija = ""
for qiymat in yuqori_harorat:
	if natija != "":
		natija = natija + ", "
	natija = natija + str(qiymat)

print("Haroratlar:", natija)
print("Kunlar soni:", len(yuqori_harorat))
