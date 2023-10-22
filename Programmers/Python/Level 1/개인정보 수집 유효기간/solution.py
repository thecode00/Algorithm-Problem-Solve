# https://school.programmers.co.kr/learn/courses/30/lessons/150370


def convert_to_day(year, month, day):   # 계산하기 편하게 년, 월을 일로 변환시키는 함수
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    for term in terms:  # 각 약관의 유효기간을 딕셔너리에 저장
        key, period = term.split()
        term_dict[key] = int(period) * 28

    today = list(map(int, today.split(".")))
    print(today)
    today_total = convert_to_day(today[0], today[1], today[2])

    for idx in range(len(privacies)):
        cur, key = privacies[idx].split()
        y, m, d = map(int, cur.split("."))    # 년, 월, 일
        cur_total = convert_to_day(y, m, d)
        if today_total - cur_total >= term_dict[key]:    # 유효기간이 지났을때
            answer.append(idx + 1)

    return answer
