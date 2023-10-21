# Solving the first coding test
target=6
nums=[3,2,4]
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])

# Sovling the second coding test
l1 = [2,4,3]
l2 = [5,6,4]
truel1=""
truel2=""
for i in range(0,len(l1)):
    truel1 = truel1 + str(l1[::-1][i])
for i in range(0,len(l2)):
    truel2 = truel2 + str(l2[::-1][i])
true=int(truel1) + int(truel2)
map(int, str(true))

#next problems
#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
I=1
V=5
X=10
L=50
C=100
D=500
M=1000
s="III"
contane=0
for i in range(0,len(s)):
    if s[i] == "I":
        contane+=1
    if s[i] == "V":
        contane+=5
    if s[i] == "L":
        contane+=50
    if s[i] == "X":
        contane+=10
    if s[i] == "C":
        contane+=100
    if s[i] == "D":
        contane+=500
    if s[i] == "M":
        contane+=1000
print(contane)