# QiuChenly 计算数据差值做特征码算法
# 部分网友提供了原始版本 虽然是用的Chatgpt写给我的 但是还是略表谢意
# 提供不定长度的多个十六进制汇编代码段 自动求出差值特征码

data = """
F8 5F BC A9 F6 57 01 A9 F4 4F 02 A9 FD 7B 03 A9 FD C3 00 91 56 08 40 F9 36 02 00 B4 F5 03 02 AA F3 03 01 AA F4 03 00 AA 40 04 42 A9 1F 00 14 EB 20 00 53 FA C0 00 00 54 E2 03 14 AA E3 03 13 AA 04 00 80 52 F8 ?? ?? 94 60 00 00 36


F8 5F BC A9 F6 57 01 A9 F4 4F 02 A9 FD 7B 03 A9 FD C3 00 91 56 08 40 F9 36 02 00 B4 F5 03 02 AA F3 03 01 AA F4 03 00 AA 40 04 42 A9 1F 00 14 EB 20 00 53 FA C0 00 00 54 E2 03 14 AA E3 03 13 AA 04 00 80 52 51 34 17 94 60 00 00 36
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
