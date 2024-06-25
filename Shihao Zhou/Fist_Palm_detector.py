import Leap
import time

dly = time.sleep

    # 创建一个控制器对象
controller = Leap.Controller()

while True:
        # 获取当前帧数据
    frame = controller.frame()

        # 检查是否有任何手部数据
    if not frame.hands.is_empty:
        for hand in frame.hands:
                # 检测左右手
            hand_type = "Left Hand" if hand.is_left else "Right Hand"
                # 检测手的握拳程度
            if hand.grab_strength > 0.5:
                print(f"{hand_type} >> Fist")
                dly(0.5)
            else:
                print(f"{hand_type} >> Palm")
                dly(0.5)
            break
    else:
        print()
        print("Where is your hand?")
        dly(0.5)

