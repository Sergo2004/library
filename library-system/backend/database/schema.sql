CREATE TABLE libraries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    phone VARCHAR(50)
);

CREATE TABLE readers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    birth_date DATE,
    phone VARCHAR(50),
    email VARCHAR(255),
    registration_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(50) UNIQUE,
    publication_year INTEGER,
    category VARCHAR(100),
    copies_total INTEGER DEFAULT 1,
    copies_available INTEGER DEFAULT 1,
    library_id INTEGER REFERENCES libraries(id)
);

CREATE TABLE issues (
    id SERIAL PRIMARY KEY,
    reader_id INTEGER REFERENCES readers(id),
    book_id INTEGER REFERENCES books(id),
    issue_date DATE DEFAULT CURRENT_DATE,
    return_date DATE,
    actual_return_date DATE,
    fine NUMERIC(10,2) DEFAULT 0
);

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    position VARCHAR(100),
    login VARCHAR(100) UNIQUE,
    password_hash TEXT,
    library_id INTEGER REFERENCES libraries(id)
);
