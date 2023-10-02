def func_one(n):
    return [str(num) for num in range(n)]

print(func_one(10))

import time

# Current time
start_time = time.time()
rs = func_one(100000)
end_time = time.time()

total_time = end_time-start_time
print(total_time)