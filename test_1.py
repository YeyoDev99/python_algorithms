from jovian.pythondsa import evaluate_test_cases

# first test: making binary search from memory

tests = []

test = {
    'input': {
        'cards': [13,11,11,8,8,6,4,2,1],
        'query': 11
    },
    'output': 1
}

tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})


tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})


def evaluate(cards, query, mid):
    if cards[mid] == query:
        # dont' forget that what we need to evaluate is that the left index is at least zero
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    elif cards[mid] > query:
        return 'right'



def binary_search(cards,query):
    high, low = len(cards) -1, 0
    # not forget that we must iterate in the worst case until we've iterated the whole list, so we need to break the cycle until the highest and lowest value coincide
    while low <= high:
        try:
            # not forget that the mid bust be calculated in each iteration 
            mid = (high + low)//2

            result = evaluate(cards,query,mid)
            if result == 'found':
                return mid
            elif result == 'left':
                high = mid - 1
            elif result == 'right':
                low = mid + 1    
        except:
            return -1
    return -1

if __name__ == '__main__':
    evaluate_test_cases(binary_search, tests)
    