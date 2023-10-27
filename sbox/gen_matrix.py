
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

def main():
	gen_matrix("")
	print()
	gen_matrix("i")


if __name__ == '__main__':
	main()
