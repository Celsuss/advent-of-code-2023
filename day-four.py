
def calculateScore(winners_count: int) -> int:
    if winners_count == 0:
        return 0

    score = 1
    for i in range(winners_count-1):
        score = score * 2
    return score


def partOne(cards: list, winning_numbers: list) -> int:
    score_sum = 0
    for card, winning_nums in zip(cards, winning_numbers):
        winners_count = 0
        for num in card:
            if num in winning_nums:
                winners_count += 1
        score = calculateScore(winners_count)
        score_sum += score

    return score_sum


def getInput(path: str) -> (list, list):
    cards, winning_numbers = [], []
    with open(path) as f:
        for line in f:
            line = line.split('|')
            card = line[0].split(':')[1].strip()
            card = [x for x in card.split(' ') if x != '']
            cards.append(card)
            winning_nums = line[1].strip()
            winning_nums = [x for x in winning_nums.split(' ') if x != '']
            winning_numbers.append(winning_nums)

    return cards, winning_numbers


def main():
    """ Tests """
    cards, winning_numbers = getInput('data/day-four-test.txt')
    res = partOne(cards, winning_numbers)
    assert(res == 13)

    """ Solutions """
    cards, winning_numbers = getInput('data/day-four.txt')
    res = partOne(cards, winning_numbers)
    print(f'Part one answer: {res}')

    return 0


if __name__ == '__main__':
    main()
