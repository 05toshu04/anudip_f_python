percent = float(input("Enter 12th percentage: "))
maths = input("Did you study Maths (yes/no): ")
score = int(input("Enter entrance exam score: "))

if percent < 75:
    print("Not eligible: Percentage less than 75")
elif maths != "yes":
    print("Not eligible: Maths not studied")
elif score < 80:
    print("Not eligible: Entrance score less than 80")
else:
    print("Eligible for Admission")