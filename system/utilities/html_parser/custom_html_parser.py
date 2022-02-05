class CustomHTMLParser:

    def get_child_node(self, html_content: str, node_name: str) -> str:
        raise NotImplemented

    def get_child_node_value(self, html_content: str, node_name: str) -> str:
        raise NotImplemented

    def save_html_page(self, html_content: str, file_path: str):
        textfile = open(file_path, "w")
        html_content = html_content.replace("\\n", "\n")[2:-1]
        textfile.write(html_content)
        textfile.close()
