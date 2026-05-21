let age = 10;
//age >= 18 eligible to vote
//age < 18 not eligible


//ternary operator
age >= 18
? console.log("Eligible to vote")
:console.log("not eligible to vote");

//if else statements
if (age >=18) {
    console.log("Hello Miss");
    console.Log("Eligible to vote")
} else { 
    console.log("how are you?");
    console.log("you are not eligible to vote")  
}


// BMI - 0 - 18.5 - underweight
// 18.5 to 25 - normal weight
// 25 to 30 - over weight
// 30 to 40 - obese
// 40 and above - how are you still alive?

let bmi = Number(prompt("Enter your BMI:"));

switch (true) {
  case (bmi >= 0 && bmi < 18.5):
    console.log("Underweight");
    break;

  case (bmi >= 18.5 && bmi < 25):
    console.log("Normal weight");
    break;

  case (bmi >= 25 && bmi < 30):
    console.log("Overweight");
    break;

  case (bmi >= 30 && bmi < 40):
    console.log("Obese");
    break;

  case (bmi >= 40):
    console.log("Very high BMI (consult a doctor)");
    break;

  default:
    console.log("Invalid BMI");
}


