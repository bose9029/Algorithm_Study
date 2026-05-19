# 에라토스테네스의 체 알고리즘으로 코드를 구현
def solution(n):
    num=set(range(2,n+1))#num 변수 범위를 2부터 n까지 지정 

    for i in range(2,n+1):# 2부터 n까지 차례대로 확인
        if i in num: # i가 아직 num 안에 있다면,
            num-=set(range(2*i,n+1,i))#생성된 배수들을 num에서 모두 제거
    return len(num)