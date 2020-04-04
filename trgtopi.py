#author:lanxiaoning
##testing probability=(pi-2)/4

import math
import random
limits=10000
def main(testnum,samplenum):
    for i in range(testnum):
        matchcount=0
        for j in range(samplenum):
            a=random.randint(1,limits)
            b=random.randint(1,limits)
            c=random.randint(1,limits)
            if(a>b):
                a,b=b,a
            if(b>c):
                b,c=c,b
            cos=float((a**2+b**2-c**2)/(2*a*b))
            if(-1<cos<0):
                matchcount=matchcount+1
        print(str(float(matchcount/samplenum)*4+2))


if(__name__=='__main__'):
    main(20,500)
