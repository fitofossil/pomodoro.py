from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from core.enums import TipoSessao


@dataclass
class Configuracao:
    """
    Entidade que armazena os parâmetros configuráveis do ciclo Pomodoro.
    O decorador @dataclass gera automaticamente __init__, __repr__ e __eq__.
    """
    foco_minutos: int = 25
    pausa_curta_minutos: int = 5
    pausa_longa_minutos: int = 15
    ciclos_ate_pausa_longa: int = 4

    def obter_duracao_segundos(self, tipo: TipoSessao) -> int:
        """
        Retorna a duração total em segundos correspondente ao tipo de sessão informado.
        Centraliza a conversão de minutos para segundos dentro da própria entidade.
        """
        duracoes = {
            TipoSessao.FOCO: self.foco_minutos,
            TipoSessao.PAUSA_CURTA: self.pausa_curta_minutos,
            TipoSessao.PAUSA_LONGA: self.pausa_longa_minutos,
        }
        return duracoes[tipo] * 60


@dataclass
class Sessao:
    """
    Entidade que representa o registro histórico de uma sessão de Pomodoro
    para persistência futura no banco de dados (SQLite).
    """
    tipo: TipoSessao
    duracao_segundos: int
    concluida: bool = False
    # default_factory garante que datetime.now() seja chamado no momento da criação de cada instância
    iniciada_em: datetime = field(default_factory=datetime.now)
    # Optional indica que o valor começa como None até a sessão terminar ou ser salva no banco
    finalizada_em: Optional[datetime] = None
    id: Optional[int] = None