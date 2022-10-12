# Weather Vane Application

# To build API image

docker build -f Dockerfile.api -t weathervane-api:latest .

# To build UI image

docker build -f Dockerfile.ui -t weathervane-ui:latest .

# To run services using docker compose

docker-compose up

# To use Application

Use http://localhost:8080/

