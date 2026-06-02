def solution(genres, plays):
    # 최종 결과를 저장할 리스트
    answer = []

    # 장르별 총 재생 수와 정보를 딕셔너리 형태로 저장
    genre_total = {}
    genre_songs = {}

    # 모든 노래를 순회하면서 데이터 정리
    for i in range(len(genres)):
        genre = genres[i]  # 현재 노래의 장르
        play = plays[i]    # 현재 노래의 재생 수

        # 처음 등장한 장르라면 초기화
        if genre not in genre_total:
            genre_total[genre] = 0
            genre_songs[genre] = []

        # 장르별 총 재생 수 누적
        genre_total[genre] += play

        # 해당 장르에 (고유번호, 재생수) 저장
        genre_songs[genre].append((i, play))

    # 장르를 총 재생 수 기준으로 내림차순 정렬
    # 재생 수가 많은 장르가 먼저 오도록 정렬
    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda genre: genre_total[genre],
        reverse=True
    )

    # 정렬된 장르를 하나씩 확인
    for genre in sorted_genres:

        # 해당 장르의 노래 목록 가져오기
        songs = genre_songs[genre]

        # 노래 재생 수를 내림차순으로 정렬
        songs.sort(key=lambda x: (-x[1], x[0]))

        # 재생 수 상위 2곡만 선택
        for song in songs[:2]:
            # 고유번호만 결과 리스트에 추가
            answer.append(song[0])
    return answer