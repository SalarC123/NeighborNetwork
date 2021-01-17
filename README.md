# NeighborNetwork


# Local Development

## Initial

[Setting up your virtual environment](https://flask.palletsprojects.com/en/1.1.x/installation/#create-an-environment)

### Windows
```
python -m pip install --user virtualenv
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

###  Linux / Mac
```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Running Server
Assuming you already activated your virtual environment e.g. `venv\Scripts\activate` (Windows) or `. venv/bin/activate` (Mac)
```
flask run
```

## Try it out
http://127.0.0.1:5000/
