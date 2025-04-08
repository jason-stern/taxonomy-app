taxonomy_data = {
    "Mammalia": {
        "Level": "Class",
        "Common Name": "Mammals",
        "Artiodactyla": {
            "Level": "Order",
            "Common Name": "Artiodacts",
            "Ancodonta": { # ungulates
                "Level": "Infraorder",
                "Common Name": "Anocdonts",
                "Bovidae": { "Level": "Family", "Common Name": "Bovids" },
                "Cervidae": { "Level": "Family", "Common Name": "Cervids" },
                "Giraffidae": { "Level": "Family", "Common Name": "Giraffids" },
                "Hippopotamidae": { "Level": "Family", "Common Name": "Hippopotamids" },
            },
            "Cetacea": { # marine mammals
                "Level": "Infraorder",
                "Common Name": "Cetaceans",
                "Mysticeti": { # baleen whales
                    "Level": "Parvorder",
                    "Common Name": "Baleen Whales",
                    "Balaenidae": { "Level": "Family", "Common Name": "Balaenids" }, # right whale, bowhead whale
                    "Balaenopteridae": {
                        "Level": "Family",
                        "Common Name": "Rorquals",
                        "Balaenoptera": { "Level": "Genus", "Common Name": "Balaenoptera" },
                        "Megaptera": { "Level": "Genus", "Common Name": "Humpback Whales" }
                    }, # rorquals
                    "Eschrichtiidae": {
                        "Level": "Family",
                        "Common Name": "Gray Whales",
                        "Eschrichtius": { "Level": "Genus", "Common Name": "Gray Whale"}
                        }, # gray whales
                },
                "Odontoceti": { # toothed whales
                    "Level": "Parvorder",
                    "Common Name": "Toothed Whales",
                    "Delphinoidea": { "Level": "Superfamily", "Common Name": "Delphinoids" }, # orca, vaquita, dolphins: Delphinidae, Monodontidae, Phocoenidae
                    "Physeteroidea": { "Level": "Superfamily", "Common Name": "Sperm Whales" }, # sperm whale, pygmy sperm whale, dwarf sperm whale
                    "Phocoenidae": { "Level": "Family", "Common Name": "Porpoises" }, # Porpoises
                    "Monotonidae": { "Level": "Family", "Common Name": "Monotonidae" },
                    "Platanistidae": { "Level": "Family", "Common Name": "River Dolphins" }, # river dolphins
                    "Ziphiidae": { "Level": "Family", "Common Name": "Beaked Whales" }, # beaked whales
                }
            }  
        },
        "Carnivora": {
            "Level": "Order",
            "Common Name": "Carnivores",
            "Caniformia": { # dog-like carnivores
                "Level": "Suborder",
                "Common Name": "Dog-Like Carnivores",
                "Canidae": { "Level": "Family", "Common Name": "Canines" }, # dogs, wolves, foxes
                "Ursidae": {
                    "Level": "Family",
                    "Common Name": "Bears",
                    "Ailuropodinae": {
                        "Level": "Subfamily",
                        "Common Name": "Pandas",
                        "Ailuropoda": { "Level": "Genus", "Common Name": "Panda bears" }
                    },
                    "Tremarctinae": {
                        "Level": "Subfamily",
                        "Common Name": "Short-faced bear",
                        "Tremarctos": { "Level": "Genus", "Common Name": "Spectacled bear" }
                    },
                    "Ursinae": {
                        "Level": "Subfamily",
                        "Common Name": "Ursinae",
                        "Ursus": { "Level": "Genus", "Common Name": "Common bears" },
                        "Melursus": { "Level": "Genus", "Common Name": "Sloth bear" },
                        "Helarctos": { "Level": "Genus", "Common Name": "Sun bear" },
                    },
                }, # bears
            },
            "Feliformia": { # cat-like carnivores
                "Level": "Suborder",
                "Common Name": "Cat-Like Carnivores",
                "Felidae": { # to do: subfamilies of felis and panthera (felinae, pantherinae, etc), so i can do ocelots and stuff
                    "Level": "Family",
                    "Common Name": "Felines",
                    "Felinae": {
                        "Level": "Subfamily",
                        "Common Name": "Small cats",
                        "Acinonyx": { "Level": "Genus", "Common Name": "Cheetah-Like Cats" },
                        "Felis": { "Level": "Genus", "Common Name": "Felis" },
                        "Puma": { "Level": "Genus", "Common Name": "Pumas" }
                    },
                    "Pantherinae": {
                        "Level": "Subfamily",
                        "Common Name": "Big cats",
                        "Panthera": { "Level": "Genus", "Common Name": "Panthers" } },
                },
                "Hyaenidae": { "Level": "Family", "Common Name": "Hyaenids" }, # hyaenas, aardwolves
            }
        },
        "Dermoptera": {
            "Level": "Order",
            "Common Name": "Dermoptera",
            "Chiroptera": { "Level": "Family", "Common Name": "Bats" }, # bats
            "Cynocephalidae": { "Level": "Family", "Common Name": "Colugos"}, # colugos
        },
        "Eulipotyphla": {
            "Level": "Order",
            "Common Name": "True Insectivores",
            "Erinaceidae": { "Level": "Family", "Common Name": "Erinaceids" },
            "Soleonodontidae": { "Level": "Family", "Common Name": "Solenodons" },
            "Soricidae": { "Level": "Family", "Common Name": "Shrews" },
        },
        "Lagomorpha": {
            "Level": "Order",
            "Common Name": "Lagomorphs",
            "Leporidae": { "Level": "Family", "Common Name": "Leporids" }, # rabbits, hares
            "Ochotonidae": { "Level": "Family", "Common Name": "Pikas" }, # pikas
        },
        "Macroscelidea": {
            "Level": "Order",
            "Common Name": "Macroscelids",
            "Macroscelidae": { "Level": "Family", "Common Name": "Elephant Shrews" }, # elephant shrews
        },
        "Perissodactyla": { # odd-toed ungulates
            "Level": "Order",
            "Common Name": "Odd-Toed Ungulates",
            "Equidae": {
                "Level": "Family",
                "Common Name": "Equids",
                "Equus": { "Level": "Genus", "Common Name": "Equus" }
            },
            "Rhinocerotidae": { "Level": "Family", "Common Name": "Rhinos" },
            "Suidae": {
                "Level": "Family",
                "Common Name": "Swines",
                "Sus": { "Level": "Genus", "Common Name": "Pigs" },
                "Porcula": { "Level": "Genus", "Common Name": "Pygmy hog" },
                "Hylocherus": { "Level": "Genus", "Common Name": "Giant forest hog" },
                "Phacochoerus": { "Level": "Genus", "Common Name": "Warthogs" },
                "Babyrousa": { "Level": "Genus", "Common Name": "Babirusas" },
            },
            "Tapiridae": { "Level": "Family", "Common Name": "Tapirs" } # tapirs
        },
        "Pilosa": {
            "Level": "Order",
            "Common Name": "Pilosans",
            "Folivora": { "Level": "Suborder", "Common Name": "Sloths" }, # sloths
            "Vermilingua": { "Level": "Suborder", "Common Name": "Anteaters" }, # anteaters
        },
        "Primates": {
            "Level": "Order",
            "Common Name": "Primates",
            "Haplorrhini": { # dry-nosed primates
                "Level": "Suborder",
                "Common Name": "Dry-Nosed Primates",
                "Simiiformes": {
                    "Level": "Infraorder",
                    "Common Name": "Simians",
                    "Catarrhini": {
                        "Level": "Parvorder",
                        "Common Name": "Catarrhines",
                        "Cercopithecidae": { "Level": "Family", "Common Name": "Old World Monkeys" }, # old world monkeys
                        "Homonidae": {
                            "Level": "Family",
                            "Common Name": "Great Apes",
                            "Pongo": { "Level": "Genera", "Common Name": "Orangutan" },
                            "Gorilla": { "Level": "Genera", "Common Name": "Gorilla" },
                            "Pan": { "Level": "Genera", "Common Name": "Chimpanzee" },
                            "Homo": { "Level": "Genera", "Common Name": "Humanoid" }
                        },
                    },
                    "Platyrrhini": {
                        "Level": "Parvorder",
                        "Common Name": "Platyrrhines",
                        "Ceboidea": { "Level": "Superfamily", "Common Name": "New World Monkeys" }, # new world monkeys
                    },
                },
                "Tarsiiformes": {
                    "Level": "Infraorder",
                    "Common Name": "Tarsiiformes",
                    "Tarsiidae": { "Level": "Family", "Common Name": "Tarsiers" }
                }
            },
            "Strepsirrhini": { # wet-nosed primates
                "Level": "Suborder",
                "Common Name": "Wet-Nosed Primates",
                "Daubentoniidae": { "Level": "Family", "Common Name": "Aye-Ayes" }, # aye aye is the one extant member; technically daubentonids is the more "correct name"
                "Lemuridae": { "Level": "Family", "Common Name": "Lemurids" },
                "Lorisidae": { "Level": "Family", "Common Name": "Lorisids" }
            }
        },
        "Rodentia": {
            "Level": "Order",
            "Common Name": "Rodents",
            "Bathyergidae": { "Level": "Family", "Common Name": "Blesmols" },
            "Castoridae": { "Level": "Family", "Common Name": "Beavers" },
            "Caviidae": { "Level": "Family", "Common Name": "Cavies" }, # guinea pigs, capybaras
            "Chinchillidae": { "Level": "Family", "Common Name": "Chinchillids" },
            "Cricetidae": { "Level": "Family", "Common Name": "Cricetids" },
            "Erethizonditae": { "Level": "Family", "Common Name": "New World Porcupines" },
            "Hystricidae": { "Level": "Family", "Common Name": "Old World Porcupines" },
            "Muridae": { "Level": "Family", "Common Name": "Murids" }, # true mouse/rat family
            "Sciuridae": { "Level": "Family", "Common Name": "Squirrels" }, # squirrel family
        },
        "Sirenia": {
            "Level": "Order",
            "Common Name": "Sea Cows",
            "Dugongidae": { "Level": "Family", "Common Name": "Dugongs" }, # dugongs
            "Trichechidae": { "Level": "Family", "Common Name": "Manatees" }, # manatees
        },
        "Tubulidentata": {
            "Level": "Order",
            "Common Name": "Tubulidentates",
            "Orycteropodidae": {"Level": "Family", "Common Name": "Aardvarks" }, # aardvarks
        },
        "Hyraxes": {
            "Level": "Order",
            "Common Name": "Hyraxes",
            "Proviidae": { "Level": "Family", "Common Name": "Dassies" },
        }
    }
}