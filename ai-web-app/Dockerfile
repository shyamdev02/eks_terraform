FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run"]

CMD [ "Home.py"]

