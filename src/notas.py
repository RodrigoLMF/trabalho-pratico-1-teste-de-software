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

def listar_todas_notas():
    """Lista todas as notas registradas."""
    return notas

def calcular_media_aluno(matricula, codigo_disciplina):
    """Calcula a média das notas de um aluno em uma disciplina."""
    if matricula not in notas or codigo_disciplina not in notas[matricula]:
        return f"Sem notas registradas para o aluno na disciplina {codigo_disciplina}."
    notas_disciplina = notas[matricula][codigo_disciplina]
    return sum(notas_disciplina) / len(notas_disciplina)

def remover_nota(matricula, codigo_disciplina, indice_nota):
    """Remove uma nota específica de um aluno em uma disciplina."""
    if matricula in notas and codigo_disciplina in notas[matricula]:
        if 0 <= indice_nota < len(notas[matricula][codigo_disciplina]):
            notas[matricula][codigo_disciplina].pop(indice_nota)
            return f"Nota removida com sucesso."
    return f"Não foi possível remover a nota."

def listar_disciplinas_com_notas(matricula):
    """Lista disciplinas em que o aluno possui notas registradas."""
    return list(notas.get(matricula, {}).keys())

def verificar_se_tem_notas(matricula, codigo_disciplina):
    """Verifica se um aluno possui notas registradas em uma disciplina."""
    return codigo_disciplina in notas.get(matricula, {})

def limpar_notas_disciplina(codigo_disciplina):
    """Remove todas as notas de uma disciplina."""
    for matricula in notas:
        if codigo_disciplina in notas[matricula]:
            del notas[matricula][codigo_disciplina]
    return f"Notas da disciplina {codigo_disciplina} removidas com sucesso."

def listar_notas_por_disciplina(codigo_disciplina):
    """Lista as notas de todos os alunos em uma disciplina."""
    resultado = {}
    for matricula, disciplinas in notas.items():
        if codigo_disciplina in disciplinas:
            resultado[matricula] = disciplinas[codigo_disciplina]
    return resultado
