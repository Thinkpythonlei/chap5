# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 18:59:26 2022

@author: Surface
"""
import time
t=time.time()
print(t)
day=int(t//(60*60*24))
hour=int(t//(60*24))
min=int(t//(24))
sec=int(t//(1))

print("从纪元到现在经历的天数为",day)
print("从纪元到现在经历的小时数为",hour)
print("从纪元到现在经历的分钟数为",min)
print("从纪元到现在经历的秒钟数为",sec)



def check_fermat(a,b,c,n):
    if (n>2 and a**n+b**n==c**n):
        print( "Holy smokes, Fermat was wrong!")
    else: 
        print( "No,that doesn’t work.")
        
check_fermat(2,3,4,5)





def is_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print("yes")
    else:
        print("no")
        
def input_is_triangle():
    a=input("请输入正整数a:")
    a=int(a)
    b=input("请输入正整数b:")
    b=int(b)
    c=input("请输入正整数c:")
    c=int(c)
    is_triangle(a,b,c)
    
input_is_triangle()




def recurse (n , s ) :
    if n == 0:
        print (s)
    else :
        recurse (n-1, n+s )

recurse (3 , 0)
#这个函数输出的是在n到s这个区间里面，如果n不等于0那么，将n每次都减1计算n到s的和，这个例子里面
#recurse (3 , 0)的输出结果为6



import turtle
bob = turtle.Turtle()
turtle.delay(0.01)


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n - 1)
    t.rt(2 * angle)
    draw(t, length, n - 1)
    t.lt(angle)
    t.bk(length * n)
draw(bob,20,10)
#这个程序允许出来是一个分支结构，分支与原来的夹角为50度，初试长度为20的一条线，然后分为
#夹角为50度的两条长度为20的二分之一的线，依次类推运行10次



def koch(t,x):
    if x >3:
        koch(t,x/3)
        t.lt(60)
        koch(t,x/3)
        t.rt(120)
        koch(t,x/3)
        t.lt(60)
        koch(t,x/3)
    else:
        t.fd(x)
        
koch(bob,300)

for i in range(3):
    koch(bob,300)
    bob.rt(120)
    
    























    