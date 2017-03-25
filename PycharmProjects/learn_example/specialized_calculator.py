numbers = []
count = 0
sum = 0

while True:
    line = input("enter a number or Enter to finish: ")
    if line:
        try:
            i = int(line)
            numbers.append(i)
            count += 1
            sum += i
            mean = sum/count
        except ValueError:
            print('Введите число!')
    else:
        break

print("numbers: " + str(numbers))
print("count = " + str(count), "sum = " + str(sum), "lowest = " + str(min(numbers)), "highest = " + str(max(numbers)), "mean = " + str(mean))