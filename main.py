# factorial
def fact_recursion(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_recursion(n-1)
number=int(input("enter the number:"))
res=fact_recursion(number)
print("the factorial of {} is {}".format(res, number)) 