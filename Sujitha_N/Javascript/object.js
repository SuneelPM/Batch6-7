let stu = {
    name: "suji",
    age: 21,
    location: "Hyd",
    female: true,
    education: ["10th", "inter", "btech", "ms"],
    address: {
        houseno: 123,
        aptname: "malaysia township,block A",
        line1: "gandhi nagar",
        line2: "kphb",
        city: "hyderabad",
        district: "RR",
        state: "telangana",
        pincode: 500087
    },
    addresses: [
        {
            houseno: 123,
            aptname: "malaysia township,block A",
            line1: "gandhi nagar",
            line2: "Rpl",
            city: "Repalle",
            district: "RR",
            state: "Ap",
            pincode: 522265
        },
        {
            houseno: 123,
            aptname: "malaysia township,block A",
            line1: "gandhi nagar",
            line2: "Rpl",
            city: "Repalle",
            district: "RR",
            state: "Ap",
            pincode: 522265
        }
    ]
};


console.log(addresses[0]);

// access values
//dot notation
console.log(stu.name);
console.log(stu.female);

// empty object & array
let emptyobj = {};
let emptyarr = [];

console.log(typeof emptyobj);
console.log(typeof emptyarr);

// correct array access
console.log(stu.education[2]);

// nested object access
console.log(stu.address.line1);