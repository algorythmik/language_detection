# language_detection
This repo contains the code for training an serving a language detector.
The model is an RNN based classifier trained to classify norwegian and dansih languages and it trained on data from the danish and norwegian wikipedia.

## Run with Docker
With Docker, you can quickly build and run the entire application.

1. First, clone the repo
    ```
    $ git clone https://github.com/algorythmik/language_detection.git
    cd language_detection
    ```
2. Build Docker image
    ```
    docker build -t flask-app:latest .
    ```

3. Run!
    ```
    docker run -p 5000:5000 flask-app
    ```
    You can test the api using an application like postman. Read about it [here](https://medium.com/aubergine-solutions/api-testing-using-postman-323670c89f6d).

The `predict` endpoint expects a json with the following schema:
```
{
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
        }
    },
    "required": ["text"],
}
```
