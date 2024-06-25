import Leap
import time

dly = time.sleep

# 创建一个控制器对象
controller = Leap.Controller()

# 无限循环，持续检测
while True:
    # 获取当前帧数据
    frame = controller.frame()

    # 检查是否有任何手部数据
    if not frame.hands.is_empty:
        for hand in frame.hands:
            # 检测手的握拳程度
            if hand.grab_strength > 0.5:
                print("Fist")
                dly(0.5)
            else:
                print("Palm")
                dly(0.5)
            break
    else:
        print()
        print("Where is your hand?")
        dly(0.5)

