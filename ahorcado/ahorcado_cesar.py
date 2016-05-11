# ENTREGA 2 VERIFIACION Y DESARROLLO - CESAR GIL MORENO
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import mock
from pymongo import MongoClient

# Para representar la parte grafica del juego, array de strings
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']


class Ahorcado:
    URL_MONGO = 'mongodb://localhost:27017/'
    DATABASE_NAME = 'verificacion'

    def __init__(self):
        self.client = MongoClient(self.URL_MONGO)
        self.db = self.client[self.DATABASE_NAME]

    def displayBoard(self, AHORCADO, wrongLetter, correctLetter, secretWord):
        print(AHORCADO[len(wrongLetter)])
        print ""
        endl = " "
        print 'Letras incorrectas:', endl
        for letter in wrongLetter:
            print (letter, endl)
        print ""
        spacing = '_' * len(secretWord)
        for i in range(len(secretWord)):  # Reemplaza los espacios en blanco por la letra bien escrita
            if secretWord[i] in correctLetter:
                spacing = spacing[:i] + secretWord[i] + spacing[i + 1:]
        for letter in spacing:  # MostrarA la palabra secreta con espacios entre letras
            print (letter, endl)
        print ""

    def chooseLetter(self, someLetter):
        # Devuelve la letra que el jugador ingreso. Esta funcion hace que el jugador ingrese una letra y no cualquier otra cosa
        while True:
            print 'Adivina una letra:'
            letter = raw_input()
            letter = letter.lower()
            if len(letter) != 1:
                print 'Introduce una sola letra.'
            elif letter in someLetter:
                print 'Ya has elegido esa letra, elige otra.'
            elif letter not in 'abcdefghijklmnopqrstuvwxyz':
                print 'Elije una letra.'
            else:
                return letter

    def selectWord(self):
        print 'Bienvenido, Introduzca la palabra secreta con la que desea jugar:'
        secretWord = raw_input()  # El jugador introduce por teclado la palabra
        secretWord = secretWord.lower()  # la palabra pasa a minusculas para evitar fallos
        self.saveWord(secretWord)
        return secretWord

    def begin(self):
        # Esta funcion devuelve True si el jugador quiere volver a jugar, de lo contrario devuelve False
        print 'Quieres jugar de nuevo? (Introduzca una s si desea jugar de nuevo\n cualquiera otra tecla para salir.)'
        return raw_input().lower().startswith('s')

    def saveWord(self, word):
        self.db.words.insert_one({word: word})

    def getAllWords(self):
        cursor = self.db.words.find()
        for document in cursor:
            print(document)

if __name__ == "__main__":
    print 'JUEGO DEL A H O R C A D O'
    partida = Ahorcado()
    wrongLetter = ""
    correctLetter = ""
    secretWord = partida.selectWord()
    name = raw_input("Cual es tu nombre?: ")
    endGame = False

    while True:
        partida.displayBoard(AHORCADO, wrongLetter, correctLetter, secretWord)
        # Llama al metodo para que el usuario introduzca una letra
        letter = partida.chooseLetter(wrongLetter + correctLetter)
        if letter in secretWord:
            correctLetter = correctLetter + letter
            # Comprueba si el jugador ha acertado
            lettersFound = True
            for i in range(len(secretWord)):
                if secretWord[i] not in correctLetter:
                    lettersFound = False
                break
            if lettersFound:
                print ('Biennn!! la palabra secreta era: ' + secretWord + 'You Win!')
                partida.saveWord(secretWord)
                endGame = True
        else:
            wrongLetter = wrongLetter + letter
            # Comprueba si el jugador ha perdido
            if len(wrongLetter) == len(AHORCADO) - 1:
                partida.displayBoard(AHORCADO, wrongLetter, correctLetter, secretWord)
                print ('YA NO QUEDAN MAS INTENTOS!\nDespues de ' + str(len(wrongLetter)) + ' letras erroneas y ' + str(
                    len(correctLetter)) + ' letras correctas, la palabra era "' + secretWord + '"')
                endGame = True
                # Pregunta al jugador si quiere jugar de nuevo
            if endGame:
                if partida.begin():
                    print 'JUEGO DEL A H O R C A D O'
                    wrongLetter = ""
                    correctLetter = ""
                    endGame = False
                    secretWord = partida.selectWord()  # para elegir de nuevo la palabra
                else:
                    break
