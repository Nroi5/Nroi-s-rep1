# def str_count(data):
#     for sym in data:
#         count = 0
#         for sym_2 in data:
#             if sym == sym_2:
#                 count +=1
#         print(sym, count)

# str_count('abccdda')

# set - множество, неупорядоченный тип данных, который содержит только уникальные значения

x={1,1,2,3}




# y= set()

def str_count(data):
    str_count = {}
    for sym in data:
        str_count[sym] = str_count.get(sym,0) + 1
    print(str_count)
str_count("naabcd")

# family ={}
# family["dad"] = 1
# family["mam"] = 1 
# print(family)
# family["child"] = 1
# print(family)
# family["child"] = family.get("child",0) + 1
# print(family)


