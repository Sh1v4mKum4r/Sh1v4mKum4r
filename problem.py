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

1 23 =  10
2 13 =  12
3 12 =  12

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
    numbers = list(range(1, n+1))
    all_combinations = []
    for r in range(1, n+1):
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

sumodd,sumeven = 0,0

#Printing the pairs and their sum

print("\nNumbers are as follows:\n\n")

for j in range(len(modified_combinations)):
    combination = modified_combinations[j]
    if(n%2!=0):
        for i in range(0,n,2):      #for odd number of digits
            sumodd+=2**combination[i]
            if i==0:
                print(combination[i],end=" ")
                continue
            print((combination[i]+(combination[i-1]*10)),end=" ")
        print(" = ",sumodd)
        sumodd = 0
    else:       #for even number of digits
        if j>=int(len(modified_combinations)/2):
            break
        for i in range(1,n,2):
            sumeven+=2**combination[i]
            print(combination[i]+(combination[i-1]*10),end=" ")
        print(" = ",sumeven)
        sumeven = 0

print("All combinations are exauhsted\n\n")

#end of code

"""
Problem solved by Shivam Kumar Arya.
-Thankyou
"""