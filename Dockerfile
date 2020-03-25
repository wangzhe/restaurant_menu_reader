FROM python:3
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./main.py" ]