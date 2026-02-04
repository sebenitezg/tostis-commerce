#!/bin/bash
# This script deploys a PostgreSQL database for the hotel service.

docker run --name ecommerce \
    -e POSTGRES_PASSWORD=secretpassword \
    -e POSTGRES_USER=developer \
    -e POSTGRES_DB=ecommerce_db \
    -p 5432:5432 \
    -d postgres