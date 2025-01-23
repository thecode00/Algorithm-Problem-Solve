// https://leetcode.com/problems/count-servers-that-communicate/description

function countServers(grid: number[][]): number {
    const serverRow = Array.from({length: grid.length}, _ => 0)
    const serverCol = Array.from({length: grid[0].length}, _ => 0)

    for (let y = 0; y < grid.length; y++){
        for (let x = 0; x < grid[0].length; x++){
            if (grid[y][x] === 1){
                serverRow[y] += 1
                serverCol[x] += 1
            }
        }
    }

    let connected = 0

    for (let y = 0; y < grid.length; y++){
        for (let x = 0; x < grid[0].length; x++){
            if (grid[y][x] === 1 && (serverRow[y] > 1 || serverCol[x] > 1)){
                connected += 1
            }
        }
    }

    return connected
};