import time

file=open('Log_Load_cell.log','r')
lines = file.readlines()
count = 0
logs = {}
for line in lines:
    logs[count] = line.strip()
    count += 1
list1=[]
list2=[]
for i in range(len(logs)):
    values=logs[i]
    values1=values.split('     ')
    list1.append(values1[0])
    list2.append(values1[1])
sleep=0
def Load_cell(ct):
    if ct!=0:
        sleep=float(list2[ct])/1000
        time.sleep(sleep)
    return list1[ct]
    
    