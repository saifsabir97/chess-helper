
from stockfish import Stockfish

from backend.system.engine.engine import Engine
from backend.system.move import Move


class StockfishEngine(Engine):

    def get_next_best_move(self, moves: [Move]) -> str:
        stockfish = Stockfish(depth=12, parameters={"threads": 8})
        fen = self._change_moves_to_fen_format(moves)
        stockfish.set_fen_position(fen)
        best_move = stockfish.get_best_move()
        return best_move
