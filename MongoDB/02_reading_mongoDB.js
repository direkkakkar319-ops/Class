use("ecommerce");

// name
// db.products.find({ "name": "Wireless Mouse" });

// category
// db.products.find({ "category": "Electronice" });

// Comparison
// 1. greater than
db.products.find({ price: { $gt: 1000 } })
// 2. greater than equal to 
db.products.find({ price: { $gte: 1000, $lte: 5000 } })

// Logical Operators
db.products.find({
    $or: [{ category: "Electronics" }, { stock: { $lt: 50 } }
    ]
})

// the id of the products will not be shown
db.products.find({}, { name: 1, price: 1, _id: 0 })

// limiting the number of output and there order
// -1 will give in decreasing order
// limit 2 will give only two products
db.products.find().sort({ price: -1 }).limit(2)