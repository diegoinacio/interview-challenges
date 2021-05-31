const assert = require("chai").assert;
const isBalanced = require("../src/balanced_brackets");

describe("Sample Tests", function () {
  describe("Case 0", function () {
    assert.equal(isBalanced("{[()]}"), "YES");
    assert.equal(isBalanced("{[(])}"), "NO");
    assert.equal(isBalanced("{{[[(())]]}}"), "YES");
  });

  describe("Case 1", function () {
    assert.equal(isBalanced("{{([])}}"), "YES");
    assert.equal(isBalanced("{{)[](}}"), "NO");
  });

  describe("Case 2", function () {
    assert.equal(isBalanced("{(([])[])[]}"), "YES");
    assert.equal(isBalanced("{(([])[])[]]}"), "NO");
    assert.equal(isBalanced("{(([])[])[]}[]"), "YES");
  });
});

describe("Custom Tests", function () {
  describe("Case 0", function () {
    assert.equal(isBalanced(""), "YES");
    assert.equal(isBalanced("13"), "YES");
    assert.equal(isBalanced("([{7}])"), "YES");
    assert.equal(isBalanced("{[()*15{}]}"), "YES");
    assert.equal(isBalanced("{[{[{()}]}])"), "NO");
  });
});
