CREATE USER IF NOT EXISTS 'eddi'@'localhost' IDENTIFIED BY 'eddi@123';
CREATE DATABASE IF NOT EXISTS llm_lecture_db;
GRANT ALL PRIVILEGES ON llm_lecture_db.* TO 'eddi'@'%';
FLUSH PRIVILEGES;
