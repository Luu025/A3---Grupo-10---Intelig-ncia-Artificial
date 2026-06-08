[](https://github.com/user-attachments/files/28721933/README.1.md)
# Detector de Spam em Emails 📧

Um sistema inteligente em Python que detecta automaticamente se uma mensagem de email é spam ou não, usando Machine Learning.

## Funcionalidades

- **Classificação Inteligente**: Usa Naive Bayes com TF-IDF para análise de texto
- **Palavras-chave**: Detecta padrões comuns em emails de spam
- **Persistência**: Salva e carrega modelos treinados
- **Confiança**: Retorna nível de confiança da predição
- **Fácil de usar**: Interface simples e intuitiva

## Quick Start (5 minutos)

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar teste automático
python spam_detector.py

# 3. Ou testar de forma interativa
python interactive_test.py
```

---

## Instalação Detalhada

### Windows (PowerShell)
```powershell
# 1. Clonar ou baixar o projeto
cd C:\Users\seuuser\Downloads\A3IA

# 2. Instalar dependências
pip install -r requirements.txt

# 3. Executar
python spam_detector.py
```

### macOS/Linux (Terminal)
```bash
# 1. Navegar até a pasta
cd ~/Downloads/A3IA

# 2. Criar ambiente virtual (opcional mas recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# ou no Windows: venv\Scripts\activate

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Executar
python spam_detector.py
```

---

## Estrutura de Arquivos

```
A3IA/
├── spam_detector.py           # Classe principal do detector
├── interactive_test.py        # Interface interativa para testes
├── requirements.txt           # Dependências do projeto
├── spam_model.pkl            # Modelo treinado (criado após 1ª execução)
└── README.md                 # Este arquivo
```

---

## Como Usar - Passo a Passo

### Passo 1: Instalar as Dependências

Abra o terminal/prompt de comando na pasta do projeto e execute:

```bash
pip install -r requirements.txt
```

**Esperado:** Você verá mensagens de download e instalação dos pacotes.

---

### Passo 2: Executar o Script Automático

Para testar o detector com exemplos prontos:

```bash
python spam_detector.py
```

**O que acontece:**
1. O modelo é treinado com 20 exemplos de emails (10 legítimos, 10 spam)
2. O modelo é salvo em um arquivo `spam_model.pkl`
3. 5 emails de teste são classificados automaticamente
4. Você vê o resultado (SPAM ou NÃO SPAM) com a confiança

**Exemplo de saída:**
```
Email 1: Olá, você tem tempo para uma rápida reunião?
Resultado: NÃO SPAM (confiança: 59.32%)

Email 2: CLIQUE AGORA! Ganhe R$ 10.000 GRÁTIS!!!
Resultado: SPAM (confiança: 66.64%)
```

---

### Passo 3: Teste Interativo

Para digitar seus próprios emails e testar:

```bash
python interactive_test.py
```

**Como funciona:**
1. O programa abre uma interface interativa
2. Digite a mensagem do email (pode ser várias linhas)
3. Pressione Enter duas vezes para finalizar
4. O programa classifica em segundos
5. Digite "sair" para encerrar

**Exemplo prático:**
```
📧 Digite o conteúdo do email para análise:
(pressione Enter duas vezes para finalizar)

OFERTA ESPECIAL! CLIQUE AQUI PARA GANHAR PRÊMIOS INCRÍVEIS!

[Resultado]
✅ Resultado: SPAM (confiança: 88.50%)
```

---

### Passo 4: Usar como Módulo em Seu Código

Crie um arquivo `meu_script.py` e adicione:

```python
from spam_detector import EmailSpamDetector

# ---- OPÇÃO A: Criar e treinar um novo modelo ----
detector = EmailSpamDetector()

# Dados de treinamento (seus próprios emails)
emails_treino = [
    # Emails legítimos (label=0)
    "Sua fatura foi gerada",
    "Confirmação de compra",
    "Bem-vindo ao nosso site",
    
    # Emails de spam (label=1)
    "GANHE MILHÕES AGORA!",
    "CLIQUE AQUI PARA PRÊMIOS!",
    "Oferta exclusiva: 99% OFF"
]

labels_treino = [0, 0, 0, 1, 1, 1]

# Treinar o modelo
detector.train(emails_treino, labels_treino)

# Salvar para usar depois
detector.save_model()

# ---- OPÇÃO B: Usar um modelo já treinado ----
detector = EmailSpamDetector()
detector.load_model()  # Carrega spam_model.pkl

# Classificar um email
email_teste = "Você foi sorteado! Clique aqui para receber seu prêmio!"
resultado = detector.classify_email(email_teste)
print(f"Classificação: {resultado}")

# Obter predição detalhada (0 ou 1, e confiança)
predicao, confianca = detector.predict(email_teste)
print(f"Predição: {'SPAM' if predicao == 1 else 'NÃO SPAM'}")
print(f"Confiança: {confianca * 100:.2f}%")
```

**Executar:**
```bash
python meu_script.py
```

---

### Passo 5: Fluxo Completo de Uso

```
┌─────────────────────────────────────┐
│ 1. Instalar dependências (pip)      │
└─────────────────────┬───────────────┘
                      ↓
┌─────────────────────────────────────┐
│ 2. Treinar o modelo (train)         │
│    ou carregar existente (load)     │
└─────────────────────┬───────────────┘
                      ↓
┌─────────────────────────────────────┐
│ 3. Classificar emails (classify)    │
└─────────────────────┬───────────────┘
                      ↓
┌─────────────────────────────────────┐
│ 4. Obter resultado (SPAM/NÃO SPAM)  │
│    com nível de confiança          │
└─────────────────────────────────────┘
```

---

### Referência Rápida dos Métodos

| Método | Função | Exemplo |
|--------|--------|---------|
| `train(emails, labels)` | Treinar modelo | `detector.train(emails, [0, 1])` |
| `predict(email)` | Predição + confiança | `pred, conf = detector.predict(email)` |
| `classify_email(email)` | Resultado legível | `print(detector.classify_email(email))` |
| `save_model()` | Salvar modelo | `detector.save_model()` |
| `load_model()` | Carregar modelo | `detector.load_model()` |

## Exemplos Práticos de Detecção

### Exemplo 1: Email Legítimo
```
Email: "Olá, podemos marcar uma reunião para discutir o projeto?"
Resultado: ✅ NÃO SPAM (confiança: 85.32%)
Motivo: Linguagem profissional, sem palavras-chave suspeitas
```

### Exemplo 2: Email de Spam Óbvio
```
Email: "CLIQUE AGORA! Ganhe R$ 10.000 GRÁTIS!!! AÇÃO URGENTE!"
Resultado: ⚠️ SPAM (confiança: 95.45%)
Motivo: Múltiplas palavras-chave: "CLIQUE", "GRÁTIS", "URGENTE"
```

### Exemplo 3: Email Legítimo (Confirmação)
```
Email: "Seu pedido #12345 foi processado com sucesso. Obrigado!"
Resultado: ✅ NÃO SPAM (confiança: 92.18%)
Motivo: Linguagem de confirmação transacional
```

### Exemplo 4: Email de Spam Disfarçado
```
Email: "Oferta exclusiva: desconto de 80% por tempo limitado! AÇÃO AGORA!"
Resultado: ⚠️ SPAM (confiança: 87.78%)
Motivo: Palavras-chave: "oferta", "desconto limitado", "ação"
```

---

## Tabela de Palavras-Chave Detectadas

O sistema detecta automaticamente essas palavras/frases comuns em spam:

| Português | English |
|-----------|---------|
| urgente | urgent |
| clique aqui | click here |
| ganhe dinheiro | make money |
| oferta especial | special offer |
| limitado | limited |
| ação agora | act now |
| prêmio | prize/winner |
| grátis | free |
| desconto | discount |
| confirmar dados | verify/confirm data |

## 🔧 Estrutura do Código

### Classe `EmailSpamDetector`

#### Métodos principais:

- **`train(emails, labels)`**: Treina o modelo com dados de entrada
- **`predict(email_text)`**: Retorna predição e confiança
- **`classify_email(email_text)`**: Retorna resultado legível
- **`save_model()`**: Salva o modelo treinado
- **`load_model()`**: Carrega modelo previamente treinado

## Características de Detecção

O detector verifica:

1. **Palavras-chave de spam**: Palavras e frases comuns em emails maliciosos
   - "urgente", "clique aqui", "ganhe dinheiro"
   - "oferta especial", "grátis", "ação agora"
   - E muitas mais...

2. **Análise de Texto (TF-IDF)**: Análise estatística do conteúdo
3. **Classificação (Naive Bayes)**: Algoritmo de aprendizado de máquina

## Solução de Problemas

### Problema: "ModuleNotFoundError: No module named 'sklearn'"
**Solução:**
```bash
pip install scikit-learn
```

### Problema: "FileNotFoundError: spam_model.pkl"
**Solução:** O arquivo do modelo ainda não existe. Execute primeiro:
```bash
python spam_detector.py
```

### Problema: "SyntaxError" ao executar
**Solução:** Certifique-se de usar Python 3.7+
```bash
python --version
```

### Problema: Resultados inconsistentes
**Motivo:** O modelo foi treinado com poucos exemplos (20)
**Solução:** Treine com mais dados para melhorar a precisão

---

## Notas

- O modelo atual é treinado com 20 exemplos simples
- Para melhor precisão, treine com centenas ou milhares de emails reais
- Você pode adicionar mais palavras-chave em `spam_keywords`

## 📄 Licença

Código aberto para fins educacionais.
