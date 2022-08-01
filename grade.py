"""
1.ask user to input their marks and convert ity to float
2.usee if condition to print grade a if the usermark is greater than 90
3. use elif to print grade b if the user mark is greater than 80 and less then equal to 90
4.again use elif condition to print grade c when usermark is greater tha 60 and less then equal to 80
.use else condition foe rest (which is less than 60)
"""

usermark=float(input("enter your mark "))
if usermark>90:
    print("grade A")
elif usermark>80 and usermark<=90:
    print("grade B")
elif usermark>60 and usermark<=80:
    print("grade C")
else :
    print("failed")

