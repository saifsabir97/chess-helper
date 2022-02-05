from system.parser.chess_dot_com_parser import ChessDotComParser
from system.parser.parser import Parser
from system.parser.lichess_parser import LichessParser
from system.constants import Platform


class ParserFactory:

    @staticmethod
    def get_board_parser(platform: Platform) -> Parser:
        if platform == Platform.lichess:
            return LichessParser()
        elif platform == Platform.chess:
            return ChessDotComParser()
        raise NotImplemented
