
import math

def karatsuba(x,y):

    if x < 10 or y < 10:
        return x*y
    else:
        m = min(len(str(x)),len(str(y)))
        l = math.floor(m/2)
        
        high1 = int(x / 10**(l))
        low1 = x % 10**(l)
        high2 = int(y / 10**(l))
        low2 = y % 10**(l)
        
        z0 = karatsuba(low1,low2)
        z1 = karatsuba((low1 + high1),(low2 + high2))
        z2 = karatsuba(high1,high2)
        
        return (z2*10**(l*2)) + ((z1 - z2 - z0)*10**(l)) + z0
            
k = karatsuba(4872139874092183,5977098709879)
print(k)
