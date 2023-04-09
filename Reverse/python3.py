def rev_rot(strng, sz):
    list=[]
    endstring=""
    total=0
    if sz<=0:
        return ""
    elif strng=="":
        return ""
    else:
        for x in range (len(strng)//sz):
            list.append(strng[x*sz:(x+1)*sz])
        for x in range (len(list)):
            total=0
            for y in range (len(list[x])):
                total+=int(list[x][y])**3
            if total%2==0:
                endstring+=(list[x])[::-1]
            else:
                endstring+=list[x][1:]+list[x][0]
        return endstring
                
