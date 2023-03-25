from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))  # gets data from our json file
# print(pets)

bp = Blueprint(
    'pet',  # name of Blueprint
    __name__,  # defining it as a name
    url_prefix='/pets'  # url route
)


@bp.route('/')
def index():
    return render_template(
        'index.html',
        pets=pets
    )


@bp.route('/<int:id>')
def get_pet(id):
    pet = pets[id - 1]
    return render_template(
        'pet_page.html',
        pet=pet,
    )
