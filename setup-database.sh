#!/bin/sh

docker run --name demo-db -p 15432:5432 -d postgres:11

echo 'Waiting for Postgres to bootstrap...'

sleep 10

docker exec -t demo-db psql -U postgres -c 'CREATE DATABASE default_db;'
docker exec -t demo-db psql -U postgres -c 'CREATE DATABASE django_q_db;'

echo 'Your disposable postgres server is now running.'
