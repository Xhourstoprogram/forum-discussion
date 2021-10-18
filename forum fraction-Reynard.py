import math
numerator = int(input("Enter a numerator. Value must be greater than 0: "))
while numerator <= 0:
    numerator = int(input("Please re-enter the numerator. Value must be greater than 0: "))
denominator = int(input("Enter a denominator. Value must be greater than 0: "))
while denominator <= 0:
    denominator = int(input("Please re-enter the denominator. Value must be greater than 0: "))
mix = numerator // denominator
number = numerator - (mix * denominator)
gcd = math.gcd(numerator, denominator)
if numerator < denominator:
    print(f"{numerator} / {denominator} is a proper fraction")
    if gcd < 2:
        print("This proper fraction cannot be reduced any further.")
    else:
        print("This proper fraction can be reduced to: ", numerator//gcd, "/", denominator//gcd)
elif numerator > denominator:
    print(f"{numerator} / {denominator} is an improper fraction")
    if gcd < 2 and denominator > 1:
        print("This improper fraction cannot be reduced any further.")
        print("The mixed number is ", mix, "and", number, "/", denominator)
    if gcd >= 2 and gcd != denominator:
        print("This improper fraction can be reduced to: ", numerator//gcd, "/", denominator//gcd)
        print("The mixed number is ", mix, "and", number, "/", denominator)
    if gcd >= 2 and gcd == denominator:
        print("This improper fraction can be reduced to: ", numerator//gcd, "/", denominator//gcd)
        print("The whole number is ", mix)
    if gcd == denominator and denominator == 1:
        print("This improper fraction cannot be reduced any further.")
        print("The whole number is ", mix)
