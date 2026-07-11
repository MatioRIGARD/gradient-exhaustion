# Gradient Exhaustion — Guide agent

## Projet

Recherche scientifique : **modéliser l'éviction des humains de la boucle économique par des optimiseurs IA** (« exhaustion asymétrique des gradients »), chercher seuils critiques et hystérésis, publier un article (Alignment Forum + arXiv). Porteur : Mathieu, développeur, non-économiste — expliquer les notions économiques simplement, en français.

**Ce repo est 100 % scientifique. Aucune mention de cryptomonnaie, token ou blockchain, nulle part.**

## Où est quoi

- `PLAN.md` — **commence ici** : plan en phases/tâches (T0.1 → T5.5) avec critères d'acceptation. Exécuter UNE tâche à la fois, celle que Mathieu demande.
- `docs/background.md` — contexte scientifique, état de l'art, contacts, lectures. ⚠️ = référence à vérifier avant citation.
- `docs/research-program.md` — le diagnostic à valider (D1/D2), les 7 questions (Q1-Q7), les critères d'abandon (K1-K4).
- `docs/decisions.md` — journal des arbitrages de design + heuristiques pour trancher. **À consulter avant de poser une question d'arbitrage à Mathieu.**
- `docs/simulation-architecture.md` — architecture cible du code (`sim/`), protocole expérimental (V1-V3, E1-E6, figures F1-F6).
- `paper/paper.md` — squelette de l'article (anglais).
- `research/raw/` — notes de recherche brutes (sources à revérifier avant citation).

## Règles non négociables

1. **Anti-tautologie** : humains et IA ne diffèrent que par des *valeurs de paramètres*, jamais par des règles spéciales. Tout terme qui force la conclusion (l'éviction humaine) est un bug. Les tests `test_sanity.py` encodent ce principe : s'ils échouent, on corrige le cœur, on ne les affaiblit pas.
2. **Ordre des validations** : V1 (accord analytique) → V2 (sanity) → V3 (invariances) avant toute expérience E*. Jamais l'inverse.
3. **Les GATES de PLAN.md appartiennent à Mathieu** — ne jamais les franchir de sa propre initiative.
4. **Critères d'acceptation contractuels** : tâche non conforme = « bloquée », pas « faite ».
5. **Résultats conditionnels** : chaque conclusion cite les ablations qui la soutiennent.
6. **Reproductibilité** : seed dérivé du hash de config ; tout chiffre cité est régénérable par une commande.

## Conventions

- Français avec Mathieu ; anglais dans `paper/` et le code.
- Python 3.12+, numpy vectorisé (populations en arrays, pas d'objets par agent), pytest, ruff (ligne 100).
- Configs d'expériences en YAML dans `experiments/configs/`, un fichier par expérience, jamais de nombre magique dans le code.
- `make setup / test / lint / format` ; à terme `make paper` régénère figures et PDF de zéro.

## Contexte historique (une ligne)

Le projet vient d'une phase exploratoire antérieure (archivée hors de ce repo, obsolète — ne pas s'y référer) ; tout ce qui compte a été distillé dans `docs/`.
