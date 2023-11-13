# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
FD 7B BF A9 FD 03 00 91 08 2C 00 D0 08 09 42 F9 1F 05 00 B1 A1 00 00 54 08 2C 00 D0 00 0D 42 F9 FD 7B C1 A8 5C D8 0C 14 00 2C 00 D0 00 40 10 91 41 25 00 B0 21 C0 21 91 89 D6 0C 94 F7 FF FF 17 08 2C 00 D0 00 05 42 F9 53 D8 0C 14 F6 57 BD A9 F4 4F 01 A9 FD 7B 02 A9 FD 83 00 91 28 2B 00 F0 00 95 46 F9 A9 F0 0C 94 FD 03 1D AA 4D D8 0C 94


FD 7B BF A9 FD 03 00 91 ?? ?? 00 ?? 08 ?? ?? F9 1F 05 00 B1 A1 00 00 54 08 2C 00 D0 00 ?? 41 F9 FD 7B C1 A8 ?? ?? 0C 14 00 2C 00 D0 00 ?? ?? 91 41 25 00 B0 21 C0 21 91 ?? ?? 0C 94 F7 FF FF 17
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
