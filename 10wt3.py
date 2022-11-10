## Chinmay D. 11/9/2022 Hg5590
def gcd(a,b):
# Naming and starting the function with 2 parameters.
    if a<b:
        return gcd(b,a)
    elif b==0:
        return a
    else:
        return gcd(b,a%b)
# Calculates the largest number that divides a & b with no remainder.
print("Greatest common divisor for (12,8): ",gcd(12,8))
print("Greatest common divisor for (20,24): ",gcd(20,24))
# Prints out the GCD for integer pairs in the work ticket.
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
print("Greatest common divisor for (a,b): ",gcd(a,b))
# Takes parameters a & b as integer input and prints out GCD
## HALF-LIFE, Ron Bass, John Richards Sr., After-Burner Elite