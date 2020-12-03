import re
from rich.traceback import install
from rich import print
install()


def go(file):
    nums = open(file, "r")
    valid_pws = 0
    for idx, row in enumerate(nums):
        s = re.split('\s', row)
        # print(idx, s)
        freq = get_range(s[0])
        letter = get_letter(s[1])
        password = s[2]
        valid_pws += validate_password(freq, letter, password)
    print(valid_pws)

# get the range from the protocol
def get_range(r):
    # split two groups of digits, dump the hyphen
    ranges = re.match(r'([0-9]+)-([0-9]+)', r)
    if ranges:
        start = int(ranges.group(1))
        end = int(ranges.group(2))
    return start, end

# get the key letter
def get_letter(c):
    return c[0]

# check the frequency of the key letter in the pw (part 1)
# check the key letter is in the right location (part 2)
def validate_password(freq, letter, password):
    count = 0

    # # Part 1
    # for c in password:
    #     if letter == c:
    #         count += 1
    # return 1 if count in range(freq[0], freq[1] + 1) else 0

    # Pert 2
    if password[freq[0]-1] == letter or password[freq[1]-1] == letter:
        count = 1
    if password[freq[0] - 1] == letter and password[freq[1] - 1] == letter:
        count = 0

    return count

go("Day2/input.txt")