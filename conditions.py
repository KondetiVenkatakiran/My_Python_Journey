has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("not Eligible for loan")

if has_good_credit or has_high_income:
    print("Eligible for loan")
else:
    print("not eligible for loan")

if has_high_income and not has_good_credit:
    print("Eligible for loan")
else:
    print("not Eligible for loan")
