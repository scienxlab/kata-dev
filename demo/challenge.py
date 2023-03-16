from collections import Counter
import numpy as np

# Currently, the following libraries are installed on the server:
#    numpy
#    striplog
#    scipy
#    pandas
#  If you need others, please let me know. 


#====================================
# NOTE
#
# The set-up and questions go in description.md. This file, challenge.py,
# provides the code for three things needed for a challenge:
# 
# (1) generating the data
# (2) answering the questions
# (3) providing the hints


#====================================
# YOUR FUNCTIONS
#
# Any functions you need to build the dataset and check the answers go here.
# You may or may not need to have functions here.

def string_to_array(data: str) -> np.ndarray:
    """
    All our answer functions will need to turn the input data into actual
    numbers, so let's do that here.
    """
    return np.array([int(n) for n in data.split(', ')])


def force_three_modes(arr: np.ndarray) -> np.ndarray:
    """
    Guarantee there are multiple modes, to ensure Question 3 is interesting.

    NB `statistics.mode()` gives the *first* mode. We could try to guarantee
    that this is not the smallest... but this is just a demo, let's not :P

    Returns the input array with three modes (just in case one is the max and
    gets clobbered by the force_only_one_max).
    """
    counter = Counter(arr)
    n_max = max(3, max(counter.values()))  # Make sure n_max is at least 2.
    nums_to_append = []
    sorted_counts = sorted(counter.items(), key=lambda item: item[1])
    for n, c in sorted_counts[-3:]:
        nums_to_append += (n_max - c) * [n]
    return np.append(arr, nums_to_append).astype(int)


def force_one_max(arr: np.ndarray) -> np.ndarray:
    """
    Guarantee there's only one maximum value, to avoid ambiguity in Question 2.

    Returns the input array with only one maximum (the last of the original
    maximums.)
    """
    if len(maxpos := np.argwhere(arr==np.max(arr))) > 1:
        arr[maxpos.flat[-1]] += 1
    return arr


#====================================
# YOU MUST PROVIDE THE `make_data` FUNCTION
#
# This function generates the input data. Make sure it's too much data to
# allow a manual solution, but check that everything runs in a reasonable
# amount of time (ideally less than 200 ms per function).

def make_data(seed: int) -> str:
    """
    This function generates you problem data. It must take a single arg
    called `seed`, which will be an integer.

    This creates your dataset. More entropy is always good. Aim for data
    which provides large ranges of possible answers. E.g. if you ask about
    how many records meet some criterion, the answer should be in the several
    hundreds so that possible answers can have a range of at least 100 or so.
    """
    # Make a random number generator and some random numbers.
    rng = np.random.default_rng(seed)
    size = rng.integers(5000, 6000)  # So users get different lengths...
    min_ = rng.integers(-100, -10)   # And different ranges.
    max_ = rng.integers(1000, 2000)
    ints = rng.integers(min_, max_, size=size)

    # Do any processing or checks. For example, I am going to ask for the
    # position of the max, so I need to check there's only one element with
    # the maximum value. And I'm going to going to ask for the mode, so we'll
    # keep it interesting by ensuring there is more than one mode and I'll
    # ask for the largest of them.
    ints = force_three_modes(ints)
    ints = force_one_max(ints)
    rng.shuffle(ints)

    # You must send back a string. If one of your challenges is about data
    # processing, you might make it tricky to parse to challenge the user.
    # Or you could send JSON, or a CSV. Any text is fine.
    return ', '.join(map(str, ints))


#====================================
# YOU MUST PROVIDE SOLUTION FUNCTIONS
#
# These functions accept the input data (all of it) and return solutions.
# The solutions you send back must compare equal (==) to the correct answer.
# This is why we prefer answers that are integers or strings.

def solve_1(data):
    """
    Returns the solution to question 1.
    Q1 is 'What is the maximum value?'.
    Remember, the data coming in is a string.
    """
    return np.max(string_to_array(data))


def solve_2(data):
    """
    Returns the solution to question 2.
    Q2 is 'What is the index of the max value?'.
    """
    return np.argmax(string_to_array(data))


def solve_3(data):
    """
    Returns the solution to question 3.
    Q3 is 'What is the largest mode of the data?'.
    """
    c = Counter(string_to_array(data))
    return max(k for k, v in c.items() if v==max(c.values()))


#====================================
# YOU MUST PROVIDE A HINT DICTIONARY
#
# Write some short hints. Remember, we only send back plain text.
# This is just a dictionary mapping question number to a string.
hints = {
    1: "There is a `max()` function in Python.",
    2: "The position of the max is called the 'argmax' of the data. NumPy has this function.",
    3: "Find the mode (the most frequent number). If there is more than one mode value, give the highest.",
}
