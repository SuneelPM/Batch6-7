let age = 10;
// age >= 18 eligible to vote
// age < 18 not eligible

// ternary operator
age >= 18
  ? console.log("Eligible to vote")
  : console.log("not eligible to vote");

// if else statements
if (age >= 18) {
  console.log("hello");
  console.log("Eligible to vote");
} else {
  console.log("how are you?");
  console.log("you are note eligible to vote");
}

// BMI - 0 - 18.5 - underweight
// 18.5 to 25 - normal weight
// 25 to 30 - over weight
// 30 to 40 - obese
// 40 and above - how are you still alive?

let bmi = 20;

bmi > 0 && bmi < 20
  ? console.log("bakka palchana")
  : bmi >= 20 && bmi < 25
    ? console.log("Normal weight")
    : console.log("over weight");
