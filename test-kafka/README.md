
# hello Docker: test-kafka

Project (Folder) name: `test-kafka`

## Project structure

```
.  
├── docker-compose.yml
├── producer
│   ├── Dockerfile
│   ├── producer_service.py
│   ├── requirements.txt
├── input
│   ├── Dockerfile
│   ├── input_service.py
│   ├── requirements.txt
├── processor
│   ├── Dockerfile
│   ├── processor_service.py
│   ├── requirements.txt
├── output
│   ├── Dockerfile
│   ├── output_service.py
│   ├── requirements.txt
├── data
    └── output  # This will store output.txt
```

## How to run it?

1. cd into project directory `...\test-kafka`
2. `docker compose build`
3. `docker compose up`

```bash
cd <change-me>\test-compose
docker compose build
docker compose up 
```

## Explanation

