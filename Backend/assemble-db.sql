CREATE DATABASE assemble;

CREATE USER assemble_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE assemble TO assemble_admin;