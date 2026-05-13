let  student={
    name : "Chaitanya",
    age:22,
    location:'hyd',
    id:'',
    female:true,
    education:['10th','inter','btech','ms']
};
let address={
    houseno:'g-1',
    aptname:"padmavati residency",
    line1:'muthyala reddy nagar 1st line',
    city:'guntur',
    district:'guntur',
    state:'ap',
    pincode:522007,
};
let address=[{
    houseno:'g-1',
    aptname:"padmavati residency",
    line1:'muthyala reddy nagar 1st line',
    city:'guntur',
    district:'guntur',
    state:'ap',
    pincode:522007,
},
{
    houseno:'f-1',
    aptname:"padmavati residency",
    line1:'muthyala reddy nagar 1st line',
    city:'chirala',
    district:'bapatla',
    state:'ap',
    pincode:522007,
}
]
// let emptyobj={};
// let emptyarr=[];
// console.log(typeof emptyobj);
// console.log(typeof emptyarr);
//access the values in  an object 
//dot notation
console.log(student.name);
console.log(student.female);
console.log(student.education[2]);

console.log(address[1].houseno);