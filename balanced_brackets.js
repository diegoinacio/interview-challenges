// ! Problem

// {[()]} is balanced.
// {[(])} is not balanced.
// {{[[(())]]}} is balanced.

// ? Function Description

// It must return a string: YES if the sequence is balanced
// or NO if it is not.

// "isBalanced" has the following parameter(s):
// - input_string: a string of brackets

function isBalanced(input_string) {
  // * Define valid bracket pairs
  const brackets = ["()", "[]", "{}"];
  // * Remove extra information from input string
  input_string = [...input_string]
    .filter((e) => brackets.join("").includes(e))
    .join("");
  // * Loop while exist some pair in the input string
  while (brackets.some((e) => input_string.includes(e))) {
    brackets.forEach((b) => {
      input_string = input_string.replace(b, "");
    });
  }
  return input_string ? "NO" : "YES";
}

module.exports = isBalanced;
