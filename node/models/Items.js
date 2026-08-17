// import of exprerss framwork for creating the backend server and the rest api 
const express = require('express');
// creating express instance to define the middleware and routes
const app = express();
// port whare the server will run 
const PORT = 3000;

/*
MIDDLEWARE
this converts the incoming data to javascript object
eg
{
    "name":"Laptop"
}
to
req.body = { name:"Laptop" }
*/
app.use(express.json());

/*
IN MEMORY DATABASE
*/
let items = [];
// used to generate unique IDs for every new item
let idCount = 1;

/*
CREATING NEW ITEM
*/
app.post('/items', (req, res) => {
    const { name } = req.body;
    const newItem = {
        id: idCount++,
        name
    };

    items.push(newItem)
    // 201 means creation of new item was successfull
    res.status(201).json(newItem);
});

/*
GET ALL ITEMS
*/
app.get('/items', (req, res) => {
    res.json(items);
})

/*
GET ITEM BY ID
*/
app.get('/items', (req, res) => {
    // we will first take the id 
    const id = parseInt(req.params.id)
    // now that id will be used to find the items
    const item = items.find(i => i.id == id)

    if (!item) {// as the item was not found we send error response
        return res.status(404).json({
            error: "Item not found"
        });
    }

    res.json(item);
});

/*
UPDATE ITEM
*/
app.put('items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const item = items.find(i => i.id == id)

    if (!item) {//if not found then we will return the not found error
        return res.status(404).json({
            error: "item not found"
        })
    }

    item.name = req.body.name;
    res.json(item)
})

/*
DELETE
*/
app.delete('items/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const index = items.findIndex(i => i.id == id)

    if (index == -1) {
        return res.status(404).json({
            error: "Item not found"
        });
    }

    // first parameter:
    // index position
    const deleteItem = items.splice(index, 1);

    // second parameter:
    // number of items to remove
    res.json(deleteItem[0]);
});

/*
START SERVER
*/
app.listen(PORT, () => {
    console.log(`Server running on http://localhost${PORT}`);
})