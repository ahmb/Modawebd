from flask import Blueprint, request, g


api = Blueprint('api', __name__)

from ..models import User
from . import comments, errors
from ..auth import authx, auth_token

@api.before_request
@auth_token.login_required
def before_request():
    """All routes in this blueprint require authentication."""
    pass

from . import customers, products, orders, items, errors

#commented out to test API
'''
@api.before_request
def before_api_request():
    if request.json is None:
        return errors.bad_request('Invalid JSON in body.')
    token = request.json.get('token')
    if not token:
        return errors.unauthorized('Authentication token not provided.')
    user = User.validate_api_token(token)
    if not user:
        return errors.unauthorized('Invalid authentication token.')
    g.current_user = user
'''