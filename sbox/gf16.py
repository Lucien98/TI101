xx = 0
yy = 0
zz = 0
tt = 0
for i in range (16):
	d = (i >> 3) & 1
	c = (i >> 2) & 1
	b = (i >> 1) & 1
	a = (i >> 0) & 1
	# print(a,b,c,d)
	x = (a + b + d + b*c + b*d + c*d + a*b*c) %2
	y = (b + c + d + a*c + b*d + a*b*d + a*c*d) %2
	z = (c + d + b*c + c*d + a*c*d + b*c*d) %2
	t = (c + d + a*d + b*d + b*c*d) %2
	print(hex(x+y*2+z*4+t*8))
	xx += x
	yy += y
	zz += z
	tt += z	
	# print(x,y,z,t)
print(xx,yy,zz,tt)
xx = 0
yy = 0
zz = 0
tt = 0

for i in range (16):
	# d = (i >> 3) & 1
	# c = (i >> 2) & 1
	# b = (i >> 1) & 1
	# a = (i >> 0) & 1
	a = (i >> 3) & 1
	b = (i >> 2) & 1
	c = (i >> 1) & 1
	d = (i >> 0) & 1
	# print(a,b,c,d)
	x = (c + d + a*c + b*c+ b*c*d) %2
	y = (d + a*c + b*c + b*d + a*c*d) %2
	z = (a + b + a*c + c*d + a*d + b*c*d) %2
	t = (b + a*c + a*d + b*d + a*b*c) %2
	# print(x,y,z,t)
	print((x+y*2+z*4+t*8))
	# print(hex(x*8+y*4+z*2+t))
	xx += x
	yy += y
	zz += z
	tt += z	
	# print(x,y,z,t)
print(xx,yy,zz,tt)
