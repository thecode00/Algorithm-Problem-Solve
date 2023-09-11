# https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    skills = set(skill)  # 선행 스킬 트리의 스킬들
    count = 0
    for skill_tree in skill_trees:
        learn_skill = 0
        is_valid = True
        for s in skill_tree:
            # 스킬트리가 선행 스킬을 따르지 않을경우 탐색 멈춤
            if s in skills and s != skill[learn_skill]:
                is_valid = False
                break
            if s == skill[learn_skill]:
                learn_skill += 1
                if len(skill) == learn_skill:
                    break

        if is_valid:
            count += 1
    return count
