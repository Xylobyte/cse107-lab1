# Accepts 10 floating point numbers and prints the running average after each number is entered

sum = 0
count = 0
avg = 0

for i in range(10):
    count += 1
    sum += float(input("Enter a number: "))
    avg = sum / count
    print(str(avg))
