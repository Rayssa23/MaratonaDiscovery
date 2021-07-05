##O programa deve permitir o cadastro dos usuários e dos títulos disponíveis, além do registro histórico dos empréstimos efetuados. O sistema deverá possuir ainda facilidades de busca dos títulos a partir de campos como título, autor, ISBN(grupo,editor, item, digito de verificação), além de fornecer a localização dos títulos nas estantes.
from datetime import datetime,date,timedelta
import random
import pickle
from operator import itemgetter
from os import system, name

def verificar_arq_titulos():
  try:
    arqTitulos = open("titulos.dat", "rb")
    titulos = pickle.load(arqTitulos)
    print('Arquivo "Titulos.dat" Aberto com sucesso! ')
    arqTitulos.close()
  except IOError:
    print("Arquivo Titulos.dat em branco, Salvarei após finalizar sessão")
    titulos = {}
  return titulos
def verificar_arq_usuarios():
  try:
    arqUsuarios = open("usuarios.dat", "rb")
    usuario = pickle.load(arqUsuarios)
    print('Arquivo "Usuarios.dat" Aberto com sucesso! ')
    arqUsuarios.close()
  except IOError:
    print("Arquivo usuarios.dat em branco, Salvarei após finalizar sessão")
    usuario = {}
  return usuario
def verificar_arq_emprestimos():
  try:
    arqEmprestimos = open('emprestimos.dat', 'rb')
    emprestimos_user = pickle.load(arqEmprestimos)
    print('Arquivo "emprestimos.dat" Aberto com sucesso! ')
    arqEmprestimos.close()
  except IOError:
    print("Arquivo emprestimos.dat em branco, Salvarei após finalizar sessão")
    emprestimos_user = {}
  return emprestimos_user

def gravar_titulos():
  arqTitulos = open("titulos.dat", "wb")
  pickle.dump(titulos, arqTitulos)
  arqTitulos.close()
def gravar_usuarios():
  arqUsuarios = open("usuarios.dat", "wb")
  pickle.dump(usuario, arqUsuarios)
  arqUsuarios.close()
def gravar_emprestimos():
  arqEmprestimos = open("emprestimos.dat", "wb")
  pickle.dump(emprestimos_user, arqEmprestimos)
  arqEmprestimos.close()

def clear():
  perg = input('\nQuer limpar a tela?(S/N) ')
  if perg.upper() == 'S':
      #windows 
    if name == 'nt': 
      _ = system('cls') 
    #mac e linux
    else:
      _ = system('clear')
  else:
    print()
def menu_login():
   print('''
    **********************************************
    ***********          MENU         ************
    **********************************************
    **  1 - Cadastrar Usuário                   **
    **  2 - Login                               **
    **  3 - Sair                                **
    **********************************************''')
   opcao = input('Insira sua Opção: ')
   opcao2 = opcao
   cargo = ''
   return opcao,opcao2,cargo
def menu_funcionario():
  print(" = = = = = = = = = = = = = = = =")
  print(" = = =   Digital Library   = = =")
  print(" = = = = = = = = = = = = = = = =")
  print("     1. Cadastrar Títulos")
  print("     2. Atualizar Títulos")
  print("     3. Excluir Título")
  print("     4. Exibir Inventário")
  print("     5. Exibir Relatório")
  print("     6. Pesquisar no Acervo")
  print("     0. Finalizar sessão")
  print()
  resp = input("Escolha sua opção: ")
  return resp
def menu_cliente():
  print('''
        **********************************************
        ***********   MENU USUÁRIO        ************
        **********************************************
        **  1 - Pesquisar Livro                     **
        **  2 - Exibir Livros disponíveis           **
        **  3 - Realizar Empréstimo                 **
        **  4 - Minha Conta                         **
        **  5 - Devolução/Renovação de empréstimo   **
        **  0 - Finalizar sessão                    **
        **********************************************''')
  opcao = input("Escolha uma opção: ")
  return opcao
def cadastrarUsuario():
    print('Módulo de cadastro de usuário')
    user = input('---Nome de Usuário: ')
    while ' ' in user:
      print('\n~~Não use Espaços para definir o usuário\n')
      user = input('---Nome de Usuário: ')
    while (user in usuario):
      print("\n~~ Esse nome de usuário já existe!\n")
      user = input('---Nome de Usuário: ')
    if user not in usuario:
      senha = input('Insira a senha para este Usuário: ')
    while ' ' in senha:
        print('\n~~Não use Espaços para definir a senha do usuário')
        senha = input('~\nInsira a senha para este Usuário: ')
    print("\nCadastrado com sucesso!!!")
    clear()
    usuario[user] = [senha,[0,'--/--/----']]
    emprestimos_user[user]= []

