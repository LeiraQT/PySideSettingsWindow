import configparser
import os

def create_config(path):
    """
    Создание default файла конфигурации по пути path
    """
    config = configparser.ConfigParser()
    config.add_section("Offset settings")
    config.add_section("Debug settings")
    config.add_section("Connection settings")

    config.set("Offset settings", "OX", "50")
    config.set("Offset settings", "OY", "50")
    config.set("Offset settings", "multiplier", "10")
    config.set("Offset settings", "height", "50")
    config.set("Offset settings", "vertical step", "50")

    config.set("Debug settings", "threshold canny filter", "50")
    config.set("Debug settings", "threshold contour", "50")
    config.set("Debug settings", "delay", "50")

    config.set("Connection settings", "IP", "192.168.0.1")
    config.set("Connection settings", "port", "8888")

    
    with open(path, "w") as config_file:
        config.write(config_file)
 
 
def get_config(path):
    """
    Возвращает config объект, расположенный по пути path 
    """
    if not os.path.exists(path):
        create_config(path)
    
    config = configparser.ConfigParser()
    config.read(path)
    return config
 
 
def get_setting(path, section, setting):
    """
    Выдает (и при необходимости печатает) настройку setting из секции section
    """
    config = get_config(path)
    value = config.get(section, setting)
    """
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )
    
    print(msg)
    """
    return value
 
 
def update_setting(path, section, setting, value):
    """
    Обновляет настройку setting значением value в секции section
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)
 
 
def delete_setting(path, section, setting):
    """
    Удалаяет настройку setting в секции section
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)