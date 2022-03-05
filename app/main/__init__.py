from flask import Blueprint
main = Blueprint('main', __name__) #name of the blueprint and __name__ variable to find the location of the blueprint
from . import views, errors #we import to avoid circular dependencies