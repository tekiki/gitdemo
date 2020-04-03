#实验6-1
a=input()#输入驼峰命名法命名的变量名
list1=list(a)#将变量名转成列表
for i in range(1,n+1):
    tup=input().split()
    tup[0]=int(tup[0])
    tup[1]=int(tup[1])
    tup[2]=int(tup[2])
    he=sum(tup)#计算总分
    tup.append(he)#添加总分
    tup.append(i)#添加学号
    lb.append(tup)#存入列表