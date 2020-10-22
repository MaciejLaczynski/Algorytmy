class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Lista:
    def __init__(self):
        self.head = Node()

    def dlugosc(self):
        wez_ob = self.head
        total = 0
        while wez_ob.next is not None:
            total += 1
            wez_ob = wez_ob.next
        return total

    def dodajwez(self, data):
        nowy_wezel = Node(data)
        poz_obecna = self.head
        while poz_obecna.next is not None:
            poz_obecna = poz_obecna.next
        poz_obecna.next = nowy_wezel
        return

    def usun(self):
        teraz = self.head
        tail = teraz
        teraz = teraz.next
        elements = []
        elements.append(teraz.data)
        print("Podany element będzie usunięty z listy: " + str(elements))
        tail.next = teraz.next
        return

    def wypisz(self):
        teraz = self.head
        elementy = []
        while teraz.next is not None:
            teraz = teraz.next
            elementy.append(teraz.data)
        print(*elementy)

list = Lista()

print(list.head)

list.dodajwez(1)
list.dodajwez(2)
list.dodajwez(3)
list.dodajwez(4)
list.dodajwez(5)
list.dodajwez(6)

list.wypisz()

list.usun()

list.wypisz()

list.usun()
list.usun()

list.wypisz()

