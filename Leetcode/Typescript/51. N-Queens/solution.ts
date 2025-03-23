// https://leetcode.com/problems/n-queens/description/

function solveNQueens(n: number): string[][] {
  const result: string[][] = [];
  placeQueen(
    n,
    [],
    new Set<number>(),
    new Set<number>(),
    new Set<number>(),
    result
  );
  return result;
}

function placeQueen(
  n: number,
  board: number[],
  cols: Set<number>,
  diag1: Set<number>,
  diag2: Set<number>,
  result: string[][]
) {
  const row = board.length;
  // Placed all queen
  if (row === n) {
    result.push(boardToString(board));
    return;
  }

  for (let col = 0; col < n; col++) {
    // Checks if a queen can be placed in the given column without being attacked by other queens
    if (canPlaceQueen(diag1, diag2, cols, col, row)) {
      board.push(col);
      cols.add(col);
      diag1.add(row + col);
      diag2.add(row - col);
      placeQueen(n, board, cols, diag1, diag2, result);
      board.pop();
      cols.delete(col);
      diag1.delete(row + col);
      diag2.delete(row - col);
    }
  }
}

function boardToString(board: number[]): string[] {
  const result: string[] = [];

  for (const col of board) {
    const rowBoard = Array.from({ length: board.length }, (_) => ".");

    rowBoard[col] = "Q";
    result.push(rowBoard.join(""));
  }

  return result;
}

function canPlaceQueen(
  diag1: Set<number>,
  diag2: Set<number>,
  cols: Set<number>,
  col: number,
  row: number
): boolean {
  if (cols.has(col) || diag1.has(row + col) || diag2.has(row - col)) {
    return false;
  }
  return true;
}
