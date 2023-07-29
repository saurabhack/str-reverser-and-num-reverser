from django.shortcuts import render

# Create your views here.
def pop(stack):
    return stack.pop()

def reverse(string):
    arr=[]
    size=len(string)
    for i in range(size):
        arr.append(string[i])
    string=''
    for j in range(size):
        string+=pop(arr)
    return string

def reverseNum(num):
    re=0
    while(int(num)>0):
        dev=int(num%10)
        re=re*10+dev
        num=num//10
    return re
def index(request):
    if request.method=='POST':
        string=request.POST['text']
        result=reverse(string)
        return render(request,'index.html',{'result':result})
    return render(request,'index.html')

def number(request):
    if request.method=='POST':
        num=request.POST['num']
        num=int(num)
        res=reverseNum(num)
        return render(request,'number.html',{'res':res})
    return render(request,'number.html')





