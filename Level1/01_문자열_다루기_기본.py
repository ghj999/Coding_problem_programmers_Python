"""
문제명: 01 문자열 다루기 기본
"""

def solution(s):
    return s.isdigit() and len(s) in (4, 6)


if __name__ == "__main__":
    print("테스트하세요.")
