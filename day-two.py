
BLUE = 'blue'
RED = 'red'
GREEN = 'green'

def partTwo():

    return


def partOne(data: []):
    """ """
    targets = {
        RED: 12,
        GREEN: 13,
        BLUE: 14,
    }


    return 0


def getData(path: str) -> [{}]:
    data = []
    with open(path) as f:
        for line in f:
            index = line.find(':')
            game_id = line[5: index]
            index += 2
            records = []

            while index >= 0:
                record = {}
                next_index = line.find(';', index)
                sub_str = line[index: next_index]



                index = next_index
                records.append(record)
                continue
        data.append({
            'game_id': game_id,
            'records': records
        })

    return data


def main():
    """ tests """
    data = getData('data/day-two-test.txt')
    res = partOne(data)
    assert(res == 8)

    """ solutions """

    return 0


if __name__ == '__main__':
    main()
