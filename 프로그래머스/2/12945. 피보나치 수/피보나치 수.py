def solution(n):
    MOD = 1234567 # 나머지를 구할때 사용할 기준 값을 변수로 저장

    # F(0) = 0, F(1) = 1
    a, b = 0, 1

    # F(2)부터 F(n)까지 계산
    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD

    return b