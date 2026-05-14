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



let BTechCse = {
  semester1: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester2: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester3: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester4: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester5: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester6: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester7: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
  semester8: {
    subject1: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject2: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject3: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject4: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
    subject5: {
      chapter1: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter2: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter3: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter4: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
      chapter5: ["Topic 1", "Topic 2", "Topic 3", "Topic 4", "Topic 5"],
    },
  },
};