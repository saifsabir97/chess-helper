from system.engine.engine_factory import EngineFactory
from system.parser.parser_factory import ParserFactory
from system.constants import EngineType, Platform


class System:

    def __init__(self, engine_type: EngineType, platform: Platform):
        self._engine = EngineFactory.get_engine(engine_type)
        self._parser = ParserFactory.get_board_parser(platform)

    def get_next_move(self, input_data: bytes) -> {}:
        moves = self._parser.get_moves(input_data)
        next_move = self._engine.get_next_best_move(moves)
        return next_move
