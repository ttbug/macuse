# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
FD 7B BF A9 FD 03 00 91 08 2C 00 D0 08 59 41 F9 1F 05 00 B1 A1 00 00 54 08 2C 00 D0 00 5D 41 F9 FD 7B C1 A8 7B D6 0C 14 00 2C 00 D0 00 C0 0A 91 41 25 00 B0 21 C0 21 91 A8 D4 0C 94 F7 FF FF 17

FD 7B BF A9 FD 03 00 91 ?? ?? 00 ?? 08 ?? ?? F9 1F 05 00 B1 A1 00 00 54 08 2C 00 D0 00 5D 41 F9 FD 7B C1 A8 7B D6 0C 14 00 2C 00 D0 00 C0 0A 91 41 25 00 B0 21 C0 21 91 A8 D4 0C 94 F7 FF FF 17
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
