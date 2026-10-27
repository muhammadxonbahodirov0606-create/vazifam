zaxira = 12

while zaxira > 2:
	sotildi = int(input("Sotildi: "))

	if sotildi <= 0 or sotildi > zaxira:
		print("daftar soni yetarli emas")
		continue

	zaxira = zaxira - sotildi
	print("Qoldi:", zaxira)

print("Ombor bosh")
