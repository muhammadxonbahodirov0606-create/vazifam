son = int(int(input("Sonni kiriting: ")))
raqamlar = 1

while son >= 10:
	son = son // 10
	raqamlar = raqamlar + 1

print("Raqamlar soni:", raqamlar)
