# Celem tego programu jest spiralne przejście przez macierz 2D


class Solution:


    
    global wynik
    wynik = []

    def rotacja( m ):
        return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]


    def spiralOrder(self,snail_map):
        if(snail_map==[[]]):
            return []

        for i in range(len(snail_map[0])):
            # print(i)
            wynik.append(snail_map[0][i])
        del(snail_map[0])
        if (snail_map):
            if len(snail_map)+len(snail_map[0])>1 :

                snail_map = Solution.rotacja(snail_map)
                Solution.spiralOrder(self,snail_map)

            else:

      

                    wynik.append((snail_map[0]))
                    del(snail_map[0])

                  

        if(wynik!=[]):
            global odp
            odp= wynik.copy()

        wynik.clear()
        if(odp):
            return odp
