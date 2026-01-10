# selenium-nanowait

**Sincronização adaptativa baseada em estado para Selenium — alimentada pelo motor NanoWait.**

---

## 🚀 O que é o `selenium-nanowait`?

O `selenium-nanowait` é uma biblioteca de suporte para Selenium que **elimina esperas frágeis baseadas em tempo**, sincronizando as ações do navegador com o estado real da página, e não com timeouts arbitrários.

Em vez de adivinhar quanto tempo esperar (`time.sleep(5)` ou `WebDriverWait(10)`), o `selenium-nanowait` aguarda o que realmente importa:
*   **Visibilidade do elemento**
*   **Estabilidade do layout** (posição e tamanho constantes)
*   **Prontidão do DOM** (`document.readyState === "complete"`)

Não é um substituto para o Selenium, mas sim uma melhoria direta que funciona lado a lado com seu código existente. Você continua usando o Selenium como sempre fez — o `selenium-nanowait` apenas torna a espera determinística, adaptativa e confiável.

## 🧠 Filosofia de Design

O `selenium-nanowait` segue três regras estritas:
1.  **Complementar, nunca substituir o Selenium.**
2.  **Esperar por estados, não por tempo.**
3.  **Manter-se explícito e opcional (opt-in).**

Não há *monkey-patching*, globais ocultos ou drivers customizados.

## 🛠️ Instalação

```bash
pip install selenium-nanowait
```

### Requisitos
*   Python ≥ 3.8
*   Selenium ≥ 4.x
*   NanoWait ≥ 4.0.0 (motor adaptativo core)

## 💡 Início Rápido: A Função `wait_for`

A função `wait_for` é o novo ponto de entrada da biblioteca. Ela encapsula toda a lógica de sincronização adaptativa e retorna um elemento pronto para interação.

### Antes (Frágil, Baseado em Tempo)
```python
import time
from selenium.webdriver.common.by import By

# Você está adivinhando quanto tempo o elemento levará para aparecer
time.sleep(3) 
driver.find_element(By.ID, "submit").click()
```

### Depois (Consciente de Estado, Determinístico)
```python
from selenium_nanowait import wait_for

# O clique só ocorre quando o elemento está realmente pronto
wait_for(driver, "#submit").click()
```

## ⚙️ API Principal

### `wait_for()`
```python
wait_for(
    driver,
    selector: str,
    *,
    timeout: float | None = None,
    **nano_kwargs
)
```
Esta função retorna um `AdaptiveElement`, um wrapper leve que estende o comportamento do Selenium sem substituí-lo.

### Métodos do `AdaptiveElement`

| Método | Descrição | Exemplo |
| :--- | :--- | :--- |
| `.click()` | Aguarda a estabilidade e clica quando o elemento está pronto. | `wait_for(driver, "#login").click()` |
| `.type(text, clear=True)` | Aguarda prontidão e digita o texto. | `wait_for(driver, "#email").type("user@email.com")` |
| `.raw()` | Retorna o `WebElement` nativo do Selenium, intocado. | `el = wait_for(driver, "#submit").raw()` |

### Verificação de Estabilidade Visual
O elemento só é considerado pronto quando:
1.  **Está visível** (`is_displayed`).
2.  **O DOM está carregado** (`document.readyState === "complete"`).
3.  **Estabilidade de Layout**: Sua posição e tamanho permanecem constantes entre verificações consecutivas.

## 🧠 Por que o `selenium-nanowait` é diferente?

| Característica | ❌ Waits Tradicionais do Selenium | ✅ `selenium-nanowait` |
| :--- | :--- | :--- |
| **Base** | Baseado em tempo/condição isolada | **Baseado em estado real e visual** |
| **Escopo** | Global ou Condicional | **Escopo de elemento adaptativo** |
| **Espera** | Baseada em estimativa | **Backoff adaptativo (NanoWait)** |
| **Instabilidade** | Frágil sob carga do sistema | **Consciente de layout e performance** |
| **Debug** | Erros genéricos de Timeout | **Diagnósticos determinísticos** |

### ⏱️ Espera Adaptativa (via NanoWait)
Internamente, a biblioteca delega as decisões de tempo ao **NanoWait**, que:
*   Adapta a frequência de polling.
*   Evita *busy-waiting*.
*   Ajusta o tempo de espera de forma inteligente com base no desempenho do sistema.

### 🔬 Diagnósticos de Falha
Em vez de erros genéricos como `TimeoutException`, o `selenium-nanowait` levanta erros descritivos:
> *"Element '#submit' was found but never became stable. Observed multiple layout shifts before timeout."*

## 🧑‍💻 Exemplos Avançados

### Digitando com parâmetros customizados
```python
wait_for(
    driver,
    "#email",
    timeout=5,
    smart=True,
    speed="fast"
).type("usuario@email.com")
```

### Uso em Páginas Dinâmicas (SPA)
Mesmo em aplicações React, Vue ou Next.js, o clique só ocorre quando o layout está estável, reduzindo falhas intermitentes em transições de página.
```python
wait_for(driver, "button.submit", verbose=True).click()
```

## 📦 Metadados do Projeto

*   **Licença:** MIT
*   **Autor:** Luiz Filipe Seabra de Marco
*   **Status:** Pronto para produção (v0.1)

---

**Resumo:** `selenium-nanowait` faz o Selenium esperar pela realidade, não pelo relógio.
