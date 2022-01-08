def escreva(text):
    size = int(len(text)) + 2
    print('~' * size)
    print(f'{text:^{size}}')
    print('~' * size)


escreva('Curso em Vídeo')
escreva('CPM')
