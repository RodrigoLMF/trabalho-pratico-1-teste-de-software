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

