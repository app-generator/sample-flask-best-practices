from flask_limiter import Limiter
from flask_seasurf import SeaSurf
from flask_talisman import Talisman
from flask_limiter.util import get_remote_address
from app.load_config import load_config_yaml

def setup_security_measure_on_application(app):
    """
    This function sets up the security measure on the flask application

    :param app: The flask app that needs to be protected
    :return: all the protection measure applied on the app
    """
    rate_config = load_config_yaml("app/config/rate_limiter.yaml")
    return {
        "csrf": SeaSurf(app),
        "limiter": Limiter(app,
                           key_func=get_remote_address,
                           default_limits=rate_config.get("RATE_LIMITER_OPTS",[])),
        "talisman": Talisman(app)}
