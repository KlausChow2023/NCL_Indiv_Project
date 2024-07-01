import Leap
import time

print("Shihao Zhou, ID: 230594553")
print("Individual Project with LEAP MOTION 1")
print("[Python 3.8.6],[Leap Orion V4.1.0]")

# 定义延迟函数
dly = time.sleep

# 创建一个控制器对象
controller = Leap.Controller()
# 把手指类型命名
finger_type_map = {
    Leap.Finger.TYPE_THUMB: "Thumb",
    Leap.Finger.TYPE_INDEX: "Index Finger",
    Leap.Finger.TYPE_MIDDLE: "Middle Finger",
    Leap.Finger.TYPE_RING: "Ring Finger",
    Leap.Finger.TYPE_PINKY: "Little Finger"
}

while True:
    try:
        # 创建一个帧对象
        frame = controller.frame()

        if not frame.hands.is_empty:    # 检测手部，如果有则执行下列语句
            for hand in frame.hands:
                hand_type = "Left Hand" if hand.is_left else "Right Hand"
                # 创建一个手掌对象
                hand_position = hand.palm_position

                try:
                    # 检测是否握拳
                    for finger in hand.fingers:
                        finger_type_str = finger_type_map.get(finger.type, "Unknown")   # 用已经命名的字符串代替finger.type
                        output = f">hand_id<{hand.id}>hand_type<{hand_type}>hand_position<{hand_position}>finger_id<{finger.id}>finger_type<{finger_type_str}>finger_tip_position<{finger.tip_position}\n"

                        # 要输出的信息
                        print(output)

                        # 以追加模式在指定文件内写入输出的数据
                        f = open('C:\\Users\\Klaus\\Desktop\\Indiv Project\\With Python\\LEAP\\Hand Track Data\\Track_data.txt',"a",)
                        # 在每行数据前加上当前时间
                        current_t = time.ctime()

                        f.write(f'>current_time<{current_t}')
                        f.write(output)
                        # 关闭文件
                        f.close()


                except Exception :
                    print('One measure done')

        else:
            print("Where is your hand?")
            dly(0.3)

    except Exception :
        print('--------------------------------------------------')
        dly(1)
    finally:
        pass
