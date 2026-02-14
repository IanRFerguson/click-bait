#!/bin/python3
set -e

if [ ! -f ./dev.env ]; then
    echo "Missing dev.env file"
    exit 1
else
    source ./dev.env
fi 

uv run src/02__example.py \
    --host $PG_HOST \
    --port $PG_PORT \
    --dbname $PG_DB \
    --user $PG_USER \
    --password $PG_PASSWORD

# Compile the binary
echo "Compiling the binary..."
make package >> /dev/null

# Copy the binary to /bin
echo "Copying the binary to /usr/local/bin/pg-click-bait..."
cp ./dist/pg-click-bait /usr/local/bin/pg-click-bait

# Run the binary
echo "Running pg-click-bait..."
pg-click-bait \
    --host $PG_HOST \
    --port $PG_PORT \
    --dbname $PG_DB \
    --user $PG_USER \
    --password $PG_PASSWORD
