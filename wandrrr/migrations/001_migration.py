steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE accounts (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(24) NOT NULL,
            last_name VARCHAR(24) NOT NULL,
            username VARCHAR(24) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(24) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE accounts;
        """
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE wandrrrs (
            wandrrrs_id SERIAL PRIMARY KEY NOT NULL,
            title VARCHAR(50) NOT NULL,
            start_date DATE NOT NULL,
            end_date DATE,
            location VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            mood VARCHAR(50),
            companion VARCHAR(150),
            companion_dropdown VARCHAR(50),
            weather VARCHAR(50),
            photos01 VARCHAR(2048) NOT NULL,
            photos02 VARCHAR(2048),
            photos03 VARCHAR(2048),
            photos04 VARCHAR(2048),
            photos05 VARCHAR(2048),
            timestamp TIMESTAMPTZ NOT NULL,
            rating INT
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE wandrrrs;
        """
    ]
]
