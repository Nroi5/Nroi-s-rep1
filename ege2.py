# s = '1' + '0' * 75
# while ('10' in s) or ('1' in s):
#     if '10' in s:
#         s= s.replace('10', '001', 1)
#     else:
#         s= s.replace('1', '00', 1)
#     print(s)
# print(s.count('0'))


# s = '1' + '0' * 75
# while ('10' in s) or ('1' in s):
#     if '10' in s:
#         s = s.replace('10', '001', 1)
#     else:
#         s = s.replace('1', '00', 1)
# print(s.count('0'))

# for n in range(4, 50):
#     s='3' + '5' * n
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '3', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s= s.replace('555', '23', 1)
#     if sum([int(i) for i in s]) == 27:
#         print(n)
#         break
# for n in range (1, 50):
#     s='1'*100 + '1' * n
#     while '111' in s:
#         s=s.replace('111', '22', 1)
#         s=s.replace('222', '11', 1)
#     if s.count('1') == 1:
#         print(100+n)
#         break

# s='9' * 65
# while '999' in s or '222' in s:
#     if '222' in s:
#         s = s.replace('222', '9', 1)
#     else:
#         s = s.replace('999', '2', 1)
# print(sum([int(i) for i in s]))

# print(sum([int(i) for i in "2355"]))


# for n in range(4, 50):
#     s= '2' + '5'*n
#     while '25' in s or '35' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '53', 1)
#         if '35' in s:
#             s = s.replace('35', '2', 1)
#         if '555' in s:
#             s = s.replace('555', '23', 1)
#     if sum([int(i) for i in s]) % 7 == 0:
#         print(n)
#         break

# for x in range(1, 1000):
#     f = 27**7 - 3 ** 11 + 36 - x 
#     s=0
#     while f:
#         s+=f%3
#         f //=3
#     if s == 22:
#         print(x)
#         break

# for x in range(1, 1000):
#     f = 5 ** 2026 + 7* 5 ** 1013 + 107 - x 
#     k5, k0 = 0, 0
#     while f:
#         if f % 6 == 5: k5+=1
#         if f%6== 0: k0 +=1
#         f //=6
#         print(f)
#     if k0 + 28 == k5:
#         print(x)
#         break

# for x in range (5, 37):
#     if int('223', x) + 1 == int('101', 8):
#         print(x)

# alph='0123456789abcde'
# for x in alph:
#     f1 = '82' + x + '19'
#     f2 = '6' + x + '073'
#     d= int(f1, 15) - int(f2, 15)
#     if d%11 == 0:
#         print(d // 11)

# for x in range(44):
#     f1= 44 ** 3 + x * 44 ** 2 + 2 * 44 + 3 
#     f2= 3 * 44 ** 3 + 2 * 44 ** 2 + x * 44 + 1
#     if (f1+f2) % 42 == 0:
#         print((f1+f2) // 42)

for p in range(1, 100):
    for x in range(p):
        for y in range(p):
            f1=p ** 3 + x * p ** 2 + 7 * p + 7
            f2= x * p ** 3 + x * p ** 2 + 7 * p + 7
            if f1+f2 == y * p ** 3  + y * p + y:
                print(y* p ** 3 + x * p ** 2 + y * p + x)