from core.taxonomy_data import taxonomy_data

class Node:
    def __init__(self, scientific_name, level, data=None):
        self.scientific_name = scientific_name
        self.level = level
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, indent=0):
        print(" " * indent + f"{self.level}: {self.scientific_name}")
        for child in self.children:
            child.print_tree(indent + 1)

def build_tree():
    return build_tree_helper(taxonomy_data)

def build_tree_helper(taxonomy_data):
    nodes = []
    for name, data in taxonomy_data.items():
        if isinstance(data, dict) and "Level" in data:
            level = data["Level"]
            scientific_name = name
            node = Node(scientific_name, level)

            # children
            for child_name, child_data in data.items():
                if child_name != "Level":
                    child_nodes = build_tree_helper( {child_name: child_data} )
                    for child_node in child_nodes:
                        node.add_child(child_node)

            nodes.append(node)


    return nodes

