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

def calcular_media_disciplina(codigo_disciplina):
    """Calcula a média geral das notas de uma disciplina."""
    soma_notas = 0
    total_notas = 0
    for matricula in notas:
        if codigo_disciplina in notas[matricula]:
            soma_notas += sum(notas[matricula][codigo_disciplina])
            total_notas += len(notas[matricula][codigo_disciplina])
    if total_notas == 0:
        return f"Sem notas registradas para a disciplina {codigo_disciplina}."
    return soma_notas / total_notas

def listar_melhor_aluno_disciplina(codigo_disciplina):
    """Lista o aluno com a maior média em uma disciplina."""
    melhor_aluno = None
    melhor_media = -1
    for matricula, disciplinas in notas.items():
        if codigo_disciplina in disciplinas:
            media = sum(disciplinas[codigo_disciplina]) / len(disciplinas[codigo_disciplina])
            if media > melhor_media:
                melhor_media = media
                melhor_aluno = matricula
    if melhor_aluno is None:
        return f"Nenhum aluno com notas registradas na disciplina {codigo_disciplina}."
    return melhor_aluno, melhor_media

def listar_melhores_alunos_por_turma():
    """Lista os melhores alunos por turma com base na média geral."""
    medias_gerais = {}
    for matricula, disciplinas in notas.items():
        soma = sum(sum(notas_disciplina) for notas_disciplina in disciplinas.values())
        total = sum(len(notas_disciplina) for notas_disciplina in disciplinas.values())
        medias_gerais[matricula] = soma / total if total > 0 else 0
    melhor_media = max(medias_gerais.values(), default=-1)
    melhores_alunos = [matricula for matricula, media in medias_gerais.items() if media == melhor_media]
    return melhores_alunos, melhor_media

def listar_alunos_com_notas_incompletas():
    """Lista alunos com disciplinas registradas mas sem notas."""
    alunos_incompletos = []
    for matricula, disciplinas in notas.items():
        for notas_disciplina in disciplinas.values():
            if len(notas_disciplina) == 0:
                alunos_incompletos.append(matricula)
                break
    return alunos_incompletos
