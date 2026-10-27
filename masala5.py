jami = 0
soni = 0
xarajat = int(input())

while xarajat != 0:
	jami = jami + xarajat
	soni = soni + 1
	xarajat = int(input())

print("Jami:", jami)
print("Kiritilgan xarajatlar soni:", soni)

if soni > 0:
	ortacha = jami / soni
else:
	ortacha = 0

print("Ortacha:", round(ortacha, 2))