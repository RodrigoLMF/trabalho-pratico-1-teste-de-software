disciplinas = {}

def adicionar_disciplina(codigo, nome):
    """Adiciona uma nova disciplina ao sistema."""
    if codigo in disciplinas:
        return f"Disciplina com código {codigo} já existe."
    disciplinas[codigo] = nome
    return f"Disciplina {nome} adicionada com sucesso."

def listar_disciplinas():
    """Lista todas as disciplinas cadastradas."""
    return disciplinas

