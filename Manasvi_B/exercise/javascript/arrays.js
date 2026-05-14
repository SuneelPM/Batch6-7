 let fruits = ['apple', 'banana', 'orange'];
// console.log(fruits.length) //used to know the length of strings.
// // for(let i = 0; i < 3; i++)
 let result = ""
 for(let i = 0; i < fruits.length; i++)
     {
         console.log(result += fruits[i])
     }


let numarray = [1, 2, 3, 4, 5];
let sum = 0
for(let i = 0; i < numarray.length; i++){
    console.log(i);
    sum += numarray[i]
}
console.log(sum)


let arr = [10, 13, 31, 42, 54, 68, 73, 84];
let i = 0;
let avg = 0;
let sum1 = 0;
let product = 1;
let gmean = 0;
while(i < arr.length){
    sum1 += arr[i]
    avg = sum/arr.length
    product *= arr[i]
    gmean = product ** (1/ arr.length) 
    i++
}
console.log(sum1)
console.log(avg)
console.log(gmean)

let arr2 = [157,166,152,153,155,152,[134,136]];
console.log(arr2[6][2])
// let sumofheights = "";
// for(let a = 0; a < sumofheights.length; a++){
//     sumofheights += heightsofstudents[a]
// }
// console.log(sumofheights/heightsofstudents.length)