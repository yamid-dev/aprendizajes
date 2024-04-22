const express = require('express');
const mongoose = require('mongoose');
const Book = require('./Book'); // Asegúrate de que la ruta sea correcta
const { MongoClient, ObjectId } = require('mongodb');
const path = require('path');
const bodyParser = require('body-parser');

const app = express();
const PORT = 1111;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public')); // Middleware para servir archivos estáticos

const MONGO_URI = 'mongodb://127.0.0.1:27017/books'; // Cambia por tu conexión MongoDB
const COLLECTION_NAME = 'books'; // Cambia por el nombre de tu colección

// Ruta para servir el archivo HTML en la ruta raíz
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});

// Ruta para obtener los datos de la base de datos
app.get('/books', async (req, res) => {
  try {
    const client = await MongoClient.connect(MONGO_URI);
    const db = client.db();
    const collection = db.collection(COLLECTION_NAME);

    const result = await collection.find({}).toArray();

    res.json(result);

    client.close();
  } catch (error) {
    console.error('Error al conectar con MongoDB:', error);
    res.status(500).json({ error: 'Error interno del servidor' });
  }
});

// Ruta para obtener una imagen por ID
app.get('/image/:id', async (req, res) => {
  try {
    const book = await Book.findById(req.params.id);
    if (!book || !book.imagen.data) {
      res.status(404).send('No image found');
    } else {
      res.set('Content-Type', book.imagen.contentType);
      res.send(book.imagen.data);
    }
  } catch (error) {
    res.status(500).send('Server error');
  }
});

app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
