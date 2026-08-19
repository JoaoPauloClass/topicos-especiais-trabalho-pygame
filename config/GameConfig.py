class EngineConfig:
    WIDTH = 1280
    HEIGHT = 720
    FPS = 15


class PlayerConfig:
    PLAYER_VELOCITY = 1
    PLAYER_SHIP = 3 # numero que pega cada uma das 4 partes do sprite sheet que encontrei

class ShipConfig:
    DADOS_NAVES = {
        0: {
            "nome": "Caça Leve",
            "vida": 3,
            "velocidade": 500,
            "tipo_tiro": "simples",
            "cooldown": 0.2,  # Atira a cada 0.2 segundos
        },
        1: {
            "nome": "Tanque Pesado",
            "vida": 8,
            "velocidade": 250,
            "tipo_tiro": "duplo",
            "cooldown": 0.5,
        },
        2: {
            "nome": "Nave Laser",
            "vida": 4,
            "velocidade": 400,
            "tipo_tiro": "laser_triplo",
            "cooldown": 0.4,
        },
        3: {
            "nome": "Nave Ágil",
            "vida": 2,
            "velocidade": 650,
            "tipo_tiro": "espalhado",
            "cooldown": 0.15,
        },
    }

