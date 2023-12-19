#!/usr/bin/env python

import sys

def find_pairs(nums, target):
    num_dict = {}
    pairs = []

    for num in nums:
        complement = target - num
        if complement in num_dict:
            pairs.append((num, complement))
        num_dict[num] = True

    return pairs

def main():
    if len(sys.argv) != 3:
        print("Usage: python app.py <comma-separated-integers> <target-integer>")
        sys.exit(1)

    try:
        nums = list(map(int, sys.argv[1].split(',')))
        target = int(sys.argv[2])
    except ValueError:
        print("Invalid input. Please enter a valid comma-separated list of integers and a target integer.")
        sys.exit(1)

    pairs = find_pairs(nums, target)

    if pairs:
        print(f"Pairs that sum to {target}: {pairs}")
    else:
        print("No pairs found.")

if __name__ == "__main__":
    main()
