import unittest
from core.enums import TipoSessao
from core.models import Configuracao, Sessao
from core.state_machine import PomodoroStateMachine

class TestCore(unittest.TestCase):
    def test_duracao_em_segundos(self):
        config = Configuracao(foco_minutos=25, pausa_curta_minutos=5, pausa_longa_minutos=15)
        self.assertEqual(config.obter_duracao_segundos(TipoSessao.FOCO), 1500)
        self.assertEqual(config.obter_duracao_segundos(TipoSessao.PAUSA_CURTA), 300)
        self.assertEqual(config.obter_duracao_segundos(TipoSessao.PAUSA_LONGA), 900)

    def test_ciclo_completo_com_pausa_longa_no_quarto_foco(self):
        config = Configuracao(ciclos_ate_pausa_longa=4)
        sm = PomodoroStateMachine(config)
        # Estado inicial deve ser FOCO
        self.assertEqual(sm.sessao_atual, TipoSessao.FOCO)
        self.assertEqual(sm.ciclos_foco_concluidos, 0)
        # Ciclos 1, 2 e 3: FOCO -> PAUSA_CURTA -> FOCO
        for ciclo in range(1, 4):
            self.assertEqual(sm.avancar_ciclo(), TipoSessao.PAUSA_CURTA)
            self.assertEqual(sm.ciclos_foco_concluidos, ciclo)
            self.assertEqual(sm.avancar_ciclo(), TipoSessao.FOCO)
        # Ciclo 4: FOCO -> PAUSA_LONGA -> FOCO
        self.assertEqual(sm.avancar_ciclo(), TipoSessao.PAUSA_LONGA)
        self.assertEqual(sm.ciclos_foco_concluidos, 4)
        self.assertEqual(sm.avancar_ciclo(), TipoSessao.FOCO)

    def test_reiniciar_fluxo(self):
        sm = PomodoroStateMachine(Configuracao())
        sm.avancar_ciclo()  # vai para PAUSA_CURTA e 1 ciclo concluído
        sm.reiniciar_fluxo()
        self.assertEqual(sm.sessao_atual, TipoSessao.FOCO)
        self.assertEqual(sm.ciclos_foco_concluidos, 0)

    def test_criacao_de_sessao(self):
        sessao = Sessao(tipo=TipoSessao.FOCO, duracao_segundos=1500)
        self.assertFalse(sessao.concluida)
        self.assertIsNotNone(sessao.iniciada_em)
        self.assertIsNone(sessao.finalizada_em)
        
if __name__ == "__main__":
    unittest.main()