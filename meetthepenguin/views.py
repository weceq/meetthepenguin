"""Views
"""
from pyramid.view import view_config

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(_):
    """Sample view
    """
    return {'project': 'meetthepenguin'}
