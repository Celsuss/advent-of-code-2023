import re


def get_data(path: str) -> [str]:
    data = []
    with open(path) as f:
        for x in f:
            data.append(x.strip())
    return data


def containLetterOrInt(row: str, letters: [str], order: int = 1) -> str:
    if row[0].isnumeric():
        return row[0]

    for letter in letters:
        row_trimmed = row[:len(letter)][::order]
        if letter == row_trimmed:
            return row_trimmed

    return None


def convert_to_int(number: str) -> int:
    if number.isnumeric():
        return int(number)

    letters_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
                   'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                   'nine': 9}
    return letters_dict[number]


def part_two(data) -> int:
    digit_sum = 0
    letters = ['one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine']

    for row in data:
        first = None
        for i in range(len(row)):
            first = containLetterOrInt(row[i:], letters)
            if first is not None:
                break

        second = None
        for i in range(len(row), -1, -1):
            second = containLetterOrInt(row[i::-1], letters, -1)
            if second is not None:
                break

        first = convert_to_int(first)
        second = convert_to_int(second)
        digit = int(str(first) + str(second))
        digit_sum += digit
    return digit_sum


def part_one(data) -> int:
    digit_sum = 0
    for row in data:
        # row = row.strip("[A-Za-z]")
        row = re.sub("[^0-9]", "", row)
        digit = int(row[0] + row[-1])
        digit_sum += digit
    return digit_sum


def main():
    """ Tests """
    data = get_data('data/day-one-part-one-test.txt')
    res = part_one(data)
    assert(res == 142)
    print(f'part one test result {res}')

    data = get_data('data/day-one-part-two-test.txt')
    res = part_two(data)
    assert(res == 281)
    print(f'part two test result {res}')

    """ Solutions """
    data = get_data('data/day-one-part-one.txt')
    res = part_one(data)
    print(f'part one result {res}')

    data = get_data('data/day-one-part-two.txt')
    res = part_two(data)
    print(f'part two result {res}')

    return


if __name__ == '__main__':
    main()
