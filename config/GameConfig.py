class EngineConfig:
    WIDTH = 1920
    HEIGHT = 1080
    FPS = 60


class PlayerConfig:
    PLAYER_VELOCITY = 1
    PLAYER_SHIP = 2 # numero que pega cada uma das 4 partes do sprite sheet que encontrei

class ShipConfig:
    DADOS_NAVES = {
        0: {
            "nome": "Caça Leve",
            "vida": 3,
            "velocidade": 100,
            "dano_tiro": 15,
            "vel_tiro": 150,
            "cooldown": 0.2,  # Atira a cada 0.2 segundos
        },
        1: {
            "nome": "Tanque Pesado",
            "vida": 8,
            "velocidade": 250,
            "dano_tiro": 50,
            "vel_tiro": 100,
            "cooldown": 0.5,
        },
        2: {
            "nome": "Nave Laser",
            "vida": 4,
            "velocidade": 25,
            "dano_tiro": 1,
            "vel_tiro": 100,
            "cooldown": 0,
        },
        3: {
            "nome": "Nave Ágil",
            "vida": 2,
            "velocidade": 3,
            "dano_tiro": 10,
            "vel_tiro": 1,
            "cooldown": 0.15,
        },
    }

