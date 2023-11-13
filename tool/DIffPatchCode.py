# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
FF 03 02 D1 F6 57 05 A9 F4 4F 06 A9 FD 7B 07 A9 FD C3 01 91 A8 25 00 90 08 09 41 F9 08 01 40 F9 A8 83 1D F8 2D 1D 0D 94 F4 03 00 AA C8 27 00 D0 08 81 0F 91 E8 17 00 F9 D5 2B 00 90 B3 AE 46 F9 05 43 00 94 E2 03 00 AA E0 03 13 AA 9E 76 0D 94 FD 03 1D AA 2A 1D 0D 94 F3 03 00 AA 48 28 00 F0 08 81 35 91 E8 03 03 A9 B5 AE 46 F9 A8 2C 00 F0 08 E1 1F 91 00 01 40 F9 E3 B6 0D 94 E2 03 00 AA E0 03 15 AA 70 76 0D 94 FD 03 1D AA 1C 1D 0D 94 F5 03 00 AA E0 23 00 F9 C8 2B 00 90 00 85 46 F9 E2 E3 00 91

FF 03 02 D1 F6 57 05 A9 F4 4F 06 A9 FD 7B 07 A9 FD C3 01 91 ?? 25 00 ?? 08 09 41 F9 08 01 40 F9 A8 83 1D F8 ?? ?? 0D 94 F4 03 00 AA ?? 27 00 ?? 08 ?? ?? 91 E8 17 00 F9 ?? 2B 00 ?? B3 ?? ?? F9 ?? 42 00 94 E2 03 00 AA E0 03 13 AA ?? ?? 0D 94 FD 03 1D AA ?? ?? 0D 94 F3 03 00 AA ?? 28 00 ?? 08 ?? ?? 91 E8 03 03 A9 B5 ?? ?? F9 ?? 2C 00 ?? 08 ?? ?? 91 00 01 40 F9 ?? ?? 0D 94 E2 03 00 AA E0 03 15 AA ?? ?? 0D 94 FD 03 1D AA ?? ?? 0D 94 F5 03 00 AA
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
