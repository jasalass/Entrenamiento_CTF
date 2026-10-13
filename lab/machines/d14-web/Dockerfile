FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-flask && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash www
RUN printf '%s\n' 'FLAG{d14_web_dbwu}' > /flag.txt && chmod 644 /flag.txt
RUN mkdir -p /srv/files && printf 'manual de usuario\n' > /srv/files/manual.txt
COPY app.py /opt/app.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
