import math
def solution(fees, records):
    dic={}
    dic1={}
    for r in records:
        t,n,s=r.split()
        h,m=map(int,t.split(":"))
        if n not in dic.keys():
            dic[n]=[]
        if dic[n] != []:
            if n not in dic1.keys():
                dic1[n] = 0
            dic1[n]+=(60*h)+m-dic[n].pop()
        else:
            dic[n].append((60*h)+m)
    for a,b in dic.items():
        if b != []:
            if a not in dic1:
                dic1[a]=0
            dic1[a]+=(1439-b[0])
    for i in dic1.keys():
        if dic1[i] <= fees[0]:
            dic1[i] = fees[1]
        else:
            dic1[i] = fees[1]+math.ceil((dic1[i]-fees[0])/fees[2])*fees[3]
    a=sorted(dic1.items(),key=lambda x:int(x[0]))
    li=[]
    for i in a:
        li.append(i[1])
    return li
