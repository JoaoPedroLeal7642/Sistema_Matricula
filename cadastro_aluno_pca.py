import pandas as pd
import os # Biblioteca para checar se o arquivo existe

#### Variáveis Globais/Constantes ####
NOME_ARQUIVO = 'alunos_cadastrados.csv'

# Lista das colunas (campos) do aluno, exceto a Matrícula
CAMPOS_ALUNO = [
    'Nome', 'Rua', 'Número', 'Bairro', 'Cidade', 'UF', 'Telefone', 'Email'
]

#### 1. Funções de Suporte (Carregamento e Matrícula) ###

def carregar_dados():
    """
    Carrega o DataFrame (tabela) do arquivo CSV. 
    Se o arquivo não existir, cria um DataFrame vazio com as colunas corretas.
    """
    if os.path.exists(NOME_ARQUIVO):
        print(f"Lendo dados de {NOME_ARQUIVO}...")
        # A matrícula será o índice, e a primeira coluna do CSV
        df = pd.read_csv(NOME_ARQUIVO, index_col='Matricula')
    else:
        print("Arquivo de dados não encontrado. Criando um novo DataFrame vazio.")
        colunas = ['Matricula'] + CAMPOS_ALUNO
        df = pd.DataFrame(columns=colunas).set_index('Matricula') # Cria o DF vazio com as colunas
    return df

def salvar_dados(df):
    """Salva o DataFrame de volta no arquivo CSV."""
    df.to_csv(NOME_ARQUIVO)
    print("\n[SUCESSO] Dados salvos no arquivo com sucesso!")

def gerar_nova_matricula(df):
    """Gera um novo número de matrícula sequencial."""
    if df.empty:
        return 1  # Primeira matrícula
    else:
        # A nova matrícula é o maior índice (Matricula) + 1
        return df.index.max() + 1

### 2. Funções CRUD ###

def inserir_aluno(df):
    """
    Permite ao usuário inserir um novo aluno.
    Gera a matrícula automaticamente e coleta os demais dados.
    """
    print("\n--- INSERIR NOVO ALUNO ---")
    
    # 1. Geração Automática de Matrícula
    nova_matricula = gerar_nova_matricula(df)
    print(f"Matrícula gerada automaticamente: **{nova_matricula}**")

    # 2. Coleta dos Dados do Aluno (Dicionário)
    novo_aluno = {}
    for campo in CAMPOS_ALUNO:
        while True:
            dado = input(f"Digite o {campo}: ").strip()
            if dado:
                novo_aluno[campo] = dado
                break
            else:
                print("Campo não pode ser vazio. Tente novamente.")

    # 3. Adiciona o novo aluno ao DataFrame
    # Converte o dicionário em uma Series e usa a matrícula como índice
    nova_linha = pd.Series(novo_aluno, name=nova_matricula)
    df.loc[nova_matricula] = nova_linha

    print(f"\n[OK] Aluno **{novo_aluno['Nome']}** inserido com a Matrícula {nova_matricula}.")
    return df

def pesquisar_aluno(df):
    """
    Permite pesquisar um aluno por Matrícula ou Nome.
    Retorna a Matrícula e o DataFrame filtrado, ou None.
    """
    print("\n--- PESQUISAR ALUNO ---")
    
    if df.empty:
        print("[ERRO] Não há alunos cadastrados.")
        return None, None
        
    termo = input("Digite o NÚMERO DE MATRÍCULA ou o NOME do aluno: ").strip()

    aluno_encontrado = None
    matricula_encontrada = None
    
    try:
        # Tenta pesquisar por Matrícula (se for um número)
        matricula = int(termo)
        if matricula in df.index:
            aluno_encontrado = df.loc[[matricula]] # Retorna um DF de uma linha
            matricula_encontrada = matricula
    except ValueError:
        # Se não for um número, pesquisa por Nome (case-insensitive)
        
        # Filtra o DF onde a coluna 'Nome' em lowercase contém o termo em lowercase
        # Nota: O requisito pede apenas que 'Nome' ou 'nome' ou 'NOME' apresentem o mesmo resultado,
        # o que implica uma comparação de igualdade, não de 'contém'. 
        # Vou implementar a comparação de igualdade, que é mais precisa:
        mask = df['Nome'].str.lower() == termo.lower()
        
        if mask.any():
            aluno_encontrado = df[mask]
            
            if len(aluno_encontrado) > 1:
                print("\n[ALERTA] Múltiplos alunos encontrados com este nome. Exibindo o primeiro:")
            
            # Pega o primeiro índice (Matrícula) do aluno encontrado
            matricula_encontrada = aluno_encontrado.index[0]
            aluno_encontrado = aluno_encontrado.iloc[[0]] # Pega apenas o primeiro

    if aluno_encontrado is not None and not aluno_encontrado.empty:
        print("\n--- DADOS DO ALUNO ENCONTRADO ---")
        print(f"Matrícula: **{matricula_encontrada}**")
        # Exibe os dados de forma formatada
        print(aluno_encontrado.T.to_string(header=False)) 
        print("-----------------------------------")
        
        return matricula_encontrada, aluno_encontrado
    else:
        print(f"\n[INFO] Aluno com Matrícula/Nome '{termo}' NÃO ENCONTRADO.")
        return None, None

