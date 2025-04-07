taxonomy_data = {
    "Mammalia": {
        "Level": "Class",
        "Artiodactyla": {
            "Level": "Order",
            "Ancodonta": { # ungulates
                "Level": "Infraorder",
                "Bovidae": { "Level": "Family" },
                "Cervidae": { "Level": "Family" },
                "Giraffidae": { "Level": "Family" },
                "Hippopotamidae": { "Level": "Family" }
            },
            "Cetacea": { # marine mammals
                "Level": "Infraorder",
                "Mysticeti": { # baleen whales
                    "Level": "Parvorder",
                    "Balaenidae": { "Level": "Family" }, # right whale, bowhead whale
                    "Balaenopteridae": { "Level": "Family" }, # rorquals
                    "Eschrichtiidae": { "Level": "Family" }, # gray whales
                },
                "Odontoceti": { # toothed whales
                    "Level": "Parvorder",
                    "Delphinoidea": { "Level": "Family" }, # orca, vaquita, dolphins
                    "Physeteroidea": { "Level": "Superfamily" }, # sperm whale, pygmy sperm whale, dwarf sperm whale
                    "Phocoenidae": { "Level": "Family" }, # Porpoises
                    "Platanistidae": { "Level": "Family" }, # river dolphins
                    "Ziphiidae": { "Level": "Family" }, # beaked whales
                }
            }  
        },
        "Carnivora": {
            "Level": "Order",
            "Caniformia": { # dog-like carnivores
                "Level": "Suborder",
                "Canidae": { "Level": "Family" }, # dogs, wolves, foxes
                "Ursidae": { "Level": "Family" }, # bears
            },
            "Feliformia": { # cat-like carnivores
                "Level": "Suborder",
                "Felidae": { "Level": "Family" }, # big cats, small cats, cheetahs
                "Hyaenidae": { "Level": "Family" }, # hyaenas, aardwolves
            }
        },
        "Dermoptera": {
            "Level": "Order",
            "Chiroptera": { "Level": "Family" }, # bats
            "Cynocephalidae": { "Level": "Family" }, # colugos
        },
        "Eulipotyphla": {
            "Level": "Order",
            "Erinaceidae": { "Level": "Family" },
            "Soleonodontidae": { "Level": "Family" },
            "Soricidae": { "Level": "Family" },
        },
        "Lagomorpha": {
            "Level": "Order",
            "Leporidae": { "Level": "Family" }, # rabbits, hares
            "Ochotonidae": { "Level": "Family" }, # pikas
        },
        "Macroscelidea": {
            "Level": "Order",
            "Macroscelidae": { "Level": "Family" }, # elephant shrews
        },
        "Perissodactyla": { # odd-toed ungulates
            "Level": "Order",
            "Equidae": { "Level": "Family" }, # horses, donkeys, zebras
            "Rhinocerotidae": { "Level": "Family" },
            "Tapiridae": { "Level": "Family" } # tapirs
        },
        "Primates": {
            "Level": "Order",
            "Haplorrhines": {
                "Level": "Suborder",
                "Simiiformes": {
                    "Level": "Infraorder",
                    "Catarrhines": {
                        "Level": "Parvorder",
                        "Cercopithecidae": { "Level": "Family" },
                        "Homonidae": { "Level": "Family" }, # great apes
                    },
                    "Platyrrhines": {
                        "Level": "Parvorder",
                        "Atelidae": { "Level": "Family" },
                    },
                },
                "Tarsiiformes": {
                    "Level": "Infraorder",
                    "Tarsiidae": { "Level": "Family" }
                }
            },
            "Strepsirrhines": {
                "Level": "Suborder",
                "Daubentoniidae": { "Level": "Family" },
                "Lemuridae": { "Level": "Family" },
                "Loridae": { "Level": "Family"}
            }
        },
        "Rodentia": {
            "Level": "Order",
            "Bathyergidae": { "Level": "Family" },
            "Castoridae": { "Level": "Family" },
            "Caviidae": { "Level": "Family" },
            "Chinchillidae": { "Level": "Family" },
            "Cricetidae": { "Level": "Family" },
            "Erethizonditae": { "Level": "Family" },
            "Hystricidae": { "Level": "Family" },
            "Muridae": { "Level": "Family" }, # true mouse/rat family
            "Sciuridae": { "Level": "Family" }, # squirrel family
        },
        "Sirenia": {
            "Level": "Order",
            "Dugongidae": { "Level": "Family" }, # dugongs
            "Trichechidae": { "Level": "Family" }, # manatees
        },
        "Tubulidentata": {
            "Level": "Order",
            "Orycteropodidae": {"Level": "Family" }, # aardvarks
        },
        "Hyraxes": {
            "Level": "Order",
            "Proviidae": { "Level": "Family" },
        }
    }
}