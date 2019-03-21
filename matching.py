from flask import Flask, render_template, redirect, url_for, request, session



def algo(
        # sexetype (string) -> homme, femme, autre, osef
        sexetype = "",
        # city (string) -> ville
        city = "",
        # distance (int) -> 10, 50, 100, 0 | valeur 0 = pas de limite de distance
        distance = int,
        # age (int)
        age = int,
        # wantedage (tableau d'int) -> (int1, int2)
        wantedage = [],
        # trait (tableau de string) -> [trait1, trait2, trait3, trait4, trait5] | minimum 2 traits
        trait = [],
        # traitimportant (string) -> oui, non, osef
        traitimportant = "",
        # allergy (tableau de string) -> [allergy1, allergy2, allergy3, allergy4, allergy5] | minimum 1 allergy
        allergy = [],
        # allergyimportant (string) -> oui, non, osef
        allergyimportant = "",
):



    return (sexetype, city, distance, age, wantedage, trait, traitimportant, allergy, allergyimportant)


def filter():
    return
