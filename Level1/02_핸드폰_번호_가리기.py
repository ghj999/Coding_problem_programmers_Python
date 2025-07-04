"""
문제명: 02 핸드폰 번호 가리기
"""

def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == "__main__":
    print("테스트하세요.")
