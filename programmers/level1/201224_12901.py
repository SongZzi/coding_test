def solution(a, b):
    answer = 0
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0

    if a < 2:
        answer = days[b % 7]
    else:
        for i in range(0, a - 1):
            day = day + month[i]
        day = day + b
        answer = days[day % 7]

    return answer