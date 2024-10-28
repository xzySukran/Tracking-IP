#!/bin/bash

# Warna untuk output
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Menampilkan pesan awal
echo -e "${GREEN}Memulai proses instalasi...${NC}"

# Memperbarui repository paket
echo -e "${GREEN}Memperbarui repository...${NC}"
sudo apt update -y

# Memastikan Python3 sudah terinstall
if ! command -v python3 &> /dev/null
then
    echo -e "${GREEN}Python3 tidak ditemukan, menginstall Python3...${NC}"
    sudo apt install python3 -y
else
    echo -e "${GREEN}Python3 sudah terinstall.${NC}"
fi

# Memastikan pip sudah terinstall
if ! command -v pip3 &> /dev/null
then
    echo -e "${GREEN}pip3 tidak ditemukan, menginstall pip3...${NC}"
    sudo apt install python3-pip -y
else
    echo -e "${GREEN}pip3 sudah terinstall.${NC}"
fi

# Menginstall dependensi requests
echo -e "${GREEN}Menginstall pustaka Python yang diperlukan (requests)...${NC}"
pip3 install requests

# Memberikan izin eksekusi pada file script tracking_IP.py
echo -e "${GREEN}Memberikan izin eksekusi pada file tracking_IP.py...${NC}"
chmod +x tracking_IP.py

# Menampilkan pesan akhir
echo -e "${GREEN}Instalasi selesai! Jalankan program dengan perintah: python3 tracking_IP.py${NC}"

