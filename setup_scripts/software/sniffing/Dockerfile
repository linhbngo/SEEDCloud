FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y nmap netwox xinetd telnetd tcpd
RUN echo 'telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd' >> /etc/inetd.conf && \
    /etc/init.d/xinetd restart && \
    DEBIAN_FRONTEND=noninteractive apt-get install -q -y tshark
RUN useradd -m -s /bin/bash seed && \
    echo "seed:dees" | chpasswd && \
    usermod -a -G sudo seed
