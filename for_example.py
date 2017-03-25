#!/usr/bin/python3.6
for i in 'hello world':
	if i == 'a':
		break
	print(i * 2, end = '')
else:
	print("Баквы 'a' в строке нет.")
