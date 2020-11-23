# pyhton3

import sys
from bst import BST


def find_second_smallest(bst):
    string_nums = str(bst)
    char_nums = string_nums.split()
    nums = list(map(int, char_nums))
    if len(nums) < 2:
        return None

    return nums[1]


def main():
    data = sys.stdin.readline()
    nums = list(map(int, data.split()))
    bst = BST()
    for num in nums:
        bst.insert(num)
    
    print(find_second_smallest(bst))


if __name__ == '__main__':
    main()