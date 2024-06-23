# Test of auto deployment of files into EC2 instances

testing CI-CD with `github actions`.

<<<<<<< HEAD
testing dev branch
=======
* testing deploy v1

```
#v1
name: Push-to-EC2
on:
  push:
    branches:
      - main
      
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout the files
      uses: actions/checkout@v3

    - name: Install rsync
      run: sudo apt-get update && sudo apt-get install -y rsync

    - name: List files in the current directory
      run: |
        echo "Listando arquivos e diretórios no diretório atual:"
        ls -la

    - name: Sync files with SSH
      uses: appleboy/ssh-action@master
      with:
        host: ${{ secrets.HOST }}
        username: ec2-user
        key: ${{ secrets.EC2_SSH_KEY }}
        port: 22
        script: |
          echo "Iniciando rsync..."
          rsync -avz --delete ./ /home/ec2-user/
          echo "Listando o conteúdo do diretório de destino:"
          ls /home/ec2-user/
```

```
#v2
name: Push-to-EC2
on:
  push:
    branches:
      - main
      
jobs:
  upload-files-ec2:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout the files
      uses: actions/checkout@v4

    - name: List files in the current directory
      run: |
        echo "Listando arquivos e diretórios no diretório atual:"
        ls -la
        
    - name: copy file via ssh key
      uses: appleboy/scp-action@v0.1.7
      with:
        host: ${{ secrets.HOST }}
        username: ec2-user
        port: 22
        key: ${{ secrets.EC2_SSH_KEY }}
        source: "./"
        target: /home/ec2-user
```
>>>>>>> main
