medicalcause=input("enter the medical cause y or n ")
attendance=int(input("enter the attendance of the student "))

if (medicalcause=="y"):
    print("you are allowed ")
else:
    if (attendance>=75):
        print("you are allowed")
    else:
        print("you are not allowed")


#electicity bill
units=int(input("enter the total input consume"))

if units <50:
    amount=units*2.60
    surcharge=25
elif units <=100:
    amount=130+(units-50)*3.25
    surcharge=35
elif units <=200:
    amount=130+162.5+(units-100)*5.75
    surcharge=45
else:
    amount=130+162.5+526+(units-200)*8.26
    surcharge=75

total=amount + surcharge
print("electricity bill = ",total)