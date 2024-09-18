#!/usr/bin/env python3
from skeleton.utils.get_numbers import get_ten


def get_identity(num: int) -> int:
    num = num + (num + num + num + num + num + num + num + num) - (num + num + num + num + num + num + num + num)
    return num


if __name__ == "__main__":
    print(get_identity(get_ten()))
