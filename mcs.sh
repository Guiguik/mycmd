#!/bin/bash

# Définition du prompt personnalisé
custom_prompt() {
    echo -n "$(whoami)@$(hostname):$(pwd)$ "
}

# Boucle principale du shell
while true; do
    # Affichage du prompt personnalisé
    custom_prompt

    # Lecture de la commande de l'utilisateur
    read -r command

    # Traitement des commandes
    case $command in
        exit)
            break
            ;;
        hello)
            echo "Hello, world!"
            ;;
        *)
            echo "Commande non reconnue. Tapez 'exit' pour quitter."
            ;;
    esac
done
