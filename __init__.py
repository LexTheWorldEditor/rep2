# -*- coding: utf-8 -*-
from _ast import If
def isPal(x):
    if x<0:
        return "Number < 0"
    temp = x
    rev = 0
    while(temp>0):
        temp2 = temp %10
        rev = rev*10 + temp2
        temp = temp//10
    if rev==x:
        print("is palindrome")
    else:
        print("not palindrome")

def listSplitter(ls):
    ls2 = []
    ls3 = []
    ls5 = []
    for i in range(0,len(ls)):
        if ls[i] % 2 == 0:
            ls2.append(ls[i])
        if ls[i] % 3 == 0:
            ls3.append(ls[i])
        if ls[i] % 5 == 0:
            ls5.append(ls[i])
    print (ls2)
    print (ls3)
    print (ls5)

def reverser(num): 
    rev_num = 0 
    if num>0:
        while (num>0):
            dop=num%10
            rev_num=rev_num*10+dop
            num = num // 10
        return rev_num
    else:
        while (num<0):
            dop= num % -10
            rev_num=rev_num*10+dop
            num=(num//10)+1
        return rev_num

def rt(num, n): 
    if num<0:
        return "Number < 0"
    approx = num / n 
    while True:
        bet = ((n-1)*approx + num / approx**(n-1)) / n 
        if abs(approx - bet) < 0.00001: 
            return bet
        approx = bet

def sim(num):
    if (num > 100000):
        return "Number > 100000"
    for i in range(2,num-1):
        if (num % i == 0): 
            return "false"
    return "true"

x = int(input("Enter number: "))
print(isPal(x))
ls = [ ]
n = int(input("Enter amount of numbers in list: "))
for i in range(0,n):
    ls.append(int(input("Enter number in list: ")))
listSplitter(ls)
print(reverser(x))

num = int(input("Enter number for root calculating: ")) 
s = float(input("Enter index of root: ")) 
print (rt(num, s))

idle = int(input("Enter number from 0 to 100000: "))
print(sim(idle))

