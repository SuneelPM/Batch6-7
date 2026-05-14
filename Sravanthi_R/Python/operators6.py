# m=int(input())
# days=m//1440
# r_mun=m%1440
# hrs=r_mun//60
# min=r_mun%60
# print(days,"days",hrs,"hrs",min,"min")


# days=int(input())
# years=days//365
# r_days=days%365
# months=r_days//30
# remining_days=r_days%30
# print(years,"years",months,"months",remining_days,"remining_days")

# n=int(input())
# d1=n//10
# d2=n%10
# reverse=d2*10
# sum=reverse+8
# total=sum+n
# print(total)

# yr=int(input())
# leap=((yr%4==0 &yr%4!=0)or(yr%400==0))
# print("leap year"*leap+"non-leap"*(1-leap))

a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a)
print(b)


