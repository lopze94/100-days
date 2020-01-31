# An array A[1....n] is said to have a majority element if more than half of its
# entries are the same. Given an array, the task is to design an efficient algorithm
# to tell whether the array has a majority element, and, if so, to find that element.
# The elements of the array are not necessarily from some ordered domain like the
# integers, and so there can be no comparisons.

def select_candidate(elements, tiebreaker=None):
    if(len(elements) % 2 == 1):
        tiebreaker = elements[-1]

    if(len(elements) == 0):
        return tiebreaker

    candidates = []
    for i in range(0, len(elements) - 1, 2):
        if(elements[i] == elements[i+1]):
            candidates.append(elements[i])

    return select_candidate(candidates, tiebreaker)


def check_frequency(candidate, elements):
    count = 0
    for i in range(0, len(elements)):
        if(elements[i] == candidate):
            count += 1

    if (count/len(elements) > (1 / 2)):
        return str(candidate) + ' is a majority element'
    else:
        return 'Not a majority element'


def majority_element(elements):
    candidate = select_candidate(elements)
    return check_frequency(candidate, elements)


e1 = [1, 1, 2, 2, 2, 'a', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c', 'c']
e2 = [1, 1, 2, 2]
e3 = [1, 1, 2, 2, 2]

print(majority_element(e1))
print(majority_element(e2))
print(majority_element(e3))

# Result: c is a majority element
# Result: Not a majority element
# Result: 2 is a majority element
