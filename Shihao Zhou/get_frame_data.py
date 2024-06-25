print("Shihao Zhou, ID: 230594553")
print("Individual Project with LEAP MOTION 1")
print("[Python 3.8.6],[Leap Orion V4.1.0]")

import Leap
import time

    # 定义延迟函数
dly = time.sleep
    # 获取当前时间
current_t = time.ctime()

    # 创建一个控制器对象
controller = Leap.Controller()

while True:
        # 创建一个帧对象
    frame = controller.frame()

    if not frame.hands.is_empty:    # 检测手部，如果有则执行下列语句
        for hand in frame.hands:
            hand_type = "Left Hand" if hand.is_left else "Right Hand"
                # 创建一个手掌对象
            hand_position = hand.palm_position
                # 要输出的信息
            output = f"It's your [{hand_type}], and position is: {hand_position}\n"
            print(output)
                # 以追加模式在指定文件内写入输出的数据
            f = open('C:\\Users\\Klaus\\Desktop\\Indiv Project\\With Python\\LEAP\\Hand Track Data\\Track_data.txt', "a",)
                # 在每行数据前加上当前时间
            f.write(f'{current_t} >>> ')
            f.write(output)
                # 关闭文件
            f.close()
                # 以0.5s作为每次检测间隔
            dly(0.5)
            break
    else:
        print("Where is your hand?")
        dly(0.5)

