FROM python:3.9.10-bullseye AS builder
ADD ./app/requirements.txt /app/

# Set timezone
RUN apt update; apt -y install tzdata && \
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

## Install Python packages
WORKDIR /app
RUN apt update; apt -y install mecab libmecab-dev mecab-ipadic-utf8; pip install -r requirements.txt

FROM python:3.9.10-bullseye AS runner

# Copy dependencies from builder / Set timezone
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /etc/localtime /etc/localtime

## Install MeCab
RUN apt update; apt -y install mecab libmecab-dev mecab-ipadic-utf8

# Add script to crontab
RUN echo '*/20 * * * * root cd /app; python run.py' >> /etc/crontab

# Cleanup
RUN rm -rf /app/banned.json.sample

# Load app
ADD ./app /app

# Run crond
ENTRYPOINT ["crond", "-f"]
