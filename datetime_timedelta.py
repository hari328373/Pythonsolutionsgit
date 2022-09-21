import datetime
string="%a %d %b %Y %H:%M:%S %z"
t=int(input())
for test in range(t):
    t1=input()
    t2=input()
    T1=datetime.datetime.strptime(t1,string)
    T2=datetime.datetime.strptime(t2,string)
    difference=T1-T2
    print(int(abs(difference.total_seconds())))
