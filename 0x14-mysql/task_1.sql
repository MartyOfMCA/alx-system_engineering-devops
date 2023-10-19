-- Create a new user with permissions to check
-- server replication status

-- Create a new user
CREATE USER 'holberton_user'@'localhost'
identified by 'projectcorrection280hbtn';

-- Grant user permissions
grant replication client on *.*
to 'holberton_user'@'localhost';
