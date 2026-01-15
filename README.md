# selenium-nanowait

Sincronização adaptativa baseada em estado para Selenium — alimentada pelo motor NanoWait.

## 🚀 O que é o `selenium-nanowait`?

`selenium-nanowait` é uma biblioteca de suporte para Selenium que **elimina esperas frágeis baseadas em tempo**, sincronizando as ações do navegador com o estado real da página, e não com *timeouts* arbitrários.

Em vez de adivinhar quanto tempo esperar (`time.sleep(5)` ou `WebDriverWait(10)`), o `selenium-nanowait` aguarda o que realmente importa:

*   **Visibilidade do elemento**
*   **Estabilidade do layout** (posição e tamanho constantes)
*   **Prontidão do DOM** (`document.readyState === "complete"`)

Além disso, o `selenium-nanowait` foi projetado para integração direta e transparente com *frameworks* de teste, permitindo adoção imediata em ambientes de QA, automação GUI e ensino.

Não é um substituto para o Selenium, mas sim uma melhoria direta que funciona lado a lado com seu código existente. Você continua usando o Selenium como sempre fez — o `selenium-nanowait` apenas torna a espera determinística, adaptativa e confiável.

## 🧠 Filosofia de Design

O `selenium-nanowait` segue três regras estritas:

1.  **Complementar**, nunca substituir o Selenium.
2.  **Esperar por estados**, não por tempo.
3.  **Manter-se explícito**, previsível e *opt-in*.

Não há *monkey-patching*, globais ocultos ou *drivers* customizados. A integração com *frameworks* de teste é *plug-and-play*, não invasiva.

## 🛠️ Instalação

```bash
pip install selenium-nanowait
```

### Requisitos

*   Python ≥ 3.8
*   Selenium ≥ 4.x
*   NanoWait ≥ 4.0.0

## 💡 Início Rápido: A Função `wait_for`

A função `wait_for` é o ponto de entrada principal da biblioteca. Ela encapsula toda a lógica de sincronização adaptativa e retorna um elemento pronto para interação.

### Antes (Frágil, Baseado em Tempo)

```python
import time
from selenium.webdriver.common.by import By

time.sleep(3)
driver.find_element(By.ID, "submit").click()
```

### Depois (Consciente de Estado, Determinístico)

```python
from selenium_nanowait import wait_for

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

Retorna um `AdaptiveElement`, um *wrapper* leve que estende o comportamento do Selenium sem substituí-lo.

### Métodos do `AdaptiveElement`

| Método                  | Descrição                                     | Exemplo                                             |
| :---------------------- | :-------------------------------------------- | :-------------------------------------------------- |
| `.click()`              | Aguarda estabilidade e executa o clique.      | `wait_for(driver, "#login").click()`                |
| `.type(text, clear=True)` | Aguarda prontidão e digita texto.             | `wait_for(driver, "#email").type("user@email.com")` |
| `.raw()`                | Retorna o `WebElement` nativo do Selenium.    | `el = wait_for(driver, "#submit").raw()`            |

## 🔎 Verificação de Estabilidade Visual

O elemento só é considerado pronto quando:

*   Está visível (`is_displayed`)
*   O DOM está totalmente carregado
*   Sua posição e tamanho permanecem constantes entre verificações consecutivas

Essa abordagem elimina falhas intermitentes causadas por *layout shifts*, animações ou *reflows* tardios.

## 🧪 Integração Plug-and-Play com Frameworks de Teste

O `selenium-nanowait` foi projetado para adoção imediata em ambientes de teste, sem exigir configuração manual ou alterações estruturais no projeto.

### ✅ Pytest (Automático)

Basta instalar a biblioteca. Nenhuma *fixture* ou *setup* adicional é necessário.

```python
def test_login(driver):
    wait_for(driver, "#login").click()
```

O *plugin* do *pytest* é carregado automaticamente via *entrypoint*, permitindo futuras extensões como:

*   *screenshots* automáticos em falhas
*   *logs* por teste
*   integração com relatórios

### ✅ unittest (Mixin opcional)

```python
from selenium_nanowait.unittest_adapter import NanoWaitTestCaseMixin

class TestUI(NanoWaitTestCaseMixin, unittest.TestCase):
    ...
```

### ✅ Robot Framework

```robotframework
Wait For    css:#submit
```

## ⚙️ Configuração Global (Opcional)

```python
from selenium_nanowait import configure

configure(
    default_timeout=10,
    nano_kwargs={"smart": True, "verbose": False}
)
```

A configuração é aplicada globalmente, respeitando a filosofia *opt-in*.

## 🧠 Por que o `selenium-nanowait` é diferente?

| Característica        | ❌ Waits Tradicionais | ✅ `selenium-nanowait` |
| :-------------------- | :-------------------- | :--------------------- |
| Base                  | Tempo fixo            | Estado real da página  |
| Escopo                | Global/condicional    | Elemento adaptativo    |
| Espera                | Estimativa            | *Backoff* adaptativo   |
| Robustez              | Frágil                | Consciente de *layout* |
| Integração QA         | Manual                | *Plug-and-play*        |

## ⏱️ Espera Adaptativa (NanoWait)

O motor NanoWait:

*   ajusta dinamicamente a frequência de *polling*
*   evita *busy-waiting*
*   adapta-se ao desempenho do sistema

## 🔬 Diagnósticos Determinísticos

Em vez de erros genéricos, o `selenium-nanowait` fornece mensagens claras e reproduzíveis:

```
"[selenium-nanowait] Element '#submit' not ready after 5s — layout remained unstable."
```

## 🧑‍💻 Exemplos Avançados

### Parâmetros customizados

```python
wait_for(
    driver,
    "#email",
    timeout=5,
    smart=True,
    speed="fast"
).type("usuario@email.com")
```

### Aplicações SPA (React, Vue, Next.js)

```python
wait_for(driver, "button.submit", verbose=True).click()
```

## 📦 Metadados do Projeto

*   **Licença**: MIT
*   **Autor**: Luiz Filipe Seabra de Marco
*   **Status**: Pronto para produção (v0.3)
*   **Resumo**: `selenium-nanowait` faz o Selenium esperar pela realidade, não pelo relógio — e agora, se integra naturalmente aos principais *frameworks* de teste.

---

## ✨ Ajude a Crescer o Projeto!

Se você achou `selenium-nanowait` útil para seus projetos de automação, por favor, considere dar uma estrela (⭐️) no nosso repositório no GitHub! Seu apoio nos ajuda a ganhar visibilidade e a continuar desenvolvendo e melhorando a biblioteca.

Adoramos contribuições! Seja reportando *bugs*, sugerindo novas funcionalidades, escrevendo documentação ou enviando *pull requests*, sua participação é muito bem-vinda. Junte-se à nossa comunidade e ajude a moldar o futuro do `selenium-nanowait`!

[Visite o repositório no GitHub](https://github.com/LuizSeabraDeMarco/NanoWaitSelenium) (substitua pelo link real do seu repositório)
