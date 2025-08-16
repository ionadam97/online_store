# Online Store

## Virtual Environment

To manage dependencies in an isolated Python environment:

1. **Activate the virtual environment:**

   ```bash
   source env/bin/activate
   ```

2. **Verify activation:**

   ```bash
   echo $VIRTUAL_ENV
   ```

3. **Install dependencies:**

   ```bash
   pip install -r scb/web/test_e2e/requirements.pip3
   ```

4. **Deactivate the environment:**
   ```bash
   deactivate
   ```

## Backend

To start the backend server:

```bash
python be/manage.py runserver
```
