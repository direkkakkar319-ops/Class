// const playground = document.getElementById('playground');

// const magicalOrb = document.createElement('div');
// magicalOrb.textContent = 'hello';
// playground.append(magicalOrb);




// const scrollWisdom = document.createElement('p');
// playground.append(scrollWisdom);
// scrollWisdom.innerText = 'sex ssux karna';
// console.log(scrollWisdom.innerText);
// scrollWisdom.textContent = 'sex ssux karna';
// console.log(scrollWisdom.textContent);




// console.log(playground.innerText);
// // only shows the visible text 
// console.log(playground.textContent);
// //shows both the visible and invisible text of the html page




// const spellBook = document.createElement('div');
// spellBook.innerHTML = '<p>Spells include:<strong>Levitation</strong> and <em>Invisibility</em>!</p>';
// playground.append(spellBook);
// playground.innerHTML = '<p>Spells include:<strong>Levitation</strong> and <em>Invisibility</em>!</p>'
// console.log(playground.textContent);//return the text we wanted to write in the html file
// console.log(playground.innerHTML);//return the tags with the text we did not want the user to see  

// const userInput = "<img src='x' onerror='alert(\'Hacked!\')>";
// playground.innerHTML = userInput;





// const temp = document.createElement('p');
// temp.textContent = "Now you see me...";
// playground.append(temp);
// temp.remove();
// playground.removeChild(temp);




// const fruitBasket = document.createElement('div');
// fruitBasket.innerHTML = '<p>Apple</p><p>Bananas</p><p>Cherry</p>';
// playground.append(fruitBasket);
// // when we dont know how many paragraphs there are
// // keep on removing the first element from the div till there are no elements left in the div
// while(fruitBasket.firstChild){
//     fruitBasket.removeChild(fruitBasket.firstChild);
// }




// const magicWord = document.createElement('div');
// magicWord.setAttribute('id', 'wand1');
// magicWord.setAttribute('class', 'magical-item wand');
// magicWord.textContent = "magic wand";
// playground.append(magicWord);
// console.log(magicWord.getAttribute('id'));
// console.log(magicWord.getAttribute('class'));
// // changing name of id and class
// magicWord.id="lol";
// magicWord.className="fuckn yoiu"
// console.log(magicWord.getAttribute('id'));
// console.log(magicWord.getAttribute('class'));




// const secretscrool = document.createElement('div');
// secretscrool.id = "secretscrool";
// secretscrool.dataset.spell = 'invisibility';
// secretscrool.dataset.components = 'moonlight, shadow essence,Evil thoughts';
// secretscrool.textContent = 'Ancient Spell Scroll';
// playground.append(secretscrool);
// console.log(secretscrool.dataset.spell);
// console.log(secretscrool.dataset.components.split(','));




// const shapeLifter = document.createElement('div');
// shapeLifter.textContent = "shapelifter";
// playground.append(shapeLifter);
// shapeLifter.classList.add("magical", "creature");
// console.log("initial classes:", shapeLifter.className);
// shapeLifter.classList.remove("creature");
// shapeLifter.classList.add("hello");
// console.log("initial classes:", shapeLifter.className);
// shapeLifter.classList.toggle('invisible');
// console.log("initial classes:", shapeLifter.className);
// console.log(shapeLifter.classList.contains('invisible'));
// shapeLifter.classList.replace("invisible","world");
// console.log("initial classes:", shapeLifter.className);
// console.log(shapeLifter.classList.contains('invisible'));
// console.log(shapeLifter.classList.item(1));




// const enchanted = document.createElement('div');
// enchanted.textContent = 'diamond';
// enchanted.style.fontSize='50px';
// enchanted.style.transition = 'all 2s';
// playground.append(enchanted);
// setInterval(()=>{
//     enchanted.style.transform = `rotate(${Math.random()*360}deg)`;
//     enchanted.style.color = `hsl(${Math.random()*360}. 100%, 50%)`;
// }, 2000);




// const magicButton = document.createElement('button');
// magicButton.textContent = "cast spell";
// playground.append(magicButton);
// magicButton.addEventListener('click', ()=>{
//     alert("magic sparkles fill the air");
// })
// magicButton.addEventListener('mouseover', (event)=>{
//     event.target.style.backgroundColor = 'purple';
// });
// magicButton.addEventListener('mouseout', (event)=>{
//     event.target.style.backgroundColor = '';
// });
// magicButton.removeEventListener('click')




// const spellList = document.createElement('ul');
// playground.append(spellList);
// function addSpell(spellName){
//     const spell = document.createElement('li');
//     spell.textContent = spellName;
//     const removeButton = document.createElement('button');
//     removeButton.textContent = 'Remove';
//     removeButton.addEventListener('click', () => spell.remove());
//     spell.append(removeButton);
//     spellList.append(spell);
// }
// addSpell('fireball');
// addSpell('frostNove');4




// const parentElement = document.createElement('div');
// const childElement1 = document.createElement('p');
// const chileElement2 = document.createElement('span');
// parentElement.append(childElement1, chileElement2);
// playground.append(parentElement); 
// console.log(parentElement.firstChild);
// console.log(parentElement.lastChild);
// console.log(childElement1.nextElementSibling);
// console.log(chileElement2.previousSibling);
// console.log(childElement1.parentElement);




