"""
문제명: 09 나머지가 1이 되는 수 찾기
"""

def solution(n):
    for x in range(1, n):
        if n % x == 1:
            return x


if __name__ == "__main__":
    print("테스트하세요.")
