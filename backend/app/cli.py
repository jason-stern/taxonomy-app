from core.taxonomy_tree import build_tree
from core.lca import find_lca

def main():
    tree = build_tree()
    user_input = "init"

    print("Welcpome to the Taxonomy Command-Line Interface! Enter one of the following valid inputs:")
    print(" - p: print the entire Mammaia taxonomy tree")
    print (" - t: find the Taxonomy path to any specified Order or Family")
    print (" - c: Check two inputs & see how closely related they are")
    print(" - q: quit the program")

    while user_input != "q":
        print("--- --- --- --- --- -l-- --- --- --- --- --- ---")
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
                print(f"{level.level}: {level.common_name} ({level.scientific_name})")
        elif user_input == "q":
            print("Ending program")
        elif user_input == "c":
            a = input("Entry #1 -- ").strip()
            b = input("Entry #2 -- ").strip()


            path_a = tree[0].find_path(a)
            path_b = tree[0].find_path(b)

            for level in path_a:
                if level in path_b:
                    print(f"SHARED {level.level}: {level.common_name} ({level.scientific_name})")
        else:
            print("Invalid input!")
            print(" - p: print the entire Mammalia taxonomy tree")
            print (" - t: find the Taxonomy path to any specified Order or Family")
            print(" - q: quit the program")

if __name__ == "__main__":
    main()