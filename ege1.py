# with (open('17.txt')) as f:
#     a=[]
#     raz_max=0
#     for i in f:
#         a.append(int(i))
#     for i in a:
#         for i in a:
            
        
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (not((not((not(w) or z) == y)) or x)):
#                     print(x, y, z, w)
# (not(x) or not(y)) and (not(x == z)) and w


# if ((not(0) or not(1)) and not(0 == 1) and 1):
#     print(1)
# else:
#     print(0)

# a='1234567890'
# print(a[2::])
# for i in range(1000000):
#     s = bin(i)[2::]
#     s += str(s.count('1') % 2)
#     s += str(s.count('1') % 2)
#     if int(s, 2) > 100:
#         print(int(s, 2))
#         break



# for n in range(1,1000):
#     s=bin(n)[2:]
#     s1= s + s[-1]
#     if s.count('1') % 2 == 0:
#         s1+="0"
#     else:
#         s1+="1"
#     if s1.count('1') % 2 == 0:
#         s1+="0"
#     else:
#         s1+="1"
#     if int(s1, 2) > 160:
#         print(n)
#         break

# for n in range(1, 100):
#     s= bin(n)[2:].zfill(8)[:-1]
#     if int(s[::-1], 2) == n:
#         print(n)


# for n in range(1, 256):
#     s= bin(n)[2:].zfill(8)
#     i= s.rindex('1')
#     s1=''
#     for x in range(i):
#         if s[x] == '1' : s1+='0'
#         else: s1+='1'
#     s1+= s[i:]
#     if int(s1, 2) == 178:
#         print(n)


# for n in range(1, 1000):
#     s=bin(n)[2:]
#     s+=s[-1]
#     if s.count('1') % 2 == 0:
#         s += '0'
#     else:
#         s+='1'
#     if int(s, 2) > 105:
#         print(int(s,2))
#         break
    
# a=0
# for i in range(8, -1, -1):
#     for j in range(8, -1, -1):
#         for k in range(8, -1, -1):
#             for l in range(8, -1, -1):
#                 for m in range(8, -1, -1):
#                     if(i!=0 and i>j and j>k and k>l and l>m): a=a+1
    
# print (a)    

# s='0'
# for a in range(1, 100):
#     for b in range(1, )
#     while not '00' in s:
#         s= s.replace('01', '210')
#         s= s.replace('02', '320')
#         s = s.replace('03', '3012')
#         if s.count('1') == 23 and s.count('2') == 48 and s.count('3') == 41:
#             print(a+b+c)

# def prost(a):
#     for d in range(2, a):
#         if a % d == 0:
#             return False
#         else: 
#             return True
















