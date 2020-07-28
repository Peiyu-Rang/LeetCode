def findMedianSortedArrays(nums1, nums2) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        isEven = (n1+n2)%2 == 0

        
        if isEven:
            kMinus1 = int((n1+n2)/2 - 1)
        else:
            kMinus1 = int((n1+n2 - 1)/2)
            
        k = kMinus1 + 1
        
        if n1 == 0:
            if isEven:
                return ((nums2[kMinus1] + nums2[k])/2)
            else:
                return (nums2[kMinus1])
        if n2 == 0:
            if isEven:
                return ((nums1[kMinus1] + nums1[k])/2)
            else:
                return (nums1[kMinus1])
        
        def helper(m1, k):
            m1 = int(m1)
            k = int(k)
            if isEven: #even
                # center index
                m2 = k-m1
                print('m2 is ' + str(m2))
                if m1 == 0:
                    cLeft1 = -float('Inf')
                else:
                    cLeft1 = nums1[m1-1]
                if m2 == 0:
                    cLeft2 = -float('Inf')
                else:
                    cLeft2 = nums2[m2-1]
                if m1 >= len(nums1):
                    cRight1 = float('Inf')
                else:
                    cRight1= nums1[m1]
                
                if m2 >= len(nums2):
                    cRight2 = float('Inf')
                else:
                    cRight2= nums2[m2]
                
                if cLeft1 <= cRight2 and cLeft2 <= cRight1:
                    cl = max(cLeft1, cLeft2)
                    cr = min(cRight1, cRight2)
                    return ('Found!', (cl+cr)/2)
                elif cLeft1 > cRight2:
                    return ('m1 should be smaller',None) 
                elif cLeft2 > cRight1:
                    return ('m1 should be larger', None)

            else:
                m2 = k - m1
                cLeft1 = nums1[m1-1]
                cLeft2 = nums2[m2-1]
                if m1 >= len(nums1):
                    cRight1 = float('Inf')
                else:
                    cRight1= nums1[m1]
                
                if m2 >= len(nums2):
                    cRight2 = float('Inf')
                else:
                    cRight2= nums2[m2]

                if m1 * m2 != 0:
                    if cLeft1 <= cRight2 and cLeft2 <= cRight1:
                        cl = max(cLeft1, cLeft2)
                        return ('Found!', cl)
                    elif cLeft1 > cRight2:
                        return ('m1 should be smaller',None) 
                    elif cLeft2 > cRight1:
                        return ('m1 should be larger', None)
                elif m1 ==0:
                    return ('Found!', nums2[kMinus1])
                else:
                    return ('Found!', nums1[kMinus1])
                
        
        m1 = int(k//2)
        if m1 > n1:
            m1 = n1
        if k-m1 > n2:
            m1 = k-n2
        ans = helper(m1,k)
        
        upper = min(n1,k)
        lower = 0
        
        while ans[0] != 'Found!':
            print(m1)
            print(ans)
            if ans[0] == 'm1 should be smaller':
                upper = m1
                m1 = (m1+lower)//2
            else:
                lower = m1
                
                if upper-m1 == 1:
                    m1 = upper
                else:
                    m1 = (m1 + upper)//2
                
            if m1 > n1:
                m1 = n1
            if k-m1 > n2:
                m1 = k-n2
            
            ans = helper(m1,k)
        
        return ans[1]
            


A = [1,2,3,4,6,7,8]
B = [5]
findMedianSortedArrays(A,B)