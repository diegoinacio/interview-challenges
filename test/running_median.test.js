const assert = require("chai").assert;
const runningMedian = require("../src/running_median");

describe("Sample Tests", function () {
  describe("Case 0", function () {
    assert.deepEqual(runningMedian([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [
      "1.0",
      "1.5",
      "2.0",
      "2.5",
      "3.0",
      "3.5",
      "4.0",
      "4.5",
      "5.0",
      "5.5",
    ]);
  });
});

describe("Custom Tests", function () {
  describe("Case 0", function () {
    assert.deepEqual(runningMedian([]), []);
    assert.deepEqual(runningMedian([16, 8, 2, 4, 32]), [
      "16.0",
      "12.0",
      "8.0",
      "6.0",
      "8.0",
    ]);
  });
});
