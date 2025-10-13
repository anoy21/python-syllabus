# EX 1

# a = 4
# b = 8
# if a < b:
#      a = a**2 + b
# else:
#      a = a + 2 * b

# if a < 20:
#      b = b + 5 * a
# else:
#      b = b + 10

# print(a,b)



# EX 2
    
# salary = int(input("Enter your salary: "))

# if salary <= 10000:
#     ptax = salary * 0.9
# elif 10001 <= salary <= 50000:
#     ptax = 0.9 * 10000 + (salary - 10000)   * 0.8
# else:
#     ptax = 0.9 * 10000 + 0.8 * 40000 + (salary - 50000) * 0.6

# print(ptax)


# EX 3

# nums = [2**i for i in range(0,8)]
# for n in reversed(nums):
#     print(n)


# EX 4

# a = 4
# b = 6
# if a < b then a  = a + 2 * b
# else  a = a**2 +b
# if a < 20 then b = b + 10

#EX 5

# def factorial_enum(n):
#     fact = 1
#     for i in range(1, n + 1):   
#         fact *= i
#     return fact
# print(factorial_enum(5))


# def factorial_pre():
#     n = int(input("Num: "))
#     i = 1
#     fact = 1
#     while i <= n:
#         fact *= i
#         i += 1
#     print(fact)

# factorial_pre()


#EX 6

# nums = list(map(int, input("Enter numbers seperated by space: ").split()))
# largest = nums[0]
# for i in range(len(nums)):
#     if nums[i] > largest:
#         largest = nums[i]

# print(largest)


# nums = list(map(int, input("Enter numbers seperated by space: ").split()))
# lowest = nums[0]
# for i in range(len(nums)):
#     if nums[i] < lowest:
#         lowest = nums[i]

# print(lowest)

#EXTRA

# N = int(input("num: "))
# i = 1
# while i < N:
#     sum = 1/N + 1/(N - i) + 1
#     i += 1
# print(sum)


N = int(input("num: "))
i = 1
while i < N:
    sum = 1 
    













