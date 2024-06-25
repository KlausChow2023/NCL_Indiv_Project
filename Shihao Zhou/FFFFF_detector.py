import Leap
import time
dly = time.sleep
# 创建一个控制器对象
controller = Leap.Controller()

# 无限循环，持续检测Leap Motion设备
while True:
    # 获取当前帧数据
    frame = controller.frame()

    # 检查是否有任何手部数据
    if not frame.hands.is_empty:
        for hand in frame.hands:
            # 检查手部中是否有手指数据
            if not hand.fingers.is_empty:
                # 初始化手指计数器
                mid_finger_detected = 0

                # 遍历手部中的每个手指
                for finger in hand.fingers:
                    # 判断手指是否为中指
                    if finger.type == Leap.Finger.TYPE_MIDDLE:
                        # 获取手指的方向向量
                        direction = finger.direction
                        # 检测中指是否竖起（方向向量的y分量大于阈值）
                        if direction.y > 0.6:  # 阈值越低，检测的灵敏度越高，可能会误检测其他手势为目标手势。
                            mid_finger_detected = 1
                        else:
                            mid_finger_detected = 0
                        break


                # 如果检测到竖中指的姿势
                if mid_finger_detected:
                    print("竖中指")
                    dly(1)
                else:
                    print("不是竖中指")
                    dly(1)
            break
    else:
        print("未检测到手部数据")
        dly(0.5)
