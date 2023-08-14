-- Create the user and set the password
-- Grant all privileges to the user on all databases
-- Flush privileges to apply the changes
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
