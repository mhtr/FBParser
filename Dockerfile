FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN echo http://mirror.ps.kz/alpine/latest-stable/main > /etc/apk/repositories; \
    echo http://mirror.ps.kz/alpine/latest-stable/community >> /etc/apk/repositories
RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    libxml2-dev\
    libxslt-dev\
    libffi-dev \
    openssl-dev \
    linux-headers; \
    pip install --no-cache-dir -r requirements.txt; \
    apk del .build-deps;
RUN apk add --no-cache tzdata
ENV NAME FBParser-alpine
ENV TZ Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
CMD ["python", "src/bot.py"]