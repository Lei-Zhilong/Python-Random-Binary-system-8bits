import random


# SetVarTo0
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
# SetVarTo(Random)
for __count in range(20):
    A = random.randint(0, 1)
    B = random.randint(0, 1)
    C = random.randint(0, 1)
    D = random.randint(0, 1)
    E = random.randint(0, 1)
    F = random.randint(0, 1)
    G = random.randint(0, 1)
    H = random.randint(0, 1)
# PrintVar
print(A, B, C, D, E, F, G, H)
print('已随机生成二进制8bit数据')
print(input('是否加密?(输入Y/N)'))
if (input() == 'Y'):
    print('正在加密...')
    for __count in range(8):
        if (random.randint(1, 8) == 1):
            if (A == 0):
                A = 1
            else:
                A = 0
        if (random.randint(1, 8) == 2):
            if (B == 0):
                B = 1
            else:
                B = 0
        if (random.randint(1, 8) == 3):
            if (C == 0):
                C = 1
            else:
                C = 0
        if (random.randint(1, 8) == 4):
            if (D == 0):
                D = 1
            else:
                D = 0
        if (random.randint(1, 8) == 5):
            if (E == 0):
                E = 1
            else:
                E = 0
        if (random.randint(1, 8) == 6):
            if (F == 0):
                F = 1
            else:
                F = 0
        if (random.randint(1, 8) == 7):
            if (G == 0):
                G = 1
            else:
                G = 0
        if (random.randint(1, 8) == 8):
            if (H == 0):
                H = 1
            else:
                H = 0
    if (A == B):
        if(random.randint(0,1) == 0):
            if(A == 0):
                A = 1
            if(A == 1):
                A = 0
        if (random.randint(0,1) == 1):
            if (B == 0):
                B == 1
            if (B == 1):
                B == 0
    if (B == C):
        if(random.randint(0,1) == 0):
            if (B == 0):
                B == 1
            if (B == 1):
                B == 0
        if (random.randint(0,1) == 1):
            if (C == 0):
                C == 1
            if (C == 1):
                C == 0
    if (C == D):
        if (random.randint(0,1) == 0):
            if (C == 0):
                C == 1
            if (C == 1):
                C == 0
        if (random.randint(0,1) == 1):
            if (D == 0):
                D == 1
            if (D == 1):
                D == 0
    if (D == E):
        if (random.randint(0,1) == 0):
            if (D == 0):
                D == 1
            if (D == 1):
                D == 0
        if (random.randint(0,1) == 1):
            if (E == 0):
                E == 1
            if (E == 1):
                E == 0
    #后面的懒得写了...
    print('加密已完成')
    print('加密结果为')
    print(A, B, C, D, E, F, G, H)
    
if (input() == 'N'):
    print('这是随机生成的二进制8bits数据')
    print(A, B, C, D, E, F, G, H)
