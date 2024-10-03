// https://bigfrontend.dev/problem/move-zeros

// This is a JavaScript coding problem from BFE.dev

/**
 * @param {Array<any>} list
 * @returns {void}
 */
// function moveZeros(list) {
//   let numIdx = 0

//   for (let idx = 0; idx < list.length; idx++){
//     if (list[idx] !== 0){
//       list[numIdx] = list[idx]
//       numIdx += 1
//     }
//   }

//   for (let idx = numIdx; idx < list.length; idx++){
//     list[idx] = 0
//   }

//   return list
// }

function moveZeros(list) {
  let index = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] !== 0) {
      [list[index++], list[i]] = [list[i], list[index]];
    }
  }
}