// const fragment = document.createDocumentFragment();
// for(let i = 0; i < 10; i++){
//     const magcialItem = document.createElement('li');
//     magcialItem.textContent = `Magical Item ${i+1}`;
//     fragment.append(magcialItem);
// }
// const spellList = document.createElement('ul');
// playground.append(spellList);
// spellList.append(fragment);




// const template = document.createElementById('wizard-template');
// function createWizard(name, specialty){
//     const wizardElement = template.content.cloneNode(true);
//     wizardElement.querySelector('.wizard-name').textContent = name;
//     wizardElement.querySelector('.wizard-specialty').textContent = specialty;
//     playground.append(wizardElement);
// }
// createWizard('Merlin', 'Time Magic');
// createWizard('Gandalf', 'Fireworks');



// local storage
// localStorage.setItem();
// localStorage.getItem();
// localStorage.removeItem();
// localStorage.clear();
// promises in java script




// getting object from local storage
// const element = JSON.parse(localStorage.getItem("user"));
// when we get any item from local storagr then it is in json format so we have to convert it to normal format using JSON.parse()



// Promise
let success = true;
const promise = new Promise((resolve, reject) => {
    if (success) {
        resolve("chud gaye guru");
    }
    else {
        reject("lode lag gaye");
    }
});
promise
    .then(result => {
        console.log(result)
    })
    .catch(error => {
        console.log(error)
    });




//async function
async function demo() {
    return 10;
}
demo()
    .then(value => console.log(value));




//async await function 
function getData() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("data loaded");
        }, 2000);
    });
}
async function showData() {
    console.log("start");
    const result = await getData();//waits here
    console.log(result);
    console.log("end");
}
showData();




// api fethcing
async function fetchUsers() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");
        const users = await response.json();
        console.log(users);
    }
    catch (error) {
        console.log(error);
    }
}
fetchUsers();




// using promises
fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(error => console.log(error))




// call stack 
function one() {
    two();
}
function two() {
    three();
}
function three() {
    console.log("hello world");
}
one();
// calling one()-->two()-->three()
// execution three()-->two()-->one()




// constructor function
function user(name) {
    this.name = name
}
let u = new user("Direk");
console.log(u);




// factory function
function createUser(name) {
    return { name }
}
let u2 = createUser("Direk");
console.log(u2);




// math functions
var arr = [9, 432432, 432, 32432, 234]
// .random();
let random = Math.floor(Math.random() * (Math.max(arr) - Math.min() + 1)) + Math.min(arr)
console.log(random);
// .sqrt()
console.log(Math.sqrt(Math.min(arr)));




// HOF methods
var arr = [9, 432432, 432, 32432, 234]
// .map()
ar_map = arr.map(x => x * 2);
console.log(ar_map);
// .filter()
arr_filter = arr.filter(x => x > 200);
console.log(arr_filter);
// .reduce();




// copying in JS
var arr = [9, 432432, 432, 32432, 234]
arr_reduce = arr.reduce((a, b) => a + b);
console.log(arr_reduce);
// shallow copy
let shallow = [...arr];
console.log(shallow);
// deep copy
let deep = JSON.parse(JSON.stringify(arr));
console.log(deep);




// date() functions
console.log(new Date().getFullYear());
console.log(new Date().getHours());
console.log(new Date().getDate());
console.log(new Date().getDay());
console.log(new Date().getMonth());
console.log(new Date().getTime());


// // asynchronous JS
// setTimeout()
console.log("hello");
setTimeout(() => {
    console.log("world");
}, 2000);
console.log("geeks")
// setInterval()
let x = 1;
let interverId = setInterval(() => {
    console.log(x);
    if (x >= 10) {
        clearInterval(interverId);
    }
    x++;
}, 2000)


// normal execution
const parent = document.getElementById("parent");
const child = document.getElementById("child");
parent.addEventListener('click', () => {
    console.log("Parent handler")
});
child.addEventListener('click', () => {
    console.log("Child handler 1");
});
child.addEventListener('click', () => {
    console.log("Child handler 2");
});
// output
// Child handler 1
// Child handler 2
// Parent handler


// event.stopPropagation()
const parent1 = document.getElementById("parent1");
const child1 = document.getElementById("child1");
parent1.addEventListener("click", () => {
    console.log("Parent clicked");
});
child1.addEventListener("click", (e) => {
    e.stopPropagation();
    console.log("Child handler 1");
});
child1.addEventListener("click", () => {
    console.log("Child handler 2");
});
// output:-
// Child handler 1
// Child handler 2


// event.stopImmediatePropagation()
const parent2 = document.getElementById("parent2");
const child2 = document.getElementById("child2");
parent2.addEventListener('click', () => {
    console.log("Parent handler");
})
child2.addEventListener('click', (e) => {
    e.stopImmediatePropagation();
    console.log("Child handler 1");
});
child2.addEventListener('click', () => {
    console.log("Child handler 2");
})
// output:-
// Child handler 1

let name = prompt("enter your name");
console.log(name);

function Person(name, age) {
    this.name = name
    this.age = age
}
Person.prototype.greet = function () {
    console.log(`hello my name ${this.name}`);
}
const person1 = new Person("Pratik Lodu", 17);
person1.greet();


// capturing
// bubbling
// call back function
// e.stopImmediatePropagation()
// e.stopPropagation()