import cherrypy
import sys
import random

class Server:
    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''

        body = cherrypy.request.json

        sides = {0:["S","E"], 1:["W","E","S"], 2:["W","E","S"], 3:["W","E","S"], 4:["W","S"], 5:["E","N","S"], 9:["W","N","S"], 10:["E","N","S"], 14:["N","W","S"], 15:["E","N","S"], 19:["N","W","S"], 20:["N","E"], 21:["W","N","E"], 22:["W","N","E"], 23:["W","N","E"], 24:["W","N"]} # coordonnées (indice de liste) qu'on peut prendre 
        directions = ['N', 'S', 'E', 'W']
        forbi = {'E': [4, 9, 14, 19, 24],'W': [0, 5, 10, 15, 20], 'N': [0, 1, 2, 3, 4], 'S': [20, 21, 22, 23, 24]} # TU VAS MOURIR!

       

        etatjeu = body["game"]
        moves = body["moves"]
        players = body["players"]
        you = body ["you"]
        cubesmoi = []
        cubesautre = []
        cubesnone = []

            

 # //           N
    # //   | 0| 1| 2| 3| 4|
    # //   | 5| 6| 7| 8| 9|
    # // W |10|11|12|13|14| E
    # //   |15|16|17|18|19|
    # //   |20|21|22|23|24|
    # //           S
    # 
        print("######################################################################################################################")

        def quisontlesjoueurs(): 
            #on sait que moi = 1 et autre = 0 ou l'inverse
            moi = players.index(you)# permet de récuperer l'indice
            if moi == 0:
                autre = 1
            else :
                autre = 0
            return moi, autre
        moi,autre = quisontlesjoueurs()
        #print("je suis : ",moi)

        def cubemoi():
            for i,v in enumerate (etatjeu):
                if v == moi:
                    cubesmoi.append(i)
            return cubesmoi
            #OU
            # for a in range(len(etatjeu)):  
            #     if etatjeu[a] == moi:
            #         cubesmoi.append(a)
        cubesmoi=cubemoi()
        #print("j'ai comme cubes:", cubesmoi)
            

        def cubeautre():
            for i,v in enumerate (etatjeu):
                if v == autre:
                    cubesautre.append(i)
            return cubesautre
        cubesautre = cubeautre()


        def cubenone():
            for i,v in enumerate (etatjeu):
                if v != moi or v != autre:
                    cubesnone.append(i)
            return cubesnone
        cubesnone = cubenone ()


        # def forbi():
        #     #1
        #     for a in cubesautre:
        #         if a == ale:
        #             ale = random.choice(sides)
        #     #2
        #     #temps plus de 10 secondes



        def cherchemax():            #cherche les valeurs max H et V et en sort 2 dictionnaire
            
            dich1 = {}
            dicv1 = {} 

            for i,v in enumerate(etatjeu):
                l=i//5
                c=i%5    
                counth = 0
                countv = 0
            
                if v == moi:
                    for a in range(0,5):
                        if etatjeu[l*5+a] == moi:
                            counth +=1
                            #dich1[l,c]= counth                  # sous forme de tableau
                            dich1[l*5 + c]= counth
                    for a in range(0,5):
                        if etatjeu[a*5+c] == moi:
                            countv += 1
                            #dicv1[l,c] = countv
                            dicv1[l*5 + c]= countv     #""" le dictionnaire a comme clé l'indice ou il faut jouer, et comme valeur, le nombre de cube de moi"""
            return dich1, dicv1
        dich, dicv = cherchemax()


        def choixmax(dic):   #choisit la ligne la plus grande de cube et le sort dans indicemax
            indicemax = 0
            val = 0
            for clé,valeur in dic.items():
                if valeur >= val:
                    val = valeur
                    indicemax = clé
            return (indicemax , val)
        indicemaxh, valh = choixmax(dich)
        indicemaxv, valv = choixmax(dicv)



        def aleatoire():
            newsides = []
            for a in sides.keys():
                newsides.append(a)
            ale = random.choice(newsides) #prend un chiffre aléatoirement

            while ale in cubesautre:   #on vérifie si il appartient pas à l'autre joueur
                ale = random.choice(newsides) #on a trouvé ale (aléatoirement)

            for cle,val in sides.items():
                if cle == ale:
                    b = random.choice (val)  #on a trouvé b (aléatoirement)
            #print("je prends aleatoirement :", (ale,b))
            #return {"move": {"cube": ale , "direction": b }, "message": (ale , b) } # direction N = venant de N
            return {"move": {"cube": ale , "direction": b }, "message": "aleatoire : ({} , {} ) ".format(ale,b) }



        def AI ():
            #print("AI")
            if etatjeu[0] == None:
                return {"move": {"cube": 0 , "direction": "S"}, "message": (0 , "S") } # direction N = venant de N
            if etatjeu[20] == None:
                return {"move": {"cube": 20 , "direction": "N"}, "message": (20 , "N") } # direction N = venant de N
                


            if etatjeu [0] != moi and etatjeu[4] != autre:
                    return {"move": {"cube": 4 , "direction": "W"}, "message": (4 , "W") } # direction N = venant de N
                    #return(4,"W")
               

            if etatjeu [5] != moi and etatjeu [9] != autre:
                return {"move": {"cube": 9 , "direction": "W"}, "message": (9 , "W") } # direction N = venant de N
                    #return(9,"W")
               
            if etatjeu [10] != moi and etatjeu [14] != autre:
                return {"move": {"cube": 14 , "direction": "W"}, "message": (14 , "W") } # direction N = venant de N
                    #return(14,"W")
               
                
            if etatjeu [15] != moi and etatjeu [19] != autre:
                return {"move": {"cube": 19 , "direction": "W"}, "message": (19 , "W") } # direction N = venant de N
                    #return(19,"W")
               

            if etatjeu [20] != moi and etatjeu [24] != autre :#on joue horiz
                return {"move": {"cube": 24 , "direction": "W"}, "message": (24 , "W") } # direction N = venant de N
                    #return(24,"W")

