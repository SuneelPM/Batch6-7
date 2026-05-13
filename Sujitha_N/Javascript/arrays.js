let fruits = ["Apple" , "Banana" , " Mango" , "kiwi"];
//console.log(fruits[0]);
//console.log(fruits.length);

let str="";
for(let i=0; i < fruits.length; i++) {
    str += fruits[i];
    //console.log(fruits[i]);
}
console.log(str);

//print sum of elements of an array
let numarray = [1,2,3,4,5,6];
let sumofelements = 0;
for (let i = 0; i < numarray.length; i++) {
    sumofelements += numarray[i];
}
console.log("sum of elements:", sum);


let arr = [10, 13, 31, 42, 54, 68, 73, 84];
//sum of array using while loop
//avg of these elements(arthimetic mean)
//avg of these ele(geometric mean)


//sum of array using while loop
let arr = [10, 13, 31, 42, 54, 68, 73, 84];

let sums = 0;
let i = 0;
while (i < arr.length) {
    sums  = sums + arr[i];
    i++;
}

console.log("Sum of array:", sums);


//avg of above elements(arthimetic mean)
let arr = [10, 13, 31, 42, 54, 68, 73, 84];

let sum = 0;
for (let i = 0; i < arr.length; i++) {
    sum = sum + arr[i];
}

let avg = sum / arr.length;

console.log("Sum:", sum);
console.log("Average:", avg);



//avg of above elements(geometric mean)
let arr = [10, 13, 31, 42, 54, 68, 73, 84];

let z =0;
let product = 1;
while (z < arr.length) {
    product *= arr[z];
    z++;
}

console.log(product);
console.log(product ** (1 / arr.length));


//sum of students height
let heightofstudents = [157, 166, 152, 153, 155, 152];

let sumofheights = 0;
for (let i = 0;i < heightofstudents.length; i++) {
    sumofheights += heightofstudents [i];
}
console.log(sumofheights / heightofstudents.length);

