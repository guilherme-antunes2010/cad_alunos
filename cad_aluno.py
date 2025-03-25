import shelve
import random
from datetime import datetime

hoje = datetime.now()

while True:
    print()
    print('---------------Bem vindo ao sistema de cadastro de alunos---------------')
    print()
    escolha = input('O que você deseja fazer\n 1. Cadastrar\n 2. Visualizar Alunos\n 3. Editar aluno \n 4. Buscar Aluno\n 5. Sair\n\n ')
    print()

    if escolha != "1" and escolha != "2" and escolha != "3" and escolha != "4" and escolha != "5":
        print("Opção inválida")
        print()
        continue
    
    if escolha == '5':
        break
    if escolha == '1':
        id = random.randrange(1, 100)
        nome  = input("Digite o nome do aluno: ")
        data_nasc = input("Digite a data de nascimento do aluno (ex: dd/mm/aaaa): ")
        data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y')
        curso = input("Digite o curso do aluno: ")
        aula = input("Digite a aula do aluno: ")
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        with shelve.open('dados.txt') as db_alunos:
            if 'alunos' not in db_alunos:
                db_alunos['alunos'] = []  # Inicializa a lista de alunos se não existir
            alunos_lista = db_alunos['alunos']
            alunos_dict = {
                'id': id,
                'nome': nome,
                'idade': idade,
                'data_nasc': data_nasc.strftime('%d/%m/%Y'),
                'curso': curso,
                'aula': aula
            }
            alunos_lista.append(alunos_dict)
            db_alunos['alunos'] = alunos_lista
    if escolha == '2':
        with shelve.open('dados.txt') as db_alunos:
            if 'alunos' not in db_alunos:
                print("Nenhum aluno cadastrado.")
                continue
            alunos_lista = db_alunos['alunos']
            for aluno in alunos_lista:
                print(f' Id: {aluno["id"]}\n Nome: {aluno["nome"]}\n Idade: {aluno["idade"]}\n Data de Nascimento: {aluno["data_nasc"]}\n Curso: {aluno["curso"]}\n Aula: {aluno["aula"]}\n')
    if escolha == '4':
        with shelve.open('dados.txt') as db_alunos:
            if 'alunos' not in db_alunos:
                print("Nenhum aluno cadastrado.")
                continue
            alunos_lista = db_alunos['alunos']
            busca = int(input("Digite o ID do aluno que deseja buscar: "))
            for aluno in alunos_lista:
                if aluno['id'] == busca: 
                    print(f' Id: {aluno["id"]}\n Nome: {aluno["nome"]}\n Idade: {aluno["idade"]}\n Data de Nascimento: {aluno["data_nasc"]}\n Curso: {aluno["curso"]}\n Aula: {aluno["aula"]}\n')
                    break
            else:
                print("Aluno não encontrado.")
    if escolha == '3':
        with shelve.open('dados.txt') as db_alunos:
            if 'alunos' not in db_alunos:
                print("Nenhum aluno cadastrado.")
                continue
            alunos_lista = db_alunos['alunos']
            busca = int(input("Digite o ID do aluno que deseja editar: "))
            for aluno in alunos_lista:
                if aluno['id'] == busca: 
                    print(f' Id: {aluno["id"]}\n Nome: {aluno["nome"]}\n Idade: {aluno["idade"]}\n Data de Nascimento: {aluno["data_nasc"]}\n Curso: {aluno["curso"]}\n Aula: {aluno["aula"]}\n')
                    print()
                    edicao = input('O que você deseja editar?\n1. Nome\n2. Data de Nascimento\n3. Curso\n4. Aula\n5.Tudo \n')

                    if edicao == '1':
                        nome = input("Digite o nome do aluno: ")
                        aluno['nome'] = nome
                    if edicao == '2':
                        data_nasc = input("Digite a data de nascimento do aluno (ex: dd/mm/aaaa): ")
                        data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y')
                        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
                        aluno['data_nasc'] = data_nasc.strftime('%d/%m/%Y')
                        aluno['idade'] = idade
                    if edicao == '3':
                        curso = input("Digite o curso do aluno: ")
                        aluno['curso'] = curso
                    if edicao == '4':
                        aula = input("Digite a aula do aluno: ")
                        aluno['aula'] = aula
                    if edicao == '5':
                        nome  = input("Digite o nome do aluno: ")
                        data_nasc = input("Digite a data de nascimento do aluno (ex: dd/mm/aaaa): ")
                        data_nasc = datetime.strptime(data_nasc, '%d/%m/%Y')
                        curso = input("Digite o curso do aluno: ")
                        aula = input("Digite a aula do aluno: ")
                        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
                        aluno['nome'] = nome
                        aluno['data_nasc'] = data_nasc.strftime('%d/%m/%Y')
                        aluno['idade'] = idade
                        aluno['curso'] = curso
                        aluno['aula'] = aula
                    break
            else:
                print("Aluno não encontrado.")
            db_alunos['alunos'] = alunos_lista