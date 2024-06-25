import Leap
import time

controller = Leap.Controller()

t = 0

while controller.is_connected == 0:
    print("Can not connect Device",end=' ')
    time.sleep(1)
    t = t + 1
    print(f"Time consume {t} s")

print("Connected")
