import Leap
import time

# 定义时间延迟函数
dly = time.sleep

# 创建LEAP Motion控制器对象
controller = Leap.Controller()

print("Press Enter to quit...")

try:
    while True:
        frame = controller.frame()

        try:
            # 检查当前帧中是否有手
            for hand in frame.hands:
                hand_type = "左手" if hand.is_left else "右手"
                print(f"{hand_type}, id {hand.id}, position: {hand.palm_position}")

                try:
                    # 迭代每只手指
                    for finger in hand.fingers:
                        print(f"手指: {finger.type}, id: {finger.id}, 长度: {finger.length}mm, 宽度: {finger.width}mm")

                        # 迭代每根骨骼
                        for b in range(4):
                            bone = finger.bone(b)
                            print(f"骨骼: {bone.type}, 起点: {bone.prev_joint}, 终点: {bone.next_joint}, 方向: {bone.direction}")
                except StopIteration:
                    print("迭代手指时发生错误")

        except SystemError as e:
            print(f"SystemError: {e}")

        # 每秒更新一次
        dly(1)

except KeyboardInterrupt:
    print("用户退出。")
finally:
    print("正在退出...")





