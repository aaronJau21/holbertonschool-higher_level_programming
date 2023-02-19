@classmethod
    def create(cls, **dictionary):
        """
        Method that return an object with all fields already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cs.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)