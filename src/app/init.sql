-- Switch to the pollapp database (no need to create it, it's set by the environment variable)
\c pollapp;

-- Create the polls table
CREATE TABLE IF NOT EXISTS polls (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    option_1 VARCHAR(255),
    option_2 VARCHAR(255),
    votes_1 INT DEFAULT 0,
    votes_2 INT DEFAULT 0
);

-- Create the votes table
CREATE TABLE IF NOT EXISTS votes (
    id SERIAL PRIMARY KEY,
    poll_id INTEGER REFERENCES polls(id),
    choice TEXT NOT NULL
);

