import re


def help_regex(message):
    regex = "^\/help"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return True
    return 0

HELP_MARKDOWN = """*Para procurar/baixar material ou mensagens*:
/procurar "PALAVRA-CHAVE"
/procurar "ARQUIVO_PARA_BAIXAR.PDF"

*Para pesquisar na internet*:
/duckduck PESQUISA

*Para administrar tarefas*:
criar tarefa "Nome da Tarefa"
del tarefa "83fab1d3...."
listar tarefas | list tasks

*Habilidades de CTF*:
Base64 En/Decoder
/b64e TEXTO
/b64d BASE64

Morse En/Decoder:
/morsee PLAINTEXT
/morsed `MORSE_CODE`

Ascii En/Decoder:
/asciie TEXTO
/asciid NN NN NN NN

Galego Cipher En/Decoder:
/galegoe TEXTO
/galegod CIPHER

Caesar Cipher En/Decryptor:
/caesare PLAINTEXT
/caesard CIPHER

Vignere Cipher En/Decryptor:
/vigneree "PLAINTEXT" "KEY"
/vignered "CIPHER" "KEY"
"""
