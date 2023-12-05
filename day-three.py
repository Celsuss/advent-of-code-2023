
SYMBOLS = '!@#$%^&*()_-+={}[]'


def getNumFromIndex(string: str, index: int) -> int:

    return 0


def getAdjacantNums(schematics: list, row_i: int, char_i: int) -> list:
    """ top row"""
    if row_i > 0:
        top =  schematics[row_i-1][char_i]
        if char_i > 0:
            top_left = schematics[row_i-1][char_i-1]
        if char_i <= len(schematics[row_i])-1:
            top_right = schematics[row_i-1][char_i+1]

    """ center row """

    """ bottom row """

    return []


def isSymbol(char) -> bool:
    if char in SYMBOLS:
        return True
    return False


def partOne(schematics: list) -> int:
    engine_parts = []
    for row_i in range(len(schematics)):
        row = schematics[row_i]
        for char_i in range(len(row)):
            char = row[char_i]
            if isSymbol(char):
                adjacant_nums = getAdjacantNums(schematics, row_i, char_i)
                engine_parts.extend(adjacant_nums)
    return sum(engine_parts)


def getData(path: str) -> list:
    with open(path) as f:
        schematics = []
        for row in f:
            schematics.append(row.strip())
    return schematics


def main():
    """ Tests """
    data = getData('data/day-three-test.txt')
    res = partOne(data)
    assert(res == 4361)

    """ Solutions """
    data = getData('data/day-three.txt')
    res = partOne(data)
    print(f'Part one solution: {res}')

    return 0


if __name__ == '__main__':
    main()
