import speech_recognition as sr
import time

#necessário estar conectado a internet
#Funcao converter áudio para texto
def main():

        #Caminho para o arquivo de audio
        pathFile = "audioFile.wav"

        #utilizando recognizer do speech_recognition
        rec = sr.Recognizer()

        with sr.WavFile(pathFile) as source:

                print("Convertendo audio para texto...")

                #Armazenando o audio
                audio = rec.listen(source)

        try:
                
                #Passando o audio para o reconhecedor de padroes.
                convertion = rec.recognize_google(audio,language="pt-BR")
                
        except Exception as e:
                print(e)

        #Criando arquivo com texto do audio
        fileExport = open('textFile.txt','w')
        #escrevendo o texto capturado
        fileExport.write(convertion)
        #Fechando arquivo
        fileExport.close()
        
        print('Audio convertido com sucesso!')
        
if __name__ == "__main__":

        main()
