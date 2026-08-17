/**
make a strore arrrat then store the ip in it then we will 
store the start time means when the first time the request was
send then we will subtract the current time from the start after 
every request if the number of reuests are still left then the 
request will be send to the server else we will say `you have reached the rate limit`
**/

const express = require('express')
const app = express()
const PORT = 3000
const rateLimitWindow = 10 * 1000
const maxRequests = 5;
store = {}

function rateLimiter(req, res, next) {
    const ip = req.ip
    const now = Date.now();

    if (!store[ip]) {
        stor[ip] = {
            count: 1,
            startTime: now
        }
        return next();
    }
}

const elapsed = Date.now() - store[ip].startTime;

if (elapsed < rateLimitWindow) {
    if (store[ip].count >= maxRequests) {
        return req.status(429).json({
            message: "too many requests. Try again later"
        })
    }
    store[ip].count++;
}
else {
    store[ip] = {
        count: 1,
        startTime: now
    }
    next();
}

app.use(rateLimiter);

app.get('/', (req, res) => {
    res.send("Hello API");
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});