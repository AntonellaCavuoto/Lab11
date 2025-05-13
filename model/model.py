import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._nodes = DAO.getProdotti()
        self._idMap = {}
        for c in self._nodes:
            self._idMap[c.Product_number] = c

    def getColori(self):
        colori = DAO.getColori()
        return colori

    def buildGraph(self, colore, anno):
        self.addNodes(colore)
        self.addEdges(anno, colore)
        return len(self._graph.edges())

    def addNodes(self, colore):
        prodCol = DAO.getProdottiColore(colore)
        for p in prodCol:
            self._graph.add_node(self._idMap[p.Product_number])

    def addEdges(self, anno, colore):
        prodAnno = DAO.getProdAnno(anno, colore)

        for i in prodAnno:
        #     peso = 1
        #     for j in prodAnno:
        #         if i.pn1 == j.pn1 and i.pn2 == j.pn2 and (i.retailer != j.retailer or i.retailer == j.retailer) and i.date != j.date:
        #             peso += 1

            list=DAO.getPeso(anno, colore, str(i.pn1), str(i.pn2))
            self._graph.add_edge(self._idMap[i.pn1], self._idMap[i.pn2], weight=len(list))

    def getArchiPesoMax(self):
        # archi_ordinati = sorted(self._graph.edges, key =lambda x: x[2], reverse = True)
        s = ""
        archi_ordinati = sorted(self._graph.edges(data=True), key=lambda x: x[2]['weight'], reverse=True)

        for u, v, data in archi_ordinati:
            s += (f"Arco {u} - {v}, peso: {data['weight']}\n")

        return s
