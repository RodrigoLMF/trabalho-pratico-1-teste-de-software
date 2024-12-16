import unittest
from src.consultas import consultar_boletim, listar_alunos_aprovados, listar_alunos_reprovados, calcular_media_turma, top_n_melhores_alunos, alunos_com_melhor_desempenho, ranking_disciplinas_por_desempenho, media_turma_por_disciplina, media_geral_todas_disciplinas, melhores_alunos_por_disciplina, melhores_alunos_geral, ranking_disciplinas_por_turma, aluno_com_mais_notas, disciplinas_sem_notas, alunos_sem_notas
from src.alunos import alunos
from src.disciplinas import disciplinas
from src.notas import notas

class TestConsultas(unittest.TestCase):
    
    def test_listar_alunos_aprovados(self):
        # Testa a listagem de alunos aprovados em uma disciplina
        codigo_disciplina = "MAT101"
        media_minima = 7.0
        aprovados = listar_alunos_aprovados(codigo_disciplina, media_minima)
        self.assertIsInstance(aprovados, list)
        self.assertTrue(all(aluno in alunos.values() for aluno in aprovados))

    def test_listar_alunos_reprovados(self):
        # Testa a listagem de alunos reprovados em uma disciplina
        codigo_disciplina = "MAT101"
        media_minima = 7.0
        reprovados = listar_alunos_reprovados(codigo_disciplina, media_minima)
        self.assertIsInstance(reprovados, list)
        self.assertTrue(all(aluno in alunos.values() for aluno in reprovados))


    def test_alunos_com_melhor_desempenho(self):
        # Testa a listagem dos alunos com melhor desempenho geral
        melhores = alunos_com_melhor_desempenho()
        self.assertIsInstance(melhores, list)

    def test_media_geral_todas_disciplinas(self):
        # Testa o cálculo da média geral de todas as disciplinas
        medias = media_geral_todas_disciplinas()
        self.assertIsInstance(medias, dict)



    def test_disciplinas_sem_notas(self):
        # Testa a listagem das disciplinas sem notas registradas
        disciplinas_sem = disciplinas_sem_notas()
        self.assertIsInstance(disciplinas_sem, list)
        self.assertTrue(all(disciplina in disciplinas.values() for disciplina in disciplinas_sem))

    def test_alunos_sem_notas(self):
        # Testa a listagem de alunos sem notas registradas
        alunos_sem = alunos_sem_notas()
        self.assertIsInstance(alunos_sem, list)
        self.assertTrue(all(aluno in alunos.values() for aluno in alunos_sem))

if __name__ == "__main__":
    unittest.main()

