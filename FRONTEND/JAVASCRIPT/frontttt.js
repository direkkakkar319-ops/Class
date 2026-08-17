
// js is a dynamic language(as at time of execution the data type of the variable will be decided)


//steps in execution of a js program                                                                        
//source code-->parser(source code-->token-->AST(abstract syntax tree))-->interpreter( converts line by line after execution of a program)
//(AST converts to byte code)-->compiler(converts the whole code to machine language before execution of the program)
// variable is a named storage location that holds a value.


// "use strict"---->for starting strict mode in java script


// intrepreter-->translates program source code line by line during runtime.
// does not produce a seperate output file
// compiler-->translates entirere program into machine code before the program is run.
// results in standalone executable file.


// java script can be used in html in 3 ways and they are---->inline, external, internal


//scope:it is the environment in which the variable is accessable
//types of scopes:-
//1.functional scope(when a variable is decalred inside a function or block so only accessible in that particular fucntion or block)
//2.global scope(when a varible is declared outside of a function or block and can be accessed in a function or block or outside of them)
//3.block scope(only for let and const)(declared inside a block and can be accessed particularly in that block)
//4.module scope(it refers to the scope present in a inside a module file eg<script type="module">)

//global scope-->var,let,const
//block scope-->let,const
//fucntional scope-->var,let,const

//re-declaration-->var,
//re-initialisation-->var,let
//re-assingment-->var



// call by value--->variable holds its own independent copy of data.
// applies to the primitive data type
// changing new varible does not affect the new varible

// call by refrence-->variable holds a refrence to the same data in memory.
// applies to the non-primitive data type
// both variables point to the same object so affects the other variable
// if we will make changes to one variable other will have the same changes done to it



// 4 types of variable declaration
x = 10;//allowed only in non strict mode
var k;//not advised due to re-initialization and re-declaration
let m;// can be reasingned later in the program.
const l = 100;//(has to be initialized when variable is declared)


// types of datatypes:-
// (1byte=8bits)
// 1.primitive data-types:-
// these are the basic fundamental building blocks of a programming language
// they store simple values
// they are predefined by the language
// diffrent types of primitive data types are:-
// a.string-->2 bytes/character
// declaration of strings:-
const st1 = new String("hello");
const st2 = 'hello world';//hello is taking total of 10bytes or 80bits of storage space
const st3 = "hello world";
const st4 = `hello world`;
// Template Literals
// 1.String interplotation
// eg
let name = "alice";
let greetings = `Hello,${name}!`;
console.log(greetings); //output:-Hello,alice!
// 2.multi-line string
//new method with back ticks
// eg:-
let multiline = `this is line one
                this is line two
                this is line three`;
//old method without backtics
let oldway = "this is line one.\nthis is line two.\n this is line three";
//properties of string:-
//length of string
str = "world is for the kings"
p = str.length;
// Accesssing string chracters
// eg:-
const username = "hello world";
const firastletter1 = username[0]//sqare bracket
const firastletter2 = username.charAt(0)//.charAt();
const firastletter3 = username.at(0)//.at();
// accessing string part:
//eg:-
// const username="hello world";
const part1 = username.slice(0, 5);//output---->hello  
const part2 = username.slice(-3);//output---->rld(-3 is considered 3 from behind and treated as upper bound of substring)
const part3 = username.substring(0, 4);//output---->hello(includes the character of last index)
const part4 = username.substring(-3, 4);//output---->hello(negative treated as 0)
// b.numbers-->8bytes
// c.bytes           
// d.boolean-->4 bytes
// e.undefined-->4 bytes
// f.null-->4 bytes
// g.bigint-->varies[for writing long integer values]
//eg:-
const num = 10n;
const num1 = Bigint(10n);
const num2 = Bigint("10");
console.log(typeof (num));
// h.symbol 
//eg:-
const s1 = Symbol("hello");
const s2 = Symbol("hello");

// 2.non-primirive data-types:-
// they are derived from primitive types
// they are usually mutable
// they store the actual value, they often store references to the memory location
// a.object
// b.array
// c.function
// d.date
// e.RegExp




//console is used for---->logging messages, executeing java script snippets for testing, learning purposes and error reporting




//hoisting and temporal dead zone

//question:-when does hoisting happens?
//answer:-hoisting only happpens when the variable is declared not initialized

//hoisting is by default behaviour of js to move the 
//declaration of the variable above the output statement  before the program has been executed

//temporal dead zone is only for let and const and not for var

//these moved due to hoisting
//var x=20;//only declaration is hoisted not the assingment or initialization

//let y=232;//only declaration is hoisted not the assingment or initialization

//let variables stay in temporal dead zone
//The Temporal Dead Zone(TDZ):-->is the period between the 
//start of a scope (like a block { } or function)
//and the point where a let or const variable is actually declared. 

console.log(x);//it shows:-un-defined
console.log(y);//it shows:-reference error(as they are hoisted but they stay in temporal dead zone)
console.log(z);//it shows:-reference error
var x = 20;
let y = 232;
const z = "desf";



