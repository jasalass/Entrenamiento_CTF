FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-flask && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash www
RUN printf '%s\n' 'FLAG{d05_web_l89k}' > /flag.txt && chmod 644 /flag.txt
COPY app.py /opt/app.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
