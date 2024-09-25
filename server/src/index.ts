import express from 'express';
import path from 'path';
import cors from 'cors';

const app = express();
const port = 3000;

app.use(cors());
app.use(cors({ origin: 'http://localhost:3000' }));


// Serve static files from the 'public' folder
app.use(express.static(path.join(__dirname, '../src')));

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
