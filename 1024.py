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
