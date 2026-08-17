// Node js event
// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// emitter.on('greet', () => {
//     console.log("Hello, event triggered!")
// });

// emitter.emit('greet');

// output
// Hello, event triggered!


// ---------------------------------------------------------

// Event vs Sync Execution Order
// shows the events are synchronous by default

// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// emitter.on('start', () => {
//     console.log('Event 1');
// });

// console.log('Before emit');
// emitter.emit('start');
// console.log('After emit');

// output
// Before emit
// Event 1
// After emit

// ---------------------------------------------------------

// setTimeout vs EventEmitter
// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// emitter.on('task', () => {
//     console.log('Event executed');
// })

// setTimeout(() => {
//     console.log('Timout Done');
// }, 0);

// emitter.emit('task');
// console.log("End")

// output
// Event executed
// End
// Timout Done
// ---------------------------------------------------------


// Async Inside Event (Misleading Order)

// const EventEmitter = require('events');
// const emitter = new EventEmitter();

// emitter.on('process', async () => {
//     console.log("Start");

//     await new Promise(res => setTimeout(res, 0));

//     console.log("End");
// });

// emitter.emit('process');

// console.log("Outside");

// output
// Start
// Outside
// End
// ---------------------------------------------------------

/*
Priority Order in Node.js
Highest Priority ot Lowest Priority
1. Synchronous code
2. process.nextTick() queue
3. Promise microtasks (.then, catch, finally)
4. Timers phase -> setTimeout, setInterval
5. Check phase -> setImmediate
*/
// Start End NextTick Promise Timeout Immediate
// console.log('Start');

// setTimeout(() => console.log('Timeout'), 0);

// setImmediate(() => console.log('Immediate'));

// process.nextTick(() => console.log('NextTick'));

// Promise.resolve().then(() => console.log('Promise'));

// console.log('End');

// let count = 0;

// function recursive() {
//     if (count < 5) {
//         count++;
//         console.log(count);

//         process.nextTick(recursive);
//     }
// }

// recursive();
// setTimeout(() => console.log('Timeout'), 0);

// output
// Start
// End
// 1
// NextTick
// 2
// 3
// 4
// 5
// Promise
// Timeout
// Timeout
// Immediate


// ---------------------------------------------------------

// process.nextTick() can block the event loop
// Dangerous if misused

// console.log('Start');
// process.nextTick(() => {
//     console.log('NextTick 1');
//     process.nextTick(() => console.log('NextTick 2'));
// });
// Promise.resolve().then(() => {
//     console.log('Promise 1');
//     process.nextTick(() => console.log('NextTick inside Promise'));
// });
// console.log('End');

//output
// Start
// End
// NextTick 1
// NextTick 2
// Promise 1
// NextTick inside Promise


// ---------------------------------------------------------

// const express = require('express');
// const app = express();
// const PORT = 3000

// app.use(express.json)

// let memory = [];
// let idCounter = 1;


// // Creating
// app.post('/items', (req, res) => {
//     const name = req.body;
//     const newItem = {
//         id: idCounter++,
//         name
//     }
//     memory.push(newItem.json())
// })


// // Fetching
// app.get('/items', (req, res) => {
//     res.json(memory)
// })

// // Fetching by id
// app.get('items/:id', (req, res) => {
//     const id = parseInt(req.params.id);
//     const item = memory.find(i => i.id == id);
//     res.json(item);
// })

// // update the items 
// app.put('/item/:id', (req, res) => {
//     const id = parseInt(req.params.id)
//     const item = memory.find(i => i.id == id)
//     const name = { ...req.body }

//     res.json(item)
// })

// // Deleting
// app.delete('items/:id', (req, res)=>{
//     const id = parseInt(req.params.id);
//     const index = memory.findIndex(i=>i.id==id)
    
//     if(index ==-1){
//         return res.status(404).json({error:'Item not found'})
//     }

//     const deleteItem = items.splice(index, 1)
    
//     res.json(deleteItem[0]);
// })

// app.listen(PORT, () => {
//     console.log(`Server running on http://localhost:${PORT}`);
// });

// ---------------------------------------------------------