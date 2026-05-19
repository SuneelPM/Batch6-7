//arrow funtions
let add1=(a,b)=>{
    return a+b;
};

//implicit return arrow funtion
let add4=(a,b)=>a+b;
//regular function
function add2(a,b){
    return a+b;
}

//funtion expression
let add3=function(a,b){
    return a+b;
};
console.log(add1(10,20))
console.log(add2(20,30))
console.log(add3(30,40))
console.log(add4(40,50))

//write an arrow funtion to multiple 2 numbers
let add = (a,b) => a + b;
let sub = (a,b) => a - b;
let mul = (a,b) => a * b;
let div = (a,b) => a / b;
let mod = (a,b) => a % b;
let power = (a,b) => a ** b;
console.log(add(10,5));
console.log(sub(10,5));
console.log(mul(10,5));
console.log(div(10,5));
console.log(mod(10,5));
console.log(power(10,5));

//convert this to an arrow function with implict return:function cube(n) {return n*n*n;}  
const cube = n => n * n * n;
console.log(cube(3));