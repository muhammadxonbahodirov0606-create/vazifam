savat = {"non": 4000, "sut": 12000, "tuxum": 18000, "yog": 25000}

dastlabki = sum(savat.values())
print("Dastlabki summa:", dastlabki, "som")

savat["shakar"] = 14000

yangi_summa = sum(savat.values())
print("Shakardan keyin:", yangi_summa, "som")