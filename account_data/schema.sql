-- sqlite3 accounts.db < schema.sql

DROP TABLE IF EXISTS users;

CREATE TABLE accounts (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    from_username TEXT NOT NULL,
    from_password TEXT NOT NULL,
    to_username TEXT NOT NULL,
    to_password TEXT NOT NULL
);
INSERT INTO accounts VALUES(1,'epam.test.email.from','Epam@test1','epam.test.email.to','Epam@test1');