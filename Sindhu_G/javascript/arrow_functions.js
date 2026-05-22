//  arrow function
let add1 = (a, b)=> {
    return a + b;
};

//  implicit return arrow function
let add4 = (a, b) => a + b;


// regular function


function add2(a, b) {
    return a + b;
}

// function expression
let add3 = function (a, b){
    return a + b;
};

console.log(add1(10,20))
console.log(add2(20,30))
console.log(add3(30,40))
console.log(add4(40,50))

// write an arrow function to multiple 2 numbers


const multiply = (a, b) => {
  return a * b;
  console.log(multiply(5, 4));
};

// subtraction

const sub = (a, b) => {
  return a - b;
  console.log(sub(5, 4));
};


// division

const div = (a, b) => {
  return a/b;
  console.log(div(5, 4));
};

// module

const module = (a, b) => {
  return a % b;
  console.log(module(5, 4));
};



