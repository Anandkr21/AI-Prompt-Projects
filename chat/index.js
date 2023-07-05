const express = require('express');
const app = express()

require('dotenv').config;

app.use(express.json())
const port = process.env.PORT || 6000
app.get('/', (req,res) =>{
    res.send('hello')
})

app.listen(port, () =>{
    console.log('run');
})