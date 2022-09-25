import ageUtils

ageCalc = "start"

while ageCalc != "exit":
    ageCalc = input("Press any key to continue and 'exit' to quit: \n")
    if ageCalc != "exit":
        age = int
        
        while(age):
            try:
                age = int(input("Please Write your Age: "))
                print(ageUtils.ageVerification(age))
                break
            except Exception:
                print("Please Enter a valid number")

    else:
        print("Thanks for using Age Calculator")
        break

