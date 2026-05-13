let fruits = ["apple", "banana", "orange", "kiwi"];

console.log(fruits.length);

let str = "";
for (let i = 0; i < fruits.length; i++) {
  str += fruits[i];
}

console.log(str);

let numArray = [1, 2, 3, 4, 5, 6];

// print sum of elements of an array

let sumOfElements = 0;
for (let a = 0; a < numArray.length; a++) {
  console.log(a);
  sumOfElements += numArray[a];
}

console.log(sumOfElements);

let arr = [10, 13, 31, 42, 54, 68, 73, 84];
// sum of elements using while loop
// average of these elements (arithmatic mean)
// geometric mean of the elements
// nth root of (muliplication of all the elements)

let e = 0;
let sum = 0;
while (e < arr.length) {
  sum += arr[e];
  e++;
}

console.log(e);

console.log(sum);
console.log(sum / arr.length);

let z = 0;
let product = 1;
while (z < arr.length) {
  product *= arr[z];
  z++;
}

console.log(product);
console.log(product ** (1 / arr.length));

let heightsOfStudents = [157, 166, 152, 153, 155, 152];

let sumOfHeights = 0;
let count = 0;
for (let i = 0; i < heightsOfStudents.length; i++) {
  sumOfHeights += heightsOfStudents[i];
  count++;
}

console.log(sumOfHeights / heightsOfStudents.length);
console.log(count);
