print("-------------")
print("Assignment 2")
print("-------------")

def ageVerification(age):
    if age < 18:
        return "You are a Child"
    elif age < 70:
        return "You are an Adult"
    elif age > 70:
        return "You are a Pensioner"