FROM brightsparklabs/appcli:3.1.0

ENTRYPOINT ["./myapp.py"]
WORKDIR /app

COPY requirements.txt .
RUN pip install --requirement requirements.txt
COPY src .

ARG APP_VERSION=latest
ENV APP_VERSION=${APP_VERSION}

