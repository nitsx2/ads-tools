

class String:

	def __init__(self, s):
		self.string = s
		self.n = len(s)



	def z_algo(self):
		zarray = [0]*self.n
		zarray[0] = self.n

		L = R = 0

		for i in range(1, self.n):
			if i > R: #outside the box #then expand R and create new box from current position
				L = R = i 

				while R < self.n and self.string[R] == self.string[R-L]:
					R += 1

				zarray[i] = R-L
				R -= 1 #because of while condition, we are one step further

			else:
				relative_element_index = i-L
				
				if zarray[relative_element_index] < R - i + 1:
					zarray[i] = zarray[relative_element_index]

				else:
					L = i

					while R < self.n and self.string[R] == self.string[R-L]:
						R += 1

					zarray[i] = R-L
					R -= 1

		return zarray



st = "xxyzxxyzwxxyzxxyzx"
string = String(st)

zarray = string.z_algo()
print(zarray)





