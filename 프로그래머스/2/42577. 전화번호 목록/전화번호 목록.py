# 해당 문제는 sort을 이용하여 풀이를 진행
def solution(phone_book):
    # 전화번호를 문자열 기준으로 정렬
    phone_book.sort()

    # 앞 번호와 뒷 번호를 비교
    for i in range(len(phone_book) - 1):

        # 다음 번호가 현재 번호로 시작하면 접두어 관계
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    # 끝까지 없으면 접두어 없음
    return True