// function hoisting
// eg:-
sayHello();
function sayHello() {
    console.log("hello")
}




// increament and decrement can be done ny ++,--,-,+
a = 10;
b = 10;
//types of operators:-
//1.arithimatic operator(+, -, /, %,*,**,++,--)
console.log(a + b);
console.log(a - b);
console.log(a * b);
console.log(a / b);//divide
console.log(a % b);//mod
console.log(a ** b);//exponential operator
console.log(++a);//increament of a
console.log(--b);//decreament of b
//2.assingment operator(=, /*, **=, -=, +=, %=, :, /=)
let x = 10;
x += 5;
console.log(x);// 15 → x = x + 5
x -= 3;
console.log(x);// 12 → x = x - 3 
x *= 2;
console.log(x);// 24 → x = x * 2 
x /= 4;
console.log(x); // 6 → x = x / 4 
x %= 4;
console.log(x); // 2 → x = x % 4 
x **= 3;
console.log(x);// 8 → x = x ** 3
//3.comparison operator(==, ===, !=,!==, >, <, >=, <=)
//== compares only value
//=== compares value and data-type
pp = 10;
ppp = "10"
console.log(pp == ppp);//true
console.log(pp === ppp);//false
//in camparison(===)value is checked first then the data type is checked 
//4.bitwise operator(&&, |, ^, (componet), >>, <<, >>>)
// here &, || oprator goes into bitwise operation and converts both the input to 
console.log(5 & 3);     // 1 → 0101 & 0011 = 0001  
console.log(5 | 3);     // 7 → 0101 | 0011 = 0111  
console.log(5 ^ 3);     // 6 → 0101 ^ 0011 = 0110 
console.log(~5);        // -6 → Bitwise NOT 
console.log(8 >> 2);    // 2 → Right shift 
console.log(3 << 2);    // 12 → Left shift 
console.log(-8 >>> 2);  // 1073741822 → Unsigned right shift




//5.logical operator(&&,||,!)
let ad = true;
let add = false;
console.log(ad && add);//output-->false
console.log(ad || add);//output-->true
console.log(!ad);//output-->false
//6.ternary operator(cond ? exp1:exp2)
let age = 18;
let status = (age >= 18) ? "adult" : "minor";
console.log(status)//output-->"adult"
//7.typof operator//tell us the type of a variable
console.log(typeof 42);//output--->"number"
console.log(typeof "hello");//output--->"string"
//8.instance operator
//It checks whether an object is an
//instance of a specific constructor(class or function).
//returns true and false
//syntax of operator--->console.log(typeof__any_operator_)
let arr = []
console.log(arr instanceof Array);//output--->true
console.log(arr instanceof Object);//output--->false
console.log(arr instanceof String);//output--->false



// input and output in the browser
// input:-prompt(), HTML Form Elements
// output:-alert(), console.log(), document.write(), document.getElementById("").innerHTML/innerText=""/

// conditional statements in java script
// if(condition){}
// if(condition){}else{}
// if(conditon1){if(condition2)}

// switch statemnt:-
let day = 0;
switch (expression) {
    case x:
        break
    case y:
        break
    case z:
        break
    default
}

// loops in java script
//for loop 
for (let i = 0; i <= 5; i++) {
    console.log(i)
}
//diffrent types of for loops 
// for....of loops(iterates over the values of iterable object)
let fruits = ["apple", "banana", "mango"]
for (let fruit of fruit) {
    console.log(fruit)
}
//for....in loops(itrates over the keys of an object)
let student = { name: "john", age: 20, grade: "A" }
for (let key in student) {
    console.log(key, ".", student[key])
}
// while loop
let i = 1;
while (i <= 5) {
    console.log(i)
    i++;
}
// do while loop
let p = 0;
do {
    console.log(p);
    p++;
}
while (p <= 5)

// loop control:- break, continue 
// break
for (let fruit of fruit) {
    console.log(fruit)
    if (fruit == "mango")
        break;
}
// continue
for (let fruit of fruit) {
    console.log(fruit)
    if (fruit == "mango")
        continue;
}



// arrays in javascript
const ar = new Array([1, 2, 3, 4, 5]);
// accessing array elements
// square bracket
console.log(ar[0])//output--->1
// .at()
console.log(arr.at(1))//output--->2
// adding elements in array
// square bracket
arr[2] = 20;//3rd element changed to 20
// push();
arr.push("john");//adds element at the end of array
// un-shift();
arr.unshift(235)//adds element in the beggining of array
// splice(); 
// syntax:-Array.splice(start-index, delet-count,element/s)
arr1 = ["hello", "world", "today", "is"];
arr1.splice(1, 0, "sachin", "virat");//here 0 means no element will be deleted
// array updated to ["hello", "sachin", "virat", "world", "today", "is"]// element updated before 1
// deleting elements form arrays
// by using pop:-
arr.pop();// removes element from the end of an array
// by using shift method:-
arr.shift();// removes element from start of the array
// by using delete keyword:-
delete arr[0]
// by using splice element:-
// arr1 = ["hello", "world", "today", "is"]; 
arr1.splice(1, 2)//deletes 2 elements starting from index 1
//array will be--->["hello", "is"]
// lenght of array:-
console.log(arr.length);
// Diffrent types of methods in an array:-
// .at()
arr.at(1)//return element from start of the array
arr.at(-1)//returns element from end of the array

