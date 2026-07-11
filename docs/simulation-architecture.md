# Architecture d'une simulation visant un article scientifique

> **Statut de ce document.** Début d'architecture (conceptuelle, expérimentale et logicielle) pour coder, *from scratch*, la simulation qui porterait l'article visé : première formalisation multi-agents du désempowerment économique (D1+D2 de `research-program.md`), avec recherche de seuils critiques et d'hystérésis. Aucune réutilisation du code antérieur. Pas encore de code ici — c'est le plan qu'on suivra pour l'écrire.

---

## 1. Ce que la simulation doit produire (en partant de l'article, à rebours)

Un article de valeur = 4 à 6 figures dont chacune répond à une question de `research-program.md`. Cible :

| Figure | Question (`research-program.md`) | Résultat espéré |
|---|---|---|
| F1 | D1 : dynamique de π (participation humaine) | π(t) sous différentes vitesses de progrès IA — déclin graduel vs effondrement |
| F2 | Q4a : seuil | Diagramme de phase : π final en fonction de 2 paramètres clés (vitesse IA × régénération de niches) — frontière nette = transition |
| F3 | Q4b : hystérésis | Aller-retour sur le paramètre de pénétration IA : la trajectoire retour ne repasse pas par la trajectoire aller → point de non-retour |
| F4 | Q5 : rôle de la compétition | π final vs nombre d'opérateurs IA (1 → N) : la compétition est-elle nécessaire ou seulement accélératrice ? |
| F5 | Q6 : stratégies riches | Ablations : collusion on/off, redistribution on/off, sortie on/off — quelles conclusions survivent |
| F6 (bonus) | Q4 : early warnings | Signatures statistiques avant le seuil (variance, autocorrélation de π) — le résultat « actionnable » |

Tout choix d'architecture ci-dessous se justifie par sa contribution à l'une de ces figures. Ce qui ne sert aucune figure ne sera pas codé en v1.

---

## 2. Le modèle (couche conceptuelle)

### 2.1 — L'objet central : le marché des gradients

L'économie est représentée par un flux d'**opportunités** (les « gradients » de H2′) plutôt que par des fonctions de production agrégées. C'est le choix de design fondamental — il rend le mécanisme D1 *représentable* au lieu de le postuler.

**Opportunité** = { valeur v, complexité k, latence de détection requise ℓ, durée de vie d }. Générées stochastiquement à taux g, dont une fraction issue de l'innovation des agents eux-mêmes (régénération schumpétérienne endogène — la réponse à Q1 vit dans ce paramètre).

