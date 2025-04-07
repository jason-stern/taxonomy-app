from core.taxonomy_tree import build_tree
from core.lca import find_lca

def main():
    tree = build_tree()
    # print("Welcome to Version Alpha of the Taxonomy App! Simply enter two Mammals and learn how they are related.")
    # print(" --------------------")
    # a = input("Enter the first animal: ").strip().lower()
    # b = input("Enter the second animal: ").strip().lower()
    # result = find_lca(a, b, tree)
    # print(result)

    for node in tree:
        node.print_tree()
    
if __name__ == "__main__":
    main()