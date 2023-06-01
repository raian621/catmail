#!/usr/bin/bash

# This script prompts the user for environment variables
# needed to run the CatMail application and stores the
# environment variables in .env files.

echo "====================================================================="
echo "WARNING! Running this script will overwrite any existing .env files"
echo "in the project directory!"
echo "====================================================================="

#########################################
# GET CATMAIL ENVIRONMENT VARIABLES
#########################################
catmail_env=()
echo "---------------------------------------------------------------------"
echo " CatMail Environment Variables:"
echo "---------------------------------------------------------------------"
read -p "What hostname do you want to host the CatMail app on? [default=localhost] " HOST
read -p "What port do you want to host the CatMail app on? [default=8532] " PORT
read -p "Enter an admin username for the CatMail app [default=admin]: " ADMIN_USERNAME
read -p "Enter an admin password for the CatMail app [default=admin]: " ADMIN_PASSWORD
HOST=${HOST:-localhost}
PORT=${PORT:-5432}
ADMIN_USERNAME=${ADMIN_USERNAME:-admin}
ADMIN_PASSWORD=${ADMIN_PASSWORD:-admin}
catmail_env+=("HOST=${HOST}")
catmail_env+=("PORT=${PORT}")
catmail_env+=("ADMIN_USERNAME=${ADMIN_USERNAME}")
catmail_env+=("ADMIN_PASSWORD=${ADMIN_PASSWORD}")

#########################################
# GET REDIS ENVIRONMENT VARIABLES
#########################################
redis_env=()
echo "---------------------------------------------------------------------"
echo " Redis Environment Variables:"
echo "---------------------------------------------------------------------"
read -p "Redis URI [default=localhost]: " REDIS_URI
read -p "Redis port [default=6379]: " REDIS_PORT
read -p "Redis username [default=]: " REDIS_USERNAME
if [ -n "$REDIS_USERNAME" ]; then
  read -p "Redis password [default=]: " REDIS_PASSWORD
fi
read -p "Redis SSL [default=n]": REDIS_SSL
REDIS_URI=${REDIS_URI:-localhost}
REDIS_PORT=${REDIS_PORT:-6379}
redis_env+=("REDIS_URI=${REDIS_URI}")
redis_env+=("REDIS_PORT=${REDIS_PORT}")
if [ -n "$REDIS_USERNAME" ]; then
  redis_env+=("REDIS_USERNAME=${REDIS_USERNAME}")
  redis_env+=("REDIS_PASSWORD=${REDIS_PASSWORD}")
fi
if [ -n "$REDIS_SSL" ]; then
  redis_env+=("REDIS_SSL=${REDIS_SSL}")
fi
case $REDIS_SSL in
  [yY]* )
    read -p "Redis SSL certfile [default=./redis_user.crt]: " REDIS_SSL_CERTFILE
    read -p "Redis SSL keyfile [default=./redis_user_private.key]: " REDIS_SSL_KEYFILE
    read -p "Redis SSL CA certs [default=./redis_ca.pem]: " REDIS_SSL_CA_CERTS    
    REDIS_SSL_CERTFILE=${REDIS_SSL_CERTFILE:-./redis_user.crt}
    REDIS_SSL_KEYFILE=${REDIS_SSL_KEYFILE:-./redis_user_private.key}
    REDIS_SSL_CA_CERTS=${REDIS_SSL_CA_CERTS:-./redis_ca.pem}
    redis_env+=("REDIS_SSL_CERTFILE=${REDIS_SSL_CERTFILE}")
    redis_env+=("REDIS_SSL_KEYFILE=${REDIS_SSL_KEYFILE}")
    redis_env+=("REDIS_SSL_CA_CERTS=${REDIS_SSL_CA_CERTS}")
    ;;
esac

#########################################
# GET SQL DATABASE ENVIRONMENT VARIABLES
#########################################
db_env=()
echo "---------------------------------------------------------------------"
echo " SQL Database Environment Variables:"
echo "---------------------------------------------------------------------"
read -p "SQL Database provider [default=postgres]: " DB_PROVIDER
read -p "SQL Database URI [default=localhost]: " DB_URI
read -p "SQL Database port [default=5432]: " DB_PORT
read -p "SQL username [default=]: " DB_USERNAME
if [ -n "$DB_USERNAME" ]; then
  read -p "SQL password [default=]: " DB_PASSWORD
fi
read -p "SQL SSL [default=n]": DB_SSL
DB_PROVIDER=${DB_PROVIDER:-postgres}
DB_URI=${DB_PROVIDER:-localhost}
DB_PORT=${REDIS_PORT:-5432}
db_env+=("DB_PROVIDER=${DB_PROVIDER}")
db_env+=("DB_URI=${DB_URI}")
db_env+=("DB_PORT=${DB_PORT}")
if [ -n "$DB_USERNAME" ]; then
  db_env+=("DB_USERNAME=${DB_USERNAME}")
  db_env+=("DB_PASSWORD=${DB_PASSWORD}")
fi
if [ -n "$DB_SSL" ]; then
  db_env+=("DB_SSL=${DB_SSL}")
fi
case $DB_SSL in
  [Yy]* )
    read -p "SQL SSL certfile [default=./redis_user.crt]: " DB_SSL_CERTFILE
    read -p "SQL SSL keyfile [default=./redis_user_private.key]: " DB_SSL_KEYFILE
    read -p "SQL SSL CA certs [default=./redis_ca.pem]: " DB_SSL_CA_CERTS    
    DB_SSL_CERTFILE=${DB_SSL_CERTFILE:-./postgres_user.crt}
    DB_SSL_KEYFILE=${DB_SSL_KEYFILE:-./postgres_user_private.key}
    DB_SSL_CA_CERTS=${DB_SSL_CA_CERTS:-./postgres_ca.pem}
    db_env+=("DB_SSL_CERTFILE=${DB_SSL_CERTFILE}")
    db_env+=("DB_SSL_KEYFILE=${DB_SSL_KEYFILE}")
    db_env+=("DB_SSL_CA_CERTS=${DB_SSL_CA_CERTS}")
    ;;
esac

#########################################
# SAVE ENVIRONMENT VARIABLES TO SRC
#########################################
set -v
cat /dev/null > src/.env
for env_var in ${catmail_env[@]}; do
  echo $env_var >> src/.env
done

cat /dev/null > src/redis.env
for env_var in ${redis_env[@]}; do
  echo $env_var >> src/redis.env
done

cat /dev/null > src/db.env
for env_var in ${db_env[@]}; do
  echo $env_var >> src/db.env
done