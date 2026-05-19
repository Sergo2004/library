from flask import Blueprint

issue_bp = Blueprint('issues', __name__)

@issue_bp.route('/issues', methods=['GET'])
def get_issues():
    return {
        'issues': []
    }
