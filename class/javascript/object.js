let student = {
  name: "Suneel",
  age: 25,
  location: "Hyderabad",
  firstName: "Suneel",
  id: "",
  male: true,
  education: ["10th", "Inter", "BTech", "MS"],
  primaryAddress: {
    houseNo: 232,
    aptName: "Malaysia township, Block A",
    line1: "Gandhi Nagar",
    line2: "KPHB",
    city: "Hyderabad",
    District: "RR",
    State: "Telangana",
    pincode: 500087,
  },
  addresses: [
    {
      houseNo: 232,
      aptName: "Malaysia township, Block A",
      line1: "Gandhi Nagar",
      line2: "KPHB",
      city: "Hyderabad",
      District: "RR",
      State: "Telangana",
      pincode: 500087,
    },
    {
      houseNo: 252,
      aptName: "Malaysia township, Block A",
      line1: "Gandhi Nagar",
      line2: "KPHB",
      city: "chirala",
      District: "Bapatla",
      State: "Andhra Pradesh",
      pincode: 523155,
    },
  ],
};

console.log(student.addresses[1].state);

let addresses = [
  {
    houseNo: 232,
    aptName: "Malaysia township, Block A",
    line1: "Gandhi Nagar",
    line2: "KPHB",
    city: "Hyderabad",
    District: "RR",
    State: "Telangana",
    pincode: 500087,
  },
  {
    houseNo: 252,
    aptName: "Malaysia township, Block A",
    line1: "Gandhi Nagar",
    line2: "KPHB",
    city: "chirala",
    District: "Bapatla",
    State: "Andhra Pradesh",
    pincode: 523155,
  },
];

console.log(addresses[1].houseNo);

// access the values in an object
// dot notation
console.log(student.name);
console.log(student.male);
console.log(student.education[5]);

console.log(student.address.line1);

/* 
properties of student object



*/

// let emptyobj = {};
// let emptyArr = [];

// console.log(typeof emptyobj);
// console.log(typeof emptyArr);
