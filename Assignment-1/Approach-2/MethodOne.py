import math

pi = 1
n = int(input("Enter the number of iterations: "))
for i in range(n , 0, -1):
	if i > 1:
		f = 2
		for j in range(1,i):
			if j < i:
				f = 2 + math.sqrt(f)

		f = math.sqrt(f)
		pi = pi * f / 2

pi *= math.sqrt(2) / 2
pi = 2 / pi

print("Approximated value of Pi= "+str(pi))
