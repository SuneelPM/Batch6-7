let student={
    name:"Sravss",
    age:21,
    location:"Hyderabad",
    firstname:"Sravss",
    id:"",
    female:true,
    education:["10th","Inter","B.Tech",1,true],
    address:{
        houseno: 123,
        aptname:"malaysia township,block A",
        line1:"gandhi namgar",
        line2: "kphb",
        city: "hyderabad",
        district: "RR",
        state: "telangana",
        pincode:500087,
}

};


let addresses=[
    {
       houseno: 123,
        aptname:"malaysia township,block A",
        line1:"gandhi namgar",
        line2: "kphb",
        city: "hyderabad",
        district: "RR",
        state: "telangana",
        pincode:500087,  
    },
    {
        houseno: 11-54,
        aptname:"nageswara rao nilayam",
        line1:"kumar bazar1",
        line2: "kumar bazar2",
        city: "tenali",
        district: "guntur",
        state: "AP",
        pincode:522213,
    }
]

//access the value in an object
//do notation
console.log(student.name);
console.log(student.age);
console.log(student.female);
console.log(student.education)
console.log(student.address.line1)
console.log(addresses[1].houseno)
console.log(student.address[1].state)