def exigir_codigo():
  codigo = input('\nDigite o código: ')
  while (len(codigo) > 10) or (len(codigo) < 10) or (not(codigo.isdigit())):
    codigo = input('\nDigite o código(com 10 números): ')
  return codigo
def cadastrar_titulo():
  titulo = input("Título:  ")
  autor = (input("Autor:  "))
  editora = (input("Editora:  "))
  edicao = (input("Edição: "))
  quant = (input("Quantidade: "))
  while  not(quant.isdigit()):
    quant = (input("Quantidade: "))
  quant = int(quant)
  codigo = (input("Deseja Digitar o Código ou quer gerar automaticamente?(D/A): "))
  
  while (codigo.upper() != "A") and (codigo.upper()!= "D"):
      print('\n ~Escolha D para Digitar ou A para gerar automaticamente!')
      codigo = (input("Deseja Digitar o Código ou quer gerar automaticamente?(D/A): "))
  if codigo.upper() == 'D':
    codigo = exigir_codigo()
  else:
    codigo = []
    for i in range(10):
      num = random.randint(0,9)
      codigo.append(str(num))
    codigo = ''.join(codigo)
  if codigo not in titulos:
    titulos[codigo] = [titulo,autor, editora, edicao, quant]
  else:
    print('\nCódigo Existente, vou gerar um para este Título!')
    while codigo in titulos:
      codigo = []
      for i in range(10):
        num = random.randint(0,9)
        codigo.append(str(num))
      codigo = ''.join(codigo)
  print("\nLivro %s cadastrado com sucesso. \nCódigo dele: %s"%(titulo,codigo))
  print()
  return titulos
def exibir_acervo():
  if len(titulos) == 0:
    print('\n\n~~ Não há livros no Acervo!\n')
  else:
    print("\n\n    = = = = = =   Módulo de Exibição = = = = = =\n")
    for livro in titulos:
      print('''
      ------------- Disponíveis: {} ---------------

                    Título: {}
                    Autor:  {}
                    Editora: {}
                    Edição:  {}
                    Código:  {}

      ---------------------------------------------
      '''.format(titulos[livro][4],titulos[livro][0],titulos[livro][1],titulos[livro][2],titulos[livro][3],livro))

def menu_pesquisar():
  print("\n\n")
  print(" = = = = = Módulo de Consulta = = = = =")
  if len(titulos) == 0:
    print('\n\n~~Não há titulos cadastrados!')
  else:
    print('''
        ............................................
        .     Escolha uma opção para seguir:       .
        .      1 - Titulo                          .
        .      2 - Autor                           .
        .      3 - Código                          .
        ............................................
    ''')
    escolha = input('\nSua escolha: ')
    return escolha
def pesquisar_por_titulo():
  pesq = input("Informe um Título a ser pesquisado: ")
  if len(titulos) == 0:
    print('\n ~Não há livros disponíveis')
  else:
    validar = True
    for  codigo in titulos:
      if pesq.upper() in titulos[codigo][0].upper():
          print('\n\n- - - - - - - - - - - - - - - - - - - - - - - ')
          print("   Título: ", titulos[codigo][0])
          print("   Autor: ", titulos[codigo][1])
          print("   Editora:", titulos[codigo][2])
          print("   Edição:", titulos[codigo][3])
          print('   Código: ',codigo)
          print('- - - - - - - - - - - - - - - - - - - - - - - ')
          validar = False
    if validar:
      print("Livro não cadastrado!!!")             
def pesquisar_por_autor():
  pesq = input("Informe o Autor do Título a ser pesquisado: ")
  if len(titulos) == 0:
    print('\n ~Não há livros disponíveis')
  else:
    validar = False
    for  codigo in titulos:
     if pesq.upper() in titulos[codigo][1].upper():
        print('- - - - - - - - - - - - - - - - - - - - - - - ')
        print("   Título: ", titulos[codigo][0])
        print("   Autor: ", titulos[codigo][1])
        print("   Editora:", titulos[codigo][2])
        print("   Edição:", titulos[codigo][3])
        print('   Código: ',codigo)
        print('- - - - - - - - - - - - - - - - - - - - - - - ')
        validar = True
  if not(validar):
    print("Livro deste Autor não cadastrado!!!")    
