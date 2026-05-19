//let fruits =["apple","banana","orange","kiwi"];
//console.log(fruits.length);
//let str ="";
//for(let i=0; i< fruits.length; i++){
    //str += fruits[i];
//}
    //console.log(str);



//let numarray = [1, 2, 3, 4, 5];
//let sumofElements = 0;
//for(let a = 0; i < numarray.length; i++){
    //sumofElements += numarray[i];
//}
//console.log(sumofElements);


//sum of elements using while loop
let arr =[10,13,31,42,54,68,73,84]
let e= 0;
let sum = 0;
while(e < arr.length){
    sum +=  arr[e];
    e++;
}
console.log(sum);
//average of these elements(arithmatic mean)
console.log(sum / arr.length);
//geometric mean
//nth root of(muliplication of all elements)

let z = 0;
let product = 1;
while(z < arr.length){
    product*=arr[z]
    z++;
}
console.log(product);
console.log(product **(1 /arr.length));

let heightsofstudents=[157,166,152,153,155,152];
let sumofheights =0;
let count =0
for(let i= 0;i<heightsofstudents.length;i++){
    sumofheights +=heightsofstudents[i];
    count++;
}
console.log(sumofheights/heightsofstudents.length);
console.log(count);

