from system.parser.parser import Parser
from system.move import Move
from system.utilities.html_parser.beautiful_soup_html_parser import BeautifulSoupCustomHTMLParser


class LichessParser(Parser):

    def __init__(self):
        self.__html_parser = BeautifulSoupCustomHTMLParser()
        self.__move_container_tag = "l4x"
        self.__move_row_tag = "<i5z>"

    def get_moves(self, html_page: bytes):
        child_node = self.__html_parser.get_child_node(str(html_page), self.__move_container_tag)
        child_node = child_node.replace("<j></j>", "")
        child_node = child_node.replace("><", ">\n<")
        child_node = child_node.split("\n")
        child_node = child_node[1:]

        moves = []
        for index, move_node in enumerate(child_node):
            xml_string = move_node.strip()
            if xml_string.startswith(self.__move_row_tag):
                white_move_index = index + 1
                black_move_index = index + 2

                if white_move_index < len(child_node):
                    move = self.__generate_move(child_node[white_move_index])
                    moves.append(move)
                if black_move_index < len(child_node):
                    move = self.__generate_move(child_node[black_move_index])
                    moves.append(move)
        return moves

    def __generate_move(self, raw_move: str) -> Move:
        raw_move = self.__html_parser.get_child_node_value(raw_move, "u8t")
        move = Move(raw_move)
        return move
