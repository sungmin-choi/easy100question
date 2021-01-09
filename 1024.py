# 1024
import numpy as np
a = input()
for i in a:
    print("'"+i+"'")
# 1025
a = input()
arr = []
for i in range(len(a)):
    arr.append(a[i]+("0"*(len(a)-i-1)))

for i in arr:
    print("["+i+"]")
# 1027
a, b, c = input().split(".")
print(c+"-"+b+"-"+a)

# 1028
a = float(input())
print("%.11lf" % a)

# 1030
a = input()
print(a)

# 1031
a = int(input())
a = format(a, 'o')
print(a)

# 1034

a = input()
a = '0o'+a
a = int(a, 8)
print(a)

# 1035

a = input()
a = '0x'+a
a = int(a, 16)
a = oct(a)[2:]
print(a)

# 1036
a = input()
print(ord(a))

# 1037
a = input()

print(chr(int(a)))

# 1038
a, b = input().split()
print(int(a)+int(b))

# 1039

a, b = input().split()
print(int(a)+int(b))

# 1040

a = int(input())


def f(a):
    if a == 0:
        return a
    else:
        return -a


print(f(a))

# 1041
a = input()

a = ord(int(a))+1
print(chr(int(a)))

# 1042
a, b = input().split()
c = int(a)//int(b)
print(c)

# 1045
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)
print("%.2f" % float(a/b))

# 1046
a = list(map(int, input().split()))
a = np.append(a)

print(sum(a))
print("%.1f" % np.mean(a))

# 1048

a, b = input().split()
print(int(a)*2**int(b))

# 1049
a, b = input().split()


def fc(a, b):
    if a > b:
        return 1
    else:
        return 0


print(fc(int(a), int(b)))

# 1050
a, b = input().split()


def f2(a, b):
    if a == b:
        return 1
    else:
        return 0


print(f2(int(a), int(b)))

# 1059
a = int(input())
a = bin(a)
for i in range(len(a)):
    if a[i] == "1":
        a[i] = "0"
    elif a[i] == "0":
        a[i] = "1"
print(format(a, 2))

# 1068
a = int(input())
if a >= 90:
    print("A")
elif a >= 70 and a <= 89:
    print("B")
elif a >= 40 and a <= 69:
    print("C")
else:
    print("D")

# 1069
a = input()

if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

# 1070
a = int(input())

if a == 12 or a == 1 or a == 2:
    print("winter")
elif a >= 3 and a <= 5:
    print("spring")
elif a >= 6 and a <= 8:
    print("summer")
elif a >= 9 and a <= 11:
    print("fall")

n = int(input())
a = list(map(int, input().split()))
for i in a:
    print(i)

# 1076

a = input()
a = ord(a)
arr = ""
for i in range(65, a+1):
    arr.append(chr(i))
print(for i in arr: print(i, end=" "))

# 1099
gmap = []
for _ in range(10):
    gmap.append(list(map(int, input().split())))

start = [2, 2]
x, y = 2, 2
gmap[x][y] = 9
while 1:
    if gmap[x][y+1] == 0:
        y += 1
        gmap[x][y] = 9
    elif gmap[x][y+1] == 1:
        if gmap[x+1][y] == 0:
            x += 1
            gmap[x][y] = 9
        elif gmap[x+1][y] == 1:
            break
        elif gmap[x+1][y] == 2
        x += 1
        gmap[x][y] = 9
        break
    elif gmap[x][y+1] == 2:
        y += 1
        gmap[x][y] = 9
        break

for i in range(10):
    print(" ".join(gmap[i]))


# 1082

a = input()
b = int('0X'+a, 16)

for i in range(1, 16):
    print(a+"*"+format(i, 'X')+"="+format(b*i, 'X'))

# 1083

a = int(input())

for i in range(1, a+1):
    if i % 3 == 0:
        print("X", end=" ")
    else:
        print(i, end=" ")

# 1084
a = list(map(int, input().split()))
c = 0
for i in range(a[0]):
    for j in range(a[1]):
        for k in range(a[2]):
            print(i, j, k)
            c += 1

print(c)

# 1087


# 2623
a, b = input().split()
a, b = int(a), int(b)
c = min(a, b)
answer = 1
for i in range(2, c+1):
    if a % i == 0 and b % i == 0:
        if answer < i:
            answer = i
print(answer)

# 2625
a = int(input())
