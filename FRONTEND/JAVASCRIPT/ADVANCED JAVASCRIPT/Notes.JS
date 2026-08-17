// GLOBAL EXECUTION CONTEXT(GEC)
// When JS starts, it creates the Global Execution Context.
// What happens?
// Two phases
// Memory Creation (Hoisting)
// Execution

console.log(a);
var a = 10;

// Memory phase
// a → undefined


// Execution phase
// console.log(a) → undefined
// a = 10
// ✅ Console output
// undefined


let b = 20;
console.log(b);
// let is stored in Temporal Dead Zone (TDZ)
// Access before declaration → ❌ error


function greet() {
  console.log("Hello");
}
greet();
// Functions are fully hoisted


console.log(greet);
function greet() {}
// ✅ Logs the function definition


this === window
// ✅ true (in browser global scope)


console.log(window);
// Global variables attach to window if declared with var



// FUNCTION EXECUTION CONTEXT(FEC)
// Created every time a function is called

function add(x, y) {
  let sum = x + y;
  return sum;
}
add(2, 3);
// Inside function add():
// 1. New memory space
// 2. Parameters initialized
// 3. Local variables stored

// Execution order
// 1. GEC
// 2. FEC for add();
// 3. Return value
// 4. FEC destroyed

// Console explanation
// Nothing prints unless logged, but memory + execution happens



// CALL STACK (How JS Executes Code)
// LIFO->Last In First Out

function one() {
  two();
}
function two() {
  three();
}
function three() {
  console.log("Done");
}
one();
// Call Stack
// 1. three()
// 2. two()
// 3. one()
// 4. global()

// Console Tab
// Done

// Stack Overflow
function infinite() {
  infinite();
}
infinite();
// arduino 
// Maximum call stack size exceeded



// SINGLE THREADED JAVASCRIPT
// JS does ONE thing at a time

console.log("A");
console.log("B");
// CSS
// A
// B



// WEB APIs (BROWSER POWER)
// Provided by browser, NOT JS
// setTimeout
// DOM
// fetch
// events

console.log("Start");
setTimeout(() => {
  console.log("Timeout");
}, 0);
console.log("End");
// Execution
// 1. Start
// 2. End
// 3. Timeout



// CALLBACK QUEUE VS MICROTASK QUEUE
// Priority:
// Microtask Queue > Callback Queue

setTimeout(() => console.log("timeout"), 0);
Promise.resolve().then(() => console.log("promise"));
console.log("sync");
// Output
// 1. sync
// 2. promise
// 3. timeout



// EVENT LOOP (EXECUTION ORDER)
// Order:-
// 1. Call Stack
// 2. Microtask Queue
// 3. Callback Queue

console.log("1");
setTimeout(() => console.log("2"), 0);
Promise.resolve().then(() => console.log("3"));
console.log("4");
// Console Tab
// 1
// 4
// 3
// 2



// CALLBACK PATERN & LIMITATIONS
// Callback Example
function fetchData(cb) {
  setTimeout(() => {
    cb("Data loaded");
  }, 1000);
}
fetchData(console.log);
// Callback Hell is formed 
// a(() => {
//   b(() => {
//     c(() => {
//       d();
//     });
//   });
// });
// ❌ Hard to read
// ❌ Hard to debug
// ❌ Error handling nightmare



// PROMISES (STATES & CHAINING)
// Promise States
// pending
// fulfilled
// rejected

const p = new Promise((resolve, reject) => {
  resolve(10);
});
p.then(v => v * 2).then(v => console.log(v));
// Console
// 20

// Rejection
Promise.reject("Error").catch(err => console.log(err));



// ERROR HANDLING IN PROMISE
Promise.resolve()
.then(() => {
    throw new Error("Oops");
})
.catch(e => console.log(e.message));



// ASYNC & AWAIT
// Cleaner syntax over promises

async function test() {
  return 5;
}
test().then(console.log);

async function fetchData() {
  const res = await Promise.resolve("Done");
  console.log(res);
}
fetchData();



// TRY & CATCH
// Works with sync + async

try {
  JSON.parse("{bad}");
} catch (e) {
  console.log("Invalid JSON");
}

// Async try-catch
async function run() {
  try {
    await Promise.reject("Fail");
  } catch (e) {
    console.log(e);
  }
}
run();

// DEBOUNCING
// Execute after delays stops

// Use case
// Search input
// Resize events

function debounce(fn, delay) {
  let timer;
  return function () {
    clearTimeout(timer);
    timer = setTimeout(fn, delay);
  };
}
// there will not be any output
// 0ms   → setTimeout registered
// 1ms   → clearTimeout called
// 2000ms → ❌ nothing happens



// Throttling
// Execute once per time interval

// Use case
// Scroll
// Button spam protection

function throttle(fn, limit) {
  let flag = true;
  return function () {
    if (!flag) return;
    flag = false;
    fn();
    setTimeout(() => flag = true, limit);
  };
}



// PERFORMANCE OPTIMIZATON
// Debounce / throttle
// Avoid deep DOM access
// Memoization
// Async operations

const memo = {};
function square(n) {
  if (memo[n]) return memo[n];
  return memo[n] = n * n;
}



// TYPE COERCION(IMPLICIT VS EXPLICIT)
// Implicit type coercion
"5" + 2   // "52"
"5" - 2   // 3
true + 1  // 2

// Explicit type coercion
Number("5") + 2
String(5)
Boolean(1)

// Weird Ones
[] + []     // ""
[] + {}     // "[object Object]"
{} + []     // 0 (browser dependent)