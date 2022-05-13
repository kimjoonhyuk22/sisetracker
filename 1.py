
class Student:
    def __init__(self,name,a,b,c):
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        # self.score = score
    def prn(self):
            print("%s %d %d %d " % (self.name, self.a, self.b, self.c))


n = int(input())
stu = []
for i in range(n):
    name, a,b,c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    stu.append(Student(name,a,b,c))

# for i in range(n-1):
#     for j in range(i+1,n):
#         if stu[i].a > stu[j].a:
#             stu[i], stu[j] = stu[j], stu[i]

# for s in stu: 
#     s.prn()

