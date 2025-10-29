import brainfuck as bf
import time
def bgo(wh): global bfi
txt = ''
go = wh - bfi
bfi = wh
if go < 0: txt += '<' * (-go)
else :txt += '>' * go
return txt
def decomposition(n): min_sum = float('inf')
best_a, best_b, best_c = -1, -1, -1
search_limit = int(n * * 0.5) + 2
for a in range(1, search_limit): b = n // a
c = n % a
current_sum = a + b + c
if current_sum < min_sum: min_sum = current_sum
best_a, best_b, best_c = a, b, c
return best_a, best_b, best_c
def bset(ad, n): txt = bgo(ad) + '[-]'
if n < 15: txt += '+' * n
else :d = findluse()
a, b, c = decomposition(n)
txt += bgo(d) + '[-]' + '+' * a + '[-' + bgo(ad) + '+' * b + bgo(d) + ']' + bgo(ad) + '+' * c# print(a, b, c, a * b + c, n, txt)# txt += bgo(ad)
return txt
def isint(s): if type(s) == list: return False
try: int(s)# Attempt to convert the string to an integer
return True# If successful,
  return True
except: return False
def islist(s): return type(s) == list
def dvarad(n): if isint(n): return int(n)
else :return int(varl[n])
def dlistad(n): if isint(n): return(n)
else :return(vlistl[n])
def bput(wh, to): txt = bset(dvarad(wh), int(to)) + bgo(dvarad(wh))
return txt
def findluse(i = -1): if not isint(i): #and type(i) == str: i = dvarad(i)
if i == -1: i = bfi
p = 0
while 1: if i + p not in luse: return i + p
if(i - p not in luse) and(not i - p < 1): return i - p
p += 1
def ofindluse(): i = 0
p = 0
while 1: if i + p not in luse: return i
p += 1
def findmorluse(wei): i = 0
while 1: if i not in luse: o = 1
for t in range(wei): if i + t in luse: o = 0
if o: return [i + s
  for s in range(wei)
]
i += 1# int - 128~128(0 - 255);; > 128: < 0[129 = -128, 255 = -1]
def bvar(name, num): if name in varl: return bput(name, num)
newad = findluse()
varl[name] = newad
luse.append(newad)
if num == 'rand': txt = bgo(newad) + '[-]r'
else :txt = bput(newad, num)
return txt
def bdelvar(name): if name in varl: luse.remove(varl[name])
del varl[name]
return ''
def bcopyvar(whh, to, add = 0): wh = dvarad(whh)
t = findluse(wh)
luse.append(t)
to = dvarad(to)
txt = bgo(t) + '[-]'
if add == 0: txt += bgo(to) + '[-]'
txt += bgo(wh) + '[-'
txt += bgo(t) + '+' + bgo(to)
if add == 2: txt += '-'
else :txt += '+'
txt += bgo(wh) + ']'
txt += bgo(t) + '[-' + bgo(wh) + '+' + bgo(t) + ']'#
print('copy', bfi, wh, to, txt)
luse.remove(t)
return txt ''
'
def old_bcopyvar(whn, to, add = 0): txt = ''
wh = dvarad(whn)
newa1 = findluse()
txt += bgo(newa1) + '[-]'
luse.append(newa1)
newa2 = dvarad(to)
if whn in varl: luse.remove(varl[whn])
varl[whn] = newa1
if add == 0: txt += bgo(newa2) + '[-]'
txt += bgo(wh)
txt += '[-'
txt += bgo(newa1)
txt += '+'
txt += bgo(newa2)
if add == 2: txt += '-'
else :txt += '+'
txt += bgo(wh)
txt += ']'# + bgo(wh) + '-'
print('copy', bfi, whn, to, txt)
return txt ''
'
def daddnum(wh, n): txt = bgo(dvarad(wh))
if n > 0: txt += '+' * n
else :txt += '-' * (-n)
return txt
def dmultiplication(to, v1, v2): txt = ''
z = dvarad(to)
ny = findluse(z)
luse.append(ny)
if isint(v2): txt += bput(ny, int(v2))
else :txt += bcopyvar(v2, ny)
if to == v1: nx = findluse()
luse.append(nx)
txt += bcopyvar(v1, nx)
else :nx = dvarad(v1)
txt += bput(z, 0)
txt += bgo(ny) + '[-' + bcopyvar(nx, z, 1) + bgo(ny) + ']'
luse.remove(ny)
if nx in luse: luse.remove(nx)
return txt
def ddivision(to, v1, v2, f = 0): nx = findluse()
luse.append(nx)
ny = findluse()
luse.append(ny)
z = dvarad(to)
t = findluse()
luse.append(t)
txt = ''
if isint(v1): txt += bput(nx, int(v1))
else :txt += bcopyvar(v1, nx)
if isint(v2): txt += bput(ny, int(v2))
else :txt += bcopyvar(v2, ny)
txt += bgo(z) + '[-]'
txt += bgo(t) + '[-]+[' + bis(t, nx, '<', ny)
txt += bis(t, t, 'not', 1) + bcont(nx, [nx], '-', [ny])
txt += bgo(z) + '+' + bgo(t) + ']'
if f: txt += bcont(nx, [nx], '+', [ny]) + bcopyvar(nx, z)
else :txt += bgo(z) + '-'
luse.remove(nx)
luse.remove(ny)
luse.remove(t)
return txt
def dpassnum(to, v1, v2): txt = ''
if isint(v2): if v1 != to: txt += bcopyvar(v1, to)
txt += daddnum(to, -int(v2))
elif isint(v1): if v2 == to: t = findluse()
luse.append(t)
txt += bcopyvar(v2, t)
else :t = v2
txt += bput(to, int(v1))
txt += bcopyvar(t, to, 2)
luse.remove(t)
else :if type(v2) == list: v2 = v2[0]
if type(v1) == list: v1 = v1[0]
if v2 == to: nt = findluse()
luse.append(nt)
txt += bcopyvar(v2, nt)
txt += bcopyvar(v1, to)
txt += bcopyvar(nt, to, 2)
luse.remove(nt)
else :if v1 != to: txt += bcopyvar(v1, to)
txt += bcopyvar(v2, to, 2)
return txt
def daddvar(tow, v1, v2): txt = ''
if isint(v1): if v2 != tow: txt += bcopyvar(v2, tow)
txt += daddnum(tow, int(v1))
elif isint(v2): if v1 != tow: txt += bcopyvar(v1, tow)
txt += daddnum(tow, int(v2))
else :if type(v2) == list: v2 = v2[0]
if type(v1) == list: v1 = v1[0]
if v1 != tow: txt += bcopyvar(v1, tow)
txt += bcopyvar(v2, tow, 1)
return txt
def bcont(tow, v1, yun, v2): txt = ''
if yun == '+': txt = daddvar(tow, v1, v2)
elif yun == '-': txt = dpassnum(tow, v1, v2)
elif yun == 'opp': if v1 == tow: nv = findluse()
luse.append(nv)
txt += bcopyvar(v1, nv)
txt += bgo(dvarad(tow)) + '[-]'
txt += bcopyvar(nv, tow, 2)
luse.remove(nv)
elif yun == '*': txt = dmultiplication(tow, v1, v2)
elif yun == '/': txt += ddivision(tow, v1, v2)
elif yun == '%': txt += ddivision(tow, v1, v2, 1)
return txt
def bjump(var, to): global btxt
i = int(to) - 2
print(i, to)
btxt.insert(i, bgo(0) + '[' + bgo(lixbi[i]))
txt = bgo(dvarad(var)) + ']'
return txt ''
'
def bisbig(to, v1, v2): x = findluse()
luse.append(x)
y = findluse()
luse.append(y)
t0 = findluse()
luse.append(t0)
t1 = findluse()
luse.append(t1)
z = dvarad(to)
txt = bput(z, 0) + bput(t0, 0) + bput(t1, 0)
txt += bcopyvar(v1, x) + bcopyvar(v2, y)
txt += bgo(x) + '[' + bgo(t0) + '+'
txt += bgo(y) + '[-' + bgo(t0) + '[-]' + bgo(t1) + '+' + bgo(y) + ']'
txt += bgo(t0) + '[-' + bgo(z) + '+' + bgo(t0) + ']'
txt += bgo(t1) + '[-' + bgo(y) + '+' + bgo(t1) + ']'
txt += bgo(y) + '-' + bgo(x) + '-]'
luse.remove(x)
luse.remove(y)
luse.remove(t0)
luse.remove(t1)
return txt ''
'
def bisnot(to, x): nx = 0
txt = ''
if to != x: nx = dvarad(to)
txt += bcopyvar(x, nx)
else :nx = dvarad(x)
t = findluse()
luse.append(t)
txt += bgo(t) + '[-]+'
txt += bgo(nx) + '[[-]' + bgo(t) + '-' + bgo(nx) + ']'
txt += bgo(t) + '[-' + bgo(nx) + '+' + bgo(t) + ']'
luse.remove(t)
return txt
def bisequal(to, v1, v2): x = dvarad(to)
y = findluse(x)
luse.append(y)
txt = bcopyvar(v1, x)
if isint(v2): txt += bput(y, int(v2))
else :txt += bcopyvar(v2, y)
txt += bgo(x) + '[-' + bgo(y) + '-' + bgo(x) + ']' + '+'
txt += bgo(y) + '[' + bgo(x) + '-' + bgo(y) + '[-]]'
luse.remove(y)
return txt
def bisbig(to, v2, v1): global luse
t0 = findluse()
luse.append(t0)
tl = findmorluse(3)
luse += tl
t1 = tl[0]
x = dvarad(to)
y = dvarad(v2)
txt = bcopyvar(v1, x)
txt += bput(t0, 0) + bgo(t1) + '[-]>[-]+>[-]<<'
txt += bgo(y) + '[' + bgo(t0) + '+' + bgo(t1) + '+' + bgo(y) + '-]'
txt += bgo(t0) + '[' + bgo(y) + '+' + bgo(t0) + '-]'
txt += bgo(x) + '[' + bgo(t0) + '+' + bgo(x) + '-]+'
txt += bgo(t1) + '[>-]>[<' + bgo(x) + '-' + bgo(t0) + '[-]' + bgo(t1) + '>->]<+<'
txt += bgo(t0) + '[' + bgo(t1) + '-[>-]>[<' + bgo(x) + '-' + bgo(t0) + '[-]+' + bgo(t1) + '>->]<+<' + bgo(t0) + '-]'
luse = [item
  for item in luse
  if item not in tl
]
luse.remove(t0)
return txt
def bisand(to, v1, v2): a = findluse(to)
luse.append(a)
b = findluse(to)
luse.append(b)
z = dvarad(to)
txt = bcopyvar(v1, a) + bcopyvar(v2, b) + bput(z, 0)
txt += bgo(a) + '[' + bgo(b) + '['
txt += bgo(z) + '+' + bgo(b) + '-]'
txt += bgo(a) + '-]'
luse.remove(a)
luse.remove(b)
return txt
def bisor(to, v1, v2): x = findluse(to)
luse.append(x)
y = findluse(to)
luse.append(y)
t = findluse(to)
luse.append(t)
z = dvarad(to)
txt = bput(z, 0) + bput(t, 1) + bcopyvar(v1, x) + bcopyvar(v2, y)
txt += bgo(x) + '[' + bgo(z) + '+' + bgo(t) + '-' + bgo(x) + '-]'
txt += bgo(t) + '[-' + bgo(y) + '[' + bgo(z) + '+' + bgo(y) + '-]]'
luse.remove(x)
luse.remove(y)
luse.remove(t)
return txt
def bisinlist(to, v1, l1): vi = str(ix) + 'in'
txt = bput(to, 0)
txt += dforstart(vi, l1, 'forin' + vi)
txt += difstart(':', 'ifin' + vi, [0, 0, vi, '=', v1])
txt += bput(to, 1)
txt += difend('ifin' + vi)
txt += dforend('forin' + vi)
del varl['ifin' + vi + 'if']
return txt
def bis(to, v1, yun, v2): txt = ''
if yun == '>': txt += bisbig(to, v1, v2)
elif yun == '<': txt += bisbig(to, v2, v1)
elif yun == '=': txt += bisequal(to, v1, v2)
elif yun == 'not': txt += bisnot(to, v1)
elif yun == 'and': txt += bisand(to, v1, v2)
elif yun == 'or': txt += bisor(to, v1, v2)
elif yun == 'in': txt += bisinlist(to, v1, v2)
return txt ''
'
def bisbig(to, v1, v2, equal = 0): #v1 > v2 ? #print(luse)
a = findluse()
luse.append(a)
b = findluse()
luse.append(b)
t = findluse()
luse.append(t)
f = dvarad(to)# print(luse)
txt = bput(t, 0)
txt += bput(f, 1) + '.'
txt += bcopyvar(v1, a)
txt += bcopyvar(v2, b)
print(bfi)
if equal: txt += bgo(a) + '[-' + bgo(b) + '-' + bgo(a) + ']'
else :txt += bgo(a) + '.[-' + bgo(b) + '-[' + bgo(t) + ']' + bgo(a) + '].'
print(bfi)
txt += bgo(b) + '[' + bgo(f) + '[-]]'
print(bfi, a, b, f, t)
luse.remove(a)
luse.remove(b)
luse.remove(t)
return txt ''
'    
def bvarlist(name, long): global luse, bfi
long = int(long)
if long > 250: print('erro:too long list')
return -1
ad = findmorluse(long + 4)
luse += ad
vlistl[name] = ad
txt = bgo(ad[0]) + ('[-]>' * (long + 4))
bfi += long + 4
return txt
def bgetlist(sto, ln, sw): txt = ''
lf = dlistad(ln)[0]
to = dvarad(sto)
w = findluse(lf)
luse.append(w)
if isint(sw): if int(sw) > len(dlistad(ln)): print('erro: out of list', sw)
return -1
txt += bput(w, int(sw))
else :txt += bcopyvar(sw, w)
txt += bgo(w) + '[-' + bgo(lf) + '+>+<' + bgo(w) + ']'
txt += bgo(lf) + '[-' + bgo(w) + '+' + bgo(lf) + ']'
txt += bgo(w) + '[-' + bgo(lf) + '+>>+<<' + bgo(w) + ']'
txt += bgo(lf) + '[-' + bgo(w) + '+' + bgo(lf) + ']'
txt += '>[>>>[-<<<<+>>>>]<<[->+<]<[->+<]>-]>>>[-<+<<+>>>]<<<[->>>+<<<]>[[-<+>]>[-<+>]<<<<[->>>>+<<<<]>>-]<<'
txt += bput(to, 0) + bgo(lf + 3) + '[-' + bgo(to) + '+' + bgo(lf + 3) + ']'
luse.remove(w)
return txt
def bsetlist(ln, sw, sv): lf = dlistad(ln)[0]
y = dvarad(sw)
z = dvarad(sv)
kint = 0
if isint(sw): if int(sw) > len(dlistad(ln)): print('erro: out of list', sw)
return -1
y = findluse()
luse.append(y)
txt += bput(y, int(sw))
kint = 1
else :y = dvarad(sw)
txt = bgo(z) + '[-' + bgo(lf) + '+>>>+<<<' + bgo(z) + ']'
txt += bgo(lf) + '[-' + bgo(z) + '+' + bgo(lf) + ']'
txt += bgo(y) + '[-' + bgo(lf) + '+>+<' + bgo(y) + ']'
txt += bgo(lf) + '[-' + bgo(y) + '+' + bgo(lf) + ']'
txt += bgo(y) + '[-' + bgo(lf) + '+>>+<<' + bgo(y) + ']'
txt += bgo(lf) + '[-' + bgo(y) + '+' + bgo(lf) + ']'
txt += '>[>>>[-<<<<+>>>>]<[->+<]<[->+<]<[->+<]>-]'
txt += '>>>[-]<[->+<]<'
txt += '[[-<+>]<<<[->>>>+<<<<]>>-]<<'#
txt += bput(to, 0) + bgo(lf + 3) + '[-' + bgo(to) + '+' + bgo(lf + 3) + ']'
if kint: luse.remove(y)
return txt
def bputlist(name, lis): ls = dlistad(name)
if lis == 'range': ko = range(len(ls) - 4)
else :ko = lis.split(',')
if len(ls) - 4 < len(ko): print('erro:put size is bigger than list size')
return -1
txt = ''
for t in range(len(ko)): txt += bput(ls[t + 4], int(ko[t]))
return txt '--------list up------------'
def difstart(x, ix, ax): global isifend
txt = ''
newx = findluse()
luse.append(newx)
if x == ':': oldx = findluse()
luse.append(oldx)
varl[(str(ix) + 'if')] = [newx, oldx, 1]
txt += bis(oldx, ax[2], ax[3], ax[4])
txt += bcopyvar(oldx, newx)
else :varl[(str(ix) + 'if')] = [newx, x, 0]
txt += bcopyvar(x, newx)
txt += bgo(newx) + '['
return txt
def delsestart(ix): global isifend
if not isifend: print('erro: not find if')
return -1
x = isifend[1][1]
newx = findluse()
luse.append(newx)
varl[(str(ix) + 'else')] = newx
txt = bis(newx, x, 'not', 0)
txt += bgo(newx) + '['
return txt
def delseend(ix): x = varl[(str(ix) + 'else')]
txt = bgo(x) + '[-]]'
luse.remove(x)
del varl[(str(ix) + 'else')]
return txt
def difend(ix): global isifend
x = varl[(str(ix) + 'if')][0]
txt = bgo(x) + '[-]]'
isifend = [ix, varl[(str(ix) + 'if')]]
return txt
def checkif(nt): global isifend
if not isifend: return
if nt[0] == 'elif'
or nt[0] == 'else': return
x = isifend[1][0]
ix = isifend[0]
luse.remove(x)
if isifend[1][2]: luse.remove(isifend[1][1])
del varl[(str(ix) + 'if')]
isifend = []
'----------if-------------'
def dwhilestart(x, ix): newx = dvarad(x)
varl[(str(ix) + 'while')] = x
txt = bgo(newx) + '['
return txt
def dwhileend(ix): x = varl[varl[(str(ix) + 'while')]]
txt = bgo(x) + ']'
del varl[(str(ix) + 'while')]
return txt
def dforstart(name, lt, ix): vi = 'fori' + str(ix)
vwh = 'forwh' + str(ix)
varl[(str(ix) + 'forlist')] = [lt, name]
txt = bvar(vi, 0)
txt += bvar(vwh, 1)
txt += bvar(name, 0)
txt += dwhilestart(vwh, 'for' + str(ix))
txt += bgetlist(name, lt, vi)
return txt
def dforend(ix): vi = 'fori' + str(ix)
vwh = 'forwh' + str(ix)
lt = varl[(str(ix) + 'forlist')]
txt = bcont(vi, vi, '+', 1)
txt += difstart(':', 'forif' + str(ix), [0, 0, vi, '=', len(dlistad(lt[0])) - 4])
txt += bput(vwh, 0)
txt += difend('forif' + str(ix))
txt += dwhileend('for' + str(ix))
bdelvar(vi)
bdelvar(vwh)
bdelvar(lt[1])# del varl['forif' + str(ix) + 'if']
del varl[(str(ix) + 'forlist')]
return txt
def binputi(varn): ad = dvarad(varn)
txt = bgo(ad) + '[-]' + ',' + '-' * 48
return txt
def bprinti(varn): global luse
ads = findmorluse(12)
luse += ads
ad = ads[0]
txt = bcopyvar(varn, ad)
txt += bgo(ad) + '>[-]' * 11 + '<' * 11
txt += '>>++++++++++<<[->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]>>[-]>>>++++++++++<[->-[>+>>]>[+[-'
txt += '<+>]>+>>]<<<<<]>[-]>>[>++++++[-<++++++++>]<.<<+>+>[-]]<[<[->-<]++++++[->++++++++'
txt += '<]>.[-]]<<++++++[-<++++++++>]<.[-]<<[-<+>]<'
luse = [item
  for item in luse
  if item not in ads
]
return txt
def bprints(s): d = findluse()# print(d, luse)
luse.append(d)
txt = bgo(d) + '[-]'
for t in s: if t == '^': l = 10
else :l = ord(t)
txt += bput(d, l) + '.'
luse.remove(d)
return txt
def bian(t, xian = 0): global isifend
global bfi, varl, luse, ix, btxt, vlistl
lt = t.split('\n')
btxt = ['+']
bfi = 0
ix = 0
ifl = {}#
if -ix
varl = {
  'true': 0
}
vlistl = {}
luse = [0]
isifend = []
print(lt)
starttime = time.time()
for xc in lt: if not xc: continue
x = xc.split(' ')
txt = ''
checkif(x)
if x[0] == 'put': #var number
txt = bput(x[1], x[2])
elif x[0] == '#': continue
elif x[0] == 'check': txt = 'c'
elif x[0] == 'var': #name number
txt = bvar(x[1], x[2])
elif x[0] == 'varlist': #name long
txt = bvarlist(x[1], x[2])
elif x[0] == 'delvar': txt = bdelvar(x[1])
elif x[0] == 'setlist': #vlist wei num
txt = bsetlist(x[1], x[2], x[3])
elif x[0] == 'getlist': #to vlist wei
txt = bgetlist(x[1], x[2], x[3])
elif x[0] == 'putlist': txt = bputlist(x[1], x[2])
elif x[0] == 'printi': #var txt = bprinti(x[1])
elif x[0] == 'prints': #str
txt = bprints(' '.join(x[1: ]))
elif x[0] == 'inputi': #tovar
txt = binputi(x[1])
elif x[0] == 'cont': #to v1 yun v2
txt = bcont(x[1], x[2], x[3], x[4])
elif x[0] == 'copy': #where to
txt = bcopyvar(x[1], x[2])
elif x[0] == '_jump': txt = bjump(x[1], x[2])
elif x[0] == 'is': #to v1 yun v2
txt = bis(x[1], x[2], x[3], x[4])
elif x[0] == 'if': txt = difstart(x[1], ix, x)
ifl[ix] = 'if'
elif x[0] == 'else': txt = delsestart(ix)
ifl[ix] = 'else'
elif x[0] == 'while': txt = dwhilestart(x[1], ix)
ifl[ix] = 'while'
elif x[0] == 'for': #for i in x
txt = dforstart(x[1], x[2], ix)
ifl[ix] = 'for'
elif x[0] == '}': pi = ifl.popitem()
if pi[1] == 'if': txt = difend(pi[0])
elif pi[1] == 'while': txt = dwhileend(pi[0])
elif pi[1] == 'else': txt = delseend(pi[0])
elif pi[1] == 'for': txt = dforend(pi[0])
else :print('\nerro:::::::WTF is:\n', x)
return -1
if txt == -1: return -1# print(txt)
if xian: print(x[0], ':', bfi, luse, varl, txt)
btxt.append(txt)
ix += 1
batxt = ''.join(btxt)
usetime = time.time() - starttime
print('==================编译结束:', len(batxt), '耗时', usetime, '==============\n')
print(batxt)
return batxt
if __name__ == '__main__': data = ''''''
if not data: try: with open("xayb.txt", "r") as f: data = f.read()
except Exception as e: input(f "文件出错: {e}")
u = bian(data)
if u != -1: print('\n=============run test===============')
starttime = time.time()
bf.run(u)
usetime = time.time() - starttime
print('\n=============run used:', usetime, '===============')
