FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo libcap2-bin python3 && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d19_pwn_5iae}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN cp /usr/bin/python3 /usr/local/bin/python3cap && setcap cap_setuid+ep /usr/local/bin/python3cap
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
