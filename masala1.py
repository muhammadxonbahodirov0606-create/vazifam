jamgarma = int(input("Boshlangich pul: "))
haftalik_qoshimcha = int(input("Haftalik qoshimcha: "))

hafta = 0
while jamgarma <= 500000:
	jamgarma += haftalik_qoshimcha
	hafta += 1

print(f"Kerakli hafta: {hafta}")
