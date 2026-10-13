FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-flask iputils-ping procps ca-certificates && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash www
RUN printf '%s\n' 'FLAG{d11_web_hdzr}' > /home/www/flag.txt && chown www:www /home/www/flag.txt && chmod 644 /home/www/flag.txt
COPY app.py /opt/app.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
