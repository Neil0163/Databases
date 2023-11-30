CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  content text,
);

-- Then the table with the foreign key second.
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comments text,
  comments_content text,
  author_name text,
  
-- The foreign key is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);