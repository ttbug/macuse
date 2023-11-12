# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
FC 6F BA A9 FA 67 01 A9 F8 5F 02 A9 F6 57 03 A9 F4 4F 04 A9 FD 7B 05 A9 FD 43 01 91 FF 03 02 D1 A0 38 00 B0 00 80 20 91 CE A0 FB 97 08 80 5F F8 08 21 40 F9 E9 03 00 91 08 3D 00 91 08 ED 7C 92 38 01 08 CB 1F 03 00 91 00 00 80 D2 9E E3 13 94 F3 03 00 AA 1C 80 5F F8 88 23 40 F9 E9 03 00 91 08 3D 00 91 08 ED 7C 92 35 01 08 CB BF 02 00 91 E9 03 00 91 37 01 08 CB FF 02 00 91 E9 03 00 91 36 01 08 CB DF 02 00 91 00 00 80 D2

FC 6F BA A9 FA 67 01 A9 F8 5F 02 A9 F6 57 03 A9 F4 4F 04 A9 FD 7B 05 A9 FD 43 01 91 FF 03 02 D1 ?? 36 00 ?? 00 ?? ?? 91 ?? ?? FC 97 08 80 5F F8 08 21 40 F9 E9 03 00 91 08 3D 00 91 08 ED 7C 92 38 01 08 CB
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
