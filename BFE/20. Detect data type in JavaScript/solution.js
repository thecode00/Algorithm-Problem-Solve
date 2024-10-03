// https://bigfrontend.dev/problem/detect-data-type-in-JavaScript

/**
 * @param {any} data
 * @return {string}
 */
function detectType(data) {
  if (typeof data !== "object") {
    return (typeof data).toLowerCase();
  }

  if (Object.is(data, null)) {
    return "null";
  }

  return data.constructor.name.toLowerCase();
}
