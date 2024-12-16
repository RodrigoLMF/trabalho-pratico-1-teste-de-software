import unittest
from disciplinas import (
    adicionar_disciplina, listar_disciplinas, remover_disciplina, buscar_disciplina_por_nome,
    total_disciplinas, atualizar_nome_disciplina, verificar_disciplina_existe, listar_disciplinas_ordenadas_por_codigo
)

class TestDisciplinas(unittest.TestCase):

    def setUp(self):
        """
        Configura o ambiente para os testes.
        Limpa o dicionário de disciplinas antes de cada teste.
        """
        global disciplinas
        disciplinas = {}

    def test_adicionar_disciplina(self):
        """Testa a função de adicionar disciplina."""
        resposta = adicionar_disciplina("CS101", "Algoritmo e Estruturas de Dados")
        self.assertEqual(resposta, "Disciplina Algoritmo e Estruturas de Dados adicionada com sucesso.")
        self.assertIn("CS101", disciplinas)
        self.assertEqual(disciplinas["CS101"], "Algoritmo e Estruturas de Dados")

    def test_adicionar_disciplina_duplicada(self):
        """Testa a tentativa de adicionar uma disciplina com código duplicado."""
        adicionar_disciplina("CS102", "Fundamentos de Programação")
        resposta = adicionar_disciplina("CS102", "Estruturas de Dados Avançadas")
        self.assertEqual(resposta, "Disciplina com código CS102 já existe.")

    def test_listar_disciplinas(self):
        """Testa a listagem de disciplinas cadastradas."""
        adicionar_disciplina("CS101", "Algoritmo e Estruturas de Dados")
        adicionar_disciplina("CS102", "Fundamentos de Programação")
        lista = listar_disciplinas()
        self.assertEqual(len(lista), 2)
        self.assertIn("CS101", lista)
        self.assertIn("CS102", lista)

    def test_remover_disciplina(self):
        """Testa a remoção de uma disciplina."""
        adicionar_disciplina("CS101", "Algoritmo e Estruturas de Dados")
        resposta = remover_disciplina("CS101")
        self.assertEqual(resposta, "Disciplina com código CS101 removida com sucesso.")
        self.assertNotIn("CS101", disciplinas)

    def test_remover_disciplina_nao_encontrada(self):
        """Testa a remoção de uma disciplina que não existe."""
        resposta = remover_disciplina("CS101")
        self.assertEqual(resposta, "Disciplina com código CS101 não encontrada.")

    def test_total_disciplinas(self):
        """Testa a função que retorna o total de disciplinas cadastradas."""
        adicionar_disciplina("CS101", "Algoritmo e Estruturas de Dados")
        adicionar_disciplina("CS102", "Fundamentos de Programação")
        self.assertEqual(total_disciplinas(), 2)

    def test_atualizar_nome_disciplina(self):
        """Testa a atualização do nome de uma disciplina."""
        adicionar_disciplina("CS101", "Algoritmo e Estruturas de Dados")
        resposta = atualizar_nome_disciplina("CS101", "Algoritmos e Estruturas Avançadas")
        self.assertEqual(resposta, "Nome da disciplina atualizado para Algoritmos e Estruturas Avançadas.")

    def test_verificar_disciplina_existe(self):
        """Testa a verificação se uma disciplina está cadastrada."""
        adicionar_disciplina("CS101", "Algoritmo e Estruturas de Dados")
        existe = verificar_disciplina_existe("CS101")
        nao_existe = verificar_disciplina_existe("CS103")
        self.assertTrue(existe)
        self.assertFalse(nao_existe)

if __name__ == "__main__":
    unittest.main()
