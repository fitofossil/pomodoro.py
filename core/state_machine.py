from core.enums import TipoSessao
from core.models import Configuracao

class PomodoroStateMachine:
    def __init__(self, config: Configuracao):
        self.config = config
        self._sessao_atual: TipoSessao = TipoSessao.FOCO
        self._ciclos_foco_concluidos: int = 0

    @property
    def sessao_atual(self) -> TipoSessao:
        return self._sessao_atual

    @property
    def ciclos_foco_concluidos(self) -> int:
        return self._ciclos_foco_concluidos

    @property
    def duracao_atual_segundos(self) -> int:
        return self.config.obter_duracao_segundos(self._sessao_atual)

    def avancar_ciclo(self) -> TipoSessao:
        if self._sessao_atual == TipoSessao.FOCO:
            self._ciclos_foco_concluidos += 1
            if self._ciclos_foco_concluidos % self.config.ciclos_ate_pausa_longa == 0:
                self._sessao_atual = TipoSessao.PAUSA_LONGA
            else:
                self._sessao_atual = TipoSessao.PAUSA_CURTA
        else:
            self._sessao_atual = TipoSessao.FOCO
        return self._sessao_atual

    def reiniciar_fluxo(self) -> None:
        self._sessao_atual = TipoSessao.FOCO
        self._ciclos_foco_concluidos = 0