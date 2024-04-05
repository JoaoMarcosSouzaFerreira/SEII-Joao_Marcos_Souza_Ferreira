
DROP TABLE IF EXISTS posts;
CREATE TABLE posts(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name text not null,
	content text not null
);
