# A scalable flask app template

Basic Flask application with a folder structure ready for scaling, and a few domain examples to clarify how new features should be added.

I posted an article on Medium where I cover the whole process of getting to this final structure. You can find it [here](https://medium.com/@gabrielsollero/domain-driven-design-in-practice-the-train-of-thought-behind-a-scalable-rest-api-with-flask-8904e9017ae9). Hope you like it!

## 💻 How to run

In the first run, I recommend you create a virtual environment and install the dependencies from `requirements.txt`. This can be achieved by running the following, from the project's root folder:

On Windows:

```powershell
$ python -m venv .venv
$ .\.venv\Scripts\activate
$ pip install -r requirements.txt
```

On Linux:

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Additionally, you must specify the environment you wanna run it on - either `development`, `testing` or `production`. As I like to do with all my projects, this one is configured for running in production by default. To enable debug mode and auto reloads, you must specify the `development` one. `testing` shouldn't be used manually in normal development. This one is used just inside unit tests.

You can specify the environment through the env variable `ENVIRONMENT`, either using a `.env` file or manually inside the terminal where you're running the app.

## 🐋 Running with Docker

As a sequel of the first article, I posted a second one documenting the process of containerizing a flask application with multi-environment support by default, that can be found [here](**TODO**). Now that we have Docker's magic implemented, you can run the application in development, test or production environments by running one of the following, from the project's root folder:

```bash
docker compose -f compose.dev.yml # development
docker compose -f compose.test.yml # test
docker compose up # production
```

Hope you like it! 😊
