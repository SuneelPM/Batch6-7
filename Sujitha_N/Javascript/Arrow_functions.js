//arrow function
let add1 = (a,b) => {
    return a+b;
};

// implicit return arrow function
let add4 = (a,b) => a+b;


//regular function
function add2(a,b) {
    return a+b;

};

//function expression
let add3 = function (a,b) {
    return a+b;
}
console.log(add1(10, 20));
console.log(add2(20, 20));
console.log(add3(30, 40));
console.log(add4(50, 60));

//wrt a arrow function to multiple 2 numbers
const mul = (a, b) => a*b
    return a * b;


const multiply = (a, b) =>a*b;
console.log(multiply(5, 3));

const add = (a, b) => a+b;
console.log(add(5, 3));

const sub = (a, b) => a-b;
console.log(sub(5, 3));

const div = (a, b) => a/b;
console.log(div(5, 3));

const mod = (a, b) => a%b;
console.log(mod(5, 3));

const power = (a, b) => a**b;
console.log(power(5, 3));


let mul1 = (a,b) => console.log(a*b);   //this is void function,returns undefined

//function cube(n) { return n* n* n;}....convert arrow function to implicit
const cube = n => n * n * n;
console.log(cube(3));  //27







   


