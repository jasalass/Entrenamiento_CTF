FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo gcc libc6-dev && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d11_pwn_tlod}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN printf '%s\n' '#include <unistd.h>' 'int main(){setgid(0);setuid(0);execl("/bin/sh","sh","-p",(char*)0);return 1;}' > /tmp/r.c && gcc /tmp/r.c -o /usr/local/bin/runner && chmod 4755 /usr/local/bin/runner && rm /tmp/r.c
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
