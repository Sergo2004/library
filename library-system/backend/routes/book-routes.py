from flask import Blueprint, request, jsonify

book_bp = Blueprint('books', __name__)

@book_bp.route('/books', methods=['GET'])
def get_books():
    return jsonify([
        {
            'id': 1,
            'title': '1984',
            'author': 'George Orwell'
        }
    ])

@book_bp.route('/books', methods=['POST'])
def add_book():
    data = request.json

    return {
        'message': 'Book added',
        'data': data
    }, 201
