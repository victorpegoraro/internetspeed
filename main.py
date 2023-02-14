#!/usr/bin/env
import speedtest
from colorama import Fore, init

print(Fore.YELLOW + "-=-=-=-=- Internet Speed -=-=-=-=- \n")
print(Fore.GREEN + "[+] Geting best servers ... \n")

# iniciando biblioteca
st = speedtest.Speedtest()
st.get_best_server() # Buscando melhor servidor

print(Fore.GREEN + "[+] Testing ... \n")

# Testando Ping
print(f"{Fore.CYAN}[$] ping : {Fore.YELLOW} {st.results.ping} ms")

# Veocidade de download
print(f"{Fore.CYAN}[$] download : {Fore.YELLOW} {round(st.download() / 1000 / 1000, 1)} Mbit/s")

# Velocidade de upload
print(f"{Fore.CYAN}[$] upload : {Fore.YELLOW} {round(st.upload() / 1000 / 1000, 1)} Mbit/s")