##############################################vertical########################################################
            if etatjeu [5] != moi and etatjeu [9] == autre:#on joue vert
                if etatjeu[20] == moi:
                    return {"move": {"cube": 20 , "direction": "N"}, "message": ((20 , "N"), "MUERTE") } # direction N = venant de N
                elif etatjeu[0]== moi :
                    return {"move": {"cube": 0 , "direction": "S"}, "message": ((0 , "N"), "MUERTE") } # direction N = venant de N
                else :
                    return aleatoire()

            if etatjeu [10] != moi and etatjeu [14] == autre:#on joue vert
                if etatjeu[20] == moi:
                    return {"move": {"cube": 20 , "direction": "N"}, "message": ((20 , "N"), "MUERTE") } # direction N = venant de N
                elif etatjeu[0]== moi :
                    return {"move": {"cube": 0 , "direction": "S"}, "message": ((0 , "N"), "MUERTE") } # direction N = venant de N
                else :
                    return aleatoire()
               
                
            if etatjeu [15] != moi and etatjeu [19] == autre:#on joue vert
                if etatjeu[20] == moi:
                    return {"move": {"cube": 20 , "direction": "N"}, "message": ((20 , "N"), "MUERTE") } # direction N = venant de N
                elif etatjeu[0]== moi :
                    return {"move": {"cube": 0 , "direction": "S"}, "message": ((0 , "N"), "MUERTE") } # direction N = venant de N
                else :
                    return aleatoire()
            else :
                hop = aleatoire ()
                return hop #pourquoi est ce que return aleatoire ne fonctionne pas 
        return AI()
        ############################

    # //           N
    # //   | 0| 1| 2| 3| 4|
    # //   | 5| 6| 7| 8| 9|
    # // W |10|11|12|13|14| E
    # //   |15|16|17|18|19|
    # //   |20|21|22|23|24|
    # //           S


    # {
	# "game": [1, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	# "moves": [],
	# "players": ["LUR", "LRG"],
	# "you": "LUR"
    # }


if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080

    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    cherrypy.quickstart(Server())











