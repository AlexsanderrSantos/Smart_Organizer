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


#Tipo de arquivos
documentos = [".pdf", ".txt", ".docx", ".xlsx", ".pptx"]
imagens = [".jpg",".png", ".gif"]
videos = [".mp4", ".mkv", ".avi"]
musicas = [".mp3", ".wav", ".flac"]

#função para organizar os arquivos
def organizar_arquivo(arquivo, pasta):
    try:
        if not pasta.exists():
            pasta.mkdir()
        
        destino = pasta / arquivo.name
        
        contador = 1
        
        while destino.exists():
            novo_nome = f"{arquivo.stem}_{contador}{arquivo.suffix}"
            destino = pasta / novo_nome
            contador += 1
            
        shutil.move(arquivo, destino)
        print(f"O arquivo {arquivo.name} foi movido para a pasta {destino.name}")
        
    except Exception as erro:
        print(f"Erro ao mover o arquivo {arquivo}: {erro}")

#Verifica se o diretório download existe e organiza os arquivos de acordo com o tipo. 
if diretorio_download.exists():
    
    for arquivo in diretorio_download.iterdir():
        
        if arquivo.is_file():
            
            extensao = arquivo.suffix.lower()
            
            if extensao in documentos:
                organizar_arquivo(arquivo, pasta_documentos)
        
            elif extensao in imagens:
               organizar_arquivo(arquivo, pasta_imagens)

            elif extensao in videos:
                organizar_arquivo(arquivo, pasta_videos)
            
            elif extensao in musicas:
                organizar_arquivo(arquivo, pasta_musicas)
            
            else:      
                organizar_arquivo(arquivo, pasta_outros)           

else: 
    print("Não tem arquivo nesta pasta")