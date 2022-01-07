string1 = 'mkds'
string2 = 'kmds'
string3 = 'mmkkdd'

def countLetters(strings):
    dict = {}
    for i in strings:
        count = dict.get(i,0)
        count += 1
        dict[i] = count
    return dict

dict1 = countLetters(string1)
dict2 = countLetters(string2)
dict3 = countLetters(string3)

#list = [dict1, dict2, dict3]
#print(list)

sum_dict = {}
for i in dict3.keys():
    sum_dict[i] = dict1.get(i,0) + dict2.get(i,0)
print(sum_dict)

def checkcond1(dict3,sum_dict):
    for i in dict3.keys():
        if (dict3.get(i) > sum_dict.get(i)):
            return 0
    return 1

def checkPos(string3,string):


pos_dict ={}
for i in dict3.keys():
    pos_dict[i] = 0

answer = checkcond1(dict3,sum_dict)
print(answer)