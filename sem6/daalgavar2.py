import datetime
m = input()
do = datetime.datetime.strptime(m,"%b")
m=do.month
print(m)