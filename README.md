# flask-event-consumer
This service exposes a HTTP API endpoint that accepts incoming JSON payloads and persists them to a file. 

# Configuration
The service can be configured through a configuration file (config.json). 
Here are the available configuration options:

* payloads_file: The location of the file where incoming payloads will be persisted.

# Installation
```bash
git clone https://github.com/saniokas/flask-event-consumer.git
pip install -r requirements.txt
flask run -h 127.0.0.1 -p 8000
```
