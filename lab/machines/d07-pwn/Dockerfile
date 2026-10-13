FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo python3 && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d07_pwn_8rho}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN echo 'ctf ALL=(root) NOPASSWD: /usr/bin/python3' > /etc/sudoers.d/ctf && chmod 440 /etc/sudoers.d/ctf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
