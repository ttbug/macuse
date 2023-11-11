# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
55 48 89 E5 41 57 41 56 41 55 41 54 53 48 81 EC 38 04 00 00 4C 89 85 B8 FB FF FF 48 89 8D B0 FB FF FF 48 89 95 A8 FB FF FF 41 89 F4 48 89 FB 48 8B 05 D2 84 1B 00 48 8B 00 48 89 45 D0 48 8B 0D 44 9E 26 00 48 8D 15 97 4F 14 00 45 31 F6 48 8D BD D0 FB FF FF BE 00 04 00 00 31 C0 E8 61 B1 01 00 48 C7 85 C0 FB FF FF 00 00 00 00 48 8D 3D 5D 4F 14 00 BE 01 00 00 00 E8 15 AB 01 00 85 C0

55 48 89 E5 41 57 41 56 41 55 41 54 53 48 81 EC 38 04 00 00 4C 89 85 B8 FB FF FF 48 89 8D B0 FB FF FF 48 89 95 A8 FB FF FF 41 89 F4 48 89 FB 48 8B 05 D2 84 1B 00 48 8B 00 48 89 45 D0 48 8B 0D 44 9E 26 00 48 8D 15 97 4F 14 00 45 31 F6 48 8D BD D0 FB FF FF BE 00 04 00 00 31 C0 E8 61 B1 01 00 48 C7 85 C0 FB FF FF 00 00 00 00 48 8D 3D 5D 4F 14 00 BE 01 00 00 00 E8 15 AB 01 00 85 C0 74 29 48 8B 05 80 84 1B 00 48 8B 00 48 3B 45 D0 0F 85 69 02 00 00 44 89 F0
"""

data1 = []

for i in data.split("\n"):
    if i == "":
        continue
    else:
        data1.append(i)
        if len(data1) > 1:
            res = " ".join(
                [
                    d1 if d1 == d2 else "??"
                    for d1, d2 in zip(data1[0].split(), data1[1].split())
                ]
            )
            data1 = [res]

print(data1[0])
