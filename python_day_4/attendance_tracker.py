# Attendance list (1 = Present, 0 = Absent)
attendance = [1,1,0,0,1,0,1,1,0,0]

print("Attendance:")
print(attendance)

# Attendance percentage
present = attendance.count(1)

percentage = (present / len(attendance)) * 100

print("Attendance Percentage =", percentage)

# Below 75%
if percentage < 75:
    print("Student below 75% attendance")
else:
    print("Attendance OK")

# Replace consecutive absences
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i+1] = "Warning"

print("Updated Attendance:")
print(attendance)