def pesquisar_por_codigo():
  if len(titulos) == 0:
    print('\n ~Não há livros disponíveis')
  else:
    codigo = exigir_codigo()
    if codigo in titulos:
      print('- - - - - - - - - - - - - - - - - - - - - - - ')
      print("   Título: ", titulos[codigo][0])
      print("   Autor: ", titulos[codigo][1])
      print("   Editora:", titulos[codigo][2])
      print("   Edição:", titulos[codigo][3])
      print('   Código: ',codigo)
      print('- - - - - - - - - - - - - - - - - - - - - - - ')
      print("\n\n")
    else:
      print('\nCódigo não Cadastrado!\n')

def menu_exluir():
  print('''
  - - - -  Módulo de Exclusão - - - -
  --         Excluir por:          --
  --    1 - Titulo                 --
  --    2 - Autor                  --
  --    3 - Código                 --
  - - - - - - - - - - - - - - - - - -\n\n''')
  excluir = input('Sua escolha: ')
  return excluir
def excluir_por_titulo():
  titulo = input('\n\nInsira o Titulo que deseja excluir: ')
  validar = False
  for codigo in titulos:
    if titulo.upper() in titulos[codigo][0].upper():
      del titulos[codigo]
      print('\n Titulo excluido!\n')
      validar = True
      return titulos
  if not(validar):
    print('\n\n~~Titulo foi digitado de forma incorreta, exiba o inventário e verifique o Titulo correto')
def excluir_por_autor():
  autor = input('\n\nIndique o nome do Autor do Livro que deseja excluir:  ')
  validar = False
  for codigo in titulos:
    if autor.upper() in titulos[codigo][1].upper():
      del titulos[codigo]
      validar = True
      print('\n Título excluido!')
      return titulos
  if not(validar):
    print('\n\n~~Autor não encontrado, exiba o inventario e verifique novamente qual o Autor do seu livro!')

def excluir_por_codigo():
  codigo = input("Informe o código do Título a ser excluído: ")
  if codigo not in titulos:
    print("\n~~ Título não encontrado na Biblioteca")
  else:
    del titulos[codigo]
    print('\nTítulo excluido com sucesso!!!\n')
    return titulos



def modo_de_emprestimo():
  print('''
  ..............................
  .     Alugar por:            .
  .    1 - Titulo              .
  .    2 - Código              .
  ..............................
  ''')
  escolha = input('\n- Sua escolha: ')
  return escolha
def emprestimo_por_titulo():
  pesq = input('\nIndique o Titulo a ser alugado: ')
  validar = False
  for codigo in titulos:
    if pesq.upper() in titulos[codigo][0].upper():
      validar = True
      return codigo
  if not(validar):
    print('\n\n~~ Titulo Inválido! Tente novamente...') 
def modulo_emprestimo():
  print("\n\n")
  print("          = = = = = = Módulo de Empréstimo = = = = = = ")
  if len(titulos) == 0:
    print('\n\nNão há livros disponíveis!')
  else:
    legal = validar_multa()
    if legal:
      escolha = modo_de_emprestimo()
      if escolha == '1':
        codigo = emprestimo_por_titulo()
      elif escolha == '2':
        codigo = exigir_codigo()
      else:
          codigo = ''
          print('\n ~~Opção Inválida! Tente novamente')
      if codigo not in titulos:
        print("\nTítulo não cadastrado!!!")
      else: 
        if titulos[codigo][4] == 0:
          print('\n~~ Este livro Está indisponivel!')
        else:
          validar = True
          for livro in emprestimos_user[login]:
            if codigo == livro[0]:
              validar = False
          if validar:
            afirmacao = input('Deseja realmente Alugar este livro(S/N): ')
            afirmacao = afirmacao.upper()
            if afirmacao == "S":
              d = dia_hoje()
              data_hoje = d.strftime('%d/%m/%Y')
              d = d + timedelta(days = 10)
              data_devolucao = d.strftime('%d/%m/%Y')
              print()
              print("DATA DE DEVOLUÇÃO: ",data_devolucao)
              lista_adicionar = [codigo,1,data_devolucao,data_hoje,True,'--/--/--','--/--/--']
              emprestimos_user[login].append(lista_adicionar)
              num = int(titulos[codigo][4])
              titulos[codigo][4] = num -1
              print('\n\nLivro Computado, Você tem  10 dias para renovar ou devolver este livro! ')
          else:
            print('\n~~Você não pode alugar o mesmo livro mais de uma vez! Pense no Proximo\n ')
      return emprestimos_user
    else:
      print('Não pode Alugar,Pois está Com Multa!')
      

