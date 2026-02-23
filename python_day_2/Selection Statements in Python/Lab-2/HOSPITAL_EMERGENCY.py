heart_rate = int(input("Enter heart rate: "))
injury = input("Severe injury? (yes/no): ")
age = int(input("Enter age: "))

if heart_rate < 60 or heart_rate > 100 or injury == "yes":
    category = "Critical"
elif 60 <= heart_rate <= 100:
    category = "Moderate"
else:
    category = "Normal"

if age > 65 and category == "Moderate":
    category = "Critical"

print("Patient Priority:", category)