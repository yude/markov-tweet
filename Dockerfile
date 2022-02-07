FROM python:3.8.11-alpine3.13
ADD ./app /app

# Set working directory
WORKDIR /app

# Set timezone
RUN apk --update add tzdata libffi-dev gcc make g++ curl openssl && \
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \
apk del tzdata
# Cleanup cache
RUN rm -rf /var/cache/apk/*

## Install MeCab
ARG _ARM_ARCH="arm-unknown-linux-gnu"
ENV MECAB_VERSION 0.996
ENV IPADIC_VERSION 2.7.0-20070801
ENV mecab_url https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE
ENV ipadic_url https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM
RUN curl -SL -o mecab-${MECAB_VERSION}.tar.gz ${mecab_url} \
    && tar zxf mecab-${MECAB_VERSION}.tar.gz \
    && cd mecab-${MECAB_VERSION} \
    # From https://github.com/gretchi/docker-mecab-neologd-python3
    && if [ `uname -m` =  "aarch64" ]; then \
            ./configure --enable-utf8-only --with-charset=utf8 --build=${_ARM_ARCH} --host=${_ARM_ARCH} --target=${_ARM_ARCH}; \
        else \
            ./configure --enable-utf8-only --with-charset=utf8; \
        fi \
    && make \
    && make install

# Install IPA dictionary
RUN curl -SL -o mecab-ipadic-${IPADIC_VERSION}.tar.gz ${ipadic_url} \
    && tar zxf mecab-ipadic-${IPADIC_VERSION}.tar.gz \
    && cd mecab-ipadic-${IPADIC_VERSION} \
    && ./configure --with-charset=utf8 \
    && make \
    && make install

## Python packages
WORKDIR /app
RUN pip install -r requirements.txt

# Add script to crontab
RUN echo '*/20 * * * * cd /app; python run.py' > /var/spool/cron/crontabs/root

# Cleanup
RUN rm -rf /app/mecab-${MECAB_VERSION}.tar.gz \
           /app/mecab-ipadic-${IPADIC_VERSION}.tar.gz \
           /app/mecab-ipadic-${IPADIC_VERSION} \
           /app/mecab-${MECAB_VERSION} \
           /app/banned.json.sample

# Run crond
ENTRYPOINT ["crond", "-f"]
