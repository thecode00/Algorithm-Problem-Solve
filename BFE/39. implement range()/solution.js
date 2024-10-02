// https://bigfrontend.dev/problem/implement-range

/**
 * @param {integer} from
 * @param {integer} to
 */
function* range(from, to) {
  for (let num = from; num <= to; num++) {
    yield num;
  }
}
