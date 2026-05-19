from flask import Blueprint

reader_bp = Blueprint('readers', __name__)

@reader_bp.route('/readers', methods=['GET'])
def get_readers():
    return {
        'readers': []
    }
