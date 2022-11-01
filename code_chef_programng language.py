test_case=int(input())
for i in range(0,test_case):
    language=list(map(int,input().split()))
    k=0
    if( language[0]==language[2] or language[0]==language[3]) and (language[1]==language[2] or language[1]==language[3]):
        k=1
    if (language[0]==language[4] or language[0]==language[5]) and (language[1]==language[4] or language[1]==language[5]):
       k=2
   
    print(k)
    