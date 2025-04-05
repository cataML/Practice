def numbers(x, y):
    if x*y <= 1000:
        return x*y
    else:
        return x+y
print(numbers(500, 200))


numbers = [1,2,3,4,5,6]
for i in range(1, len(numbers)):
    current_number = numbers[i]
    prev_number = numbers[i-1]
    sum_of_numbers = current_number + prev_number
    print(f'current number is {current_number}, previous is {prev_number} and their total is {sum_of_numbers} ')


for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end=' ')
    print('\t\t')

print()
name = 'microphone'
L = list(name)
print(L[0: :2])
print()

for num in range(1, 7):
    for i in range(num):
        print(i, end=' ')
    print('\t') 
