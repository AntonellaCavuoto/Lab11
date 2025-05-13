import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listColor = []

    def fillDD(self):
        colori = self._model.getColori()
        for j in colori:
            self._view._ddcolor.options.append(ft.dropdown.Option(j))
            self._view._page.update()

        i = 2015
        for j in range(4):
            if i <= 2018:
                self._view._ddyear.options.append(ft.dropdown.Option(str(i)))
                i += 1
            self._view._page.update()



    def handle_graph(self, e):
        pass



    def fillDDProduct(self):
        pass


    def handle_search(self, e):
        pass
