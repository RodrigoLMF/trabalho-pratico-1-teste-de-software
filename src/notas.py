notas = {}

def registrar_nota(matricula, codigo_disciplina, nota):
    """Registra a nota de um aluno em uma disciplina."""
    if matricula not in notas:
        notas[matricula] = {}
    if codigo_disciplina not in notas[matricula]:
        notas[matricula][codigo_disciplina] = []
    notas[matricula][codigo_disciplina].append(nota)
    return f"Nota {nota} registrada com sucesso."

def listar_notas_aluno(matricula):
    """Lista as notas de um aluno."""
    return notas.get(matricula, {})

