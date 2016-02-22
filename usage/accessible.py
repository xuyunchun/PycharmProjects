class Secretive:
    def __inaccessible(self):
        print "Bet you cant't see me..."

    def accessible(self):
        print "The secret message is:"
        self.__inaccessible()
