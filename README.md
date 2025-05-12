# 🛡️ CriptRuch - Sistema de Segurança Modular

**Autor:** Cristiano Martins  
**Versão:** Protótipo 1.2  
**Última atualização:** Maio 2025  

---

## 📌 Descrição

O **CriptRuch** é uma ferramenta modular de segurança desenvolvida em Python para detectar ameaças em múltiplas frentes do sistema operacional.  
Ideal para testes locais de segurança, análises de integridade e monitoramento básico de comportamento suspeito.

O sistema executa análises automatizadas nos seguintes aspectos:

- 🧬 Verificação de integridade de arquivos monitorados
- 🦠 Detecção de assinaturas virais conhecidas
- ⚠️ Monitoramento de processos com comportamento suspeito
- ⚙️ Checagem de arquivos críticos do sistema

---

## ⚙️ Funcionalidades

| Módulo                       | Descrição                                                                 |
|-----------------------------|--------------------------------------------------------------------------|
| **Integridade de Arquivos** | Gera e compara hashes SHA-256 para detectar alterações                  |
| **Assinatura Viral**        | Busca strings virais (e.g. `"eicar"`) em arquivos monitorados           |
| **Processos Suspeitos**     | Lista processos e compara com uma whitelist baseada no sistema operacional |
| **Arquivos do Sistema**     | Verifica presença e consistência de arquivos essenciais como `bash` ou `cmd.exe` |
| **Relatórios & Logs**       | Exporta relatório em `.txt` e registra logs com nível `WARNING`         |

---

## 🖥️ Requisitos

- Python 3.7+
- Sistemas suportados: Windows, Linux, macOS (com pequenas adaptações)

---

## 📂 Estrutura de Arquivos

CriptRuch/
├── criptRuch.py
├── hashes_db.json
├── arquivos_monitorados/
│ └── [seus arquivos aqui]
├── relatorio_YYYYMMDD_HHMMSS.txt
└── criptRuch.log



## 🚀 Como Usar

### 📦 1. Instalar Dependências
Não há dependências externas. Apenas Python.

### 📁 2. Criar a pasta de monitoramento (automático)
Ao rodar o script pela primeira vez, a pasta `arquivos_monitorados/` será criada automaticamente, se não existir.

### 🔍 3. Rodar o Antivírus

#### Modo padrão (apenas verificação):
```bash
python criptRuch.py



🧪 Exemplo de Saída

Iniciando análise de segurança (integridade, vírus, comportamento, sistema)...

== ALERTAS DETECTADOS ==
ALERTA: arquivos_monitorados/config.ini foi modificado!
POTENCIAL PROCESSO SUSPEITO DETECTADO: crack_tool
VÍRUS DETECTADO em arquivos_monitorados/fake_virus.txt

Relatório exportado para 'arquivos_monitorados/relatorio_20250512_1530.txt'.


🧱 Arquitetura (Simplificada)

+-------------------+
| criptRuch.py      |
|-------------------|
| - verificar_hash  |
| - detectar_virus  |
| - comportamento   |
| - integridade_OS  |
+--------+----------+
         |
         v
+-----------------------------+
| arquivos_monitorados/      |
| hashes_db.json              |
| relatorio_*.txt             |
| criptRuch.log               |
+-----------------------------+


🧑‍💻 Contato
Cristiano Martins
📧 cristianomartinscrs26@gmail.com
🔗 Projeto público no GitHub
