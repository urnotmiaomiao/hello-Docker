
# EdgeSys start project: test-compose

Project (Folder) name: `test-compose`

## Project structure

```
.  
├── docker-compose.yml
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

1. cd into project directory `...\test-compose`
2. `docker-compose build`
3. `docker-compose up`
4. open a new terminal window, `curl -X POST -H "Content-Type: application/json" -d '{"string": "Hello World"}' http://localhost:5000/send`

```bash
cd <change-me>\test-compose
docker-compose build
docker-compose up
curl -X POST -H "Content-Type: application/json" -d '{"string": "Hello World"}' http://localhost:5000/send
```

## Explanation

