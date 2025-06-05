# 🎉 Gerenciador de Sorteios

Bem-vindo ao **Gerenciador de Sorteios**, um sistema simples e prático para criar, gerenciar e realizar sorteios de forma automatizada!  
Ideal para quem organiza promoções, rifas, sorteios entre amigos ou qualquer outra dinâmica que envolva sorte. 🍀

---

## 🚀 Funcionalidades

- ✅ Cadastro de participantes via formulário web
- 🎰 Sorteio aleatório com base nos dados cadastrados
- 📜 Registro e exibição do ganhador
- 🧾 Interface simples com templates em HTML
- 🔁 Possibilidade de reiniciar sorteios facilmente

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Flask** (framework web)
- **HTML/CSS** (Templates)
- **Random** (para lógica do sorteio)

---

## 📦 Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina:

- [Python 3.x](https://www.python.org/)
- `pip` para instalar bibliotecas
- Recomendado: ambiente virtual (`venv`)

---

## ⚙️ Instalação

```bash
# Clone o repositório
git clone https://github.com/ItaloElias/Gerenciador_Sorteio.git

# Acesse o diretório
cd Gerenciador_Sorteio

# (Opcional) Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

# Instale as dependências
pip install flask
```

---

## ▶️ Como Usar

1. Execute o arquivo principal:
```bash
python app.py
```

2. Acesse o navegador e vá para:
```
http://127.0.0.1:5000
```

3. Cadastre os participantes e clique para realizar o sorteio!

---

## 📁 Estrutura do Projeto

```
Gerenciador_Sorteio/
├── app.py               # Arquivo principal com a lógica da aplicação
├── dicionario.py        # Script auxiliar (provavelmente para armazenar dados temporários)
├── Templates/           # Contém os arquivos HTML para a interface
│   ├── index.html
│   └── resultado.html
```

---

## 👨‍💻 Autor

Desenvolvido por **Italo Elias**  
🔗 [GitHub - ItaloElias](https://github.com/ItaloElias)

---

## 📄 Licença

Este projeto está sob a licença **MIT**.  
Sinta-se livre para utilizar, modificar e compartilhar!

---

## ⭐ Contribua

Se este projeto foi útil para você, deixe uma estrela ⭐ no repositório!  
Feedbacks e sugestões também são muito bem-vindos. 😄
