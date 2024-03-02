# ------------------------- Q 1 ---------------------------
print('Q 1')

n = 5
i = 1
while i <= n :
    print(i)
    i = i +1 

# ------------------------- Q 2 ---------------------------
    
print('Q 2')

num = 10
j = 1
s = 0 
while j <=num:
    s = s + j
    j = j + 1
print(s)

#---------------------------- Q 3 --------------------------

print("Q 3")

num2 = 5
fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)     

#---------------------------- Q 4 --------------------------

print('Q 4')

str1 = 'qwefghjzxcfghuio'
str2 = str1.upper()
cnt = 0
for i in str2:
    if i == 'A' or  i == 'E' or i == 'I' or i == 'O' or i == 'U' : 
        cnt = cnt + 1
print(cnt)        

#----------------------------- Q 5 ---------------------------

print("Q 5")

for i in range(n +1):
    for j in range(i):
        print("#" , end = " ")
    print()    

#----------------------------- Q 6 ----------------------------

print('Q 6')

cnt = 10
tb = 8
for i in range(1,cnt+1):
    print(f"{tb} X {i} = {tb * i }")