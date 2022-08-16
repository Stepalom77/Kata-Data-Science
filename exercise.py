weight = input("Weight: ")
grams = input("(K)g or (L)bs: ")
if grams.upper() == "K":
    print("Weight in Lbs:" + " " + str(float(weight) * 2.22))
elif grams.upper() == "L":
    print("Weight in Kgs:" + " " + str(float(weight) / 2.22))

