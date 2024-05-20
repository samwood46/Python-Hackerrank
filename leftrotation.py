def left_rotation(a,d):
	while d > 0:
		i = 0
		last = a[0]
		while i < len(a)-1:
			a[i] = a[i+1]
			i += 1
		a[-1] = last
		d -= 1
	return a

print (left_rotation([1,2,3,4,5],4))