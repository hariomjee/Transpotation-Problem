cost=[
	  [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8, 3, 3, 2]
     ]
supply = [300, 400, 500]
demand = [250, 350, 400, 200]

def TopLeftCorner(s,d):
	table=[]
	for x in range(s):
		temp=[]
		for y in range(d):
			temp.append(0)
		table.append(temp)
	toAllocate(table,0,0)
	return table

def toAllocate(table2,x,y):
	global sTot,dTot
	if sTot==0 and dTot==0:
		return table2
	if supply[x]<demand[y]:
		table2[x][y]=supply[x]
		demand[y]-=supply[x]
		supply[x]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,x+1,y)
	elif supply[x]>demand[y]:
		table2[x][y]=demand[y]
		supply[x]-=demand[y]
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,x,y+1)
	elif supply[x]==demand[y]:
		table2[x][y]=supply[x]
		supply[x]=0
		demand[y]=0
		sTot=sum(supply)
		dTot=sum(demand)
		toAllocate(table2,x+1,y+1)

sTot=sum(supply)
dTot=sum(demand)
s=len(supply)
d=len(demand)
if sTot<dTot:
	s+=1
	supply.append(dTot - sTot)
	sTot=sum(supply)
	temp=[]
	for x in range(len(demand)):
		temp.append(0)
	cost.append(temp)

elif sTot>dTot:
	d+=1
	demand.append(sTot - dTot)
	dTot=sum(demand)
	for x in range(len(supply)):
		cost[x].append(0)

resultTable=TopLeftCorner(s,d)
print("Cost Table:")
for row in cost:
	print(row)
print("\nAllocation Table:")
for row in resultTable:
	print(row)
print("\nCost Minimum:")
Cost=0
flag=0
for x in range(s):
	for y in range(d):
		if resultTable[x][y]==0:
			continue
		if flag==1:
			print(" + ", end='')
		print("%d"%(resultTable[x][y]),end='')
		print("x%d"%(cost[x][y]),end='')
		if x<s-1 or y<d-1:
			flag=1
		Cost+=resultTable[x][y]*cost[x][y]
print(" =",Cost)
