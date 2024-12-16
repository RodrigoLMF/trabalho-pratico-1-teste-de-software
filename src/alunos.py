alunos = {}

def cadastrar_aluno(matricula, nome):
    """Cadastra um novo aluno no sistema."""
    if matricula in alunos:
        return f"Aluno com matrícula {matricula} já está cadastrado."
    alunos[matricula] = nome
    return f"Aluno {nome} cadastrado com sucesso."

def listar_alunos():
    """Lista todos os alunos cadastrados."""
    return alunos

def remover_aluno(matricula):
    """Remove um aluno do sistema."""
    if matricula not in alunos:
        return f"Aluno com matrícula {matricula} não encontrado."
    del alunos[matricula]
    return f"Aluno com matrícula {matricula} removido com sucesso."

def buscar_aluno_por_nome(nome):
    """Busca alunos pelo nome."""
    return {matricula: aluno for matricula, aluno in alunos.items() if nome.lower() in aluno.lower()}

def total_alunos():
    """Retorna o total de alunos cadastrados."""
    return len(alunos)

def atualizar_nome_aluno(matricula, novo_nome):
    """Atualiza o nome de um aluno."""
    if matricula not in alunos:
        return f"Aluno com matrícula {matricula} não encontrado."
    alunos[matricula] = novo_nome
    return f"Nome do aluno atualizado para {novo_nome}."

def verificar_aluno_existe(matricula):
    """Verifica se um aluno está cadastrado no sistema."""
    return matricula in alunos

def listar_alunos_por_matricula_ordenada():
    """Lista os alunos ordenados pela matrícula."""
    return dict(sorted(alunos.items()))

def listar_alunos_por_nome_ordenado():
    """Lista os alunos ordenados pelo nome."""
    return dict(sorted(alunos.items(), key=lambda item: item[1].lower()))
