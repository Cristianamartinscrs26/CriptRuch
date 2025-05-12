# 🔐 Instalação e Execução do CriptRuch no Linux (Kali, Ubuntu, etc.)

# 1. Clone o repositório do CriptRuch (substitua pelo seu link)
git clone https://github.com/seu-usuario/criptRuch.git

# 2. Acesse a pasta do projeto
cd criptRuch

# 3. Torne o script principal executável
chmod +x criptruch.py

# 4. (Opcional) Mova o script para /usr/local/bin para poder usar em qualquer lugar
sudo cp criptruch.py /usr/local/bin/criptruch

# 5. Execute o CriptRuch
./criptruch.py         # ou: criptruch (se tiver movido para /usr/local/bin)

# 6. Para atualizar os hashes salvos (modo de aprendizado)
./criptruch.py --atualizar



✅ Dicas
Certifique-se de que o Python 3 está instalado (em Kali já vem por padrão).

Você pode editar o nome do script para algo mais curto se quiser (criptruch.py → criptruch).

O script já deve começar com esta linha no topo:

python
Copiar
Editar
#!/usr/bin/env python3
