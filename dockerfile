from python:3.14.3
COPY __init__.py /app/
copy database.py /app/
copy main.py /app/
copy models.py /app/
copy schemas.py /app/
copy requirements.txt /app/
run pip install --no-cache-dir --upgrade -r /app/requirements.txt
workdir /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
