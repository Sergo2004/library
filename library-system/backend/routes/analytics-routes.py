from flask import Blueprint

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/analytics/popular-books')
def popular_books():
    return {
        'books': [
            {
                'title': '1984',
                'issues': 152
            }
        ]
    }

@analytics_bp.route('/analytics/overdue')
def overdue_books():
    return {
        'overdue_count': 12
    }
