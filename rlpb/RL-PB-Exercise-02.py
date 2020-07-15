import random
number = random.randint(1, 100)
print(number)

guess = int(input('Enter a number from 1-100: '))

if guess == number:
    print(f'Hurrah, {number} is the right guess!')
elif guess < number:
    print(f'Nope, {guess} is too low')
else:
    print(f'Nope, {guess} is too high')

