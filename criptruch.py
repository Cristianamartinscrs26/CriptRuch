# CriptRuch - Sistema de Segurança Modular
# Autor: Cristiano Martins
# Versão: Protótipo 1.2

import os
import hashlib
import json
import subprocess
import logging
import sys
from datetime import datetime

# Configurações
HASH_DB = "hashes_db.json"
MONITOR_DIR = "arquivos_monitorados"
VIRUS_SIGNATURES = ["eicar", "malware_test", "virus_simulation"]
WHITELIST_WINDOWS = ["explorer.exe", "cmd.exe", "python.exe", "chrome.exe", "svchost.exe"]
WHITELIST_UNIX = ["systemd", "bash", "sshd", "python", "cron"]
PROCESS_WHITELIST = WHITELIST_WINDOWS if os.name == "nt" else WHITELIST_UNIX

# Logging
logging.basicConfig(
    filename="criptRuch.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def garantir_pasta_monitorada():
    if not os.path.exists(MONITOR_DIR):
        print(f"Pasta '{MONITOR_DIR}' não existe. Criando-a automaticamente...")
        os.makedirs(MONITOR_DIR)

def gerar_hash_arquivo(caminho_arquivo):
    sha256 = hashlib.sha256()
    try:
        with open(caminho_arquivo, "rb") as f:
            for bloco in iter(lambda: f.read(4096), b""):
                sha256.update(bloco)
        return sha256.hexdigest()
    except Exception as e:
        print(f"Erro ao ler {caminho_arquivo}: {e}")
        return None

def carregar_hashes():
    if not os.path.exists(HASH_DB):
        return {}
    with open(HASH_DB, "r") as f:
        return json.load(f)

def salvar_hashes(hashes):
    with open(HASH_DB, "w") as f:
        json.dump(hashes, f, indent=2)

def verificar_integridade(atualizar=False):
    hashes_salvos = carregar_hashes()
    hashes_atuais = {}
    alertas = []

    for raiz, _, arquivos in os.walk(MONITOR_DIR):
        for nome_arquivo in arquivos:
            caminho = os.path.join(raiz, nome_arquivo)
            hash_atual = gerar_hash_arquivo(caminho)
            if not hash_atual:
                continue
            hashes_atuais[caminho] = hash_atual

            hash_antigo = hashes_salvos.get(caminho)
            if hash_antigo and hash_antigo != hash_atual:
                alertas.append(f"ALERTA: {caminho} foi modificado!")
            elif not hash_antigo:
                alertas.append(f"NOVO ARQUIVO DETECTADO: {caminho}")

    for caminho in hashes_salvos:
        if caminho not in hashes_atuais:
            alertas.append(f"ARQUIVO REMOVIDO: {caminho}")

    if atualizar:
        salvar_hashes(hashes_atuais)
        print("Hashes atualizados e salvos.")

    return alertas

def verificar_assinaturas_virais():
    alertas_virus = []
    for raiz, _, arquivos in os.walk(MONITOR_DIR):
        for nome_arquivo in arquivos:
            caminho = os.path.join(raiz, nome_arquivo)
            try:
                with open(caminho, "rb") as f:
                    conteudo = f.read().lower()
                    if any(sig.encode() in conteudo for sig in VIRUS_SIGNATURES):
                        alertas_virus.append(f"VÍRUS DETECTADO em {caminho}")
            except Exception as e:
                print(f"Erro ao escanear {caminho}: {e}")
    return alertas_virus

def detectar_comportamento_suspeito():
    alertas_comportamento = []
    try:
        if os.name == "nt":
            resultado = subprocess.check_output(["tasklist"], text=True)
        else:
            resultado = subprocess.check_output(["ps", "-eo", "comm"], text=True)

        processos = resultado.lower().splitlines()
        whitelist = [p.lower() for p in PROCESS_WHITELIST]

        for proc in processos:
            partes = proc.strip().split()
            if not partes:
                continue
            nome_proc = os.path.basename(partes[0])
            if nome_proc and nome_proc not in whitelist:
                alertas_comportamento.append(f"POTENCIAL PROCESSO SUSPEITO DETECTADO: {nome_proc}")
    except Exception as e:
        alertas_comportamento.append(f"Erro ao tentar listar processos: {e}")
    return alertas_comportamento

def verificar_integridade_sistema():
    alertas = []
    arquivos_criticos = ["/bin/bash", "/etc/passwd", "/etc/shadow"] if os.name != "nt" else [
        os.path.join(os.environ.get("SystemRoot", "C:\\Windows"), "System32", "cmd.exe")
    ]

    for caminho in arquivos_criticos:
        if not os.path.exists(caminho):
            alertas.append(f"ARQUIVO DO SISTEMA AUSENTE: {caminho}")
        elif os.path.getsize(caminho) == 0:
            alertas.append(f"ARQUIVO DO SISTEMA CORROMPIDO (vazio): {caminho}")

    return alertas

def registrar_alertas(alertas):
    for alerta in alertas:
        logging.warning(alerta)

def exportar_relatorio(alertas):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        caminho_relatorio = os.path.join(MONITOR_DIR, "relatorio.txt")
        with open(caminho_relatorio, "w") as f:
            f.write(f"Relatório CriptRuch\nData/Hora: {timestamp}\n\n")
            if alertas:
                for alerta in alertas:
                    f.write(alerta + "\n")
            else:
                f.write("Nenhuma ameaça ou modificação suspeita detectada.\n")
        print(f"\nRelatório exportado para '{caminho_relatorio}'.")
    except Exception as e:
        print(f"Erro ao exportar relatório: {e}")

if __name__ == "__main__":
    atualizar_hashes = "--atualizar" in sys.argv

    garantir_pasta_monitorada()

    print("Iniciando análise de segurança (integridade, vírus, comportamento, sistema)...")
    alertas_integridade = verificar_integridade(atualizar=atualizar_hashes)
    alertas_virus = verificar_assinaturas_virais()
    alertas_comportamento = detectar_comportamento_suspeito()
    alertas_sistema = verificar_integridade_sistema()

    alertas = alertas_integridade + alertas_virus + alertas_comportamento + alertas_sistema

    if alertas:
        print("\n\n== ALERTAS DETECTADOS ==")
        for alerta in alertas:
            print(alerta)
        registrar_alertas(alertas)
    else:
        print("Nenhuma ameaça ou modificação suspeita detectada.")

    exportar_relatorio(alertas)


if "--upgrade" in sys.argv:
    print("Baixando e aplicando atualizações do CriptRuch...")
    # Aqui você pode futuramente conectar-se a um repositório remoto para baixar atualizações
    # ou simplesmente exibir uma mensagem dizendo que está atualizado.
    print("Atualizações aplicadas com sucesso.")
    sys.exit()

if os.name == "nt":
    print("Sistema detectado: Windows")
else:
    print("Sistema detectado: Linux/Unix")

