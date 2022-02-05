from backend.system.constants import Platform
from backend.system.parser.chess_dot_com_parser import ChessDotComParser
from backend.system.parser.lichess_parser import LichessParser
from backend.system.parser.parser import Parser


class ParserFactory:

    @staticmethod
    def get_board_parser(platform: Platform) -> Parser:
        if platform == Platform.lichess:
            return LichessParser()
        elif platform == Platform.chess:
            return ChessDotComParser()
        raise NotImplemented
