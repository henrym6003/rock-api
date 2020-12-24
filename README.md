#Rock API
A gravity simulator for falling rocks

## Architecture
Rock API is written in python and makes use of the Flask framework. 

## Run locally
```
pip install -r requirements.txt

export FLASK_APP=main.py
flask run
```

## Routes

### `[POST]/init-world`
Creates a new world by supplying rocks

Accepted body Content-Type: `text/plain`
```
. .
. .
 :T.
. .
   .
```
Response:
```
{
    "message": "new world created successfully",
    "world_uuid": "b2a1eb89-a596-46c9-b889-56f8c180d6d8"
}
```
### `[GET]/world/<UUID>`
using the `world_uuid` received after initializing, we can graphically visualize the current state of the world

Response:
```
  : 
  T 
.  
::.:
```

## Tests
Execute the unit test suite with the below:
```
pytest tests/
```