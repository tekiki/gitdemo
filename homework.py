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
#使用冒泡排序
for i in range(0,n-1):
    change=False
    for j in range(0,n-i-1):
        if lb[j][3]<lb[j+1][3]:#比较总分
            lb[j],lb[j+1]=lb[j+1],lb[j]
            change=True#发生了替换
        elif lb[j][3]==lb[j+1][3]:#总分相同
            if lb[j][0]<lb[j+1][0]:#比较数分成绩
                lb[j],lb[j+1]=lb[j+1],lb[j]
                change=True#发生了替换
            elif lb[j][0]==lb[j+1][0]:#数分成绩相同
                if lb[j][4]>lb[j+1][4]:#比较学号
                    lb[j],lb[j+1]=lb[j+1],lb[j]
                    change=True#发生了替换
    if change==False:
        break#未发生替换，结束循环