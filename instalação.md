# 🛡️ CriptRuch - Sistema de Segurança Modular

**Autor:** Cristiano Martins
**Versão:** Protótipo 1.2

CriptRuch é uma ferramenta modular de segurança desenvolvida para detectar ameaças em múltiplas frentes do sistema operacional.

## 📌 Funcionalidades

* Verificação de integridade de arquivos
* Detecção de vírus por assinatura
* Monitoramento de comportamentos suspeitos
* Análise de corrupção ou ausência de arquivos essenciais
* Registro de alertas e geração de relatório

## ⚙️ Requisitos

* Python 3 instalado (Linux, Windows ou WSL)

## 💾 Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/CriptRuch.git
cd CriptRuch
```

## 🚀 Executando no Linux (Kali, Ubuntu etc.)

Dê permissão de execução e rode:

```bash
chmod +x criptruch.py
./criptruch.py --atualizar
```

Depois, para novas análises:

```bash
./criptruch.py
```

Ou via Python diretamente:

```bash
python3 criptruch.py
```

## 🪟 Executando no Windows

Abra o terminal (cmd ou PowerShell) e execute:

```bash
python criptruch.py --atualizar
```

Para execuções futuras:

```bash
python criptruch.py
```

## 📤 Relatório

Após a execução, o CriptRuch salva um relatório com os resultados em:

```
/arquivos_monitorados/relatorio.txt
```

## 🧠 Observações

* Use `--atualizar` na primeira execução para registrar os hashes originais dos arquivos.
* Os logs também serão salvos em `criptRuch.log`.
* Os processos permitidos estão definidos na lista branca (whitelist).

---

**Projeto em desenvolvimento. Sugestões são bem-vindas!**
