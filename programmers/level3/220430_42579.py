def solution(genres, plays):
    answer = []
    genres_type = []  # 장르 종류
    d = dict()  # {'장르 종류': [(고유 번호, 재생 횟수)]}

    # dictionary에 장르 별 노래의 (고유 번호, 재생 횟수) 정보 담기
    for i in range(len(genres)):
        if genres[i] not in genres_type:
            genres_type.append(genres[i])
        if genres[i] not in d:
            d[genres[i]] = [(i, plays[i])]
        elif genres[i] in d:
            d[genres[i]].append((i, plays[i]))

    total_plays = [0] * len(genres_type)
    # 각 장르별 재생 횟수 배열에 담기
    for i in range(len(genres)):
        for j in range(len(genres_type)):
            if genres[i] == genres_type[j]:
                total_plays[j] += plays[i]

    genres_sorted = []
    # 장르 종류를 총 재생 횟수 높은 순으로 정렬
    for i in range(len(genres_type)):
        num = max(total_plays)
        idx = total_plays.index(num)
        total_plays[idx] = 0
        genres_sorted.append(genres_type[idx])

    for i in range(len(genres_sorted)):
        d[genres_sorted[i]].sort(key=lambda x: (-x[1], x[0]))  # (고유 번호, 재생 횟수)에서 재생 횟수에 대해 내림차순 정렬, 재생 횟수 같을 경우 고유 번호에 대해 오름차순 정렬
        arr = d[genres_sorted[i]]
        for j in range(len(arr)):  # 가장 많이 재생된 2개 노래 수록하기
            if j < 2:
                answer.append(arr[j][0])

    return answer