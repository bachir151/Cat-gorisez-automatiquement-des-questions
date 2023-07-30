import numpy as np
from flask import Flask, request, jsonify, render_template
from modules import preprocessing, predict_tags, final_preprocessing

# Création de l'application Flask
flask_app = Flask(__name__)

# endpoints pour la page d'accueil
@flask_app.route("/")
def Home():
    return render_template("index.html")

# endpoints pour la prédiction
@flask_app.route("/predict/", methods=["POST"])
def predict():
    # Récupération du texte saisi par l'utilisateur dans les champs "title" et "body" du formulaire
    title = request.form['title']
    body = request.form['body']

    # Concaténation du titre et du corps pour former le texte complet à prédire
    X = title + body

    # Prétraitement du texte : suppression des caractères spéciaux, mise en minuscules, etc.
    doc = preprocessing(X, rejoin=True)
    doc = final_preprocessing(doc)

    # Prédiction des tags pour le texte donné
    prediction = predict_tags(doc)

    # Renvoi des résultats de prédiction au template "index.html" pour affichage à l'utilisateur
    return render_template("index.html", prediction_text="Tag(s) prédit(s) : {}".format(prediction))

# Démarrage de l'application Flask
if __name__ == "__main__":
    flask_app.run(debug=True)



