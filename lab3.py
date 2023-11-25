import math

def function_1(x):
    return x**3 - 8*x + 1

def function_2(x):
    return -12*math.sin(x) - 10*math.cos(x)

for y in reversed(range(-50, 51)):
    if y % 10 == 0:
        print(f"{y/10:2.1f}", end=' ')
    else:
        print('   ', end=' ')
    for x in range(-50, 51):
        x_val = x / 10
        y_val_1 = function_1(x_val)
        y_val_2 = function_2(x_val)

        if abs(y_val_1 - y/10) < 0.5 or abs(y_val_2 - y/10) < 0.5:
            print('*', end='')
        elif y == 0 and x != 0:
            print('-', end='')
        elif x == 0 and y != 0:
            print('|', end='')
        else:
            print(' ', end='')
    print()

print('  ', end='')
for i in range(-50, 51, 5):
    if i % 10 == 0:
        print(f"{i/10:^5.1f}", end='')
    else:
        print(' ' * 5, end='')
print()

