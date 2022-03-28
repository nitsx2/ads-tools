# power
# sqrt
# is_prime
# gcd
# lcm
import math
class Math:
	#abs(a)
	#math.sqrt(num)
	#math.floor(num)
	#math.ceil(num)
	def sqrt(num):
		if num == 0 or num == 1: return 1
		if num < 0: return None
		start_val = 0
		end_val = num/2
		while start_val <= end_val:
		
			mid = (start_val+end_val)/2
		
			if (mid*mid) == num:
				return mid
			elif mid*mid > num:
				end_val = mid - 1
			else:
				start_val = mid + 1
		
		return math.floor(start_val)

	#math.gcd(a,b)
	def gcd(x,y):
		while y:
			x,y = y, x%y
		return x

	# def gcd(a, b):
	# 	if b > a: return Math.gcd(b,a)
	# 	if b == 0: return a
	# 	return Math.gcd(b ,a%b)


	def lcm(x,y):
		lcm = (x*y) // Math.gcd(x,y)
		return lcm


	def is_prime(num):
		if num < 2: return False
		if num == 2: return True
		i = 2
		while i <= int(math.sqrt(num)):
			if num % i == 0: return False
			if num % (num//i) == 0: return False
			i += 1
		return True

	#math.pow(2,3)
	def power(num, pow):
		if num == 1: return 1

		res = 1
		while pow > 0:
			if pow % 2 == 0:
				num *= num
				pow //= 2
			else:
				res *= num
				pow -= 1
		return res





