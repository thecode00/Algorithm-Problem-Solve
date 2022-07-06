# https://programmers.co.kr/learn/courses/30/lessons/72412

# TODO: 나중에 풀기
def solution(info, query):
    answer = []
    applicant = [list(spec.split()) for spec in info]
    q = list(s.split(" and ") for s in query)
    print(q)
    for idx in range(len(q)):
        temp = []   # 임시로 조건에맞는 지원자들을 담을 리스트
        for i in range(len(q[idx])):
            if temp:
                for app in range(len(temp)):
                    if temp[app][i] != q[idx][i] and q[idx][i] != "-":
                        print(i)
            else:
                if i == 0:
                    for app in applicant:
                        if app[i] == q[idx][i] or q[idx][i] == "-":
                            temp.append(app)
                else:
                    break
        answer.append(len(temp))
    return answer
