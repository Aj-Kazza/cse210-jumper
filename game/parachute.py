class Parachute:
    """
    Parachute class: keeps score and prints parachute
    """
    def __init__(self):
        """
        has score as attribute
        """
        self._score = 4


    #the original parachute sprites
    """
    def jump(self):
        if self._score == 4:
            print("  ___ ")
            print(" /___\\")
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 3:
            print(" /___\\")
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 2:
            print(" \\   /")
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 1:
            print("  \\ /")
            print("   0")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
        elif self._score == 0:
            print("   x")
            print("  /|\\")
            print("  / \\")
            print("")
            print("^^^^^^^")
    """


    def score_number(self, number):
        """
        changes score
        """
        self._score = number

    def get_score(self):
        """
        return score
        """
        return self._score

    #altered ascii sprites
    def jump(self):
        """
        prints parachute sprite
        """
        if self._score == 4:
            print("░░░░░░░░░░░░▄▄▄▄▄▄▄▄▄░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░███████████░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░█│││││││││█░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▀███████▀░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▐░░░░░░░▌░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░█▄░█░▄█░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░o▄██░██▄o░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░║░░║░░║░░║░░║░░║░░░░░░░░░░░░░░░\n"
            "░░░░░░░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬░░░░░░░░░░░░░░░")
        elif self._score == 3:
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░╬██╬█╬█╬██╬░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░█│││││││││█░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▀███████▀░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▐░░░░░░░▌░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░█▄░█░▄█░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░o▄██░██▄o░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░║░░║░░║░░║░░║░░║░░░░░░░░░░░░░░░\n"
            "░░░░░░░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬░░░░░░░░░░░░░░░")
        elif self._score == 2:
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░█│││││││││█░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▀███████▀░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▐░░░░░░░▌░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░█▄░█░▄█░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░o▄██░██▄o░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░║░░║░░║░░║░░║░░║░░░░░░░░░░░░░░░\n"
            "░░░░░░░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬░░░░░░░░░░░░░░░")
        elif self._score == 1:
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░▐█▌░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░!░!░!░!░!░▐█▌░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░▐░░░░░░░▌░░▄░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░█▄░█░▄█░░░▀░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░o▄██░██▄o░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░║░░║░░║░░║░░║░░║░░░░░░░░░░░░░░░\n"
            "░░░░░░░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬░░░░░░░░░░░░░░░")
        elif self._score == 0:
            print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░oh░well░░░░░░░░░\n"
            "░░░░░░░░░░░_░░▄░╬░▄░░_░░¯\_(ツ)_/¯░░░░░░\n"
            "░░░░░░░░░░░░▀▄██░██▄▀░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░█░█░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n"
            "░░░░░░░░░║░░║░░║░░║░░║░░║░░░░░░░░░░░░░░░\n"
            "░░░░░░░░╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬░░░░░░░░░░░░░░░")