def editar_aluno(df, matricula):
    """Permite ao usuário editar um dado específico de um aluno."""
    print("\n--- EDITAR DADOS DO ALUNO ---")
    
    # 1. Cria o menu de edição
    campos_editaveis = CAMPOS_ALUNO
    print("\nEscolha o dado a ser editado:")
    for i, campo in enumerate(campos_editaveis):
        # Exibe o valor atual para ajudar o usuário
        valor_atual = df.loc[matricula, campo]
        print(f"{i + 1} - {campo} (Atual: {valor_atual})")
    print("0 - CANCELAR EDIÇÃO")
    
    # 2. Recebe a escolha do usuário
    while True:
        try:
            escolha = int(input("Digite o número da opção desejada: "))
            if 1 <= escolha <= len(campos_editaveis):
                campo_a_editar = campos_editaveis[escolha - 1]
                break
            elif escolha == 0:
                print("[INFO] Edição cancelada.")
                return df # Retorna o DF sem modificação
            else:
                print("Opção inválida.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            
    # 3. Solicita o novo valor
    novo_valor = input(f"Digite o NOVO valor para **{campo_a_editar}**: ").strip()
    
    if novo_valor:
        # 4. Aplica a mudança no DataFrame
        df.loc[matricula, campo_a_editar] = novo_valor
        print(f"\n[OK] Campo '{campo_a_editar}' alterado para '{novo_valor}' (Matrícula {matricula}).")
    else:
        print("[INFO] Valor vazio. Nenhum dado foi alterado.")
        
    return df

def remover_aluno(df, matricula):
    """Permite ao usuário remover um aluno do DataFrame."""
    print("\n--- REMOVER ALUNO ---")
    
    confirmacao = input(f"ATENÇÃO: Deseja REALMENTE remover o aluno de Matrícula **{matricula}**? (S/N): ").upper().strip()
    
    if confirmacao == 'S':
        # Remove a linha pelo índice (Matrícula)
        df.drop(index=matricula, inplace=True)
        print(f"\n[SUCESSO] Aluno de Matrícula {matricula} removido permanentemente.")
    else:
        print("[INFO] Remoção cancelada.")
        
    return df

### 3. Função Principal (Menu) ###

def main():
    """Função principal que gerencia o fluxo do programa e o menu."""
    
    # Carrega os dados existentes no início
    df_alunos = carregar_dados()

    while True:
        print("\n" + "="*40)
        print("🏛️  SISTEMA DE CADASTRO DE ALUNOS")
        print("="*40)
        print("1 - INSERIR NOVO ALUNO")
        print("2 - PESQUISAR, EDITAR ou REMOVER ALUNO")
        print("3 - SAIR")
        print("="*40)
        
        opcao = input("Digite a opção desejada: ").strip()
        
        if opcao == '1':
            df_alunos = inserir_aluno(df_alunos)
            salvar_dados(df_alunos)
            
        elif opcao == '2':
            # A pesquisa retorna a matrícula e o DF (1 linha) do aluno
            matricula, aluno_encontrado_df = pesquisar_aluno(df_alunos)
            
            if matricula is not None:
                while True:
                    print("\n[AÇÃO] Deseja EDITAR (E), REMOVER (R) ou VOLTAR ao Menu (V)?")
                    acao = input("Digite a opção (E/R/V): ").upper().strip()
                    
                    if acao == 'E':
                        df_alunos = editar_aluno(df_alunos, matricula)
                        salvar_dados(df_alunos)
                        break
                    elif acao == 'R':
                        df_alunos = remover_aluno(df_alunos, matricula)
                        salvar_dados(df_alunos)
                        break
                    elif acao == 'V':
                        print("[INFO] Voltando ao menu principal.")
                        break
                    else:
                        print("Opção inválida.")

        elif opcao == '3':
            print("\nEncerrando o programa. Até logo!")
            break
            
        else:
            print("\nOpção inválida. Por favor, escolha 1, 2 ou 3.")

### Execução do Programa ###
if __name__ == "__main__":
    main()