import yaml
from app.app_logger import message_handle

def load_config_yaml(conf="config.yaml"):
    """
    This function loads the configuration yaml for a spcified path
    :param conf: path the the yaml file
    :return: the yaml file as a json
    """
    with open(conf, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            message_handle(msg=str(exc))