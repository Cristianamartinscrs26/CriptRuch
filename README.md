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


