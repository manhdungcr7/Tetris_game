class Colors:
    dark_grey = (238, 180, 180)
    green = (0, 255, 0)
    red = (255, 0, 0)
    orange = (185, 69, 0)
    yellow = (255, 255, 0)
    purple = (166, 0, 227)
    cyan = (0, 0, 0)
    blue = (0, 10, 255)
    white = (250, 250, 210)
    dark_blue = (128, 128, 128)
    light_blue = (50, 0, 100)
    menu = (36, 73, 200)

    @classmethod
    def get_cell_colors(cls):
        """
        Trả về danh sách các màu dùng để thể hiện các ô trong ứng dụng.

        Returns:
            list: Danh sách các tuple màu RGB.
                Bao gồm các màu: dark_grey, green, red, orange, yellow, purple, cyan, blue.
        """
        return [ cls.cyan, cls.green, cls.red, cls.dark_grey, cls.white, cls.orange, cls.yellow, cls.purple, cls.blue]