def dia_hoje():
  agora = str(datetime.now())
  ano = int(agora[:4])
  mes = int(agora [5:7])
  dia = int(agora[8:10])
  d = date(ano,mes,dia)
  return d

def devolver():
  d = dia_hoje()
  devolucao = d.strftime('%d/%m/%Y')
  validar = True
  comprovante = 0
  for num in range(len(emprestimos_user[login])):
    if codigo == emprestimos_user[login][num][0] and emprestimos_user[login][num][4]:
      if (codigo in titulos):
        titulos[codigo][4] += 1
        emprestimos_user[login][num][5] = devolucao
        emprestimos_user[login][num][4] = False
        validar =  emprestimos_user[login][num][4]
        print("Devolvido com sucesso!!!")
        data_dev = d
        data1 = str(emprestimos_user[login][num][2])
        data_marcada = datetime.strptime(data1,'%d/%m/%Y').date()
    if codigo != emprestimos_user[login][num][0]:
      comprovante += 1
    
  if validar:
    data_dev = 1
    data_marcada = 2
  return validar,data_dev,data_marcada,devolucao,comprovante
def validar_renovacao():
  comprovante = 0
  contabilizar = False
  for elemento in range (len(emprestimos_user[login])):
    if codigo in emprestimos_user[login][elemento] and emprestimos_user[login][elemento][4]:
      contabilizar = True
      num = elemento
      dat = emprestimos_user[login][elemento][2]
      data_dev = datetime.strptime(dat,'%d/%m/%Y').date()
    else:
      comprovante += 1
  if not(contabilizar):
    data_dev = 0
    num = 0
  return data_dev,contabilizar,comprovante,num
def renovar():
  d = dia_hoje()
  agora = d + timedelta(days = 10)
  data_renov = agora.strftime('%d/%m/%y')
  emprestimos_user[login][num][2] = data_renov
  hoje = d.strftime('%d/%m/%y')
  emprestimos_user[login][num][6] = hoje
  print("Renovado com sucessso!!!")
  print()
  return emprestimos_user
def multa():
  print('\n\n--- !! MULTA POR ATRASO !!  ---')
  multa = int((100 * (data_dev - data_marcada))/30)
  usuario[login][1][0] = multa
  usuario[login][1][1] = devolucao
  print('\n %d dias de punição sem Aluguel, a partir do dia '%(multa,devolucao))
  return usuario
def validar_multa():
  legal = False
  if usuario[login][1][0] != 0:
    d = dia_hoje()
    dia_multa = datetime.strptime(usuario[login][1][1],'%d/%m/%Y').date()
    diferenca = d - dia_multa
    usuario[login][1][0] = diferenca = int(str(diferenca)[0])
  if usuario[login][1][0] != 0:
    legal = False
    print('Faltam %d dias de penalidade!'%diferenca)
  else:
    legal = True
    print('Usuário não possui Multas!')
  return legal

def pesq_update_por_codigo():
  palavra = 'Atualizar'
  codigo = input('\n- Insira o código do livro a %s: '%palavra)
  if codigo in titulos:
    return codigo
  else:
    print('\n~~Código Inválido, Tente novamente!')
    return 0
def pesq_update_por_titulo():
  palavra = 'Atualizar'
  titulo = input('\n- Insira o Titulo a %s: '%palavra)
  validar = False
  for codigo in titulos:
    if titulo.upper() in titulos[codigo][0].upper():
      validar = True
      return codigo
  if not(validar):
    print('\n~Titulo não cadastrado!')
    return 0
def pesq_update_por_autor():
  autor = input('\nInforme o autor do livro a %s: '%palavra)
  validar = False
  for codigo in titulos:
    if autor.upper() in titulos[codigo][1].upper():
      validar = True
      return codigo
  if not(validar):
    print('\n~Autor(a) não encontrado!')
    return 0

