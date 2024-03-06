nested_dict = {
    'first_level_key1': {
        'second_level_key1': 'value1',
        'second_level_key2': 'value2'
    },
    'first_level_key2': {
        'second_level_keyA': 'valueA',
        'second_level_keyB': 'valueB'
    }
}
print(nested_dict['first_level_key1']['second_level_key2'])
