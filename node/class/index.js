// rest api to manage a list of items

const express = require('express')
const app = express()
const PORT = 3000

// parsing
app.use(express.json())

let memory = [];
let idCounter = 1;

// creating item
app.post('/items', (req, res) => {
    const name = req.body;

    const newItem = {
        id: idCounter++,
        name
    }

    memory.push(newItem.json())
});

// fetchig itm
app.get('/items', (req, res) => {
    res.json(memory)
})

// get item by id
app.get('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const item = memory.find(i => i.id === id);

    res.json(item);
})

// update the item
app.put('/items/:id', (req, res) => {
    const id = parseInt(req.params.id)
    const item = memory.find(i => i.id == id)

    const name = { ...req.body }
    res.json(item)
})

app.delete('/items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const index = memory.findIndex(i => i.id === id);

    if (index === -1) {
        return res.status(404).json({ error: 'Item not found' });
    }
    
    const deletedItem = items.splice(index, 1);
    
    res.json(deletedItem[0]);
})

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});