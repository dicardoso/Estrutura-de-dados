class Filme:
    
    def __init__(self, id, nome, ano):
        self.id = id
        self.nome = nome
        self.ano = ano

    def __str__(self):
        texto = 'ID: {}\nFilme: {}\nAno: {}'.format(
            self.id,
            self.nome,
            self.ano
        )
        return texto