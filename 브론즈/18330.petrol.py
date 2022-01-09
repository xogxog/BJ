fuel = int(input())
remain_credit = int(input())

total_credit = 60 + remain_credit

if total_credit >= fuel :
    print(fuel*1500)
else :
    print(((fuel-total_credit)*3000)+(total_credit*1500))