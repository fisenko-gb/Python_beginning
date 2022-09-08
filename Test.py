
import time
i = 100
while i > 0:
    print('%.9f' % time.time())
    # print(time.monotonic_ns())
    i -= 1
    time.sleep(0.00001)
