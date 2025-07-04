"""
문제명: 06 자릿수 더하기
"""

def solution(n):
    return sum(int(digit) for digit in str(n))


if __name__ == "__main__":
    print("테스트하세요.")
