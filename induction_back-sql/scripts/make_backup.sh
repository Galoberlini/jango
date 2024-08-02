export PGPASSWORD=desarrollo

pg_dump -p 5432 -U equality -h 127.0.0.1 db_develop > backup.sql