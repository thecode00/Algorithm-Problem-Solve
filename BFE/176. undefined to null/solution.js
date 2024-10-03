// https://bigfrontend.dev/problem/undefined-to-null

/**
 * @param {any} arg
 * @returns {any}
 */

/**
 * @param {any} arg
 * @returns {any}
 */
function undefinedToNull(arg) {
  // Filter undefind and null
  if (Object.is(arg, null) || arg === undefined) {
    return null;
  }
  // Filter array
  if (Array.isArray(arg)) {
    return arg.map(undefinedToNull);
  }
  // Filter object ignore primitive type
  if (typeof arg === "object") {
    for (const key in arg) {
      if (arg.hasOwnProperty(key)) {
        arg[key] = undefinedToNull(arg[key]);
      }
    }
  }

  return arg;
}

undefinedToNull({ a: undefined, b: "BFE.dev" });
