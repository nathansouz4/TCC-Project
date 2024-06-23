# 1. Usar uma imagem base com Conda
FROM continuumio/miniconda3:main

# 2. Copiar o arquivo env.yml para o diretório atual do contêiner
COPY env.yml /tmp/env.yml

# 3. Usar o Conda para criar o ambiente Python a partir do arquivo env.yml
RUN conda env create -f /tmp/env.yml

# 4. Ativar o ambiente. Este passo é um pouco diferente em Docker,
# porque você não pode usar `conda activate` diretamente em um Dockerfile.
# Então, você precisa modificar o PATH manualmente.
# Substitua `your_env_name` pelo nome do seu ambiente Conda.
ENV PATH /opt/conda/envs/test_env/bin:$PATH

# Garantir que os comandos sejam executados dentro do ambiente conda
SHELL ["conda", "run", "-n", "test_env", "/bin/bash", "-c"]

# 5. Definir o diretório de trabalho e copiar o código do projeto para o contêiner
WORKDIR /app
COPY . /app

# 6. Expor a porta que o Streamlit usa
EXPOSE 8501

# 7. Comando para executar a aplicação Streamlit
#nohup
CMD ["python3","-m","streamlit", "run", "test.py"]