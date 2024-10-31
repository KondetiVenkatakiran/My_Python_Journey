weight = int(input("weight: "))
unit = input("(L)bs or Kgs: ")
if unit.upper() == "L":
    converter = weight * 0.45
    print(f"{converter} in kilos")
else:
    converter = weight / 0.45
    print(f"{converter} in lbs")