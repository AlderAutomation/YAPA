import pygame
from time import sleep


class yapa_media_player():
    def __init__(self) -> None:
        pygame.mixer.init()


    def play(self, song_file):
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()


    def stop(self):
        pygame.mixer.music.stop()


    def pause():
        pass


    def forward():
        pass


    def back():
        pass


    def convert_mp3_to_wav():
        pass


def main():
    yapa_media_player().play("./Downloads/test.wav")
    sleep(10)


if __name__ == "__main__":
    main()