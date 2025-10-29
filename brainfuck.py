import random as rn
def dlist(i,l):
    if i+1>len(l):
        l+=[0]*(i-len(l)+1)

    
def run(t,zpo=0):
    
    i=0
    zl=[]
    ix=0
    bushu=0
    try:
        t[ix]
        while ix<len(t):
            x=t[ix]
            if x=='>':
                i+=1
            elif x=='<':
                i-=1
                if i<0:
                    print('erro: i<0')
                    return -1
            elif x=='+':
                dlist(i,zl)
                zl[i]+=1
                if zl[i]>255:zl[i]=0
            elif x=='-':
                dlist(i,zl)
                zl[i]-=1
                if zl[i]<0:zl[i]=255
            elif x==',':
                dlist(i,zl)
                gt=input('~')
                if gt:
                    zl[i]=ord(gt[0])
                else:zl[i]=0
            elif x=='.':
                dlist(i,zl)
                print(chr(zl[i]),end='')
            elif x=='[':
                dlist(i,zl)
                if zl[i]==0:
                    lp=0
                    co=0
                    for nx in t[ix+1:]:
                        co+=1
                        if nx=='[':
                            lp+=1
                        elif nx==']':
                            if lp==0:
                                break
                            else:
                                lp-=1
                    ix+=co
            elif x==']':
                dlist(i,zl)
                if zl[i]!=0:
                    lp=0
                    co=0
                    for nx in t[:ix][::-1]:
                        co+=1
                        if nx==']':
                            lp+=1
                        elif nx=='[':
                            if lp==0:
                                break
                            else:
                                lp-=1
                    ix-=co
            elif x=='r':
                dlist(i,zl)
                zl[i]=rn.randint(0,99)
            elif x=='c':
                print(bushu,zl,i,ix)

            ix+=1
            bushu+=1
            if zpo:print(ix,zl,i,x)
    except Exception as e:
            print('erro:',zl,i,ix,t[ix],e)


if __name__ == '__main__' :
    run('''
,>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-
<+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++
<]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<
''')
