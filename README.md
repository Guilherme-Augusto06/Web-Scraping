# 📈 IBOV Top 10 Visualizer

Eu utilizei Python para criar este Web Scraping com as bibliotecas Pandas e Matplotlib. Ele exibe e plota um gráfico com as 10 ações de maior participação na carteira teórica do IBOVESPA do dia 27/06/2025.  
O arquivo CSV para web scraping foi baixado pelo site público oficial:  
🔗 https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-composicao-da-carteira.htm

---

## ✅ Requisitos

- Python **3.13**
- `pandas`
- `matplotlib`

---

## 🧰 Instalação das dependências

> As instruções abaixo funcionam tanto para **Windows** quanto para **Linux**.

### 1. Crie um ambiente virtual (opcional, mas recomendado)

#### Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

#### Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2. Instale as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install pandas matplotlib
```

---

## ▶️ Como executar o script

Após instalar as dependências e garantir que o arquivo CSV (`IBOVDia_27-06-25.csv`) está no mesmo diretório do script Python, execute:

### No Windows:

```powershell
python webScraping.py
```

### No Linux:

```bash
python3 webScraping.py
```

---

## 🧪 Funcionamento do script

Quando você roda o script, um menu interativo será exibido:

```text
Menu:
1 - Ver Top 10 Ações
2 - Ver Gráfico
3 - Sair
Escolha uma opção:
```

### Opções disponíveis:

- **1 - Ver Top 10 Ações**  
  Exibe no terminal as 10 ações com maior participação na carteira teórica do IBOVESPA em 27/06/2025.

- **2 - Ver Gráfico**  
  Gera e exibe um gráfico de pizza mostrando visualmente a distribuição percentual dessas ações.

- **3 - Sair**  
  Encerra o programa.

---
