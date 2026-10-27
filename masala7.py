A = (7, 5)
B = (4, 2)

a_yigindi = A[0] + A[1]
b_yigindi = B[0] + B[1]

print("A yigindisi:", a_yigindi)
print("B yigindisi:", b_yigindi)

if a_yigindi > b_yigindi:
	print("A yigindisi katta")
elif b_yigindi > a_yigindi:
	print("B yigindisi katta")
else:
	print("Yigindilar teng")