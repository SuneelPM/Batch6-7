let fruits=["apple","banana","orange","kiwi"]
console.log(fruits.length)
for(let i=0;i<fruits.length;i+=2){
    console.log(fruits[i])
}


let str=""
for(let i=0;i<fruits.length;i++){
    str+=fruits[i];
}
console.log(str);


let numArray=[1,2,3,4,5,6];//print sum of elements of an array
let sum = 0;
for(let i= 0; i < numArray.length; i++){
    console.log(i)
    sum = sum + numArray[i];
}
console.log("Sum of array elements is:", sum);



let arr=[10,13,31,42,54,68,73,84]
let sums = 0;
let i= 0;
while(i < arr.length){
    sums = sums + arr[i];
    i++;
}
console.log("Sum of array elements is:", sums);
console.log(sum/arr.length);//average of these elements


let arrs = [10,13,31,42,54,68,73,84];
let product = 1;
let s = 0;
while(s< arrs.length){
    product = product * arrs[s];
    s++;
}
console.log(product**(1 / arrs.length));
console.log(product);


let heightofstudents=[157,166,152,153,155,152];
let sumofheights=0
for(let i=0;i<heightofstudents.length;i++){
    sumofheights+=heightofstudents[i];
}
console.log(sumofheights/heightofstudents.length)
