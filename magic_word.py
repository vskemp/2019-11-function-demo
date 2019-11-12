#TYPED IN BASH PYTHON3

magic_word = "abracadabra"
magic_word[0]
'a'
magic_word[0:4]
'abra'
magic_word[0]
'a'
magic_word[0] = "z"

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment

list(magic_word)
['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
magic_list = list(magic_word)
magic_word
'abracadabra'
>>> magic_list
['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
magic_list[0] = "z"
magic_list
['z', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
str(magic_list)
"['z', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']"
''.join(magic_list)
'zbracadabra'
