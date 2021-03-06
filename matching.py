def algo(
        # DONNEES DU USER #
        # (données admin créées dans app.py ) #

        # sex (string) -> homme, femme
        sex = "",
        # sexetype (string) -> homme, femme, osef
        wantedsex = "",
        # region (string) -> ville
        region = "",
        # age (int)
        age = int,
        # wantedage (tableau d'int) -> (int1, int2)
        wantedage = [],
        # trait (tableau de string) -> [trait1, trait2, trait3, trait4, trait5] | minimum 2 traits
        trait = [],
        # traitimportant (string) -> oui, non
        traitimportant = "",
        # allergy (tableau de string) -> [allergy1, allergy2, allergy3, allergy4, allergy5] | minimum 1 allergy
        allergy = [],
        # allergyimportant (string) -> oui, non, osef
        allergyimportant = "",

):
    match = []
    # DONNEES EN DUR (testt) #
    persona = ["femme", "homme", "bretagne", 19, [18, 30], ["insupportable", "gentil", "doux"], "non", ["eau", "nuage", "sable"], "oui"],\
              ["homme", "homme", "bretagne", 25, [25, 30], ["patient", "test", "distrait"], "non", ["eau", "nuage", "sable"], "oui"],\
              ["femme", "osef", "bretagne", 27, [25, 30], ["aimable", "rêveur", "distrait"], "non", ["eau", "nuage", "sable"], "oui"],\
              ["homme", "osef", "bretagne", 30, [25, 30], ["joueur", "test", "distrait"], "non", ["eau", "nuage", "sable"], "oui"],\
              ["homme", "femme", "bretagne", 25, [25, 30], ["loufoque", "rêveur", "distrait"], "non", ["eau", "test", "sable"], "oui"],\
              ["femme", "femme", "bretagne", 25, [25, 30], ["mignion", "test", "distrait"], "non", ["eau", "nuage", "sable"], "oui"],\
              ["homme", "osef", "bretagne", 70, [25, 30], ["insupportable", "rêveur", "distrait"], "non", ["eau", "test", "sable"], "oui"],\
              ["femme", "femme", "bretagne", 25, [25, 30], ["vigilant", "test", "distrait"], "non", ["eau", "nuage", "sable"], "oui"],\
              ["homme", "homme", "bretagne", 25, [25, 30], ["élégant", "rêveur", "distrait"], "non", ["eau", "test", "sable"], "oui"],\
              ["femme", "homme", "centre", 25, [25, 30], ["insupportable", "rêveur", "distrait"], "non", ["eau", "nuage", "sable"], "oui"]

    for onepersona in persona:
        linktrait = []
        linkallergy = []
        sex2 = onepersona[0]
        wantedsex2 = onepersona[1]
        region2 = onepersona[2]
        age2 = onepersona[3]
        wantedage2 = onepersona[4]
        trait2 = onepersona[5]
        traitimportant2 = onepersona[6]
        allergy2 = onepersona[7]
        allergyimportant2 = onepersona[8]

        # Start with sextype
        if wantedsex == sex2 and wantedsex2 == sex or \
                wantedsex == "osef" and wantedsex2 == sex or \
                wantedsex == "osef" and wantedsex2 == "osef":

            # Region
            if region == region2:

                # Age
                if wantedage[0] <= age2 <= wantedage[1] and wantedage2[0] <= age <= wantedage2[1]:

                    # Trait verification)
                    for onetrait in trait:
                        if onetrait in trait2:
                            linktrait.append(onetrait)
                        else:
                            print("pas ce trait là")
                    if linktrait or traitimportant == "non" and traitimportant2 == "non":  # match possible si les deux n'ont pas de traits en commun
                        print("###############", linktrait)
                        # Allergy
                        for oneallergy in allergy:
                            if oneallergy in allergy2:
                                linkallergy.append(oneallergy)
                            else:
                                print("pas cette allergie là")
                        if linkallergy:
                            match.append([sex2, wantedsex2, region2, age2, linktrait, linkallergy])

                            #return "##### TABLEAU[id, Nom, Prénom, age, description, region, linktrait, linkallergy] #####"
                            # display matching par qualité du matching
                        else:
                            print("Pas d'allergie, pas de match")
                    else:
                        print("rien trouvé & trait important")
                else:
                    print("pas le bon age")
            else:
                print("Pas la bonne region")
        else:
            print("pas le bon sexe")
    print("####################### MATCH(s) ###########################")
    print(match)
    print("############################################################")
    return "look console"
