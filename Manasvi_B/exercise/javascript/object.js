let students = {
    firstname: "Bezawada",
    middlename: "Manasvi",
    lastname: "Chowdary",
    age: 25,
    location: "Hyd",
    id: "",
    female: true,
    education:["10th", "Inter", "BTech", 1, true],
    address:{
        houseno: 101,
        aptname:"TKR CHAITRA RESIDENCY",
        line1:"Mithilanagar",
        area:"Pragathinagar",
        city:"Hyderabad",
        district:"Medchal",
        state:"Telangana",
        pincode:500090,
    },
};

console.log(students.name);
console.log(students.female);
console.log(students.education[2])
console.log(students.address.houseno);

let addresses = [{
        houseno: 102,
        aptname:"TCR",
        line1:"ABC",
        area:"CBA",
        city:"BCA",
        district:"BAC",
        state:"T",
        pincode:500010,
    },
    {
        houseno: 103,
        aptname:"TRK",
        line1:"DEF",
        area:"FED",
        city:"EFD",
        district:"EDF",
        state:"A",
        pincode:500020,
    },];
console.log(addresses[0]);
console.log(addresses[0].houseno);