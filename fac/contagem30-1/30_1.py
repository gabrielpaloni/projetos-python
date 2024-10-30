import time
x = 31
while x >= 2:
    x = x - 1
    if x % 4 == 0:
        print(f'[{x}]', end=' ', flush=True)
    else:
        print(f'{x}', end=' ', flush=True)
    time.sleep(0.2)
