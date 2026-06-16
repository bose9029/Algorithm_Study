def solution(answers):
    # 각 수포자의 반복되는 찍기 패턴
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    # 각 수포자의 점수
    scores = [0, 0, 0]

    # 정답 배열을 순회하면서 채점
    for i in range(len(answers)):
        # i % 패턴길이 를 사용해 반복 패턴 비교
        if answers[i] == pattern1[i % len(pattern1)]:
            scores[0] += 1

        if answers[i] == pattern2[i % len(pattern2)]:
            scores[1] += 1

        if answers[i] == pattern3[i % len(pattern3)]:
            scores[2] += 1

    # 가장 높은 점수
    max_score = max(scores)

    # 가장 높은 점수를 받은 사람 번호 저장
    result = []

    for i in range(3):
        if scores[i] == max_score:
            result.append(i + 1)

    return result