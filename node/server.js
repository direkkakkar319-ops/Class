const express = require("express");
const connectDB = require("./db");
const User = require("./models/User");
const Items = require("./models/Items");

const app = express();

connectDB();

app.get("/", async (req, res) => {

    const user = await User.create({
        name: "Direk",
        age: 21
    });

    res.send(user);
});

app.listen(5000, () => {
    console.log("Server started on port 5000");
});