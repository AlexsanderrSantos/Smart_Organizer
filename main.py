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
    ".flac":pasta_musicas  
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
            shutil.move(arquivo, destino)
        else:
            print(f"O arquivo {arquivo.name} foi movido para a pasta {pasta.name}")
            shutil.move(arquivo, destino)
        
    except Exception as erro:
        print(f"Erro ao mover o arquivo {arquivo}: {erro}")

#Verifica se o diretório download existe e organiza os arquivos de acordo com o tipo. 
if diretorio_download.exists():
    
    for arquivo in diretorio_download.iterdir():
        
        if arquivo.is_file():
            extensao = arquivo.suffix.lower()
            
            pasta_extensao = pastas_por_extensao.get(extensao)
            
            pasta_destino = pasta_extensao
            if pasta_destino is None:
                pasta_destino = pasta_outros
                
            organizar_arquivo(arquivo, pasta_destino)
            
             

else: 
    print("Não tem arquivo nesta pasta")