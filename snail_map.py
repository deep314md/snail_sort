import math

snail_map = [
         [1,2,3,5],
         [4,5,6,7],
         [7,8,9,8],
         [-1,8,2,1]
        ]

def snail(snail_map):
    if snail_map == [[]] : return []
    res = []
    ln = len(snail_map)

    def run(i, j, l, i_step, j_step, arr):
        result = []
        for el in range(l-1):
           result.append(arr[ i + el * i_step ][ j + el * j_step ])
        return result

    for coord in range(0, math.ceil(ln/ 2), 1):
        l = ln-2*coord
        if l != 1 :
            res += run(coord, coord, l, 0, 1, snail_map)
            res += run(coord, coord+l-1, l, 1, 0, snail_map)
            res += run(coord+l-1, coord+l-1, l, 0, -1, snail_map)
            res += run(coord+l-1, coord, l, -1, 0, snail_map)
        else :
            res += [ snail_map[coord][coord] ]
    return res

print(snail(snail_map))