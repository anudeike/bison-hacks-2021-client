require('dotenv').config()
const express = require("express")
const app = express()
const cors = require("cors")
fs = require('fs');

// use cors
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

const port = process.env.PORT || 6060;

app.get('/', (req, res) => {
    res.send('Hello World!')
})

app.get('/all-tweets', (req, res) => {
    // get the file information
    // get the slice that you want
    let amount = req.query.count || 10
    let raw = fs.readFileSync('all_tweets.json')

    let output = JSON.parse(raw)
    output = output.slice(0, amount)

    res.status(202).json(output);
})

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
})