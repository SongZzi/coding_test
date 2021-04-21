def solution(new_id):
    answer = new_id

    # step1
    answer = answer.lower()
    # step2
    answer = list(answer)
    while '~' in answer:
        answer.remove('~')
    while '!' in answer:
        answer.remove('!')
    while '@' in answer:
        answer.remove('@')
    while '#' in answer:
        answer.remove('#')
    while '$' in answer:
        answer.remove('$')
    while '%' in answer:
        answer.remove('%')
    while '^' in answer:
        answer.remove('^')
    while '&' in answer:
        answer.remove('&')
    while '*' in answer:
        answer.remove('*')
    while '(' in answer:
        answer.remove('(')
    while ')' in answer:
        answer.remove(')')
    while '=' in answer:
        answer.remove('=')
    while '+' in answer:
        answer.remove('+')
    while '[' in answer:
        answer.remove('[')
    while '{' in answer:
        answer.remove('{')
    while ']' in answer:
        answer.remove(']')
    while '}' in answer:
        answer.remove('}')
    while ':' in answer:
        answer.remove(':')
    while '?' in answer:
        answer.remove('?')
    while ',' in answer:
        answer.remove(',')
    while '<' in answer:
        answer.remove('<')
    while '>' in answer:
        answer.remove('>')
    while '/' in answer:
        answer.remove('/')
    # step3
    answer1 = []
    for i in range(len(answer)):
        answer1.append(answer[i])
        if (len(answer1) >= 2 and answer1[len(answer1) - 1] == '.' and answer1[len(answer1) - 2] == '.'):
            answer1.pop()
    # step4
    if answer1[0] == '.' and answer1[-1] != '.':
        answer1 = answer1[1:]
    elif answer1[0] != '.' and answer1[-1] == '.':
        answer1 = answer1[:-1]
    elif answer1[0] == '.' and answer1[-1] == '.':
        answer1 = answer1[1:-1]
    # step5
    if len(answer1) == 0:
        answer1.append('a')
    # step6
    answer1 = answer1[:15]
    if answer1[-1] == '.':
        answer1 = answer1[:-1]
    # step7
    if len(answer1) <= 2:
        value = answer1[-1]
        while len(answer1) < 3:
            answer1.append(value)
    answer = ''.join(answer1)

    return answer