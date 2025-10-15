create user if not exists 'test-hiring'@'localhost' identified by 'qwer1234';

grant all privileges on test_hiring_devops.* to 'test-hiring'@'localhost' ;
## create database if it doesnt exist 
create database if not exists test_hiring_devops ;

##
CREATE TABLE if not exists test_hiring_devops.users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO test_hiring_devops.users (name, email)
VALUES ('Alice', 'alice@example.com'),
       ('Bob', 'bob@example.com');
# ---------------------------------------------------------------------------------