**Capture** : une opportunité est capturée par le premier agent qui (a) la détecte (fonction de son coût d'information et de sa latence), (b) a la capacité de l'exploiter (capacité ≥ k). Le revenu v va au capteur. C'est une course — la transposition « deux espèces » de Grossman-Stiglitz (piste A de `research-program.md`) en est le cas dégénéré à 2 agents, ce qui donnera le point d'ancrage analytique.

### 2.2 — Les agents

Deux espèces économiques, **différenciées uniquement par leurs paramètres, jamais par des règles spéciales** (principe anti-tautologie n°1) :

- **Agents humains** : latence ℓ_h et coût d'information c_h constants, capacité plafonnée, apprentissage lent. Perçoivent aussi un revenu de travail tant que des opportunités « exigent » de l'humain (fraction de tâches non automatisables, paramètre décroissant ou endogène).
- **Agents IA-opérés** (entreprises/opérateurs) : latence et coût décroissants avec l'**investissement** — le revenu capturé peut être réinvesti en capacité. C'est LA boucle de rétroaction du modèle : capture → revenu → réinvestissement → meilleure capture. L'emballement, s'il existe, doit *émerger* de cette boucle, pas d'un terme ad hoc.
- **(v2) État(s)** : agents de politique — taxent, redistribuent, subventionnent des niches humaines. En v1, la redistribution est un simple paramètre exogène (taux de transfert), pour garder F1-F4 propres.

**Démographie économique** : entrée/sortie endogène (un agent dont le revenu < coût de participation sort du marché ; des entrants apparaissent là où il y a du profit). La sortie des humains du marché EST la variable observée — elle ne doit jamais être forcée.

### 2.3 — La boucle de demande (le garde-fou de Korinek)

Sans demande, pas de valeur : la valeur v des opportunités dépend d'un pool de demande alimenté par les revenus des agents (humains et opérateurs). Si les revenus humains s'effondrent, la demande finale se contracte (crise de réalisation) — sauf si la demande inter-IA devient autoporteuse, ce que le modèle doit permettre (paramètre : part de la demande émanant des opérateurs eux-mêmes). Ce bloc répond à Q2 et évite le reproche standard « votre modèle oublie qui achète ».

### 2.4 — Espace de stratégies (la leçon des modèles naïfs)

En v1, trois stratégies au-delà de « capturer » : **colluder** (partage de gradients entre opérateurs — réduit la concurrence, comportement par défaut documenté, cf. `background.md`), **sortir/autarcie** (un agent peut quitter le marché commun), **investir vs distribuer** (pour les opérateurs). En v2 : manipulation de la mesure (Goodhart sur π) et lobbying (influence sur le taux de redistribution). Chaque conclusion de l'article devra préciser sous quelles stratégies actives elle tient (F5).

### 2.5 — La métrique π

Définie via `research-program.md` (phase 1 du plan). Implémentation prévue : π = part du revenu total capté par des agents humains (revenu de capture + travail + transferts *comptés séparément* — π_marché sans transferts, π_total avec ; l'écart entre les deux est lui-même un résultat : « les humains ne vivent plus que de perfusion »).

### 2.6 — Rationalité des agents : trois niveaux, pour la robustesse

Le choix du mécanisme d'apprentissage des agents est le point le plus attaquable de tout ABM. Parade : implémenter la décision comme une interface avec trois implémentations interchangeables, et vérifier que les figures F1-F4 survivent aux trois :
1. **Heuristique/réplication** (dynamique de réplicateur : les stratégies rentables se propagent) — rapide, interprétable, standard en évolution ;
2. **Meilleure réponse myope** (chaque agent optimise à un pas) ;
3. **Apprentissage** (bandit/Q-learning simple) — le niveau qui permet à la collusion d'*émerger* au lieu d'être scriptée, comme dans Calvano et al.

Pas d'agents LLM en v1 : coûteux, non reproductibles, et la littérature (axe 6) note que les simulateurs LLM ne sont pas pris plus au sérieux — au contraire — pour ce type de question d'équilibre.

---

## 3. Protocole expérimental

### 3.1 — Validation avant production (l'ordre est important)

1. **V1 — Cas dégénéré analytique** : 1 humain + 1 IA, flux d'opportunités homogène → le simulateur doit reproduire la solution fermée du modèle minimal (piste A, `research-program.md`). Test automatisé, tolérance chiffrée. Tant que V1 ne passe pas, aucune expérience ne compte.
2. **V2 — Sanity économiques** : sans IA (deux populations humaines identiques), le marché doit être stationnaire et équitable ; avec IA à capacité gelée, π doit se stabiliser au-dessus de zéro. Si l'éviction se produit même sans avantage IA, le modèle est tautologique (critère K1 de `research-program.md`).
3. **V3 — Invariances** : résultats stables sous permutation des seeds (n ≥ 30 réplications, intervalles de confiance systématiques), sous doublement de la population d'agents, sous raffinement du pas de temps.

### 3.2 — Expériences de production (mappées sur les figures)

- **E1 (→F1)** : balayage de la vitesse de progrès IA (taux d'amélioration coût/latence par unité de réinvestissement). 
- **E2 (→F2)** : grille 2D vitesse IA × taux de régénération de niches humaines g_h. Détection de la frontière de phase par la discontinuité de π final et par la bimodalité des distributions.
- **E3 (→F3)** : rampe montante puis descendante du paramètre de pénétration (protocole d'hystérésis standard) ; mesurer l'aire de la boucle.
- **E4 (→F4)** : nombre d'opérateurs IA ∈ {1, 2, 5, 20}, à capacité agrégée constante — isole l'effet compétition (Q5).
- **E5 (→F5)** : matrice d'ablations de stratégies (2³ combinaisons collusion/sortie/redistribution).
- **E6 (→F6)** : sur les trajectoires d'E3, calcul des indicateurs d'alerte précoce (variance glissante, autocorrélation lag-1, skewness de π) avant le point de bascule.

Chaque expérience = un fichier de configuration versionné + une commande reproductible + un dossier de résultats horodaté. Prédictions d'E2/E3 **écrites avant** l'analyse empirique (piste C de `research-program.md`).

---

## 4. Architecture logicielle

Python 3.12+, numpy/scipy au cœur, pas de framework ABM externe (Mesa coûte plus qu'il ne rend à cette échelle ; la vectorisation numpy est le bon outil pour 10³-10⁴ agents × 10⁴ pas × 30 seeds).

```
sim/
├── core/
│   ├── opportunities.py   # génération, vieillissement, pool de demande
│   ├── agents.py          # état des populations (arrays numpy, pas d'objets par agent)
│   ├── capture.py         # le mécanisme de course (détection, allocation)
│   └── dynamics.py        # boucle principale, réinvestissement, entrée/sortie
├── strategies/
│   ├── base.py            # interface de décision (les 3 niveaux de rationalité)
│   ├── replicator.py
│   ├── best_response.py
│   └── learning.py
├── metrics/
│   └── indices.py         # π (marché/total), Gini, durée de vie des niches, early warnings
├── experiments/
│   ├── configs/           # un YAML/JSON par expérience (E1-E6, V1-V3)
│   └── runner.py          # exécution, réplication multi-seeds, parallélisation
├── analysis/
│   ├── phase.py           # détection de frontière, bimodalité, hystérésis
│   └── figures.py         # F1-F6, style publication
└── tests/
    ├── test_analytic.py   # V1 : accord avec la solution fermée
    ├── test_sanity.py     # V2 : non-tautologie
    └── test_invariance.py # V3
```

**Choix structurants :**
- **Populations vectorisées, pas d'agents-objets** : chaque espèce est un jeu d'arrays (capacité, latence, richesse, stratégie). C'est ce qui rend E2 (grille 2D × 30 seeds) calculable sur un laptop en heures, pas en jours.
- **Séparation stricte modèle / expérience / analyse** : le cœur ne connaît ni les scénarios ni les figures. Tout paramètre vient de la config ; aucun nombre magique dans le code.
- **Reproductibilité totale** : seed unique par run dérivé du hash de la config ; résultats en parquet/npz avec la config embarquée ; un `make paper` doit régénérer toutes les figures de zéro.
- **Tests = garde-fous épistémiques** : test_sanity échoue si l'éviction se produit sans avantage IA — le principe anti-tautologie est *dans la CI*, pas seulement dans les intentions.

**Hors périmètre v1 (explicitement)** : mécanismes de protection (on diagnostique d'abord — le simulateur doit juste être *extensible* : un mécanisme futur = une stratégie d'État en v2), agents LLM, calibration macro fine (on vise des régimes qualitatifs et des seuils, pas des prévisions chiffrées du PIB).

---

## 5. Risques du projet de simulation, et parades

| Risque | Parade |
|---|---|
| Le modèle encode sa conclusion (le péché du premier prototype) | V2 en CI ; revue de chaque terme de payoff avec la question « ce terme force-t-il le résultat ? » ; les humains ne diffèrent que par des paramètres |
| Le seuil (F2/F3) n'existe pas | Prévu par K2 (`research-program.md`) : l'article pivote sur « déclin graduel + conditions », toujours publiable |
| Résultats dépendants du mécanisme d'apprentissage | Les 3 niveaux de rationalité interchangeables ; ne publier que ce qui survit aux trois |
| Complexité qui explose avant d'avoir un résultat | Discipline « une figure = une raison de coder » ; v1 = F1-F4 seulement si nécessaire |
| Être doublé pendant le développement | Le modèle minimal analytique (phase 2 de `research-program.md`) est publiable seul en post court — occuper le terrain tôt |

---

## 6. Premier jalon concret

Pour démarrer (probablement notre prochaine session de travail) :
1. Rédiger la définition de π (1-2 pages, doc de travail) — phase 1 de `research-program.md`.
2. Poser le modèle minimal (piste A) sur papier et tenter la résolution du cas dégénéré.
3. Bootstrapper `sim/core` + `tests/test_analytic.py` sur ce cas — V1 comme premier test rouge/vert.

À ce stade on saura si le cœur formel tient, et tout le reste de l'architecture a été conçu pour s'y greffer sans refonte.

---

*Lecture associée : `docs/background.md` (contexte scientifique), `docs/research-program.md` (méthode de validation), `PLAN.md` (découpage en tâches).*
