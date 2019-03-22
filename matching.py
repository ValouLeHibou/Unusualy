def algo(
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
    sex2= "femme"
    wantedsex2 = "homme"
    region2 = "bretagne"
    age2 = 20
    wantedage2 = [18, 30]
    trait2 = ["insupportable", "yala", "yolo"]
    traitimportant2 = "non"
    allergy2 = ["eau", "nuage", "sable"]
    allergyimportant2 = "oui"

    linktrait = []
    linkallergy = []

    # Start with sextype
    if wantedsex == sex2 and wantedsex2 == sex or \
            wantedsex == "osef" and wantedsex2 == sex or \
            wantedsex == "osef" and wantedsex2 == "osef":

        # Region
        if region == region2:

            # Age
            if wantedage[0] <= age2 <= wantedage[1] and wantedage2[0] <= age <= wantedage2[1]:

                # Trait verification
                for onetrait in trait:
                    if onetrait in trait2:
                        linktrait.append(onetrait)
                        print(linktrait)
                if linktrait or traitimportant == "non" and traitimportant2 == "non":

                    # Allergy
                    for oneallergy in allergy:
                        if oneallergy in allergy2:
                            linkallergy.append(oneallergy)
                    if linkallergy:
                        print(linkallergy)
                        return "##### TABLEAU[id, Nom, Prénom, age, description, region, linktrait, linkallergy] #####"
                        # display matching par qualité du matching
                    else:
                        print("Pas d'allergie, pas de match")
                else:
                    print("rien trouvé & trait important")
            else:
                print("t'as merdé (age)")
        else:
            print("t'as merdé (region)")
    else:
        print("t'as merdé (sexe)")

    return "ok"
   # return (sex, wantedsex, region, age, wantedage, trait, traitimportant, allergy, allergyimportant)
