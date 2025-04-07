from core.taxonomy_tree import build_tree
from core.lca import find_lca

def main():
    tree = build_tree()
    user_input = "init"

    print("Welcpome to the Taxonomy Command-Line Interface! Enter one of the following valid inputs:")
    print(" - p: print the entire Mammalia taxonomy tree")
    print (" - t: find the Taxonomy path to any specified Order or Family")
    print(" - q: quit the program")

    while user_input != "q":
        print("--- --- --- --- --- --- --- --- --- --- --- ---")
        user_input = input("Enter a valid input -- ").strip().lower()

        if user_input == "p":
            for node in tree:
                node.print_tree()
        elif user_input == "t":
            user_input_tosearch = input("Please enter the *scientific* taxonomical name of any Order/Family within Mammalia -- ").strip()
            path = tree[0].find_path(user_input_tosearch)
            if path == None:
                print("No path found. Check your spelling?")
                continue
            for level in path:
                print(f"{level.level}: {level.scientific_name}")
        elif user_input == "q":
            print("Ending program")
        else:
            print("Invalid input!")
            print(" - p: print the entire Mammalia taxonomy tree")
            print (" - t: find the Taxonomy path to any specified Order or Family")
            print(" - q: quit the program")

if __name__ == "__main__":
    main()