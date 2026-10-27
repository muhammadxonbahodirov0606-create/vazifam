ombor = {"olma": 12, "banan": 8, "anor": 15, "uzum": 6}

eng_kop = max(ombor, key=ombor.get)
eng_kam = min(ombor, key=ombor.get)
jami = sum(ombor.values())

print("Eng ko‘p:", eng_kop, f"({ombor[eng_kop]} ta)")
print("Eng kam:", eng_kam, f"({ombor[eng_kam]} ta)")
print("Jami mahsulot:", jami, "ta")