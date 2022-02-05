from system.move import Move
import chess


class Engine:

    def get_next_best_move(self, game) -> str:
        raise NotImplemented

    def _change_moves_to_fen_format(self, moves: [Move]):
        san_mainline = []
        for move in moves:
            san_mainline.append(move.get_move())
        separator = " "
        san_mainline = separator.join(san_mainline)
        board = chess.Board()
        for move in san_mainline.split():
            board.push_san(move)
        return board.fen()
