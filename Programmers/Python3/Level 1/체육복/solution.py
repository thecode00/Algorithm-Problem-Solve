# https://programmers.co.kr/learn/courses/30/lessons/42862

# for문으로 구현했을때 알수없는 오류가 나서 set으로 고친 코드
def solution(n, lost, reserve):
    # 여벌체육복을 가져온 학생들중 도둑맞은 학생들 제거
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    # 그리디하게 왼쪽에 있는 학생부터 빌려줌
    for student in set_reserve:  # 여벌체육복을 가져온 학생의 주변에 도둑맞은 학생이 있는지 검사
        if student - 1 in set_lost:
            set_lost.remove(student - 1)
        elif student + 1 in set_lost:
            set_lost.remove(student + 1)

    answer = n - len(set_lost)
    return answer
