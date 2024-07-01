import json

# 定义文件路径
txt_file_path = "C:\\Users\\Klaus\\Desktop\\Indiv Project\\With Python\\LEAP\\Hand Track Data\\Track_data.txt"
json_file_path = "C:\\Users\\Klaus\\Desktop\\Indiv Project\\With Python\\LEAP\\Hand Track Data\\Track_data.json"

# 读取txt文件内容
with open(txt_file_path, 'r') as file:
    lines = file.readlines()

# 解析txt文件内容
data = []
for line in lines:
    entry = {}
    parts = line.strip().split('>')  # 使用strip()去除每行末尾的换行符
    for part in parts:
        if '<' in part:
            key, value = part.split('<')
            entry[key] = value
    data.append(entry)

# 将解析的数据转换为JSON格式
with open(json_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file was stored")
