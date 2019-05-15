# AI_Quixo
Programme python "intelligent", qui renvoie des mouvement valides pour le jeu "QUIXO" 

Comment procède notre intelligence pour jouer un mouvement?

*  Premièrement, nous initialisons quelques variables à chaque tour. Ces variables sont par exemple un dictionnaire comptenant en clé tous les pions sur le bord du plateau et en valeur les directions valables qui leurs sont associées. Nous effectuons aussi une fonction qui se charge de vérifier quel joueur nous sommes (0 ou 1 dans ce jeu ci).

*  Deuxièmement, plusieurs autres fonctions s'exécutent afin d'analyser la variable "game" récupérée. On peut donc dès lors créer des listes qui contiennent les cases nous appartenant, ainsi que les cases vides et celle de notre adversaire.

*  Troisièmement, notre intelligence va toujours essayer de jouer sur la colonne verticale de gauche. Elle va d'abord prendre le cube du dessus ( position 0 ) et le placé en (20 , "S" ), tout en ayant vérifier si elle pouvait effectuer ce mouvement.. Le tour d'après, 	nous récupérons à nouveau les listes consititué  de l'état du jeu, qui nous permet de nous adapté aux coups effectué par notre adversaire. 


Aucune bibliothèque n'a été utilisé pour la création de ce code.



[Réalisé par Noélie De Leeuw (17275) et Sacha Capouet (17309).]
