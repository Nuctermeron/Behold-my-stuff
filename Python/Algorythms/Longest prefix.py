def longestCommonPrefix(strs):
    if len(strs) == 0:
        return '' 
    ret_string = ''
    strs = sorted(strs)
    for i in strs[0]:
        if strs[-1].startswith(ret_string+i):
            ret_string += i
        else:
            break
    return ret_string

st_list =["flower","flow","flight"] 
print(longestCommonPrefix(st_list))
