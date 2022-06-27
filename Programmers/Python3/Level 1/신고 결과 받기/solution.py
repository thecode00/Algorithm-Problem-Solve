# https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict


def solution(id_list, report, k):
    # 중복 신고는 무시하므로 set로 설정
    report_dict = defaultdict(set)

    # 신고당한 유저를 key로 삼고 value에 신고한 유저를 넣는다
    for str in report:
        name, reported_user = str.split(" ")
        report_dict[reported_user].add(name)

    # 결과 메일수를 체크할 dict
    user_dict = dict.fromkeys(id_list, 0)

    for key in report_dict:
        # 총 신고유저가 k를 넘었으면 정지를 당한것이므로 해당유저를 신고한 모든 유저의 결과메일 수를 +1 시킨다
        if len(report_dict[key]) >= k:
            for i in report_dict[key]:
                user_dict[i] += 1

    answer = []
    for user in user_dict.values():
        answer.append(user)

    return answer
