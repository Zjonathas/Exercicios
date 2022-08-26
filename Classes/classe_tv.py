"""Classe TV: faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""


class Tv:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def diminuir_volume(self, voluminho):
        self.volume = self.volume - voluminho
        if self.volume < 0:
            self.volume = 0

    def aumentar_volume(self, volumao):
        self.volume = self.volume + volumao
        if self.volume > 100:
            self.volume = 100

    def mudar_canal(self, new_chanel):
        if new_chanel > 100:
            return None
        elif new_chanel < 0:
            return None
        self.canal = new_chanel
