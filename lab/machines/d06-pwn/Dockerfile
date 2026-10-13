FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo cron procps && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d06_pwn_eld2}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN printf '%s\n' '#!/bin/sh' 'echo backup ok' > /opt/backup.sh && chmod 777 /opt/backup.sh
RUN echo '* * * * * root /opt/backup.sh' > /etc/cron.d/backup && chmod 644 /etc/cron.d/backup
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
