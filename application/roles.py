from functools import wraps
from flask import redirect, url_for

from .db import GetRoles

def roles_required(*required_roles):
    # This decorator ensures that a user has a specific role
    # If the user doesn't it will redirect them to another page

    """
    
    Example::

        @route('/adminPage')
        @roles_accepted('Admin')
        def admin_view(): ## The User has to be an admin to access this page
            ...

    """

    def wrapper(view_function):

        @wraps(view_function)
        def decorator(*args, **kwargs):

            roles = GetRoles()
            for role in required_roles:
                if role not in roles:
                    return redirect(url_for("main_bp.home"))

            return view_function(*args, **kwargs)
        
        return decorator

    return wrapper
