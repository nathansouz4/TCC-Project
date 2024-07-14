# Desenvolvimento de um Assistente Chatbot Inteligente para Instalações Elétricas

## Visão Geral

Este projeto de Trabalho de Conclusão de Curso (TCC) consiste no desenvolvimento de um assistente chatbot inteligente para instalações elétricas. O chatbot é baseado em um Modelo de Linguagem Grande (LLM) e utiliza a técnica RAPTOR - Recursive Abstractive Processing for Tree-Organized Retrieval para fornecer respostas precisas e contextualizadas a questões relacionadas a instalações elétricas.

## Índice

- [Introdução](#introdução)
- [Objetivos](#objetivos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O propósito deste TCC é desenvolver um assistente chatbot que possa auxiliar engenheiros, técnicos e estudantes de engenharia elétrica a resolverem dúvidas e problemas comuns em instalações elétricas. Utilizando a técnica RAPTOR, o chatbot é capaz de navegar por documentos técnicos complexos, como a norma ABNT NBR 5410, e fornecer respostas abstrativas e contextualizadas.

## Objetivos

Os principais objetivos deste projeto são:

1. Desenvolver um modelo de chatbot baseado em LLM capaz de entender e responder perguntas sobre instalações elétricas.
2. Implementar a técnica RAPTOR para otimizar a recuperação de informações e fornecer respostas abstrativas e contextualizadas.
3. Validar a eficácia do chatbot através de testes e avaliações práticas.

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python
- **Framework de Desenvolvimento de Chatbots**: [LangChain, Streamlit]
- **Processamento de Linguagem Natural (NLP)**: [Bibliotecas utilizadas, ex: spaCy, NLTK]
- **Documentação Técnica**: ABNT NBR IEC 60079-14
- **Técnica de Indexação**: RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)

## Estrutura do Projeto

```plaintext
├── RAG_RAPTOR.ipynb
├── RAG_summaries.ipynb
├── README.md
├── app
│   ├── __pycache__
│   │   └── app.cpython-312.pyc
│   ├── app.py
│   └── src
│       ├── core
│       │   ├── __pycache__
│       │   │   └── service.cpython-312.pyc
│       │   └── service.py
│       ├── database
│       │   └── pdf
│       │       ├── ABNT_NBR_IEC_60079_14.pdf
│       │       ├── NBR_10898.pdf
│       │       ├── NBR_13570.pdf
│       │       ├── NBR_14039.pdf
│       │       ├── NBR_15514.pdf
│       │       ├── NBR_16280.pdf
│       │       ├── NBR_5410.pdf
│       │       ├── NBR_5413.pdf
│       │       ├── NBR_5419_1.pdf
│       │       ├── NBR_5419_2.pdf
│       │       ├── NBR_5419_3.pdf
│       │       └── NBR_5419_4.pdf
│       └── shared
│           ├── __pycache__
│           │   └── style.cpython-312.pyc
│           ├── style
│           │   └── images
│           │       ├── logo_2.png
│           │       └── ufrn-logo.png
│           └── utils
│               ├── __pycache__
│               │   └── utils.cpython-312.pyc
│               └── utils.py
├── dockerfile
├── env.yml
├── pdf_processing.log
├── test
│   └── nr-10.pdf
└── vectorstore_db
    ├── 7f5c301c-89d1-495e-8c6a-656f8cb9e948
    │   ├── data_level0.bin
    │   ├── header.bin
    │   ├── length.bin
    │   └── link_lists.bin
    └── chroma.sqlite3
=======
# Projeto RAG com LangChain

Bem-vindo ao repositório do Projeto RAG (Retrieval-Augmented Generation) utilizando o framework LangChain. Este projeto tem como objetivo construir um sistema que combina a recuperação de informações (retrieval) com a geração de texto (generation) para fornecer respostas aprimoradas e contextualmente relevantes.

## Sumário

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

Este projeto demonstra como implementar um sistema RAG usando o framework LangChain. O objetivo principal é melhorar a precisão e relevância das respostas geradas por um modelo de linguagem ao integrar um componente de recuperação de informações que busca dados em uma base de conhecimento específica.

## Recursos

- **LangChain Framework**: Utilização do LangChain para conectar a recuperação de informações com a geração de texto.
- **Componentes Modulares**: Arquitetura modular que facilita a manutenção e a expansão do sistema.
- **Customização Fácil**: Facilidade para personalizar a base de conhecimento e ajustar os parâmetros do modelo.

## Instalação

Para começar a usar este projeto, siga as etapas abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto-rag-langchain.git
   cd projeto-rag-langchain
>>>>>>> dev
