import time
study=int(input("Enter the duration to study (mins): "))
relax=int(input("Enter the duration of break (mins): "))
count=int(input("Enter the number of cycles: "))

for i in range(0, count):
    time.sleep(study*60)
    print("Break time! Yay!")
    print('\a')
    time.sleep(relax*60)
    print("Get back to work")
    print('\a')
