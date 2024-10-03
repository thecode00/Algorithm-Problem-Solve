// https://bigfrontend.dev/problem/reorder-array-with-new-indexes

/**
 * @param {any[]} items
 * @param {number[]} newOrder
 * @return {void}
 */
function sort(items, newOrder) {
  for (let index = 0; index < newOrder.length; index++) {
    while (newOrder[index] !== index) {
      const position = newOrder[index];
      [items[index], items[position]] = [items[position], items[index]];
      [newOrder[index], newOrder[position]] = [
        newOrder[position],
        newOrder[index],
      ];
    }
  }
}
