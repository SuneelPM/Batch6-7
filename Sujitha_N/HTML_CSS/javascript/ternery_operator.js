let age=10;
//age>=18 eligible to vote
//age<18 nolt eligible

//ternary operater
age>=18 
  ? console.log("eligible to vote")
  : console.log("not eligible")

  //if else statements
if(age>=18 ){
  console.log("Hello");
  console.log("eligible to vote");
}else{
  console.log("How are you");
  console.log("not eligible to vote");
}

// BMI 0-18.5...underweight
// 18-5...normal weight
// 25-30...over weight
// 30-48...obese
//  40-above...how are you still alive?       
// if else ,switch case,ternary prgm

      

let bmi = 20;

(bmi > 0 && bmi < 18.5) 
  ? console.log("bakka palchana")
  : (bmi >= 18.5 && bmi < 25)
    ? console.log("normal weight")
    : (bmi >= 25 && bmi < 30)
      ? console.log("over weight")
      : (bmi >= 30 && bmi < 48)
        ? console.log("obese")
        : console.log("how are you still alive?");

        



let category = "OBC";
switch(category) {
  case "OC":
      console.log("6 Attempts");
      break;
  case "OBC":
      console.log("9 Attempts");
      break;
  case "SC":
      console.log("Unlimited Attempts");
      break;
  default:
      console.log("Invalid Category");
}