-- Create a new user for SQL replication
CREATE USER 'replica_user'@'%'
identified by 'projectcorrection280hbtn';

-- Grant new user permissions on replication
grant replication slave on *.*
to 'replica_user'@'%';

-- Grant holberton_user permission to view users
grant select on mysql.user
to 'holberton_user'@'localhost';
