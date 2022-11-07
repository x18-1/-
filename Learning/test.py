

s = [i.replace("\n","") for i in open('1.txt',encoding='utf-8') if i not in ['\n',' ','']]
ss = [k for k,i in enumerate(s) if ". (填空题)" in i or ". (判断题)" in i or ". (简答题)" in i]
# print(ss,len(ss))
count = 0
for i in ss:
    i = i+count
    s.insert(i,"$")
    count+=1

def f(s):
    result = [[] for i in range(51)]
    scan,i = 0,0
    while i<len(s):
        if s[i] != "$":
            result[scan].append(s[i])
        elif s[i]=="$":
            scan+=1
        i+=1
    return result

print(f(s))
            