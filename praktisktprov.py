#Author: Peter Leisborn
#Date: 2024-09-25

list = []
result = 1
list = input('Vilka tabeller vill du multiplicera?:')
numbers = list.split()

if numbers == []:
    pass

else:
    for i in range(len(numbers)):
        for j in range(1,11):
            print(f'{int(numbers[i])} * {j} = {int(numbers[i])*j}')
        print(' ') #tom rad