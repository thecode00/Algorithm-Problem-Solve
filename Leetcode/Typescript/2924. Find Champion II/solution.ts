// https://leetcode.com/problems/find-champion-ii/description

function findChampion(n: number, edges: number[][]): number {
    const inDegree: number[] = Array.from({ length: n }, () => 0);


    for (const [_, weak] of edges){
        inDegree[weak] += 1
    }

    let champCount = 0, champTeam = -1

    for (let team = 0; team < n; team++){
        if (inDegree[team] === 0){
            champTeam = team
            champCount += 1
        }
    }

    return champCount === 1 ? champTeam : -1
};
