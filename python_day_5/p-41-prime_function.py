def check_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

num = int(input("Enter number: "))
print(check_prime(num))