CREATE TABLE IF NOT EXISTS
    user(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(45),
        last_name VARCHAR(45),
        job_title TEXT,
        active BOOLEAN DEFAULT TRUE
    );

INSERT INTO user(
        first_name,
        last_name,
        job_title)
    VALUES(
        "Katie",
        "Collins",
        "Crew member"
    );