#/bin/bash
set -x

#
# setup Anaconda
#
wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
bash Anaconda3-5.3.0-Linux-x86_64.sh -b
echo "export PATH=/home/seed/anaconda3/bin:$PATH" >> .bashrc
source ~/.bashrc

#
# setup scapy
#

# work around due to https://github.com/conda/conda/issues/7267
echo "unset SUDO_UID SUDO_GID SUDO_USER" >> .bashrc

echo "Run infinite UPD program in background"
