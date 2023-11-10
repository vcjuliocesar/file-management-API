# file-management-API
 
 Welcome to the **file-management-API** repository! This is a simple guide to help you get started with settings up and running the project.

 ## Actual version

 The actual version is [v0.1.0]()
___

## Requirements
 
 * Python:3 :snake:

 * PIP:3 :snake:

 * Docker :whale:

 ## Getting Started

Follow these steps to set up and run the project on your local machine:

### Clone the repository

`git clone git@github.com:vcjuliocesar/file-management-API.git`

**Create enviroment file:** rename .env.example by .env

add your enviroment variables

## Docker

It is important that you have docker installed on your computer

```docker
docker compose build

docker compose up
```

Once the project is up and running, you can access it through your browser or API client.

**Default: [http://127.0.0.1:8000](http://127.0.0.1:8000)**

If you prefer do not use docker follow these steps

It is important that you have python and pip installed on your computer

**Create a Virtual Environment**

`python3 -m venv env`

**Activate the Virtual Environment: On macOS/Linux**

`source env/bin/activate`

**On Windows**

`.\env\Scripts\activate`

**Install dependencies**

`pip3 install --no-cache-dir --upgrade requirements.txt`

**Run the project**

`uvicorn src.app.main:app --reload`

#### Happy Code! :smiley: