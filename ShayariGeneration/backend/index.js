const express = require('express');
const axios = require('axios');

require('dotenv').config();
const cors = require('cors'); // Add this line

const app = express();
const port = process.env.PORT || 5000;

app.use(express.json());
app.use(cors());

// app.get('/', (req, res) => {
//     res.send('hello')
// })

app.get('/shayari', async (req, res) => {
    try {
        const keyword = req.query.keyword;
        const response = await axios.post('https://api.openai.com/v1/engines/text-davinci-003/completions', {
            prompt: `give Shayari on ${keyword}`,
            max_tokens: 100,
            temperature: 0.7,
            n: 1
        }, {
            headers: {
                'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
                'Content-Type': 'application/json'
            }
        });

        const shayari = response.data.choices[0].text.trim();
        res.json({ shayari });
    } catch (error) {
        console.error('Error:', error.response.data);
        res.status(500).json({ error: 'Something went wrong' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port http://localhost:${port}`);
});