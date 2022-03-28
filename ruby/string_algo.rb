
class StringAlgo
#find z index for each index in string.
#z[i]=> largest common prefix size of string[i..(n-1)] and string[0..n-1]

#if i is out of the box then create a box of equal size from starting box.
#else calculate z index for values which are inside the box.
#z[corresponding-b1] < r-i+1 then z[i] = z[corresponding-b1] #value is smaller than boundry
#value is larger than boundry -> start the new box from here. and do bruteforce for it.

	def z_algo(s)#return z-index
		l = 0
		r = 0
		n = s.size
		z = Array.new(n)
		z[0] = n
		i = 1
		
		while i < s.size
			if i > r
				l = i
				r = i
				while (r < n && s[r] == s[r-l])
					r += 1
				end
				z[i] = r-l
				r -= 1
			else
				j = i - l
				if z[j] < (r-i + 1)#inside boundry
					z[i] = z[j]
				else#on boundry
					l = i # if we do r = i here also then we revert the alrady calculated Rs which are further.
					while r < n && s[r] == s[r-l]
						r += 1 
					end
					z[i] = r-l
					r-= 1
				end
			end
			i += 1
		end
		return z
	end


end

string = "xxyzxxyzwxxyzxxyzx"
StringAlgo.new.z_algo(string)

#TODO- KMP, RabinKarp