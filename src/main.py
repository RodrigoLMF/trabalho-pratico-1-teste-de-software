from src.alunos import cadastrar_aluno, listar_alunos
from src.disciplinas import adicionar_disciplina, listar_disciplinas
from src.notas import registrar_nota, listar_notas_aluno
from src.consultas import consultar_boletim, listar_alunos_aprovados, listar_alunos_reprovados

if __name__ == "__main__":
    # Cadastro de alunos
    print(cadastrar_aluno(1, "João Silva"))
    print(cadastrar_aluno(2, "Maria Oliveira"))

    # Cadastro de disciplinas
    print(adicionar_disciplina("MAT101", "Matemática"))
    print(adicionar_disciplina("POR101", "Português"))

    # Registro de notas
    print(registrar_nota(1, "MAT101", 8.5))
    print(registrar_nota(1, "MAT101", 7.0))
    print(registrar_nota(2, "MAT101", 5.0))

    # Consultas
    print(consultar_boletim(1))
    print(consultar_boletim(2))
    print(f"Aprovados em Matemática: {listar_alunos_aprovados('MAT101', 6.0)}")
    print(f"Reprovados em Matemática: {listar_alunos_reprovados('MAT101', 6.0)}")

