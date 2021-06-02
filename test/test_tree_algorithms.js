const assert = require("chai").assert;
const {
  BinaryTree,
  BuildTree,
  get_preOrder,
  get_postOrder,
  get_inOrder,
  get_levelOrder,
  get_height,
} = require("../src/tree_algorithms");

// Given the binary tree
//
//           5
//         /   \
//        2     3
//      /  \   / \
//     4    1 9   8
//   /  \        /
//  6    7     10
//

BT = new BinaryTree(5);
BuildTree(BT.root, [
  [2, 3],
  [4, 1],
  [9, 8],
  [6, 7],
  [-1, -1],
  [-1, -1],
  [10, -1],
  [-1, -1],
  [-1, -1],
  [-1, -1],
]);

describe("Tree Traversal Tests", function () {
  describe("Depth-first Order", function () {
    describe("PreOrder", function () {
      assert.deepEqual(get_preOrder(BT.root), [5, 2, 4, 6, 7, 1, 3, 9, 8, 10]);
    });

    describe("PostOrder", function () {
      assert.deepEqual(get_postOrder(BT.root), [6, 7, 4, 1, 2, 9, 10, 8, 3, 5]);
    });

    describe("InOrder", function () {
      assert.deepEqual(get_inOrder(BT.root), [6, 4, 7, 2, 1, 5, 9, 3, 10, 8]);
    });
  });

  describe("Level Order", function () {
    assert.deepEqual(get_levelOrder(BT.root), [5, 2, 3, 4, 1, 9, 8, 6, 7, 10]);
  });
});

describe("Feature Tests", function () {
  describe("Get Height", function () {
    assert.equal(get_height(BT.root), 3);
  });
});
