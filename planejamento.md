# 🗺️ Planejamento Detalhado de Implementação do Sistema CRUD

Este documento descreve as etapas e as decisões técnicas tomadas para desenvolver o sistema de Cadastro de Alunos, conforme os requisitos do trabalho prático.

### 1. Definição da Estrutura e Ferramentas

* A linguagem de programação escolhida foi **Python** pela sua flexibilidade e rapidez no desenvolvimento de protótipos e sistemas de gestão de dados.
* A biblioteca **Pandas** foi adotada como ferramenta principal para a manipulação dos dados em memória (DataFrame), devido à sua eficiência em operações de tabela.
* O arquivo `alunos_cadastrados.csv` foi definido como o meio de persistência, garantindo que os registros sejam mantidos entre as sessões do programa.
* A inicialização do sistema inclui uma função para **carregar o DataFrame** do CSV. Se o arquivo não existir, um DataFrame vazio com a estrutura correta é criado.

### 2. Gerenciamento de Identificação e Dados

* O **Número de Matrícula** foi estabelecido como a chave primária (índice) do DataFrame.
* A função de geração de matrícula garante que o número seja **automático e sequencial**, sendo o maior índice existente incrementado em 1.
* A entrada de dados de um novo aluno é intermediada por um **dicionário (`dict`)**, que facilita a validação e organização dos campos antes da inserção na tabela.
* As informações obrigatórias para cadastro incluem: Nome, Rua, Número, Bairro, Cidade, UF, Telefone e Email.

### 3. Implementação do Fluxo de Controle

* O menu principal (INSERIR, PESQUISAR, SAIR) é gerenciado por um **loop infinito (`while True`)** na função `main()`, que só é encerrado pela opção SAIR.
* Qualquer alteração bem-sucedida nos dados (inserção, edição, remoção) dispara a função de salvamento, que **atualiza o arquivo CSV imediatamente**.

### 4. Conformidade e Funcionalidades CRUD

* **Funcionalidade INSERIR:** Adiciona o novo registro ao DataFrame e salva.
* **Funcionalidade PESQUISAR:** Permite a busca por **Matrícula** (diretamente no índice) ou **Nome**.
    * A busca por nome utiliza métodos de *string* do Pandas para garantir que seja **case-insensitive**, atendendo ao requisito de flexibilidade na consulta.
* **Funcionalidade EDITAR:**
    * O sistema pergunta **qual campo específico** o usuário deseja alterar (mantendo o restante inalterado).
    * O campo Matrícula é **excluído** das opções de edição.
* **Funcionalidade REMOVER:**
    * O processo é precedido por uma **confirmação de segurança** por parte do usuário.
    * A remoção é permanente, deletando o registro tanto do DataFrame quanto do arquivo CSV.