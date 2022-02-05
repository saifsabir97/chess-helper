from backend.system.constants import EngineType
from backend.system.engine.engine import Engine
from backend.system.engine.stockfish_engine import StockfishEngine


class EngineFactory:

    @staticmethod
    def get_engine(engine_type: EngineType) -> Engine:
        if engine_type == EngineType.stockfish:
            return StockfishEngine()
        else:
            raise NotImplemented
