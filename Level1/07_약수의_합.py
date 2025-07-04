"""
문제명: 07 약수의 합
"""

def solution(n):
    return sum(i for i in range(1, n+1) if n % i == 0)


if __name__ == "__main__":
    print("테스트하세요.")
