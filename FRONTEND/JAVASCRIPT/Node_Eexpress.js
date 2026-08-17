// importing express library in js file
const express = require("express");
// here app is the central object that stores the express application instance
const app = express();



// Middleware
// 
// regestration of built-in middleware that will parse JSON request bodies and populates req.body
// we use this when we expect clints to send JSON
app.use(express.json());
// regestration of a coustom middleware function
app.use((req, res, next) => {
    console.log(req.method, req.url);// it logs HTTP method and path to ou Node.js server then Node.js prints it in stdout
    // passing control to next middleware or route
  next();// if it is not called the request will hang as it tells express that it is done and next middleware or route handler can continue further
});



// Route Handler
//  
// defines a route handler for request by user here it is GET further requesting mathcing path 
app.get("/users/:id", async (req, res) => { 
  // async used so we can use await in our function
  const userId = req.params.id;// extracts id and stores it
  const user = await fakeDB.getUserById(userId);
  // here await pauses fakeDB.getUserById.. till it resolves but it does not block 
  // other processes due to the featuer of Node.js that is non-blocking model
  if (!user) return res.status(404).send("User not found");
  // if user is not found then error '404' is send
  res.json(user);
  // it stringifys the object
});



// Start server
// 
// callback function will run once the server is ready and simply logs a message
app.listen(3000, () => console.log("Server running on port 3000"));



// Fake database
const fakeDB = {
  async getUserById(id) {
    return { id, name: "John Doe" };
  },
};
