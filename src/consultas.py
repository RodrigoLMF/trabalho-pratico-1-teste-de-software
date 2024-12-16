from src.alunos import alunos
from src.disciplinas import disciplinas
from src.notas import notas

def consultar_boletim(matricula):
    """Consulta o boletim de um aluno."""
    if matricula not in alunos:
        return f"Aluno com matrícula {matricula} não encontrado."
    if matricula not in notas:
        return f"Aluno {alunos[matricula]} não possui notas registradas."
    boletim = f"Boletim do aluno {alunos[matricula]}:\n"
    for codigo, notas_disciplina in notas[matricula].items():
        media = sum(notas_disciplina) / len(notas_disciplina)
        boletim += f"  - {disciplinas[codigo]}: Média = {media:.2f}\n"
    return boletim

def listar_alunos_aprovados(codigo_disciplina, media_minima):
    """Lista os alunos aprovados em uma disciplina."""
    aprovados = []
    for matricula, notas_aluno in notas.items():
        if codigo_disciplina in notas_aluno:
            media = sum(notas_aluno[codigo_disciplina]) / len(notas_aluno[codigo_disciplina])
            if media >= media_minima:
                aprovados.append(alunos[matricula])
    return aprovados

def listar_alunos_reprovados(codigo_disciplina, media_minima):
    """Lista os alunos reprovados em uma disciplina."""
    reprovados = []
    for matricula, notas_aluno in notas.items():
        if codigo_disciplina in notas_aluno:
            media = sum(notas_aluno[codigo_disciplina]) / len(notas_aluno[codigo_disciplina])
            if media < media_minima:
                reprovados.append(alunos[matricula])
    return reprovados

def calcular_media_turma(codigo_disciplina):
    """Calcula a média geral da turma em uma disciplina."""
    if codigo_disciplina not in disciplinas:
        return f"Disciplina com código {codigo_disciplina} não encontrada."
    total_notas = 0
    quantidade_notas = 0
    for matricula, notas_aluno in notas.items():
        if codigo_disciplina in notas_aluno:
            total_notas += sum(notas_aluno[codigo_disciplina])
            quantidade_notas += len(notas_aluno[codigo_disciplina])
    if quantidade_notas == 0:
        return f"Nenhuma nota registrada para a disciplina {disciplinas[codigo_disciplina]}."
    return total_notas / quantidade_notas

def alunos_sem_notas():
    """Lista alunos que ainda não possuem notas registradas."""
    sem_notas = [alunos[matricula] for matricula in alunos if matricula not in notas]
    return sem_notas

def disciplinas_sem_notas():
    """Lista disciplinas que ainda não possuem notas registradas."""
    disciplinas_sem_nota = set(disciplinas.keys())
    for matricula, notas_aluno in notas.items():
        disciplinas_sem_nota -= set(notas_aluno.keys())
    return [disciplinas[codigo] for codigo in disciplinas_sem_nota]

def top_n_melhores_alunos(codigo_disciplina, n):
    """Lista os N melhores alunos em uma disciplina."""
    if codigo_disciplina not in disciplinas:
        return f"Disciplina com código {codigo_disciplina} não encontrada."
    medias = []
    for matricula, notas_aluno in notas.items():
        if codigo_disciplina in notas_aluno:
            media = sum(notas_aluno[codigo_disciplina]) / len(notas_aluno[codigo_disciplina])
            medias.append((alunos[matricula], media))
    medias.sort(key=lambda x: x[1], reverse=True)
    return medias[:n]

def alunos_com_melhor_desempenho():
    """Lista os alunos com melhor desempenho geral."""
    desempenho = {}
    for matricula, notas_aluno in notas.items():
        total_notas = sum(sum(notas_disciplina) for notas_disciplina in notas_aluno.values())
        total_disciplinas = sum(len(notas_disciplina) for notas_disciplina in notas_aluno.values())
        desempenho[matricula] = total_notas / total_disciplinas if total_disciplinas > 0 else 0
    melhor_desempenho = max(desempenho.values(), default=0)
    return [alunos[matricula] for matricula, media in desempenho.items() if media == melhor_desempenho]

def ranking_disciplinas_por_desempenho():
    """Retorna o ranking de disciplinas por média geral."""
    medias_disciplinas = {}
    for codigo in disciplinas:
        media = calcular_media_turma(codigo)
        if isinstance(media, (int, float)):
            medias_disciplinas[codigo] = media
    return sorted(medias_disciplinas.items(), key=lambda x: x[1], reverse=True)
