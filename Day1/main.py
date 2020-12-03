from rich.traceback import install
from rich import print
install()
# nasty brute force
def go(file):
    nums = [int(i) for i in open(file, "r")]
    found = False
    for idx, num1 in enumerate(nums):
        for num2 in nums:
            for num3 in nums:
                if found:
                    break
                if num1 + num2 + num3 == 2020:
                    print(idx, "pair", num1, num2, num3)
                    print("product", num1 * num2 * num3)
                    found = True

go("Day1/input.txt")

