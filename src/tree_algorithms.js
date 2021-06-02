class Node {
  constructor(data) {
    this._data = data;
    this._left = null;
    this._right = null;
  }

  get data() {
    return this._data;
  }

  set data(value) {
    this._data = value;
  }

  get left() {
    return this._left;
  }

  set left(value) {
    this._left = new Node(value);
  }

  get right() {
    return this._right;
  }

  set right(value) {
    this._right = new Node(value);
  }
}

class BinaryTree {
  constructor(value = null) {
    this._root = value && new Node(value);
  }

  get root() {
    return this._root;
  }

  set root(value) {
    this._root = new Node(value);
  }
}

function BuildTree(root, indices) {
  if (root instanceof Node) {
    // * Init stacking the root note
    const stack = [root];
    // * Loop through indices
    for (const [l, r] of indices) {
      // * Get the first element from the stack
      const node = stack.shift();
      // * Store left node if not -1
      if (l !== -1) {
        node.left = l;
        stack.push(node.left);
      }
      // * Store right node if not -1
      if (r !== -1) {
        node.right = r;
        stack.push(node.right);
      }
    }
  }
}

function get_preOrder(root, order = []) {
  if (root instanceof Node) {
    // * First get the data of node
    order.push(root.data);
    // * Then recur on left child
    get_preOrder(root.left, order);
    // * Finally recur on right child
    get_preOrder(root.right, order);
  }
  // * Return a list of order
  return order;
}

function get_postOrder(root, order = []) {
  if (root instanceof Node) {
    // * First recur on left child
    get_postOrder(root.left, order);
    // * Then recur on right child
    get_postOrder(root.right, order);
    // * Finally get the data of node
    order.push(root.data);
  }
  // * Return a list of order
  return order;
}

function get_inOrder(root, order = []) {
  if (root instanceof Node) {
    // * First recur on left child
    get_inOrder(root.left, order);
    // * Then get the data of node
    order.push(root.data);
    // * Finally recur on right child
    get_inOrder(root.right, order);
  }
  // * Return a list of order
  return order;
}

function get_levelOrder(root, order = []) {
  if (root instanceof Node) {
    // * Init stacking the root note
    const stack = [root];
    // * While the stack is not empty
    while (stack.length) {
      // * Get the first element
      const node = stack.shift();
      if (node) {
        // * Store the level order
        order.push(node.data);
        // * Stack the left and right nodes
        stack.push(node.left, node.right);
      }
    }
  }
  // * Return a list of order
  return order;
}

function get_height(root) {
  return root
    ? Math.max(get_height(root.left), get_height(root.right)) + 1
    : -1;
}

module.exports = {
  BinaryTree,
  BuildTree,
  get_preOrder,
  get_postOrder,
  get_inOrder,
  get_levelOrder,
  get_height,
};
