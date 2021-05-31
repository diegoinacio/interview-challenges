const assert = require("chai").assert;
const contacts = require("../src/contacts");

describe("Sample Tests", function () {
  describe("Case 0", function () {
    assert.deepEqual(
      contacts([
        ["add", "hack"],
        ["add", "hackerrank"],
        ["find", "hac"],
        ["find", "hak"],
      ]),
      [2, 0]
    );
  });

  describe("Case 1", function () {
    assert.deepEqual(
      contacts([
        ["add", "ed"],
        ["add", "eddie"],
        ["add", "edward"],
        ["find", "ed"],
        ["add", "edwina"],
        ["find", "edw"],
        ["find", "a"],
      ]),
      [3, 2, 0]
    );
  });
});

describe("Custom Tests", function () {
  describe("Case 0", function () {
    assert.deepEqual(
      contacts([
        ["add", "diego"],
        ["add", "diogo"],
        ["add", "diogenes"],
        ["find", "die"],
        ["find", "dio"],
      ]),
      [1, 2]
    );
  });

  describe("Case 1", function () {
    assert.deepEqual(
      contacts([
        ["add", "diego"],
        ["add", "diogo"],
        ["find", "die"],
        ["add", "diogenes"],
        ["find", "dio"],
        ["add", "diegones"],
        ["add", "dialogo"],
        ["find", "die"],
        ["find", "dio"],
        ["find", "dia"],
      ]),
      [1, 2, 2, 2, 1]
    );
  });
});
