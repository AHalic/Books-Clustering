def is_language_eng(data):
  """
    Função que verifica se o livro possui lingua inglesa
    `param` data: json contendo os dados do livro
    `return`: boolean
  """
  if  data['language_code'] == 'en' or data['language_code'] == 'eng' or data['language_code'] == 'en-GB' or data['language_code'] == 'en-US'or data['language_code'] == 'en-CA':
    return True
  else:
    return False

def find_genre(filename):
  """
    Função que encontra o genero do livro
    `param` filename: string contendo o nome do arquivo do tipo goodreads_books_genre.json
    `return`: string 
  """
  string = filename.partition('.')
  string = string[0]
  name = string[16:]

  if name == 'comics_graphic':
    name = 'comics'
  elif name == 'mystery_thriller_crime':
    name = 'mystery'
  elif name == 'fantasy_paranormal':
    name = 'paranormal'
  elif name == 'history_biography':
    name = 'biography'

  return name

def verify_conditions_book(book):
  """
    Função que retorna True caso o livro tenha as condições:
      lingua inglesa e descrição não vazia
    `param` book: json contendo o livro
    `return`: boolean
  """
  if is_language_eng(book):
    # verifica se a descrição não é vazia
    if book['description']:
      return True
  
  return False