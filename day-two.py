import math

BLUE = 'blue'
RED = 'red'
GREEN = 'green'

def getProductOfBalls(balls: set()) -> int:
    product = 0
    for color in balls:
        if product == 0:
            product = balls[color]
        else:
            product *= balls[color]
    return product

def partTwo(games: list) -> int:
    products = []
    for game in games:
        minimum_balls = {
            RED: -math.inf,
            GREEN: -math.inf,
            BLUE: -math.inf
        }
        for record in game['records']:
            for color in record:
                if int(record[color]) > minimum_balls[color]:
                    minimum_balls[color] = int(record[color])
                continue
        products.append(getProductOfBalls(minimum_balls))
    
    res = sum(products)
    return sum(products)


def getImpossibleGames(games: list, targets: dict()) -> set():
    impossible_games = set()
    for game in games:
        for record in game['records']:
            for color in record:
                if int(record[color]) > int(targets[color]):
                    impossible_games.add(game['game_id'])
                    break
    return impossible_games


def getSumOfGameIds(games_ids: list) -> int:
    ids_sum = 0
    for game_id in games_ids:
        ids_sum += int(game_id)
    return ids_sum


def partOne(games: list):
    targets = {
        RED: 12,
        GREEN: 13,
        BLUE: 14,
    }

    impossible_games = getImpossibleGames(games, targets)
    all_games = {game['game_id'] for game in games}
    possible_games = all_games - impossible_games
    return getSumOfGameIds(list(possible_games))


def getData(path: str) -> list(set()):
    def getBallsFromLine(line: str) -> {}:
        index = 0
        next_index = 0
        balls = {}
        while next_index >= 0:
            next_index = line.find(',', index)
            count = line[index:line.find(' ', index)]
            color = line[index+2:next_index if
                         next_index != -1 else None].strip()
            index = next_index+2
            balls[color] = count
        return balls

    games = []
    with open(path) as f:
        for line in f:
            index = line.find(':')
            game_id = line[5: index]
            index += 2
            next_index = index
            records = []

            while next_index >= 0:
                next_index = line.find(';', index)
                sub_str = line[index: next_index]
                record = getBallsFromLine(sub_str)
                index = next_index+2
                records.append(record)

            games.append({
                'game_id': game_id,
                'records': records
            })

    return games


def main():
    """ tests """
    data = getData('data/day-two-test.txt')
    res = partOne(data)
    assert(res == 8)
    print(f'Part one test answer: {res}')

    data = getData('data/day-two-test.txt')
    res = partTwo(data)
    assert(res == 2286)
    print(f'Part two test answer: {res}')

    """ solutions """
    data = getData('data/day-two.txt')
    res = partOne(data)
    print(f'Part one answer: {res}')

    data = getData('data/day-two.txt')
    res = partTwo(data)
    print(f'Part two answer: {res}')

    return 0


if __name__ == '__main__':
    main()
