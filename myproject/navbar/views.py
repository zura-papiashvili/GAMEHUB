from flask import Blueprint,render_template

navbar_blueprint = Blueprint("navbar",__name__,template_folder="templates/navbar")

@navbar_blueprint.route("/categories")
def categories():
    return render_template("categories.html")

@navbar_blueprint.route("/championship")
def championship():
    return render_template("csgo-champtionship.html")

@navbar_blueprint.route("/matches")
def matches():
    return render_template("matches.html")