def converter_titulo_em_codigo():
  titulo = input('\n- Insira o Titulo a %s: '%palavra)
  for codigo in titulos:
    if titulo.upper() in titulos[codigo][0].upper():
      return codigo 
def converter_autor_em_codigo():
  titulo = input('\n- Insira o Autor do Titulo a %s: '%palavra)
  for codigo in titulos:
    if titulo.upper() in titulos[codigo][1].upper():
      return codigo           
def validar_codigo_acao():
  codigo = ('\nInsira o Código do livro a %s: '%palavra)
  validar = False
  for num in range(len(emprestimos_user[login])):
    if codigo == emprestimos_user[login][num][0]:
      validar = True
      return codigo,validar
  if not(validar):
    codigo = ''
    return codigo,validar
def modulo_update():
  print()
  print("         - - - - - Dados atuais - - - - -")
  print('            Título : ', titulos[codigo][0])
  print('            Autor(a)  : ', titulos[codigo][1])
  print('            Editora: ', titulos[codigo][2])
  print('            Edição : ', titulos[codigo][3])
  print('            Quantidade: ', titulos[codigo][4])
  print('            Código: ',codigo)
  print('          - - - - - - - - - - - - - - -\n')
  print('''
    - - - - - - - - - - - - - - - - -
    1- Título      2- Autor   5 - Quantidade
    3- Editora     4- Edição  6 - Prateleira
    - - - - - - - - - - - - - - - - -''')
  update = input('\n Sua opção: ')
  print()  
  if update == '1':
      titulo = input("Novo Título: ")
      titulos[codigo][0] = titulo
  elif update == '2':
      autor = input("Novo Autor: ")
      titulos[codigo][1] = autor
  elif update == '3':
      editora = input("Nova Editora: ")
      titulos[codigo][2] = editora
  elif update == '4':
      edicao = input("Nova Edição: ")
      titulos[codigo][3] = edicao
  elif update == '5':
    quantidade = input('Nova Quantidade: ')
    while not(quantidade.isdigit()):
      quantidade = input('Nova Quantidade(Apenas números): ')
    titulos[codigo][4] = int(quantidade)
  else:
      print("\nOpção inválida! \n~ Selecione novamente o módulo de atualização!")
  print("Título atualizado com sucesso! ") 
  return titulos

def cabecario_conta():
  print("%-12s | %-12s | %-20s | %-20s | %-10s | %-20s | %-20s |%-25s | "%("Código","Quantidade","Data do emprestimo","Data para Devolver",'Status','Data Devolução','Renovação','Titulo'))
  print('-'*13, '-'*13, '-'*22, '-'*22,'-'*12,'-'*22,'-'*22,'-'*26)
def tabela_livro_locado():
  print("%-12s | %-12s | %-20s | %-20s | %-10s |%-24s | %-24s |%-25s |"%(emprestimos_user[login][x][0], emprestimos_user[login][x][1], emprestimos_user[login][x][3], emprestimos_user[login][x][2],locado,emprestimos_user[login][x][5],emprestimos_user[login][x][6],titulos[emprestimos_user[login][x][0]][0])) 
def tabela_livro_renovado():
  print()


def menu_relatorio():
  esc = input('''
  _______________________________________________________
                      Menu Relatório   
  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    1 - Exibir Quantidade de Emprestimos dos Usuários        
    
    2 - Exibir Usuários com Multas

    3 - Exibir Locação de todas as pessoas

    4 - Exibir lista de usuarios                                             
  ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
  Sua escolha: ''')
  if esc == '1':
    quant_emprest()
  elif esc == '2':
    user_multas()
  elif esc == '3':
    loc_pessoa()
  elif esc == '4':
    print('\n','- '*20)
    cont = 1
    for pessoa in usuario:
        print('         nº %d : '%cont,pessoa,end=';\n')
        cont += 1
  else:
    print('\n~~Opção inválida!')
def quant_emprest():
  dic = {}
  for pessoa in emprestimos_user:
    dic[pessoa]=len(emprestimos_user[pessoa])
  info = dic.items()
  decrescente = sorted(dic.items(), key=itemgetter(1), reverse=True)
  cont = 1
  print('\n\n')
  for i in decrescente:
    print('%d º--'%cont,i[0],':',i[1],end='\n')
    cont += 1
