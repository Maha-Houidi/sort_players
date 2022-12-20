n=int(input()) #nb of players
ds,dt={},{}
for i in range(n):
    result = input()
    n,s,t = result.split()
    ds[n]=int(s[:s.index("%")]) #store the score of each player
    dt[n]=int(t[:t.index(":")])*60+int(t[t.index(":")+1:]) #store the time of each player in seconds
dic={}
unique_scores=list(set( val for val in ds.values()))
unique_scores.sort(reverse=True) 
for score in unique_scores:
    dic[score]={}
    for key in ds:
        if ds[key] == score:
            dic[score][key]=dt[key]

for key in dic:
    df=dict(sorted(dic[key].items(), key=lambda item: item[1]))
    dic[key]=df

print("-------------------------")
for key in dic :
    for k in dic[key]:
        print(k , str(key)+"%" , str(dic[key][k]//60)+":"+str(dic[key][k]%60))