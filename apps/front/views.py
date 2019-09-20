from flask import Blueprint

bp = Blueprint('front',__name__)  #因为是前台直接访问不用加url_prefix

@bp.route('/')
def index():
    return 'front index'

