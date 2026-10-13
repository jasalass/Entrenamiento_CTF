FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo gcc libc6-dev && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d20_pwn_986l}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN printf '%s\n' 'Defaults env_keep += "LD_PRELOAD"' 'ctf ALL=(root) NOPASSWD: /usr/bin/id' > /etc/sudoers.d/ctf && chmod 440 /etc/sudoers.d/ctf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
