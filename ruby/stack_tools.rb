class StackTools
	def nge_left(a)
	i = a.size-1
	stack = []
	ans = Array.new(a.size, -1)
	
	while  i >= 0
		chr = a[i]
		if stack.empty? || chr <= a[top(stack)]
			stack << i
		else
			while !stack.empty? && chr > a[top(stack)]
				index = stack.pop
				ans[index] = chr
			end
			stack << i
		end
		i -= 1
	end

	while !stack.empty?
		index = stack.pop
		ans[index] = -1
	end
	
	return ans

end

def nge_right(a)
	i = 0
	stack = []
	ans = Array.new(a.size, -1)
	
	while i < a.size
		if stack.empty? || a[i] < a[top(stack)]
			stack << i
		else
			while !stack.empty? &&  a[i]  >  a[top(stack)]
				index = stack.pop
				ans[index] = a[i]	
			end
			stack << i
		end
		i += 1
	end

	while !stack.empty?
		index = stack.pop
		ans[index] = -1
	end
	
	return ans

end


def nse_left(a)
	i = a.size-1
	stack = []
	ans = Array.new(a.size, -1)
	
	while  i >= 0
		chr = a[i]
		if stack.empty? || chr >= a[top(stack)]
			stack << i
		else
			while !stack.empty? && chr < a[top(stack)]
				index = stack.pop
				ans[index] = chr
			end
			stack << i
		end
		i -= 1
	end

	while !stack.empty?
		index = stack.pop
		ans[index] = -1
	end
	
	return ans

end

def nse_right(a)
	i = 0
	stack = []
	ans = Array.new(a.size, -1)
	
	while i < a.size
		if stack.empty? || a[i] >= a[top(stack)]
			stack << i
		else
			while !stack.empty? &&  a[i]  < a[top(stack)]
				index = stack.pop
				ans[index] = a[i]	
			end
			stack << i
		end
		i += 1
	end

	while !stack.empty?
		index = stack.pop
		ans[index] = -1
	end
	
	return ans

end

def top(stack)
	return -1 if stack.empty?
	stack[stack.size-1]
end

end