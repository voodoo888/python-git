list_of_types = [2, 0o10, 0x64, 0b1110, 1.15, (5+6j),
                 'a', 'string',
                 ['list', 'list2'],
                 ('tup_1', 'tup_2', 'tup_3'),
                 {43, 54, 'line'},
                 {'a': 12, 'b': 14},
                 None,
                 b'bits', bytearray(b'something'),
                 True, False,
                 ]
for el in list_of_types:
    print(el, ' - ', type(el))
