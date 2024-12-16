import unittest
from notas import (
    registrar_nota, listar_notas_aluno, listar_todas_notas, calcular_media_aluno, remover_nota,
    listar_disciplinas_com_notas, verificar_se_tem_notas, limpar_notas_disciplina
)

class TestNotas(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente para os testes.
        Limpa o dicionário de notas antes de cada teste.
        """
        global notas
        notas = {}

    def test_registrar_nota(self):
        """Testa o registro de uma nota para um aluno em uma disciplina."""
        resposta = registrar_nota("12345", "CS101", 8.5)
        self.assertEqual(resposta, "Nota 8.5 registrada com sucesso.")
        self.assertIn("12345", notas)
        self.assertIn("CS101", notas["12345"])
        self.assertEqual(notas["12345"]["CS101"], [8.5])

    def test_listar_notas_aluno(self):
        """Testa a listagem das notas de um aluno."""
        registrar_nota("12345", "CS101", 8.5)
        registrar_nota("12345", "CS102", 7.0)
        notas_aluno = listar_notas_aluno("12345")
        self.assertEqual(notas_aluno, {"CS101": [8.5], "CS102": [7.0]})

    def test_listar_todas_notas(self):
        """Testa a listagem de todas as notas registradas no sistema."""
        registrar_nota("12345", "CS101", 8.5)
        registrar_nota("67890", "CS102", 9.0)
        todas_notas = listar_todas_notas()
        self.assertEqual(len(todas_notas), 2)
        self.assertIn("12345", todas_notas)
        self.assertIn("67890", todas_notas)

    def test_calcular_media_aluno(self):
        """Testa o cálculo da média das notas de um aluno em uma disciplina."""
        registrar_nota("12345", "CS101", 8.5)
        registrar_nota("12345", "CS101", 7.5)
        media = calcular_media_aluno("12345", "CS101")
        self.assertEqual(media, 8.0)

    def test_remover_nota(self):
        """Testa a remoção de uma nota específica de um aluno."""
        registrar_nota("12345", "CS101", 8.5)
        registrar_nota("12345", "CS101", 7.0)
        resposta = remover_nota("12345", "CS101", 0)
        self.assertEqual(resposta, "Nota removida com sucesso.")
        self.assertEqual(notas["12345"]["CS101"], [7.0])

    def test_remover_nota_invalida(self):
        """Testa a remoção de uma nota inválida (índice fora de alcance)."""
        registrar_nota("12345", "CS101", 8.5)
        resposta = remover_nota("12345", "CS101", 1)
        self.assertEqual(resposta, "Não foi possível remover a nota.")

    def test_listar_disciplinas_com_notas(self):
        """Testa a listagem de disciplinas em que o aluno possui notas registradas."""
        registrar_nota("12345", "CS101", 8.5)
        registrar_nota("12345", "CS102", 7.0)
        disciplinas = listar_disciplinas_com_notas("12345")
        self.assertEqual(disciplinas, ["CS101", "CS102"])

    def test_verificar_se_tem_notas(self):
        """Testa a verificação se um aluno possui notas registradas em uma disciplina."""
        registrar_nota("12345", "CS101", 8.5)
        tem_notas = verificar_se_tem_notas("12345", "CS101")
        nao_tem_notas = verificar_se_tem_notas("12345", "CS102")
        self.assertTrue(tem_notas)
        self.assertFalse(nao_tem_notas)

if __name__ == "__main__":
    unittest.main()

