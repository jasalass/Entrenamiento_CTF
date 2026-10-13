FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo gcc libc6-dev procps && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d25_pwn_wkls}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN printf '%s\n' '#include <stdlib.h>' '#include <unistd.h>' 'int main(){setuid(0);setgid(0);system("ps");return 0;}' > /tmp/m.c && gcc /tmp/m.c -o /usr/local/bin/monitor && chmod 4755 /usr/local/bin/monitor && rm /tmp/m.c
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
