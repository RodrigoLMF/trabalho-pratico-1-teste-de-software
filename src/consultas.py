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

def media_turma_por_disciplina(codigo_disciplina):
    """Calcula a média da turma para uma disciplina específica."""
    if codigo_disciplina not in disciplinas:
        return f"Disciplina com código {codigo_disciplina} não encontrada."
    soma_notas = 0
    total_notas = 0
    for matricula, notas_aluno in notas.items():
        if codigo_disciplina in notas_aluno:
            soma_notas += sum(notas_aluno[codigo_disciplina])
            total_notas += len(notas_aluno[codigo_disciplina])
    if total_notas == 0:
        return f"Nenhuma nota registrada para a disciplina {disciplinas[codigo_disciplina]}."
    return soma_notas / total_notas

def media_geral_todas_disciplinas():
    """Calcula a média geral de todas as disciplinas."""
    medias = {}
    for codigo_disciplina in disciplinas:
        medias[codigo_disciplina] = media_turma_por_disciplina(codigo_disciplina)
    return medias

def melhores_alunos_por_disciplina(codigo_disciplina, top_n=3):
    """Lista os melhores alunos de uma disciplina específica."""
    if codigo_disciplina not in disciplinas:
        return f"Disciplina com código {codigo_disciplina} não encontrada."
    medias_alunos = []
    for matricula, notas_aluno in notas.items():
        if codigo_disciplina in notas_aluno:
            media = sum(notas_aluno[codigo_disciplina]) / len(notas_aluno[codigo_disciplina])
            medias_alunos.append((alunos[matricula], media))
    medias_alunos.sort(key=lambda x: x[1], reverse=True)
    return medias_alunos[:top_n]

def melhores_alunos_geral(top_n=5):
    """Lista os melhores alunos com base na média geral."""
    medias_alunos = []
    for matricula in alunos:
        if matricula in notas:
            soma_notas = 0
            total_notas = 0
            for notas_disciplina in notas[matricula].values():
                soma_notas += sum(notas_disciplina)
                total_notas += len(notas_disciplina)
            if total_notas > 0:
                media_geral = soma_notas / total_notas
                medias_alunos.append((alunos[matricula], media_geral))
    medias_alunos.sort(key=lambda x: x[1], reverse=True)
    return medias_alunos[:top_n]

def ranking_disciplinas_por_turma():
    """Gera um ranking de disciplinas com base na média da turma."""
    ranking = []
    for codigo_disciplina in disciplinas:
        media = media_turma_por_disciplina(codigo_disciplina)
        ranking.append((disciplinas[codigo_disciplina], media))
    ranking.sort(key=lambda x: x[1], reverse=True)
    return ranking

def aluno_com_mais_notas():
    """Encontra o aluno que possui mais notas registradas."""
    max_notas = 0
    aluno_top = None
    for matricula, notas_aluno in notas.items():
        total_notas = sum(len(notas_disciplina) for notas_disciplina in notas_aluno.values())
        if total_notas > max_notas:
            max_notas = total_notas
            aluno_top = alunos[matricula]
    return aluno_top, max_notas

def disciplinas_sem_notas():
    """Lista todas as disciplinas que ainda não possuem notas registradas."""
    disciplinas_sem_registros = []
    for codigo_disciplina in disciplinas:
        if all(codigo_disciplina not in notas_aluno for notas_aluno in notas.values()):
            disciplinas_sem_registros.append(disciplinas[codigo_disciplina])
    return disciplinas_sem_registros

def alunos_sem_notas():
    """Lista todos os alunos que ainda não possuem notas registradas."""
    alunos_sem_registros = []
    for matricula in alunos:
        if matricula not in notas:
            alunos_sem_registros.append(alunos[matricula])
    return alunos_sem_registros
