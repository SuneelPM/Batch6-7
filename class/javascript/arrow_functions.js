// arrow function
let add1 = (a, b) => {
  return a + b;
};

// implicit return arrow function

let add4 = (a, b) => a + b;

// regular function

function add2(a, b) {
  return a + b;
}

// function expression

let add3 = function (a, b) {
  return a + b;
};

console.log(add1(10, 20));
console.log(add2(20, 30));
console.log(add3(30, 40));
console.log(add4(40, 50));

// write an arrow function to multiple 2 numbers

let mul1 = (a, b) => console.log(a * b); // this is a void function, returns undefined
let mul2 = (a, b) => a * b; // it returns value
console.log("value of mul: ", mul1(10, 20));
