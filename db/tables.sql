-- Write sql queries to create the various database tables --
DROP TABLE question;
DROP TABLE USER; 

CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT,
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMPTZ,
    question_title VARCHAR(150),
    question_summary TEXT,
    CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES user(id) ON DELETE CASCADE,
);

/*
CREATE TABLE answers (
    id
    created_at
    question
);


CREATE TABLE comments (

);
*/