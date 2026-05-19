//arrow function
let add = (a, b) =>{
    return a + b;//explicit return
};

let add1 = (a, b) => a + b;//implicit return

//regular function
function add2(a, b){
    return a + b;
};

//function expression
let add3 = function(a, b){
    return a + b;
};

console.log(add(10, 20));
console.log(add1(10, 20));
console.log(add2(10, 20));
console.log(add3(10, 20));

let mul=(a, b) =>a * b;
console.log(mul(2, 10));

let sub=(a, b) => a - b;
console.log(sub(1, 2));

let div=(a, b) => a / b;
console.log(div(10, 2));

let exp=(a, b) => a ** b;
console.log(exp(2, 2));

let mod=(a, b) => a % b;
console.log(mod(1, 2));

let cube = n => n * n * n;
console.log(cube(3))