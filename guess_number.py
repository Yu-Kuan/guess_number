# 產生一個隨機整數1~100(不要印出)
# 讓使用者重複輸入數字去猜
# 猜對的話印出"終於猜對了"
# 猜錯的話要告訴他比答案大/小

import random
r = random.randint(1, 100)
count = 0
while True:
	num = input('請猜數字: ')
	num = int(num)
	count = count + 1 #count += 1
	print('這是你猜了', count, '次')
	if num == r:
		print('終於猜對了!')
		break
	else:
		if num > r:
			print('猜錯了', num, '比答案大!')
		elif num < r:
			print('猜錯了', num, '比答案小!')
