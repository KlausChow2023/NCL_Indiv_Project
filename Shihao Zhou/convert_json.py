import json

# 输入的文本文件路径
i_file = 'C:\\Users\\Klaus\\Desktop\\Indiv Project\\With Python\\LEAP\\Hand Track Data\\Track_data.txt'

# 输出的 JSON 文件路径
o_file = 'C:\\Users\\Klaus\\Desktop\\Indiv Project\\With Python\\LEAP\\Hand Track Data\\Track_data.json'

# 准备存储数据的列表
data_to_save = []

    # 以只读方式打开输入的文件
with open(i_file, 'r') as f:
        # 一次性读取全部行
    lines = f.readlines()

# 解析每一行数据
for line in lines:
    # 去除换行符和空格
    line = line.strip()
    if line:
        # 按照文档内容的格式进行分割和提取
        timestamp_part, data_part = line.split(">current_time<")
        timestamp = timestamp_part.strip()
        hand_type, position_str = data_part.strip().split(">hand_type<")
        position = eval(position_str)  # 将位置信息字符串转换为元组

        # 构建字典
        entry = {
            "timestamp": timestamp,
            "hand_type": hand_type.strip("[]"),
            "position": position
        }

        # 添加到数据列表中
        data_to_save.append(entry)

    # 将数据保存为 JSON 文件
with open(o_file, 'w') as f:
        # indent=4，代表每个级别缩进四个空格。
    json.dump(data_to_save, f, indent=4)

print('-----JSON Covert Done-----')
