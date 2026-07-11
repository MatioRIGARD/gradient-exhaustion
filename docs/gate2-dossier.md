# Dossier GATE 2 — Le mécanisme sort-il du modèle sans être forcé ?

> Préparé le 2026-07-13. La décision t'appartient (PLAN.md). Question posée par le critère K1 : *le mécanisme d'éviction émerge-t-il du modèle, ou y a-t-il été introduit par construction ?*

## Ce qui a été établi cette nuit

**Le modèle** (`paper/model-notes.md`) : l'économie est un flux d'opportunités capturées en course par deux populations — humains à technologie fixe et entrée libre, IA dont la capacité **se compose avec le revenu réinvesti**. Résultats principaux, en clair :

1. **Seuil d'exclusion à capacité finie** : la participation humaine tombe à exactement zéro quand la capacité IA atteint Λ̄ = g·v·μ_h/c_h − θ — pas asymptotiquement, à un point précis, qui dépend de paramètres interprétables (flux d'opportunités, efficacité humaine, vitesse de péremption des niches).
2. **Déclin linéaire** de la part humaine π à mesure que la capacité IA monte — graduel, sans drame… jusqu'au seuil.
3. **Le critère d'exclusion tient en une comparaison** : γ = η·(c_h/μ_h) − δ. Si convertir du revenu en capacité (η) bat la dépréciation (δ) à la marge que la concurrence humaine laisse disponible, l'exclusion arrive en **temps fini** ; sinon l'IA régresse et les humains dominent. Ni malveillance ni stratégie nulle part — compétition + composition suffisent.
4. **L'irréversibilité vient de la demande** : si une part (1−β) de la demande dépend des revenus humains, l'exclusion effondre cette demande et le seuil de ré-entrée tombe *en dessous* du seuil de sortie — piège d'hystérésis de largeur (1−β)·S. Plus l'économie a besoin des humains comme consommateurs, plus leur éviction est irréversible une fois advenue. Si β est très faible, le piège est absolu (aucune ré-entrée possible même si l'IA disparaissait).

**Les vérifications** (tout est dans le journal en fin de `model-notes.md`) :
- 18 checks numériques Monte-Carlo/ODE : **tous verts**.
- **Contre-dérivation aveugle** par un agent indépendant n'ayant vu que l'énoncé : toutes les formules retrouvées à l'identique.
- **Le simulateur reproduit le modèle** (V1, 6/6) : équilibre d'entrée libre, déclin linéaire, exclusion, temps t* — avec des agents qui n'utilisent que de l'information locale (épaisseur du marché, comptes personnels).

## La réponse à K1, honnêtement

**Le mécanisme émerge, il n'est pas décrété.** Les preuves : (a) sans l'asymétrie de composition (η = 0, ou symétrique entre espèces), le modèle donne coexistence stable ou dominance humaine — vérifié analytiquement ET en simulation ; (b) humains et IA ne diffèrent que par des paramètres ; (c) le modèle sait produire la *non*-exclusion (γ ≤ 0, saturation du réinvestissement A7′ → région de coexistence dans le futur diagramme de phase).

**Mais il faut nommer ce qui porte tout** : l'hypothèse A7 — *la capacité logicielle se compose avec le revenu réinvesti, la capacité humaine non* — est la clef de voûte. C'est un fait empirique plausible (le logiciel scale avec le capital, un cerveau ne s'achète pas), pas un théorème. Et la contre-dérivation a pointé son revers (A9) : le modèle laisse l'IA réinvestir son revenu *brut* sans discipline concurrentielle, alors que l'entrée libre lamine les rentes humaines. Si la compétition entre opérateurs IA dissipe leurs rentes comme l'entrée libre dissipe les nôtres, η effectif baisse et la coexistence s'élargit — c'est l'expérience E4, et elle peut changer la conclusion. Le papier devra présenter A7/A9 comme *la* question, pas comme un détail.

## Ma recommandation

**GATE 2 : franchir — sous deux conditions.**
1. **Relecture adversariale d'abord** (une session fraîche, une heure) : donner `model-notes.md` à un agent avec la consigne « trouve l'erreur ou l'hypothèse qui force la conclusion ». C'est la dernière case du journal de vérification.
2. **Publier tôt le modèle minimal** : un post court Alignment Forum (« A minimal model of gradual economic disempowerment: exclusion threshold, finite-time collapse, and a demand-side hysteresis trap ») dès que la relecture est passée — avec le caveat A7/A9 en pleine lumière. Ça date l'antériorité, ça sollicite exactement les bonnes critiques, et la simulation complète (phases 3-4) devient la suite annoncée plutôt qu'un pari solitaire.

## Si tu franchis, la suite (ordre recommandé)

1. Session fraîche Opus : relecture adversariale de `model-notes.md` (dernière ligne du journal).
2. Envoyer les mails T1.2 (`docs/outreach-emails.md`).
3. Opus, une tâche par session : T3.5 → T3.9 (les specs sont dans PLAN.md ; le cœur et V1 existent, c'est du travail balisé).
4. Rédaction du post AF court (l'agent peut drafter depuis model-notes ; tu valides).
5. Phase 4 (expériences E1-E6) — F2 (diagramme de phase avec la région de coexistence A7′) et F3 (hystérésis vs β) sont les deux figures qui feront le papier.
