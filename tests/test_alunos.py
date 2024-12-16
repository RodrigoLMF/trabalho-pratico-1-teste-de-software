import unittest
from alunos import (
    cadastrar_aluno, listar_alunos, remover_aluno, buscar_aluno_por_nome,
    total_alunos, atualizar_nome_aluno, verificar_aluno_existe, listar_alunos_por_matricula_ordenada
)

class TestAlunos(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente para os testes.
        Limpa o dicionário de alunos antes de cada teste.
        """
        global alunos
        alunos = {}

    def test_cadastrar_aluno(self):
        """Testa a função de cadastro de aluno."""
        resposta = cadastrar_aluno("2024001", "Rodrigo Ferreira")
        self.assertEqual(resposta, resposta)

    def test_cadastrar_aluno_duplicado(self):
        """Testa o cadastro de aluno com matrícula duplicada."""
        cadastrar_aluno("2024002", "Maria Silva")
        resposta = cadastrar_aluno("2024002", "Ana Souza")
        self.assertEqual(resposta, "Aluno com matrícula 2024002 já está cadastrado.")

    def test_listar_alunos(self):
        """Testa a listagem de alunos cadastrados."""
        cadastrar_aluno("2024001", "Rodrigo Ferreira")
        cadastrar_aluno("2024002", "Maria Silva")
        lista = listar_alunos()
        self.assertEqual(len(lista), 2)
        self.assertIn("2024001", lista)
        self.assertIn("2024002", lista)

    def test_remover_aluno(self):
        """Testa a remoção de um aluno."""
        cadastrar_aluno("2024001", "Rodrigo Ferreira")
        resposta = remover_aluno("2024001")
        self.assertEqual(resposta, "Aluno com matrícula 2024001 removido com sucesso.")
        self.assertNotIn("2024001", alunos)

    def test_remover_aluno_nao_encontrado(self):
        """Testa a remoção de um aluno que não existe."""
        resposta = remover_aluno("2024001")
        self.assertEqual(resposta, "Aluno com matrícula 2024001 não encontrado.")

    def test_total_alunos(self):
        """Testa a função que retorna o total de alunos cadastrados."""
        cadastrar_aluno("2024001", "Rodrigo Ferreira")
        cadastrar_aluno("2024002", "Maria Silva")
        self.assertEqual(total_alunos(), 2)

    def test_atualizar_nome_aluno(self):
        """Testa a atualização do nome de um aluno."""
        cadastrar_aluno("2024001", "Rodrigo Ferreira")
        resposta = atualizar_nome_aluno("2024001", "Rodrigo Macêdo")
        self.assertEqual(resposta, "Nome do aluno atualizado para Rodrigo Macêdo.")

    def test_verificar_aluno_existe(self):
        """Testa a verificação se um aluno está cadastrado."""
        cadastrar_aluno("2024001", "Rodrigo Ferreira")
        existe = verificar_aluno_existe("2024001")
        nao_existe = verificar_aluno_existe("2024002")
        self.assertTrue(existe)

if __name__ == "__main__":
    unittest.main()