def user_multas():
  dic = {}
  print('Lista por quantidade de dias de multa')
  validar = True
  for pessoa in usuario:
    if usuario[pessoa][1][0] != 0:
      dic[pessoa] = usuario[pessoa][1][0]
      validar = False
  if validar:
    print('~~Não há Usuários com multas')
  else:
    decrescente = sorted(dic.items(), key=itemgetter(1), reverse=True)
    cont = 1
    print('\n\n')
    for i in decrescente:
      print('%d º--'%cont,i[0],':',i[1],end='\n')
      cont += 1
def loc_pessoa():
  for pessoa in emprestimos_user:
      print('\n         - - - User: %s - - -'%pessoa)
      if len(emprestimos_user[pessoa]) == 0:
          print('\n         Usuário não Alugou livros!')
      else:
        for livro in emprestimos_user[pessoa]:
          if livro[4]:
            status = 'Locado'
          else:
            status = 'Devolvido'
          print('''
          Título: {}
          Código: {}    
          Data do emprestimo: {}
          Renovação: {}
          Data para devolução: {}
          Data devolução: {}
          Status: {}'''.format(titulos[livro[0]][0],livro[0],livro[3],livro[6],livro[2],livro[5],status))    


def exibir_users():
  pergt = input('''
  ---  ---  ---  ---  ---  ---  ---    
      
      Quer a Lista de Usuários?
              (S/N)
  ---  ---  ---  ---  ---  ---  ---  
  -Sua escolha: 
  ''')
  if pergt.upper() == 'S':
    cont = 1
    for pessoa in usuario:
        print('Usuário nº %d : '%cont,pessoa,end=';\n')
        cont += 1

## --------------- PROGRAMA  -------------- ##
titulos = verificar_arq_titulos()
usuario = verificar_arq_usuarios()
emprestimos_user = verificar_arq_emprestimos()
lista_data = []
opcao2 = ''


