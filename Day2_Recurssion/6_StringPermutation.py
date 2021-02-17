def StringPermutaion(str,l,r):
    if l==r-1:
        print("".join(str))
    else:
        for i in range(l,r):
            str[l],str[i]=str[i],str[l]
            StringPermutaion(str,l+1,r)
            str[l],str[i]=str[i],str[l]

str="ABC"
str=list(str)
l=0
r=len(str)
StringPermutaion(str,l,r)