let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

class MinHeap {
  constructor() {
    this.heap = [BigInt(0)];
  }

  isBiggerThanChildren(idx) {
    if (this.heap[2 * idx]) {
      return (
        this.heap[idx] > this.heap[2 * idx] ||
        this.heap[idx] > this.heap[2 * idx + 1]
      );
    } else {
      return false;
    }
  }

  swapValue(idx1, idx2) {
    [this.heap[idx1], this.heap[idx2]] = [this.heap[idx2], this.heap[idx1]];
  }

  insert(value) {
    this.heap.push(value);

    let currentIdx = this.heap.length - 1;
    let parentIdx = Math.floor(currentIdx / 2);

    while (currentIdx > 1 && this.heap[currentIdx] < this.heap[parentIdx]) {
      this.swapValue(currentIdx, parentIdx);
      currentIdx = parentIdx;
      parentIdx = Math.floor(currentIdx / 2);
    }
  }

  sum() {
    return this.heap.reduce((a, b) => a + b, BigInt(0));
  }

  remove() {
    if (this.heap.length > 1) {
      if (this.heap.length === 2) return this.heap.pop();

      let removedVal = this.heap[1];
      this.heap[1] = this.heap.pop();
      let currentIdx = 1;

      while (this.isBiggerThanChildren(currentIdx)) {
        if (this.heap[2 * currentIdx + 1] < this.heap[2 * currentIdx]) {
          if (this.heap[2 * currentIdx + 1] < this.heap[currentIdx]) {
            this.swapValue(2 * currentIdx + 1, currentIdx);
            currentIdx = 2 * currentIdx + 1;
          }
        } else {
          if (this.heap[2 * currentIdx] < this.heap[currentIdx]) {
            this.swapValue(2 * currentIdx, currentIdx);
            currentIdx = 2 * currentIdx;
          }
        }
      }

      return removedVal;
    } else return null;
  }
}

let [N, M] = input.shift().split(" ").map(Number);
let arr = input.shift().split(" ").map(BigInt);
let pq = new MinHeap();

for (let i = 0; i < arr.length; i++) {
  pq.insert(BigInt(arr[i]));
}

while (M > 0) {
  let first = pq.remove();
  let second = pq.remove();
  pq.insert(first + second);
  pq.insert(first + second);
  M--;
}
console.log(pq.sum().toString());