while opcao2 != '3':
  opcao,opcao2,cargo = menu_login()
  while opcao != '3':
    if opcao == "1":
      cadastrarUsuario()
    elif opcao == '2':
      cargo = input('\nQual seu cargo (Cliente(C) ou Funcionário(F)): ')
      cargo = cargo.upper()
      while (cargo != 'C') and (cargo != 'F'):
        cargo = input('\nQual seu cargo (Cliente(C) ou Funcionário(F)): ')
        cargo = cargo.upper()
      login = input("- Usuário: ")
      if login  in usuario:
        senha = input("- Senha: ")
        tentativas = 0
        while usuario[login][0] != senha and tentativas < 1:
          tentativas += 1
          print('~~ Senha incorreta, tente mais uma vez!')
          senha = input("Senha: ")
        if senha == usuario[login][0]:
          break
      else:
        print('\n\n~~Usuário não cadastrado ou senha incorreta\n')
    else:
      print("Opção inválida!")
    opcao,opcao2,cargo = menu_login()
  if cargo == 'F' and opcao2 != '3':
    resp = ""
    while resp.lower() != "0":
      clear()
      resp = menu_funcionario()
      if resp == "1":
        titulos = cadastrar_titulo()
      elif (resp == "2"):
        if len(titulos) == 0:
          print('\n~~Não há livros no Acervo!')
        else:
          escolha = menu_pesquisar()
          palavra = 'Atualizar'
          if escolha == '1':
            codigo = pesq_update_por_titulo()
          elif escolha == '2':
            codigo = pesq_update_por_autor()
          elif escolha == '3':
            codigo = pesq_update_por_codigo()
          else:
            print('\n~~Opção Inválida')
          if codigo != 0:
            titulos = modulo_update()
          else:
            print('Tente novamente...')

      elif (resp == '3'):
        excluir = menu_exluir()
        if excluir == '1':
          excluir_por_titulo()
        elif excluir == '2':
          excluir_por_autor()
        elif excluir == '3':
         excluir_por_codigo()
        else:
          print('\n\n~~Opção inválida!')  
      elif (resp == '4'):
        exibir_acervo()
      elif(resp == '5'):
        menu_relatorio()  
      elif (resp == '6'):
        escolha = menu_pesquisar()
        if escolha == '1':  
          pesquisar_por_titulo()
        elif escolha == '2':
          pesquisar_por_autor()
        elif escolha == '3':
          pesquisar_por_codigo()
        else:
          print('\n\n~~Opção inválida!')
      elif (resp == '0'):
        print('\n~~Sessão finalizada com sucesso, Até a proxima!')
      else:
        print('\n\n~~Escolha inválida!') 
  elif cargo == 'C' and opcao2 != '3':
    while opcao != '0':
      clear()
      opcao = menu_cliente()
      if opcao == "1":
        escolha = menu_pesquisar()
        if len(titulos) == 0:
          print()
        else:
          palavra = 'atualizar'
          if escolha == '1':  
            pesquisar_por_titulo()
          elif escolha == '2':
            pesquisar_por_autor()
          elif escolha == '3':
            pesquisar_por_codigo()
          else:
            print('\n\n~~Opção inválida!')
      elif opcao == "2":
          exibir_acervo()
      elif opcao == "3":
        emprestimos_user = modulo_emprestimo()
      elif opcao == "4":
          print("\n\n")
          print('_____________________')
          print(" Módulo Minha Conta ")
          print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯\n')
          if len(titulos) == 0:
            print('\n~~Não há livros no Acervo\n')
          else:
            if login in emprestimos_user:      
              cabecario_conta()
              for x in range (len(emprestimos_user[login])):
                if emprestimos_user[login][x][4]:		
                  locado = 'Locado'
                  tabela_livro_locado()
                elif not(emprestimos_user[login][x][4]):
                  locado = "Devolvido"
                  tabela_livro_locado()
            else:
              print('Você não tem emprestimos feitos!')
      elif opcao == "5":
          print("\n\n")
          print("Módulo de Devolução/Renovação de empréstimo")
          if len(titulos) == 0:
            print('\n~~Não há livros no Acervo\n')
          else:
            if len(emprestimos_user[login]) == 0:
              print('\n~~Você não tem livros a renovar')
            else:
              print("\n-- Informe: \n-- 'D' para Devolução ou 'R' para Renovação")
              resp = input("\n- O que deseja?(D/R) ")
              if resp.upper() == 'D':
                escolha = menu_pesquisar()
                palavra = 'Devolver'
                if escolha == '1':
                  codigo =converter_titulo_em_codigo()
                elif escolha == '2':
                  codigo = pesq_update_por_autor()
                elif escolha == '3':
                  codigo = pesq_update_por_codigo()
                else:
                  codigo = ''
                  print('\n~~Opção Inválida')
                validar,data_dev,data_marcada,devolucao,comprovante = devolver()
                if data_dev > data_marcada:
                  usuario = multa()
                if validar and (comprovante < len(emprestimos_user[login])):
                  print('\n~Você já devolveu este Livro!\n')
                if comprovante == len(emprestimos_user[login]):
                  print('\n~~Você não alugou este Titulo!')    
              elif resp.upper() == 'R': 
                escolha = menu_pesquisar()
                palavra = 'renovar'
                if escolha == '1':
                  codigo = converter_titulo_em_codigo()
                elif escolha == '2':
                  codigo = converter_autor_em_codigo()
                elif escolha == '3':
                  codigo = validar_codigo_acao()
                else:
                  print('\n~Livro não encontrado!')
                contabilizar = False
                agora = dia_hoje()
                data_dev,contabilizar,comprovante,num= validar_renovacao()
                if comprovante < len(emprestimos_user[login]) and emprestimos_user[login][num][4]:
                  if agora > data_dev:
                      usuario = multa()
                  else:  
                    emprestimos_user = renovar()
                else:
                  print('\n É necessario estar com o Livro para renova-lo !')
              else:
                print('\n~~Opção Inválida!')     
      elif opcao == "0":
          print("\n\n")
          print("Módulo de Encerramento")
          print("Obrigado por usar o nosso programa")
          print()
      else:
          print("\n\n")
          print("Opção Inválida!")
          print("Tente novamente...")

gravar_emprestimos()
gravar_titulos()
gravar_usuarios()
print('\n\nTodos os arquivos foram salvos!\n\n--- Fim do programa!')
print('\nObrigado Por Usar nosso Programa.\nSe gostou deixa o like, increva-se e Ative o sininho!\nPassa lá no Canal da Twitch e deixa o follow(twitch.com/renanplayerow)\n\nBy: Renan Vale Dantas & Rayssa Nayara Santos de Almeida\n\nInstagram: @ooo.renan & @n_salmeida')