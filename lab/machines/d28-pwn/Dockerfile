FROM debian:bookworm-slim
RUN apt-get update && apt-get install -y --no-install-recommends openssh-server sudo libcap2-bin && rm -rf /var/lib/apt/lists/*
RUN useradd -m -s /bin/bash ctf && echo 'ctf:ctf' | chpasswd
RUN mkdir -p /run/sshd && ssh-keygen -A
RUN printf '%s\n' 'FLAG{d28_pwn_z3w5}' > /root/flag.txt && chmod 600 /root/flag.txt
RUN cp /bin/cat /usr/local/bin/catcap && setcap cap_dac_read_search+ep /usr/local/bin/catcap
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]
