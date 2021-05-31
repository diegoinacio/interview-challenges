// ! Problem

// {1, 2, 3} -> 2 is the median.
// {1, 2, 3, 4} -> (2 + 3)/2 = 2.5 is the median.

// ? Function Description

// * Given an input stream of  integers, you must ..
// * perform the following task for each i_th integer:
// 1 - Add the i_th integer to a running list of integers.
// 2 - Find the median of the updated list (i.e., for the ..
//     first element through the i_th element).
// 3 - Print the list's updated median on a new line. The ..
//     printed value must be a double-precision number ..
//     scaled to 1 decimal place (i.e., 12.3 format).

// * {16, 8, 2, 4, 32} -> {16.0, 12.0, 8.0, 6.0, 8.0}

function runningMedian(inputList) {
  let result = [];
  for (let i = 0; i < inputList.length; i++) {
    const currentList = inputList.slice(0, i + 1).sort((a, b) => a - b);
    const n = currentList.length;
    const middle = Math.floor(n / 2);
    const median =
      n % 2
        ? currentList[middle]
        : (currentList[Math.floor(n / 2)] + currentList[middle - 1]) / 2;
    result.push(median.toFixed(1));
  }
  return result;
}

module.exports = runningMedian;
