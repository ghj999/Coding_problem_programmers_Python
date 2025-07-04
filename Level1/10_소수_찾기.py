"""
문제명: 10 소수 찾기
"""

def solution(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return sum(sieve)


if __name__ == "__main__":
    print("테스트하세요.")
