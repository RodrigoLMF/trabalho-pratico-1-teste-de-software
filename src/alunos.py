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

