def solution(s):
    # 현재 열려있는 괄호의 개수를 저장
    count = 0

    # 문자열을 한 글자씩 확인
    for ch in s:

        # 여는 괄호인 경우
        if ch == '(':
            count += 1

        # 닫는 괄호인 경우
        else:
            count -= 1

        # 닫는 괄호가 더 많아지면
        if count < 0:
            return False

    # 모든 괄호를 확인한 뒤
    # count가 0이면 괄호가 모두 짝지어진 상태
    return count == 0