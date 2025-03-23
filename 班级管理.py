class Student:
    def __init__(self,name,nums,score,level):
        self.name=name
        self.nums=nums
        self.score=score
        self.level=level
    def information(self):
        print(f"{self.name}'s student number is {self.nums}, and his grade is {self.score}.He submitted {len(self.level.split())} assignments,each with a grade of {self.level}")
a=input()
b=input()
c=int(input())
d=input()
m=Student(a,b,c,d)
m.information()