// .push()
arr.push(3, 4)// adding one or more elemets to the end of the array

// .pop()
arr.pop()// removes the last element from array

// .unshift()
arr.unshift(1, 2)// adding one or more elements at the beggning of the array//1,2 are the elements we are adding at the beggining of the array

// .shift()
arr.shift()// removes the first element  

// .concat()
arr.concat(arr1)// for merging two arrays

// .indexOf();
// array.indexOf(element of the array to be checked);
arr.indexOf(5)// for getting index of an element if not then returns -1

// .lastindexOf()
arr.lastIndexOf(5)// returns the last index of the elment found in the array

// .includes()
pop1 = arr.includes(/*element to be checked*/);//performes ===, returns true if element is found in array or false if not found

//.find()--->returns first element that satisfies the condition in callback-function
arr033 = [5, 12, 8, 130, 44];
console.log(arr033.find(el => el > 10));//output--->12

// .slice()
console.log(arr.slice());//returns copy of the portion of the slected part of array

// .sort()
console.log(`this function returns sorted array ${arr.sort()}`);// returns the sorted array

// .reverse()
arr.reverse()// reverse the order of array

// .toSorted(conpareFn)---returns the copy of sorted array
a12rr = [21, 24, 143, 332, 312]
pp022 = a12rr.toSorted((a, b) => b - a);
console.log(p022);//output--->[21,24,143,312,332]//ascending order

// .toReversed()
console.log(arr.toReversed());// returns copy of reversed array
// diffrent methods of iteration in arrays:-

// .forEach(callback(current_value,index,array));
let fruit12 = ["cherry", "mago", "watermelon"];
fruit12.forEach(function (item) { console.log(item); });
// output---> cherry mango watermelon

// .map()
let nums432 = [1, 24, 4, 32, 4, 32, 34];
let squares = nums432.map(x => x * x);
console.log(squares);// output--->[1,24,4,32,4,32,34]

// .filter()
let big = nums432.filter(n => n > 10);// output--->[24,4,32,32,34](elements less than 10 are removed)

// .reduce()
let summm = nums432.reduce((acc, curr) => acc + curr, 0);//returns the total sum of elements of array

// .every(callback(element,index,array),thisArg);
let aerges = [20, 43, 12, 39, 2];
let alfefw = aerges.every(age => age >= 18);// output-->false(as all the elements dont pass the test case) 

// .some(callback(element,index,array),thisArg);
let fgegeg = aerges.some(age => 18 >= 18);//output--->true(as one or more of the element staifies the condition)

// .findIndex(callbackFn)
// syntax--->array.findIndex()
console.log(aerges.findIndex(x => x === 7));// returns the index of the first element that satifies the condition in the callback



// copying of an array
// <----shallow copying---->//for nested arrays or objects
// 1.spread operator
// let aerges = [20, 43, 12, 39, 2];
var newarray = [aerges];
// 2.from();
var newarray = Array.from(oldarray)
//  3.slice();
var newarray = oldarray.slice();
// 4.concact();
var newarray = [].concact(oldarray);
// 5.map();
var newarray = oldarray.map(element => element);
// if we have to add +1 in the new array by suing mapping
var newarray = oldarray.map(element => element + 1);

// <----deep copying---->//not used for nested arrays or nested objects
// gives complete independence between old and new array
// JSON serialization
// syntax---->JSON.parse(JSON.stringify(oldarray));
// data lose their type--->converted to plain strings

// MODREN structured cloning
// Syntax--->structuredClone(oldArray);
// library solutions --->lodash
// syntax--->_.cloneDeep(oldArray);



// callback function
// it is a function passed as an argument to another function
// it is executed after some kind of event
function greet(callback) {
    console.log("hello wrold hof");
    callback();
}
hof(fun){ } //it is a higher order function}
// parameter - alreadty defined
// argumtemts - actual value given to the function

// ?.map()
// returns a neew array

// ?.filter()

// forEach(callback)
const arr = [1, 32, 43, 234, 53, 43];
arr.forEach((value, index, arr) => {
    console.log(value);
})

// for callback hell dealing we use the Promises
// Promises --> microtasks()
// notify the user for the success failure pending fullfille or resolved

// IIFE immediate invocation function expression
// {
//     function() {
//         var a = 10;
//         console.log("Hi");
//     }
// }
// example use case
// for(var i=0; i<=5; i++){
//     (function() {
//         setTimeout(()=>{
//             var a = 10;
//             console.log("Hi");
//         },2000)
//     })(i);
// }

// Closure - A closure is a function that remembers the variables 
// from its outer scope even after that outer scope has finished executing.
function outer() {
    let counter = 1;
    function inner() {
        console.log(counter);
        counter++;
    }
    return inner;
}
const num01 = outer();
num01()
num01()
num01()

// 1. Throttling
// 2. Debouncing