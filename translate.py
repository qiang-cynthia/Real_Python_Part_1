# -*- coding: utf-8 -*-

sentense = str(input('Enter some text: '))
sentense_1 = sentense

# Bulid a replace_dict
replace_dict = {'a':4, 'b':8, 'e':3, 'l':1, 'o':0, 's':5, 't':7}
print(replace_dict)


# Translate sentense by replacing key with value
for key,value in replace_dict.items():
    sentense = sentense.replace(str(key), str(value))

print(sentense)


# Change the replace_dict by converting the keys and values
replace_dict_1 = {}
for key, value in replace_dict.items():
    replace_dict_1[value] = key
print(replace_dict_1)


# Translate sentense_1 by replacing key with value
for key,value in replace_dict.items():
    sentense_1 = sentense_1.replace(str(key), str(value))

print(sentense_1)

# enter 'I like to eat eggs and spam.'
# the result should be 'I 1ik3 70 347 3gg5 4nd 5p4m.'
