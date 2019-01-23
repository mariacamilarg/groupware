DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  online BOOLEAN NOT NULL CHECK (online IN (0,1)) DEFAULT 0
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  last_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  programming_language TEXT NOT NULL,
  being_updated BOOLEAN NOT NULL CHECK (online IN (0,1)) DEFAULT 0,
  FOREIGN KEY (author_id) REFERENCES user (id)
);