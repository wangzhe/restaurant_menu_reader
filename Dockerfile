FROM python:3
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    && apt-get clean \
    && apt-get autoremove

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./main.py" ]

# install poppler in Linux
# Most distros ship with pdftoppm and pdftocairo. If they are not installed, refer to your package manager to install poppler-utils