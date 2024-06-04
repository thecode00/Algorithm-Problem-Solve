// https://school.programmers.co.kr/learn/courses/30/lessons/49993?language=javascript

function solution(skill, skill_trees) {
  const skillSet = new Set(skill);
  let answer = 0;

  for (const userSkillTree of skill_trees) {
    let learnedSkill = 0,
      isValid = true;

    for (const userSkill of userSkillTree) {
      if (skillSet.has(userSkill) && userSkill !== skill[learnedSkill]) {
        isValid = false;
        break;
      }

      if (userSkill === skill[learnedSkill]) {
        learnedSkill += 1;
      }

      if (learnedSkill === skill.length) {
        break;
      }
    }

    answer += isValid;
  }
  return answer;
}
