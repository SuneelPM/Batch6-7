let student = {
  name: "Karthik",
  age: 22,
  location: "Ongole",
  id: "",
  male: true,
  education: ["10th", "12th", "BTech", "MS"],
  address: {
    houseNo: 234,
    aptName: "SR Prime",
    line1: "Gandhi Nagar",
    line2: "KPHB",
    city: "HYD",
    District: "RR",
    State: "Telengana",
    pincode: 500087,
  },
};

let addresses = [
  {
    houseNo: 234,
    aptName: "SR Prime",
    line1: "Gandhi Nagar",
    line2: "KPHB",
    city: "HYD",
    District: "RR",
    State: "Telengana",
    pincode: 500087,
  },
  {
    houseNo: 234,
    aptName: "SR Prime",
    line1: "Gandhi Nagar",
    line2: "KPHB",
    city: "ONG",
    District: "RR",
    State: "Telengana",
    pincode: 500087,
  },
];
console.log(addresses[0].city);
console.log(student.address.line2);
console.log(student.education[2]);
let empty = {};
let emptyArr = [];

console.log(typeof empty);
console.log(typeof emptyArr);