# Online Store

## Virtual Environment

To manage dependencies in an isolated Python environment, follow these steps:

* Activate the virtual environment:
```bash
source env/bin/activate
```

* Verify that the virtual environment is active:
```bash
echo $VIRTUAL_ENV
```

* Install all dependencies:
```bash
pip install -r scb/web/test_e2e/requirements.pip3
```

* Deactivate the virtual environment:
```bash
deactivate
```