// Name: Direk Kakkar 
// Batch: 1A
// JavaScript Assignment 1

// Task 1: Hello, Stranger!

//ask the user to enter their name
var name = prompt("Enter your name:");
//display a welcome message using string concatenation
console.log("Hello " + name + "! Welcome to JavaScript land");


Task 2: Lucky Number

//ask the user to enter a number and convert it from string to number
let number = Number(prompt("Enter a number:"));
//print double of that number using template literals
console.log(Double of your number is ${number * 2});



Task 3: Mini Cart

//ask the user to enter an item name
let item = prompt("Enter your choice:");
//ask the user to enter the price of that item and convert it to a number
let item_price = Number(prompt("Enter the price of the item:"));
//display a message showing what item was added and its price

console.log(You added ${item} worth ${item_price} rupees to your cart);



Task 4 : Funny Nickname

// ask the user to enter their name
let name = prompt("Enter your name:");
//convert the name to uppercase and take the first 3 letters
let nickname = name.toUpperCase().slice(0, 3) + "inator";
//show the funny nickname using template literals
console.log(Your funny nickname will be: ${nickname});



Task 5: Simple Calculator

//ask the user for the first number and convert it to a number
let a = Number(prompt("Enter first number:"));
//ask the user for the second number and convert it to a number
let b = Number(prompt("Enter second number:"));
//show the sum of the two numbers
console.log(Sum: ${a + b});
//show the difference between the two numbers
console.log(Difference: ${a - b});
//show the product of the two numbers
console.log(Product: ${a * b});
//show the quotient (result of division)
console.log(Quotient: ${a / b});
//show the remainder when first number is divided by second number
console.log(Remainder: ${a % b});
Task 6: Grade Evaluator

// defining a function to check grade
function getScore() {
//asking user to enter marks
  const marks = prompt("Enter your marks (0-100): ");
//converting string input into integer
  const grade = parseInt(marks);
//checking different conditions for grade
  if (grade >= 90) {
    console.log("A Grade");  // if marks are 90 or above
  } else if (grade >= 75) {
    console.log("B Grade");  // if marks are 75-89
  } else if (grade >= 50) {
    console.log("C Grade");  // if marks are 50-74
  } else {
    console.log("Fail");     // if marks are below 50
  }
}

//calling the function so it actually runs
getScore();


Task 7:Ternary Operator

//ask the user if they are hungry
let hungry = prompt("Are you hungry? (yes/no)");  
// prompt() shows a box and takes input from user
// we store that input in the variable 'hungry'
//check with if-else
if (hungry.toLowerCase() === "yes") {  
 // if the user typed "yes", then this block will run
  console.log("Grab Pizza");  
  // this prints "Grab Pizza" in the console
} else {  
  // if the user did not type "yes"
  console.log("Stay Coding");  
  // this prints "Stay Coding" in the console
}
