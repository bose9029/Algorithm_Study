def solution(brown, yellow):
    total = brown + yellow

    # 세로 길이부터 확인
    for height in range(3, total + 1):

        # 전체 칸 수가 나누어떨어져야 가로 * 세로가 가능
        if total % height == 0:
            width = total // height

            # 가로는 세로보다 크거나 같아야 함
            if width < height:
                continue

            # 테두리 1줄을 제외한 내부 영역이 yellow와 같은지 확인
            if (width - 2) * (height - 2) == yellow:
                return [width, height]