# 🍅 Pomodoro Timer

Aplicação desktop de gerenciamento de tempo baseada na técnica Pomodoro, construída em Python com arquitetura modular, orientada a eventos e persistência local em SQLite.

---

## 📂 Estrutura do Projeto

```text
# 🍅 Pomodoro Timer

Aplicação desktop de gerenciamento de tempo baseada na técnica Pomodoro, construída em Python com arquitetura modular, orientada a eventos e persistência local em SQLite.

---

## 📂 Estrutura do Projeto

```text
pomodoro/
├── core/
│   ├── __init__.py
│   ├── enums.py            # Enumerações de estados e tipos de sessão
│   ├── models.py           # Entidades de dados (Configuracao, Sessao)
│   └── state_machine.py    # Regras de transição entre ciclos
├── engine/
│   ├── __init__.py
│   ├── event_bus.py        # Gerenciador de eventos (Padrão Observer)
│   └── timer_engine.py     # Controlador do relógio monotônico
├── storage/
│   ├── __init__.py
│   ├── repository.py       # Interface abstrata (ABC) de persistência
│   └── sqlite_repo.py      # Implementação concreta em SQLite
├── ui/
│   ├── __init__.py
│   ├── controller.py       # Ponte entre o Engine e as Janelas
│   ├── main_window.py      # Janela principal completa
│   ├── mini_widget.py      # Widget flutuante na área de trabalho
│   ├── tray_icon.py        # Ícone e menu na bandeja do sistema
│   └── sound_player.py     # Reprodutor de alertas sonoros
└── main.py                 # Ponto de entrada (Injeção de Dependências)
```

---

## 🏗️ Arquitetura e Módulos

### 1. `core/` — Domínio e Regras de Negócio
Contém a lógica pura do Pomodoro, sem dependências de interface gráfica ou banco de dados.
- **`enums.py`**: Define os estados do timer (`IDLE`, `RUNNING`, `PAUSED`, `FINISHED`) e tipos de sessão (`WORK`, `SHORT_BREAK`, `LONG_BREAK`).
- **`models.py`**: Estruturas de dados e entidades do domínio, como `Configuracao` (tempos de foco/pausa, ciclos) e `Sessao` (histórico de execução).
- **`state_machine.py`**: Controla a transição automática ou manual entre ciclos de foco, pausas curtas e pausas longas.

### 2. `engine/` — Motor de Tempo e Eventos
Responsável pela precisão do cronômetro e comunicação desacoplada entre componentes.
- **`event_bus.py`**: Implementa o padrão *Observer / Pub-Sub* para emitir eventos (ex: `tick`, `session_completed`, `state_changed`).
- **`timer_engine.py`**: Gerencia a contagem regressiva utilizando relógio monotônico (`time.monotonic`) para evitar desvios de tempo (*drift*).

### 3. `storage/` — Persistência de Dados
Camada isolada para armazenamento de configurações e histórico de sessões.
- **`repository.py`**: Contratos e interfaces abstratas (`ABC`) para operações de leitura e escrita.
- **`sqlite_repo.py`**: Implementação concreta utilizando SQLite para salvar sessões concluídas e preferências do usuário.

### 4. `ui/` — Interface do Usuário e Recursos Visuais/Sonoros
Camada de apresentação e interação com o sistema operacional.
- **`controller.py`**: Faz a mediação entre os eventos do `engine` e as atualizações visuais nas janelas.
- **`main_window.py`**: Interface principal com controles completos, estatísticas e configurações.
- **`mini_widget.py`**: Janela compacta (*always-on-top*) para acompanhamento discreto durante o foco.
- **`tray_icon.py`**: Integração com a bandeja do sistema (*System Tray*) para ações rápidas em segundo plano.
- **`sound_player.py`**: Gerencia a reprodução de notificações e alertas sonoros ao fim de cada ciclo.

### 5. `main.py` — Ponto de Entrada
- Inicializa o banco de dados, o barramento de eventos, o motor de tempo e a interface gráfica, realizando a **injeção de dependências** entre as camadas.

---

## 🚀 Como Executar

1. **Clone o repositório ou acesse a pasta do projeto:**
   ```bash
   cd pomodoro
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   ```

3. **Execute a aplicação:**
   ```bash
   python main.py
   ```
```

---

## 🏗️ Arquitetura e Módulos

### 1. `core/` — Domínio e Regras de Negócio
Contém a lógica pura do Pomodoro, sem dependências de interface gráfica ou banco de dados.
- **`enums.py`**: Define os estados do timer (`IDLE`, `RUNNING`, `PAUSED`, `FINISHED`) e tipos de sessão (`WORK`, `SHORT_BREAK`, `LONG_BREAK`).
- **`models.py`**: Estruturas de dados e entidades do domínio, como `Configuracao` (tempos de foco/pausa, ciclos) e `Sessao` (histórico de execução).
- **`state_machine.py`**: Controla a transição automática ou manual entre ciclos de foco, pausas curtas e pausas longas.

### 2. `engine/` — Motor de Tempo e Eventos
Responsável pela precisão do cronômetro e comunicação desacoplada entre componentes.
- **`event_bus.py`**: Implementa o padrão *Observer / Pub-Sub* para emitir eventos (ex: `tick`, `session_completed`, `state_changed`).
- **`timer_engine.py`**: Gerencia a contagem regressiva utilizando relógio monotônico (`time.monotonic`) para evitar desvios de tempo (*drift*).

### 3. `storage/` — Persistência de Dados
Camada isolada para armazenamento de configurações e histórico de sessões.
- **`repository.py`**: Contratos e interfaces abstratas (`ABC`) para operações de leitura e escrita.
- **`sqlite_repo.py`**: Implementação concreta utilizando SQLite para salvar sessões concluídas e preferências do usuário.

### 4. `ui/` — Interface do Usuário e Recursos Visuais/Sonoros
Camada de apresentação e interação com o sistema operacional.
- **`controller.py`**: Faz a mediação entre os eventos do `engine` e as atualizações visuais nas janelas.
- **`main_window.py`**: Interface principal com controles completos, estatísticas e configurações.
- **`mini_widget.py`**: Janela compacta (*always-on-top*) para acompanhamento discreto durante o foco.
- **`tray_icon.py`**: Integração com a bandeja do sistema (*System Tray*) para ações rápidas em segundo plano.
- **`sound_player.py`**: Gerencia a reprodução de notificações e alertas sonoros ao fim de cada ciclo.

### 5. `main.py` — Ponto de Entrada
- Inicializa o banco de dados, o barramento de eventos, o motor de tempo e a interface gráfica, realizando a **injeção de dependências** entre as camadas.

---

## 🚀 Como Executar

1. **Clone o repositório ou acesse a pasta do projeto:**
   ```bash
   cd pomodoro
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   ```

3. **Execute a aplicação:**
   ```bash
   python main.py
   ```
└── main.py                 # Ponto de entrada (Injeção de Dependências)
