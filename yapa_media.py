import pygame
from time import sleep

song_file = "/home/matthew/Share/Code/Python/yapa/Downloads/test.wav"

class yapa_media_player():
    def __init__(self) -> None:
        pygame.mixer.init()


    def play(self, song_file):
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()


    def stop(self):
        pygame.mixer.music.stop()


def main():
    yapa_media_player().play(song_file)
    sleep(10)


if __name__ == "__main__":
    main()