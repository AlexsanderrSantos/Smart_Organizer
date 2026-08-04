from pathlib import Path
import shutil

#Diretorio home do usuário
diretorio_home = Path.home() #C://

#diretorios
diretorio_download = diretorio_home / "Downloads"

pasta_documentos = diretorio_download / "Documentos"
pasta_imagens = diretorio_download / "Imagens"
pasta_videos = diretorio_download / "Videos"
pasta_musicas = diretorio_download / "Musicas"
pasta_outros = diretorio_download / "Outros"
pasta_sem_extensao = diretorio_download / "Sem Extensão"

#Dicionário para mapear as extensões.

pastas_por_extensao ={
    ".pdf":pasta_documentos,
    ".txt":pasta_documentos,
    ".docx":pasta_documentos,
    ".xlsx":pasta_documentos,
    ".pptx":pasta_documentos,
    
    ".jpg":pasta_imagens,
    ".png":pasta_imagens,
    ".gif":pasta_imagens,
    
    ".mp4":pasta_videos,
    ".mkv":pasta_videos,
    ".avi":pasta_videos,
    
    ".mp3":pasta_musicas,
    ".wav":pasta_musicas,
    ".flac":pasta_musicas,
    
    "":pasta_sem_extensao
}

#função para organizar os arquivos
def organizar_arquivo(arquivo, pasta):
    try:
        if not pasta.exists():
            pasta.mkdir()
        
        destino = pasta / arquivo.name
        arquivo_renomeado = False
        
        contador = 1
        
        while destino.exists():
            novo_nome = f"{arquivo.stem}_{contador}{arquivo.suffix}"
            destino = pasta / novo_nome
            contador += 1
            arquivo_renomeado = True
            
        if arquivo_renomeado:
            print(f"O arquivo {destino} já existe e foi renomeado para {novo_nome} e enviado para a pasta {pasta.name}")
    
        else:
            print(f"O arquivo {arquivo.name} foi movido para a pasta {pasta.name}")
            
        shutil.move(arquivo, destino)
        return True
        
    except Exception as erro:
        print(f"Erro ao mover o arquivo {arquivo}: {erro}")
        return False
        
        

#Verifica se o diretório download existe e organiza os arquivos de acordo com o tipo. 
if diretorio_download.exists():
    
    contadores = {
        "documentos": 0,
        "imagens": 0,
        "videos": 0,
        "musicas": 0,
        "outros": 0,
        "sem_extensao": 0
    }
    
    for arquivo in diretorio_download.iterdir():
        
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()
            
            pasta_destino = pastas_por_extensao.get(extensao)
            
            if pasta_destino is None:
                pasta_destino = pasta_outros
                
            sucesso = organizar_arquivo(arquivo, pasta_destino)     
            if sucesso:
                if pasta_destino == pasta_documentos:
                    contadores["documentos"] += 1
                elif pasta_destino == pasta_imagens:
                    contadores["imagens"] += 1
                elif pasta_destino == pasta_videos:
                    contadores["videos"] += 1
                elif pasta_destino == pasta_musicas:
                    contadores["musicas"] += 1
                elif pasta_destino == pasta_sem_extensao:
                    contadores["sem_extensao"] += 1
                else:
                    contadores["outros"] += 1
                    
    print(f"Os arquivos organizados foram:")
    for tipo, quantidade in contadores.items(): #items entrega chave e valor junto
        print(f"{tipo}: {quantidade}")
          
    
else: 
    print("Não tem arquivo nesta pasta")