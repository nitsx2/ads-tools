def bs(self, a, t): #lowerbound

        s = 0
        e = len(a)-1
        while s < e:
            mid = s + (e-s) // 2 
            if t > a[mid]:
                s = mid+1
            else:
                e = mid
        
        return a[s]
