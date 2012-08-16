def dec2base62(n):
    
    chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    b = 62
    s = []
    
    while n >= b: 
        s.append(chars[n % b])
        n = n / b
    s.append(chars[n]) 
    
    return ''.join(s)
    
    
def base622dec(s):
    
    chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    b = 62
    sum = 0
    i = 0
    
    for c in s:
        sum += chars.index(c) * b**i
        i += 1
        
    return sum