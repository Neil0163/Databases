DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
  id SERIAL PRIMARY KEY,
  name text,
  cooking_time_minutes int,
  rating int
);


INSERT INTO recipes (name, cooking_time_minutes, rating) VALUES ('Chilli', '20', '3');
INSERT INTO recipes (name, cooking_time_minutes, rating) VALUES ('Burgers', '25', '4');
INSERT INTO recipes (name, cooking_time_minutes, rating) VALUES ('Chicken Curry', '25', '4');