from core.taxonomy_data import taxonomy_data

class Node:
    def __init__(self, scientific_name, common_name, level, data=None):
        self.scientific_name = scientific_name
        self.common_name = common_name
        self.level = level
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_path(self, target, path=None):
        if path is None:
            path = []
        path.append(self)

        if self.scientific_name.lower() == target.lower() or self.common_name.lower() == target.lower():
            return path
        for child in self.children:
            result = child.find_path(target, path.copy())
            if result:
                return result
            
        return None

    def print_tree(self, indent=0):
        print(" " * indent + f"{self.level}: {self.common_name} ({self.scientific_name})")
        for child in self.children:
            child.print_tree(indent + 1)

def build_tree():
    return build_tree_helper(taxonomy_data)

def build_tree_helper(taxonomy_data):
    nodes = []
    for name, data in taxonomy_data.items():
        if isinstance(data, dict) and "Level" in data:
            level = data["Level"]
            common_name = data["Common Name"]
            scientific_name = name
            node = Node(scientific_name, common_name, level)

            # children
            for child_name, child_data in data.items():
                if child_name != "Level":
                    child_nodes = build_tree_helper( {child_name: child_data} )
                    for child_node in child_nodes:
                        node.add_child(child_node)

            nodes.append(node)


    return nodes

