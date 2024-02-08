const mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/books', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'Error de conexión a la base de datos:'));
db.once('open', async () => {
  console.log('Conexión exitosa a la base de datos');

  // Define el esquema del usuario
  const booksSchema = new mongoose.Schema({
    name: String,
    year: String,
    // Otros campos del usuario
  });

  // Crea el modelo del usuario
  const Book = mongoose.model('Books', booksSchema);

  try {
    // Ejemplo de consulta a la colección de usuarios utilizando await
    const books = await Book.find({});
    console.log('Libros encontrados:', books);
  } catch (err) {
    console.error('Error al buscar usuarios:', err);
  } finally {
    // Cierra la conexión después de la consulta
    mongoose.connection.close();
  }
});
