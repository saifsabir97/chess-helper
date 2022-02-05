from bs4 import BeautifulSoup

from backend.system.utilities.html_parser.custom_html_parser import CustomHTMLParser


class BeautifulSoupCustomHTMLParser(CustomHTMLParser):

    def __init__(self):
        super().__init__()
        self.__parser_type = "lxml"

    def get_child_node(self, html_content: str, node_name: str) -> str:
        parsed_html = BeautifulSoup(html_content, self.__parser_type)
        return str(parsed_html.body.find(node_name))

    def get_child_node_value(self, html_content: str, node_name: str) -> str:
        parsed_html = BeautifulSoup(html_content, self.__parser_type)
        return parsed_html.body.find(node_name).text
