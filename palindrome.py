try:
    def func(n):
        reverse=0
        while n>0:
            reminder=n%10
            reverse=reverse*10+reminder
            n=n//10
        return reverse
    a = int(input("Enter the Number of test cases:\t"))
    l=[]
    for i in range(1,a+1):
        l.append(int(input(f"{int(i)} = ")))
    for j in l:
        n=int(j)
        while True:
            y=func(n)
            if n==y:
                print(f"The next palindrome of {j} is {n}")
                j=j+1
                break
            else:
                n=n+1
except Exception as e:
    print("You have done something wrong, Enter correctly")
