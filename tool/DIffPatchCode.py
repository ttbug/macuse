# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
FC 6F BB A9 F8 5F 01 A9 F6 57 02 A9 F4 4F 03 A9 FD 7B 04 A9 FD 03 01 91 FF 03 07 D1 F3 03 01 AA F4 03 00 AA 08 03 01 B0 08 01 45 F9 08 01 40 F9 A8 83 1B F8 F7 00 00 94 60 00 00 37 16 01 00 94 00 02 00 36 35 00 80 52 A8 83 5B F8 09 03 01 B0 29 01 45 F9 29 01 40 F9 3F 01 08 EB 61 1D 00 54 E0 03 15 AA FF 03 07 91 FD 7B 44 A9 F4 4F 43 A9 F6 57 42 A9 F8 5F 41 A9 FC 6F C5 A8 C0 03 5F D6 2A 5B 64 94 1F 30 00 71 21 03 00 54 35 00 80 52 28 FB 91 52 68 06 A0 72 7F 02 08 6B 8D 01 00 54 48 FB 91 52 68 06 A0 72 7F 02 08 6B E0 FC FF 54 C8 93 83 52 28 0C A0 72 7F 02 08 6B 60 FC FF 54 08 96 83 52 28 0C A0 72 07 00 00 14 A8 D2 93 52 E8 01 A0 72 7F 02 08 6B 80 FB FF 54 E8 3D 8A 52

FC 6F BB A9 F8 5F 01 A9 F6 57 02 A9 F4 4F 03 A9 FD 7B 04 A9 FD 03 01 91 FF 03 07 D1 F3 03 01 AA F4 03 00 AA ?? ?? 01 ?? 08 ?? ?? F9 08 01 40 F9 A8 83 1B F8 ?? 00 00 94 60
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
