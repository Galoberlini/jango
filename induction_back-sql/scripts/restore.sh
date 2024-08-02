export PGPASSWORD=desarrollo

cd /home/app/scripts

dropdb -U equality -h 127.0.0.1 db_develop
createdb -U equality -h 127.0.0.1 db_develop

psql -U equality -h 127.0.0.1 db_develop < ../backups/backup.sql