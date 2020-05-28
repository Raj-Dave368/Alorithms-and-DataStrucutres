# maro mahakal


import time

grid = [list(range(0,8)),list(range(8,16)),list(range(16,24)),list(range(24,32)),list(range(32,40)),list(range(40,48)),list(range(48,56)),list(range(56,64))]
for i in grid:
	print(i)

taken = []

def up_left(i):
	return i-8-8-1
def up_right(i):
	return i-8-8+1
def down_left(i):
	return i+8+8-1
def down_right(i):
	return i+8+8+1
def left_up(i):
	return i-1-1-8
def left_down(i):
	return i-1-1+8
def right_up(i):
	if i in [7, 15, 23, 31, 39,47,55]:
		return -1
	return i+1+1-8
def right_down(i):
	if i in [7, 15, 23, 31, 39,47,55]:
		return -1
	return i+1+1+8


def recursive_approach(current, end, stepno):
	print(current,"oMNS",stepno)
	# if current == end:
	# 	print("got it")
	# 	return stepno
	# elif current in taken:
		# print("~~~~~~~~~~~~~~", current)
		# return None
	# else:
		
		
	v1,v2,v3,v4,v5,v6,v7,v8 = (up_left(current),up_right(current),down_left(current),down_right(current),left_up(current),left_down(current),right_up(current),right_down(current))
	l = [v1,v2,v3,v4,v5,v6,v7,v8]
	print(l)
	for i in l:
		if end == i:
			print(i)
			return stepno
	################################### DUMP ##########################################
	# for i in l:
	# 	print(i)
	# 	if  63 < i or  i < 0 or i % 8 == 0 or i in taken:
	# 		l.remove(i) #----------------------------- THANK YOU SO MUH MARA BABUDA for remind me the concept of iterator and iterable
	# 	else:
	# 		taken.append(i)
	################################### DUMP ##########################################
	index = 0
	while index < len(l):
		i = l[index]
	
		if  63 < i or  i < 0 or i % 8 == 0 or i in taken:
			l.remove(i) #----------------------------- THANK YOU SO MUH MARA BABUDA 
			index -= 1
		else:
			taken.append(i)
		index += 1
	print(l)
	return l
"""
		val1 = recursive_approach(up_left(current), end, stepno+1) if  64 > up_left(current) >= 0 and  current % 8 != 0 and up_left(current) not in don_t_trigger_it else None
		val2 = recursive_approach(up_right(current), end, stepno+1) if  64 > up_right(current) >= 0 else None
		val3 = recursive_approach(down_left(current), end, stepno+1) if  64 > down_left(current) >= 0 and  current % 8 != 0 else None
		val4 = recursive_approach(down_right(current), end, stepno+1) if  64 > down_right(current) >= 0 else None
		val5 = recursive_approach(left_up(current), end, stepno+1) if  64 > left_up(current) >= 0 and  current % 8 != 0 else None
		val6 = recursive_approach(left_down(current), end, stepno+1) if  64 > left_down(current) >= 0 and  current % 8 != 0 else None
		val7 = recursive_approach(right_up(current), end, stepno+1) if  64 > right_up(current) >= 0 else None
		val8 = recursive_approach(right_down(current), end, stepno+1) if 64 >  right_down(current) >= 0 else None
		"""
		
		# temp = [val1, val2, val3, val4, val5, val6, val7, val8]
		# t = []
		# for i in temp:
		# 	if i:
		# 		return i
def keepLists(start, end, step):
	l = [start]
	new = []
	ii = 0
	while True and len(new) < 64 and ii < 1000:

		for i in l:
			returned =  recursive_approach(i, end, step)
			if isinstance(returned, (list)):
				new += returned

				# again mara mahakal A proove karyu - Always must think with 
				# "Different Different worst cases and With why questions" whlie wrinting code
			else:
				if returned:
					return returned
			ii += 1
		l = new
		step += 1
		new = []

print(keepLists(0,1,0))