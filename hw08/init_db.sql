DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discipline STRING UNIQUE NOT NULL,
    teacher REFERENCES teachers (id)
);
-- Table: groups
DROP TABLE IF EXISTS [groups];
CREATE TABLE [groups] (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    [group] STRING UNIQUE
);
-- Table: ratings
DROP TABLE IF EXISTS ratings;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student REFERENCES students (id),
    discipline REFERENCES disciplines (id),
    date_of DATE NOT NULL,
    grade INTEGER NOT NULL
);
-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student STRING UNIQUE NOT NULL,
    [group] REFERENCES [groups] (id)
);
-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher STRING UNIQUE NOT NULL
);