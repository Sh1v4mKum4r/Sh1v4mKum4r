"""

This code is a
solution for the problem where all possible combinationa are generated and then modified to get the desired output
The problem is as follows:
. Given a number n, we need to find all the possible combinations of n numbers and then modify the combination to make a pair (if even then the first digit will be unparied)
. and then find the sum of 2 to the power of the second digit of the pairs, print the pairs and their sum

Example:

Input: 3

Output:

Numbers are as follows:

[1, 23] = 2+8 = 10
[2, 13] = 4+8 = 12
[3, 12] = 8+4 = 12

All combinations are exauhsted

"""

#start of code

def generate_combinations(numbers, r):      #function to generate all possible combinations
    combinations = [[]]
    
    for _ in range(r):
        new_combinations = []
        for combination in combinations:
            for number in numbers:
                if number not in combination:
                    new_combinations.append(combination + [number])
        combinations = new_combinations
    
    return combinations

def get_combinations(n):        #function to get all possible combinations
    numbers = list(range(2,n+2))    #list of numbers[1 - (n+1)] to generate combinations taking value of zero into account
    all_combinations = []
    for r in range(1,n+1):
        combinations = generate_combinations(numbers, r)
        all_combinations.extend(combinations)
    
    return all_combinations

def modify_combinations(all_combinations, n):       #function to modify the combinations
    if n%2==0:
        three_element_lists = [comb for comb in all_combinations if len(comb) == n and all(comb[i] < comb[i+1] for i in range(0, n-1, 2))]
    else:
        three_element_lists = [comb for comb in all_combinations if len(comb) == n and all(comb[i] < comb[i+1] for i in range(1, n-1, 2))]
    modified_combinations = [[element-1 for element in comb] for comb in three_element_lists]
    return modified_combinations

n=int(input())+1        #input the number

all_combinations = get_combinations(n)

modified_combinations = modify_combinations(all_combinations, n)

l1,l2=[],[]
for i in range(n//2 if n%2==0 else n//2+1):
    l2.append(0)
l1=[l2[:] for i in range(len(modified_combinations) if n%2!=0 else len(modified_combinations)//2)]  #list to store the pairs

#Printing the pairs and their sum

print("\nNumbers are as follows:\n")

for j in range(len(modified_combinations)):
    combination = modified_combinations[j]
    if(n%2!=0):
        c=1
        for i in range(0,n,2):      #for odd number of digits
            if i==0:
                l1[j][i]=combination[i]
                continue
            l1[j][c]=(combination[i]+(combination[i-1]*10))     #storing the pairs
            c+=1
    
    else:       #for even number of digits
        if j>=int(len(modified_combinations)/2):
            break
        c=0
        for i in range(1,n,2):
            l1[j][c]=(combination[i]+(combination[i-1]*10))     #storing the pairs
            c+=1
    l1[j].sort()
l1.sort()

lf=[]       #list to store the pairs
c=0

for i in range(len(l1)):        #removing duplicates
    if l1[i][:]!=l1[i-1][:]:
        lf.append([x-11 for x in l1[i][:]])     #reverting the list of numbers to [0-n] as it was modified to be [1-(n+1)] to generate combinations and take the value of zero into account
        lf[c][0]+=10 if n%2!=0 else 0
        c+=1


for i in lf:        #printing the pairs and their sum
    print(i,end=" = ")
    sum=0
    for j in range(len(i)):
        twopower=2**i[j] if i[j]<10 else 2**(i[j]%10)       #finding the sum of 2 to the power of the second digit of the pairs
        sum+=twopower
        print(twopower,end="+"if j!=len(i)-1 else " = ")
    print(sum)

print("\nAll combinations are exauhsted\n\n")


#end of code

"""
Problem solved by Shivam Kumar Arya.
-Thankyou
"""