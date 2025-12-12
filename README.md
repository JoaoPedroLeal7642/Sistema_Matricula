# 🏛️ Sistema de Cadastro de Alunos (PCA - AV2)

## 🎓 Desenvolvedores

| Nome do Aluno | Matrícula |
| :--- | :--- |
| **João Pedro de Souza Leal** | 06015057 |
| **Arthur dos Santos de Araújo** | 06014864 |

## 🌟 Visão Geral do Projeto

Este projeto implementa um sistema básico de **CRUD** (Create, Read, Update, Delete) para o gerenciamento de registros de alunos. O sistema foi construído em Python, focado em modularização, e utiliza a biblioteca `pandas` para a manipulação eficiente e persistência dos dados.

---

## 🛠️ Detalhes Técnicos

* **Tecnologia Principal:** Python 🐍
* **Gerenciamento de Dados:** Biblioteca **`pandas`** (DataFrames).
* **Persistência:** Todos os registros são salvos em um arquivo `.csv` (`alunos_cadastrados.csv`).
* **Chave Única:** O número de Matrícula é gerado **automaticamente** e serve como índice do DataFrame.
* **Estrutura:** O código é modularizado em funções claras para cada operação, conforme as boas práticas de programação.

---

## ✨ Funcionalidades do Menu

| Opção | Ação | Conformidade com o Requisito |
| :---: | :--- | :--- |
| **1** | **INSERIR** | Gera a Matrícula sequencial. Coleta Nome, Endereço e Contato (e-mail, Telefone, etc.). |
| **2** | **PESQUISAR** | Permite buscar por **Matrícula** ou **Nome**. A busca por nome é **case-insensitive** (não diferencia maiúsculas/minúsculas). |
| **Ações 2** | **EDITAR** | Acessado após a pesquisa. Permite editar um campo específico sem redigitar todos os dados (Matrícula não é editável). |
| **Ações 2** | **REMOVER** | Acessado após a pesquisa. Exige **confirmação** antes de apagar o registro permanentemente. |
| **3** | **SAIR** | Finaliza a execução do programa. |

---

## 🚀 Como Executar

### Pré-requisito

Instale a biblioteca `pandas` no seu ambiente Python:

```bash
pip install pandas
Rodando o Script
Execute o arquivo principal no terminal:

Bash

python seu_arquivo_principal.py 
# Exemplo: python cadastro_alunos.py
O sistema carregará os dados salvos anteriormente e apresentará o menu interativo.
