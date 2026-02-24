num = int(input("Enter number: "))
low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))

if num >= low and num <= high:
    print("Number is within range")
else:
    print("Number is outside range")