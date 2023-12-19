
SYMBOLS = '!@#$%^&*()_-+={}[]/%'


def convertStringArrayToIntArray(array: list) -> list:
    return [int(x) for x in array]


def getNumStartAndEndIndex(row: str, index: int) -> (int, int):
    start_index = 0
    end_index = -1
    for i in range(index, -1, -1):
        if row[i].isnumeric() is False:
            start_index = i+1
            break
    for i in range(index, len(row)):
        if row[i].isnumeric() is False:
            end_index = i
            break
    return (start_index, end_index)


def getAdjacantNumsInRow(row: list, index: int) -> list:
    adjacant_nums = []
    start_index = index-1
    end_index = start_index
    i = start_index

    while i <= index+1 and i >= 0:
        if i >= 0 and i <= len(row)-1 and row[i].isnumeric():
            start_index, end_index = getNumStartAndEndIndex(row, i)
            if end_index == -1:
                num = row[start_index:]
                adjacant_nums.append(num)
                break

            num = row[start_index:end_index]
            adjacant_nums.append(num)
            i = end_index+1
        else:
            i = i+1
    return adjacant_nums


def getAdjacantNums(schematics: list, row_i: int, char_i: int,
                    adjacant_nums_count: int = None) -> list:
    adjacant_nums = []
    """ top row"""
    if row_i > 0:
        adjacant_nums.extend(getAdjacantNumsInRow(schematics[row_i-1], char_i))

    """ center row """
    adjacant_nums.extend(getAdjacantNumsInRow(schematics[row_i], char_i))

    """ bottom row """
    if row_i < len(schematics)-1:
        adjacant_nums.extend(getAdjacantNumsInRow(schematics[row_i+1], char_i))

    if (adjacant_nums_count is not None
       and adjacant_nums_count != len(adjacant_nums)):
        return []
    return adjacant_nums


def isSymbol(char) -> bool:
    if char in SYMBOLS:
        return True
    return False


def partTwo(schematics: list) -> int:
    gear_ratios = []
    for row_i in range(len(schematics)):
        row = schematics[row_i]
        for char_i in range(len(row)):
            char = row[char_i]
            if isSymbol(char):
                adjacant_nums = getAdjacantNums(schematics, row_i, char_i, 2)
                if len(adjacant_nums) == 0:
                    continue
                gear_ratio = int(adjacant_nums[0]) * int(adjacant_nums[1])
                gear_ratios.append(gear_ratio)
    engine_parts = convertStringArrayToIntArray(gear_ratios)
    return sum(engine_parts)


def partOne(schematics: list) -> int:
    engine_parts = []
    for row_i in range(len(schematics)):
        row = schematics[row_i]
        for char_i in range(len(row)):
            char = row[char_i]
            if isSymbol(char):
                adjacant_nums = getAdjacantNums(schematics, row_i, char_i)
                engine_parts.extend(adjacant_nums)
    engine_parts = convertStringArrayToIntArray(engine_parts)
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

    data = getData('data/day-three-test.txt')
    res = partTwo(data)
    assert(res == 467835)

    """ Solutions """
    data = getData('data/day-three.txt')
    res = partOne(data)
    print(f'Part one solution: {res}')
    assert(res == 537832)

    data = getData('data/day-three.txt')
    res = partTwo(data)
    print(f'Part two solution: {res}')

    return 0


if __name__ == '__main__':
    main()
