from enum import Enum, auto


class EstadoTimer(Enum):
    """
    Enumeração que define os estados possíveis do motor de tempo (TimerEngine).
    Usa auto() pois os valores internos servem apenas para comparação lógica.
    """
    INATIVO = auto()  # Cronômetro parado/resetado no início de uma sessão
    RODANDO = auto()  # Contagem regressiva em andamento
    PAUSADO = auto()  # Contagem interrompida temporariamente pelo usuário


class TipoSessao(Enum):
    """
    Enumeração das etapas do ciclo Pomodoro.
    Os valores são strings legíveis para facilitar a exibição na UI e gravação no banco.
    """
    FOCO = "Foco"
    PAUSA_CURTA = "Pausa Curta"
    PAUSA_LONGA = "Pausa Longa"