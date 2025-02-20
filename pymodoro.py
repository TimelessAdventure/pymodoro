import time
study=int(input("Enter the duration to study (mins): "))
relax=int(input("Enter the duration of break (mins): "))
count=int(input("Enter the number of cycles: "))

def display(timed):
    while (timev): 
        mins, secs = divmod(timed, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        timed -= 1   

for i in range(0, count):
    study=studyb
    print("Time till break: ")
    display(study)
    print("Break time! Yay!")
    print('\a')
    print("Remaining break time: ")
    relax=relaxb
    display(relax)
    print("Get back to work")
