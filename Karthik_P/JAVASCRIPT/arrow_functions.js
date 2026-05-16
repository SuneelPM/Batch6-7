//arrow function
let add1 = (a, b) => {
  return a + b;
};
//implicit return arrow function
let add4 = (a, b) => a + b;
let cube = (n) => n * n * n;

//regular function
function add2(a, b) {
  return a + b;
}

//function expression
let add3 = function (a, b) {
  return a + b;
};

console.log(add1(10, 20));
console.log(add2(20, 40));
console.log(add3(40, 50));
console.log(add4(50, 60));

//write an arrow function to multiple 2 numbers
let mul1 = (a, b) => a * b;
let sub = (a, b) => a - b;
console.log(sub(4, 5));

let div = (a, b) => a / b;
console.log(div(4, 5));

let madular = (a, b) => a % b;
console.log(madular(4, 5));

let squre = (a, b) => a ** b;
console.log(squre(4, 5));
