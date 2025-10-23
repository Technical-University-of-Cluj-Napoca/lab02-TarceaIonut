def group_anagrams(strs: list[str]) -> list[list[str]]:
    map_cod_list = dict()
    for string in strs:
        code:int = 0
        for c in string:
            code |= 1 << (ord(c) - ord('a'))
        if map_cod_list.get(code) is None:
            map_cod_list[code] = []
        map_cod_list[code].append(string)
    result = []
    for code in map_cod_list:
        result.append(map_cod_list[code])

    return result


#print(group_anagrams(['ab','ba','c', 'c']))