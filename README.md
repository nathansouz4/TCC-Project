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
- **Framework de Desenvolvimento de Chatbots**: [Nome do Framework, ex: Rasa, GPT-3]
- **Processamento de Linguagem Natural (NLP)**: [Bibliotecas utilizadas, ex: spaCy, NLTK]
- **Documentação Técnica**: ABNT NBR IEC 60079-14
- **Técnica de Indexação**: RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval)

## Estrutura do Projeto

```plaintext
├── data/
│   └── documentos_tecnicos/
│       └── ABNT_NBR_IEC_60079-14.pdf
├── src/
│   ├── main.py
│   ├── chatbot/
│   │   ├── __init__.py
│   │   ├── raptor.py
│   │   └── modelo_llm.py
│   ├── nlp/
│   │   ├── __init__.py
│   │   ├── processamento.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── test_chatbot.py
│   └── test_raptor.py
├── README.md
└── requirements.txt
