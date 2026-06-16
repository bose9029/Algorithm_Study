def solution(sizes):
    max_width = 0
    max_height = 0

    for w, h in sizes:
        # 긴 쪽을 가로, 짧은 쪽을 세로로 통일
        width = max(w, h)
        height = min(w, h)

        # 최대 가로 길이
        max_width = max(max_width, width)

        #  세로 길이
        max_height = max(max_height, height)

    # 필요한 지갑의 최소 크기
    return max_width * max_height