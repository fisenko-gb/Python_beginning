
import fan_function as fan

# import time
# i = 100
# while i > 0:
#     print('%.9f' % time.time())
#     # print(time.monotonic_ns())
#     i -= 1
#     time.sleep(0.00001)

i = 0
while i < 10:
    random_list = fan.random_list(1, 10, 10)
    print(random_list)
    i += 1
