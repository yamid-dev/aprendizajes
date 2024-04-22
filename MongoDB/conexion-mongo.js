const mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/books', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'Error de conexión a la base de datos:'));
db.once('open', async () => {
  console.log('Conexión exitosa a la base de datos');

  const booksSchema = new mongoose.Schema({
    Nombre: {
      type: String,
      required: true
    },
    Año: {
      type: String,
      required: true
    },
    imagen: {
      data: Buffer,
      contentType: String
    }
  });
  

  const Book = mongoose.model('Books', booksSchema);
  module.exports = Book;

  try {
    const books = await Book.find({});
    console.log('Libros encontrados:', books);
  } catch (err) {
    console.error('Error al buscar usuarios:', err);
  } finally {
    mongoose.connection.close();
  }
});
