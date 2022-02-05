from system.parser.parser import Parser
from system.move import Move
from system.utilities.html_parser.beautiful_soup_html_parser import BeautifulSoupCustomHTMLParser


class ChessDotComParser(Parser):

    def __init__(self):
        self.__html_parser = BeautifulSoupCustomHTMLParser()
        self.__eco_opening_tag = "eco-opening"
        self.__eco_opening_links_tag = "div"

    def get_moves(self, html_page: bytes):
        eco_opening_node = self.__html_parser.get_child_node(str(html_page), self.__eco_opening_tag)
        eco_opening_links = self.__html_parser.get_child_node(eco_opening_node, self.__eco_opening_links_tag)

        total_length = len(eco_opening_links)
        index = 0
        prefix_match = "moveList"
        raw_moves = ""
        while index < total_length:
            if eco_opening_links[index:].startswith(prefix_match):
                move_index = index + len(prefix_match) + 1
                while move_index < total_length and eco_opening_links[move_index] != '&':
                    raw_moves += eco_opening_links[move_index]
                    move_index += 1
                break
            index += 1
        raw_moves = raw_moves.split('+')
        moves = []
        for raw_move in raw_moves:
            move = Move(raw_move)
            moves.append(move)
        return moves
