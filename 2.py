# class Student:
#     def __init__(self,name,a,b,c,score):
#         self.name = name
#         self.a = a
#         self.b = b
#         self.c = c
#         self.score = score
#     def prn(self):
#             print("%s %d %d %d %d" % (self.name, self.a, self.b, self.c, self.score))


# n = int(input())
# stu = []
# for i in range(n):
#     name, a,b,c = input().split()
#     a = int(a)
#     b = int(b)
#     c = int(c)
#     score = a+b+c
#     stu.append(Student(name,a,b,c,score))

# for i in range(n):
#     for j in range(n-i-1):
#         if stu[j].score < stu[j+1].score:
#             stu[j], stu[j+1] = stu[j+1], stu[j]



# for s in stu: 
#     s.prn()

#################################


# class Square:
#     def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
#         self.x1=x1
#         self.y1=y1
#         self.x2=x2
#         self.y2=y2
#         self.x3=x3
#         self.y3=y3
#         self.x4=x4
#         self.y4=y4
   
#     def prn(self):
#             print("%d %d %d %d" % (self.a, self.b, self.c, self.score))



# x1,y1,x2,y2 = input().split()
# x1 = int(x1)
# y1 = int(y1)
# x2 = int(x2)
# y2 = int(y2)

# x3,y3,x4,y4 = input().split()
# x3 = int(x3)
# y3 = int(y3)
# x4 = int(x4)
# y4 = int(y4)


# Square().prn




# class Square:
#     def __init__(self,xa,ya,xb,yb):
#         self.xa=xa
#         self.ya=ya
#         self.xb=xb
#         self.yb=yb
   
#     def prn(self):
#             print("%s %s %s %s" % (self.xa, self.yb, self.xb, self.yb))


# x1,y1,x2,y2 = input().split()
# x1 = int(x1)
# y1 = int(y1)
# x2 = int(x2)
# y2 = int(y2)

# x3,y3,x4,y4 = input().split()
# x3 = int(x3)
# y3 = int(y3)
# x4 = int(x4)
# y4 = int(y4)

# if x1<x3:
#     xa=x1
# else:
#     xa=x3

# if y1<y3:
#     ya=y1
# else:
#     ya=y3

# if x2>x4:
#     xb=x2
# else:
#     xb=x4

# if y2>y4:
#     yb=y2
# else:
#     yb=y4

# print(xa,ya,xb,yb)
# s=Square(xa,ya,xb,yb)
# s.prn


####################### 함수3 형성평가 3

# arr=[0,0,0,0,0,0,0,0,0,0,0]


# def output():
#     sum=0 
#     for i in arr:
#         sum+=i
#     if sum-1==M:
#         for i in range(1,N+1):
#             print(arr[i],end=" ",)
#         print("\n")

# def dice(level):
#     if (level > N):
#         output()
#         return()

#     for i in range(arr[level-1],7):
#         arr[level] = i
#         dice(level+1)
 
# N,M = map(int,input().split(" "))
# arr[0] = 1
# dice(1)


 
sum=[0,0,0,0,0,0,0,0,0,0]
a = 0
N,M=0

def dice(N,M):
    for i in range(7):
        sum[a] = i
        if (a == N-1):
            total = 0
            for j in range(a+1):
                total += sum[j]
 
            if (total == M):
                for k in range (N+1):
                    print(sum[k])
                print("\r\n")
        else:
            a=+1
            dice(N, M)
            a=-1


N,M = map(int,input().split(" "))
dice(N, M)
 