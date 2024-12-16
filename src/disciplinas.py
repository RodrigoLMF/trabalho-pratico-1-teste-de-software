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

def remover_disciplina(codigo):
    """Remove uma disciplina do sistema."""
    if codigo not in disciplinas:
        return f"Disciplina com código {codigo} não encontrada."
    del disciplinas[codigo]
    return f"Disciplina com código {codigo} removida com sucesso."

def buscar_disciplina_por_nome(nome):
    """Busca disciplinas pelo nome."""
    return {codigo: disciplina for codigo, disciplina in disciplinas.items() if nome.lower() in disciplina.lower()}

def total_disciplinas():
    """Retorna o total de disciplinas cadastradas."""
    return len(disciplinas)

def atualizar_nome_disciplina(codigo, novo_nome):
    """Atualiza o nome de uma disciplina."""
    if codigo not in disciplinas:
        return f"Disciplina com código {codigo} não encontrada."
    disciplinas[codigo] = novo_nome
    return f"Nome da disciplina atualizado para {novo_nome}."

def verificar_disciplina_existe(codigo):
    """Verifica se uma disciplina está cadastrada no sistema."""
    return codigo in disciplinas

def listar_disciplinas_ordenadas_por_codigo():
    """Lista as disciplinas ordenadas pelo código."""
    return dict(sorted(disciplinas.items()))

def listar_disciplinas_ordenadas_por_nome():
    """Lista as disciplinas ordenadas pelo nome."""
    return dict(sorted(disciplinas.items(), key=lambda item: item[1].lower()))

def listar_disciplinas_por_trecho_nome(trecho):
    """Lista disciplinas contendo um trecho específico no nome."""
    return {codigo: nome for codigo, nome in disciplinas.items() if trecho.lower() in nome.lower()}

def listar_disciplinas_com_codigo_maior_que(limite):
    """Lista disciplinas com código maior que o limite especificado."""
    return {codigo: nome for codigo, nome in disciplinas.items() if codigo > limite}

def listar_disciplinas_com_tamanho_nome_maior_que(tamanho):
    """Lista disciplinas com nomes maiores que o tamanho especificado."""
    return {codigo: nome for codigo, nome in disciplinas.items() if len(nome) > tamanho}

def disciplinas_com_codigo_iniciando_por(inicio):
    """Lista disciplinas cujo código inicia com um valor especificado."""
    return {codigo: nome for codigo, nome in disciplinas.items() if str(codigo).startswith(str(inicio))}
