CREATE TABLE IF NOT EXISTS
    user(
        last_name VARCHAR(45) PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(45),
        last_name VARCHAR(45),
        job_title TEXT,
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