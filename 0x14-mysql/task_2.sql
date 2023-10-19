-- Create new database
create database tyrell_corp;

-- Switch to database created
use tyrell_corp;

-- Create a new table
create table nexus6
(
	id int primary key,
	name varchar(60) not null
);

-- Add a record into the table
insert into nexus6 values(1, 'Leon');

-- Grant holberton_user select permission
-- on the new table created
grant select on tyrell_corp.nexus6
to 'holberton_user'@'localhost';
