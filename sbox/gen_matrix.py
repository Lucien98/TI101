

# paper81
def gen_matrix(inv):
	with open(inv + 'matrix.txt', 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			# print (terms)
			s = "y" + str(i) + ' = '
			for t in terms[0:-1]:
				t = int(t)
				t = 7-t
				s += 'x'
				s += str(t)
				s += ' + '
			s = s[0:-3]
			print(s)

# A More Efficient AES Threshold Implementation
def gen_gf_mul16(out_name, in_name, sqscl):
	with open('gf_mul16.txt', 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			s = "%s[%d] = " % (out_name, 3-i) # out[3] = 

			for t in terms[0:-1]:
				if len(t) == 1 and sqscl == 0: continue
				if len(t) == 2:
					t0 = int(t[0])
					t1 = int(t[1])
					t0 = 8 - t0
					t1 = 8 - t1
					s += ("(%s_1[%d] & %s_2[%d])" % (in_name, t0%4, in_name, t1))
					s += ' ^ '
				if len(t) == 1:
					t0 = int(t[0])
					t0 = 8 - t0
					if t0 >= 4:
						s += ("%s_1[%d] ^ "% (in_name, t0%4) )
					else:
						s += ("%s_2[%d] ^ "% (in_name, t0) )
			s = s[0:-3]
			s += ";"
			print(s)

def gen_gf_mul16_latex(out_name, in_name, sqscl):
	with open('gf_mul16.txt', 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			s = "&%s_%d = " % (out_name, 3-i) # out[3] = 

			for t in terms[0:-1]:
				if len(t) == 1 and sqscl == 0: continue
				# if len(t) == 1 and sqscl == 1: 
					# continue
				if len(t) == 2 and sqscl != 2:
					t0 = int(t[0])
					t1 = int(t[1])
					t0 = 8 - t0
					t1 = 8 - t1
					s += ("%s_%d %s_%d" % (in_name, t0, in_name, t1))
					s += ' + '
				if len(t) == 1:
					t0 = int(t[0])
					t0 = 8 - t0
					if t0 >= 4:
						s += ("%s_%d + "% (in_name, t0) )
					else:
						s += ("%s_%d + "% (in_name, t0) )
			s = s[0:-3]
			s += r"\\"
			print(s)

def gen_gf_inv16_latex(out_name, in_name):
	with open('gf_inv16.txt', 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			s = "&%s_%d = " % (out_name, 3-i) # out[3] = 

			for t in terms[0:-1]:
				if len(t) == 3:
					t0 = int(t[0])
					t1 = int(t[1])
					t2 = int(t[2])
					t0 = 4 - t0
					t1 = 4 - t1
					t2 = 4 - t2
					s += ("%s_%d %s_%d %s_%d" % (in_name, t0, in_name, t1, in_name, t2))
					s += ' + '
				if len(t) == 2:
					t0 = int(t[0])
					t1 = int(t[1])
					t0 = 4 - t0
					t1 = 4 - t1
					s += ("%s_%d %s_%d" % (in_name, t0, in_name, t1))
					s += ' + '
				if len(t) == 1:
					t0 = int(t[0])
					t0 = 4 - t0
					if t0 >= 4:
						s += ("%s_%d + "% (in_name, t0) )
					else:
						s += ("%s_%d + "% (in_name, t0) )
			s = s[0:-3]
			s += r"\\"
			print(s)

def gen_gf_inv16_abc_little(out_name, in_name):
	with open('gf_inv16_r.txt', 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			# s = "&%s_%d = " % (out_name, 3-i) # out[3] = 
			s = ""
			if i == 0: s = "&t = "
			if i == 1: s = "&z = "
			if i == 2: s = "&y = "
			if i == 3: s = "&x = "

			for t in terms[0:-1]:
				if len(t) == 3:
					t0 = int(t[0])
					t1 = int(t[1])
					t2 = int(t[2])
					t0 = 4 - t0
					t1 = 4 - t1
					t2 = 4 - t2
					s += ("%s %s %s" % ( chr(97 + t0), chr(97+t1), chr(97+t2)))
					s += ' + '
				if len(t) == 2:
					t0 = int(t[0])
					t1 = int(t[1])
					t0 = 4 - t0
					t1 = 4 - t1
					s += ("%s %s" % (chr(97+t0), chr(97+t1)))
					s += ' + '
				if len(t) == 1:
					t0 = int(t[0])
					t0 = 4 - t0
					if t0 >= 4:
						s += ("%s + "% (chr(97+t0)) )
					else:
						s += ("%s + "% (chr(97+t0)) )
			s = s[0:-3]
			s += r"\\"
			print(s)

def gen_gf_inv16_abc_big(file_name, out_name, in_name):
	with open(file_name, 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			s=""
			# s = "&%s_%d = " % (out_name, 3-i) # out[3] = 
			if i == 0: s = "&x = "
			if i == 1: s = "&y = "
			if i == 2: s = "&z = "
			if i == 3: s = "&t = "
			for t in terms[0:-1]:
				if len(t) == 3:
					t0 = int(t[0])
					t1 = int(t[1])
					t2 = int(t[2])
					s += ("%s %s %s" % ( chr(96 + t0), chr(96+t1), chr(96+t2)))
					s += ' + '
				if len(t) == 2:
					t0 = int(t[0])
					t1 = int(t[1])
					s += ("%s %s" % (chr(96+t0), chr(96+t1)))
					s += ' + '
				if len(t) == 1:
					t0 = int(t[0])
					if t0 >= 4:
						s += ("%s + "% (chr(96+t0)) )
					else:
						s += ("%s + "% (chr(96+t0)) )
			s = s[0:-3]
			s += r"\\"
			print(s)

def gen_gf_inv16_x_big(out_name, in_name):
	with open('gf_inv16_r.txt', 'r', encoding='utf-8') as f:
		for i, ann in enumerate(f.readlines()):
			line = ann.strip('\n')
			# print(ann)
			terms = line.split(',')
			s = "&%s_%d = " % (out_name, 3-i) # out[3] = 

			for t in terms[0:-1]:
				if len(t) == 3:
					t0 = int(t[0])
					t1 = int(t[1])
					t2 = int(t[2])
					s += ("%s_%d %s_%d %s_%d" % (in_name, t0, in_name, t1, in_name, t2))
					# s += ("%s %s %s" % ( chr(96 + t0), chr(96+t1), chr(96+t2)))
					s += ' + '
				if len(t) == 2:
					t0 = int(t[0])
					t1 = int(t[1])
					s += ("%s_%d %s_%d" % (in_name, t0, in_name, t1))
					# s += ("%s %s" % (chr(96+t0), chr(96+t1)))
					s += ' + '
				if len(t) == 1:
					t0 = int(t[0])
					s += ("%s_%d + "% (in_name, t0) )
			s = s[0:-3]
			s += r"\\"
			print(s)


def main():
	gen_gf_inv16_abc_little("t", "x")
	print()
	gen_gf_inv16_abc_big('gf_inv16.txt', "t", "x")
	print()
	gen_gf_inv16_x_big("t", "x")
	print()
	# generate the equation in re-consolidating fisrt-order masking schemes
	gen_gf_inv16_abc_big('gf_inv16_re-con.txt', "t", "x")

def test():
	gen_matrix("")
	print()
	gen_matrix("i")
	gen_gf_mul16("assign out","in", 0)
	print()
	gen_gf_mul16_latex("t","x", 0)
	print()
	gen_gf_mul16_latex("t","x", 1)
	print()
	gen_gf_mul16_latex("t","x", 2)
	print()
	gen_gf_inv16_latex("t","x")
	print()
	gen_gf_mul16("assign out","in", 1)


if __name__ == '__main__':
	main()
