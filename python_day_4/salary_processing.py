# Employee salaries list
salaries = [20000, 55000, 48000, 70000, 15000, 52000, 30000]

print("Original Salaries:")
print(salaries)

# Remove salaries below minimum wage (20000)
valid_salary = []

for s in salaries:
    if s >= 20000:
        valid_salary.append(s)

# Add 5% bonus if salary > 50000
for i in range(len(valid_salary)):
    if valid_salary[i] > 50000:
        valid_salary[i] = valid_salary[i] + (valid_salary[i]*0.05)

# Sort descending
valid_salary.sort(reverse=True)

print("Processed Salaries:")
print(valid_salary)

# Top 3 salaries
print("Top 3 Salaries:")
print(valid_salary[:3])