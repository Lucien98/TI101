def affine_input (x0, x1, x2, x3, x4, x5, x6, x7):
	y0 = x0 + x1 + x2 + x5 + x6 + x7
	y1 = x0 + x4 + x5 + x6
	y2 = x0 + x1 + x5 + x6
	y3 = x0 + x5 + x6 + x7
	y4 = x0 + x1 + x3 + x4 + x7
	y5 = x0
	y6 = x0 + x5 + x6
	y7 = x0 + x1 + x2 + x3
	return y0%2, y1%2, y2%2, y3%2, y4%2, y5%2, y6%2, y7%2

def SqSclMul_GF16 (a,b,c,d,e,f,g,h):
	x = a*e + a*f + a*g + b*e + b*h + c*e + c*g + d*f + d*h + a + e
	y = a*e + a*h + b*f + b*g + b*h + c*f + c*h + d*e + d*f + d*g + d*h + a + b + e + f
	z = a*e + a*g + b*f + b*h + c*e + c*g + c*h + d*f + d*g + b + d + f + h
	t = a*f + a*h + b*e + b*f + b*g + b*h + c*f + c*g + d*e + d*f + d*h + a + c + e + g
	return x%2,y%2,z%2,t%2

def SqSclMul_GF4 (a,b,c,d):
	x = a*c + a*d + b*c + b + d
	y = a*d + b*c + b*d + a + b + c + d
	return x%2,y%2

def Mul_GF4 (a, b, c, d):
	x = a*d + b*c + b*d
	y = a*c + a*d + b*c
	return x%2,y%2

def Mul_GF16 (a, b, c, d, e, f, g, h):
	x = a*e + a*f + a*g + b*e + b*h + c*e + c*g + d*f + d*h
	y = a*e + a*h + b*f + b*g + b*h + c*f + c*h + d*e + d*f + d*g + d*h
	z = a*e + a*g + b*f + b*h + c*e + c*g + c*h + d*f + d*g
	t = a*f + a*h + b*e + b*f + b*g + b*h + c*f + c*g + d*e + d*f + d*h
	return x%2,y%2,z%2,t%2

def affine_output (x0, x1, x2, x3, x4, x5, x6, x7):
	y0 = x2 + x4
	y1 = x0 + x4
	y2 = x1 + x7
	y3 = x0 + x2 + x4
	y4 = x0 + x1 + x2 + x3
	y5 = x1 + x2 + x4 + x5
	y6 = x2 + x3 + x6
	y7 = x1 + x3 + x6
	return y0%2 , y1%2, y2%2, y3%2, y4%2, y5%2, y6%2, y7%2

def GFInv256 (x0, x1, x2, x3, x4, x5, x6, x7):
	x1,y1,z1,t1 = SqSclMul_GF16 (x0, x1, x2, x3, x4, x5, x6, x7)
	x2,y2 = SqSclMul_GF4 (x1,y1,z1,t1)
	x3,y3 = x2,y2
	x4,y4 = Mul_GF4(x1,y1, x3,y3)
	z4,t4 = Mul_GF4(x3,y3, z1,t1)
	xx0,xx1,xx2,xx3 = Mul_GF16(x0, x1, x2, x3, x4, y4, z4, t4)
	xx4,xx5,xx6,xx7 = Mul_GF16(x4, y4, z4, t4, x4, x5, x6, x7)
	return xx0%2 ,xx1%2,xx2%2,xx3%2,xx4%2,xx5%2,xx6%2,xx7%2

def sbox (t0, t1, t2, t3, t4, t5, t6, t7):
	# t0, t1, t2, t3, t4, t5, t6, t7 = affine_input (t0, t1, t2, t3, t4, t5, t6, t7)
	t0, t1, t2, t3, t4, t5, t6, t7 = GFInv256 (t0, t1, t2, t3, t4, t5, t6, t7)
	# t0, t1, t2, t3, t4, t5, t6, t7 = affine_output (t0, t1, t2, t3, t4, t5, t6, t7)
	# t0, t1, t2, t3, t4, t5, t6, t7 = t0+1, t1+1, t2, t3, t4, t5, t6+1, t7+1
	return t0%2 , t1%2, t2%2, t3%2, t4%2, t5%2, t6%2, t7%2

def main():
	for i in range(256):
		x0 = (i>>0) & 1
		x1 = (i>>1) & 1
		x2 = (i>>2) & 1
		x3 = (i>>3) & 1
		x4 = (i>>4) & 1
		x5 = (i>>5) & 1
		x6 = (i>>6) & 1
		x7 = (i>>7) & 1
		sin = 0
		sin += x0 << 7 
		sin += x1 << 6 
		sin += x2 << 5 
		sin += x3 << 4 
		sin += x4 << 3 
		sin += x5 << 2 
		sin += x6 << 1 
		sin += x7 << 0
		t0, t1, t2, t3, t4, t5, t6, t7 = sbox(x0, x1, x2, x3, x4, x5, x6, x7)
		sout = 0
		sout += t0 << 0 
		sout += t1 << 1 
		sout += t2 << 2 
		sout += t3 << 3 
		sout += t4 << 4 
		sout += t5 << 5 
		sout += t6 << 6 
		sout += t7 << 7
		print(hex(sin), hex(sout)) 

if __name__ == '__main__':
	main()
