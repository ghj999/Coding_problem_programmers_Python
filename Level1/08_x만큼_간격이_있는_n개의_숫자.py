"""
문제명: 08 x만큼 간격이 있는 n개의 숫자
"""

def solution(x, n):
    return [x * i for i in range(1, n+1)]


if __name__ == "__main__":
    print("테스트하세요.")
