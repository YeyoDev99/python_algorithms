from jovian.pythondsa import evaluate_test_case


# step 1: stating the problem clearly:
def locate_card(cards, query):
    pass
# step 2: identify inputs and outputs:
test = {
    'input': {
        'cards': [13,11,12,7,4,3,1,0],
        'query': 7
    },
    'output': 3
}
# step 3: turn up each card one by one anf if the card numbers coincides with the query we return it's position
# if not we continue until we reach the end of the list and if we didn't find the card then we return -1 

# step 4: then we can translate this into code

def locate_card(cards,query):
    position = 0
    while True:
        try:
            if cards[position] == query:
                break
            else:
                position += 1
                if position == len(cards):
                    position = -1
                    break
        except:
            position = -1
            break        
    return position 

# result = test['output'] == locate_card(test['input']['cards'], test['input']['query'])
# result = test['output'] == locate_card(**test['input'])
# print(result)         
evaluate_test_case(locate_card, test)

# the optimal way to apply this rough solution is:
# also the return statement breaks the function by itself
def locate_card(cards, query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1
evaluate_test_case(locate_card, test)


# step 5: using binary technique to optimize the code  
def locate_card(cards, query):
    highest = len(cards) - 1
    lowest = 0
    while lowest <= highest:
        mid_position = (highest + lowest) // 2
        middle_number = cards[mid_position]
        
        print(f'high:{highest}, low:{lowest}, mid:{mid_position}, middle_number:{middle_number}')

        if middle_number == query:
            return mid_position
        elif middle_number < query:
            highest = mid_position - 1     
        elif middle_number > query:
            lowest = mid_position + 1  
    return -1

evaluate_test_case(locate_card, test)

# the refined binary search code look like this:

test = {
    'input': {
        'cards': [13,12,12,12,11,11,7,4,3,1,0],
        'query': 12
    },
    'output': 1
}


def test_location(cards, query, mid):
    mid_number = cards[mid]
    print("mid:", mid, ", mid_number:", mid_number)
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    lo, hi = 0, len(cards) - 1
    
    while lo <= hi:
        print("lo:", lo, ", hi:", hi)
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1

evaluate_test_case(locate_card, test)
