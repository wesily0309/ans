from datetime import datetime
a=input()
b=input()
a= datetime.strptime(a, "%H:%M:%S")
b= datetime.strptime(b, "%H:%M:%S")
t=False 
if a<b:
	a,b=b,a
	t=True
bc=(a-b)
if t:
	print(f'快 {bc.seconds} 秒')
else:
	print(f'慢 {bc.seconds} 秒')
