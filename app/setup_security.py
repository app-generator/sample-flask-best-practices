from flask_limiter import Limiter
from flask_talisman import Talisman
from flask_limiter.util import get_remote_address

def setup_security_measure_on_application(app):
    """
    This function sets up the security measure on the flask application

    :param app: The flask app that needs to be protected
    :return: all the protection measure applied on the app
    """
    return {
        "limiter": Limiter(app,
                           key_func=get_remote_address,
                           default_limits=app.config['RATE_LIMITER_OPTS']),
        "talisman": Talisman(app)}
