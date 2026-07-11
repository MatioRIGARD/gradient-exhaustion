# Contexte scientifique du projet

> Synthèse condensée de la phase de recherche préparatoire (juillet 2026). Notes brutes et bibliographies complètes (~100 URLs annotées) dans `research/raw/`. Les références des 10 lectures prioritaires (§4) et les références « à revérifier » d'origine ont été vérifiées une par une (T0.1, 2026-07-12) : voir `docs/biblio-verification.md`. Tag `[VÉRIFIÉ]` = existence + métadonnées + thèse confirmées.

---

## 1. Le sujet

**Question de recherche : la généralisation d'optimiseurs économiques surhumains (IA) évince-t-elle structurellement les humains de la boucle économique, et cette éviction présente-t-elle des seuils critiques et de l'irréversibilité ?**

Le diagnostic étudié tient en deux propositions (détaillées dans `research-program.md`) :
- **D1 (mécanisme micro, « exhaustion asymétrique des gradients »)** : toute opportunité de profit exploitable par un humain (niche, arbitrage, asymétrie d'information, idée nouvelle) est détectée et capturée par une IA avant qu'un humain puisse la capturer, ou à un coût qui rend l'investissement humain non rentable. Le revenu *humain* de ces gradients tend vers zéro même si le profit total du système reste positif.
- **D2 (équilibre système)** : ce processus est un équilibre robuste — aucun acteur n'a intérêt à le freiner unilatéralement — pouvant présenter transition de phase et hystérésis.

## 2. État de l'art en cinq points

**2.1 — Le diagnostic qualitatif existe déjà ; la formalisation n'existe pas.** « Gradual Disempowerment » (Kulveit, Douglas, Ammann, Turan, Krueger, Duvenaud — arXiv:2501.16946 ; version ICML 2025 publiée sous le titre « Position: Humanity Faces Existential Risk from Gradual Disempowerment », PMLR 267:81678-81688) argumente que l'IA incrémentale érode l'influence humaine sur l'économie, l'État et la culture *parce que ces systèmes cessent de dépendre de la participation humaine*. « The Intelligence Curse » (Drago & Laine, 2025) formule l'analogie avec les États rentiers : un acteur dont la richesse vient de « l'intelligence sur robinet » perd tout intérêt à investir dans les humains. Critch (RAAPs, 2021) et Christiano (« What Failure Looks Like », 2019) avaient posé les mécanismes compétitifs et le déclin par proxies. **Aucun de ces travaux ne propose de modèle formel ni de simulation** ; c'est le trou que ce projet vise : *première formalisation multi-agents du désempowerment économique, avec caractérisation des seuils*.

**2.2 — Les équilibres multi-agents tragiques sont établis, la collusion est le défaut.** Le rapport CAIF « Multi-Agent Risks from Advanced AI » (Hammond et al., arXiv:2502.14143, 2025, ~50 auteurs) documente que l'alignement individuel ne garantit pas l'équilibre collectif (pressions de sélection, problèmes d'engagement). Empiriquement : des algorithmes de pricing convergent spontanément vers la collusion sans communication en environnement expérimental (Calvano et al. 2020), et sur un marché réel l'adoption du pricing algorithmique augmente les marges (marché allemand de l'essence, Assad, Clark, Ershov & Xu, *JPE* 2024 [VÉRIFIÉ]) ; résultats répliqués avec des agents LLM ; la coordination peut être dissimulée par stéganographie (arXiv:2402.07510). Conséquence de design : **toute simulation crédible doit inclure la collusion dans l'espace des stratégies.**

**2.3 — L'hypothèse « mort thermique économique » est fragmentée dans six traditions, unifiée nulle part.** Composantes documentées : théorème du profit nul en concurrence parfaite ; paradoxe de Grossman-Stiglitz (1980 — l'efficience informationnelle parfaite s'auto-détruit ; **jamais transposé formellement à l'IA surhumaine**) ; baisse tendancielle du taux de profit (Marx) et son cas limite « automatisation totale = fin de la valorisation » (littérature 2023-2026) ; « crise de réalisation » post-AGI (Korinek : salaires → 0 ⇒ demande → 0) ; stagnation séculaire ; éconophysique (Georgescu-Roegen, Yakovenko — jamais reliés à l'IA). Empirie en faveur de la version *asymétrique* (les gradients ne disparaissent pas, ils sortent de portée humaine) : compression des spreads et raccourcissement des fenêtres d'arbitrage sous le trading algorithmique [VÉRIFIÉ] (phénomène documenté ; ancres : Hasbrouck & Saar 2013 pour les spreads, littérature FX pour la disparition des fenêtres d'arbitrage) ; hausse séculaire des markups (moyenne mondiale ~1,1 → ~1,6 entre 1980 et 2016, De Loecker & Eeckhout), concentrée sur un petit nombre de grandes firmes. La question de la **transition de phase** par sur-optimisation : zéro littérature identifiée.

**2.4 — La version « attrition des populations par des ASIs nationales » n'est pas défendable ; la version « marginalisation » l'est.** L'analyse par prémisses (voir `research/raw/5`) crédite ~10-20 % au scénario d'attrition programmée (aucun précédent d'un État ciblant la baisse de sa population ; alternatives stables type MAIM — Hendrycks, Schmidt & Wang 2025) mais ~40-50 % au scénario « désinvestissement persistant type État rentier ». Conséquence de design : **la variable pertinente n'est pas la population mais la part de la boucle économique passant par des humains (indice π)**. Corollaire épistémique : le narratif de « course » est en partie autoréalisateur (Marcus et al.) — modéliser l'intensité compétitive comme paramètre, jamais comme fatalité.

**2.5 — Les solutions connues butent toutes sur le même mur (hors périmètre v1, mais utile au cadrage).** Windfall Clause, taxation IA, fonds souverains, data dignity : des politiques macro de redistribution qui présupposent un pouvoir d'enforcement que l'IA érode (critiques « techno-féodalisme », capture réglementaire — voir bibliographie de l'ancienne phase exploratoire). Presque rien n'attaque le mécanisme micro de D1. Le projet reste **diagnostic d'abord** ; le simulateur doit seulement être extensible aux interventions (stratégie d'État en v2).

## 3. Communauté et publication

- **Personnes** : Jan Kulveit (ACS Prague), David Duvenaud (Toronto), Rudolf Laine & Luke Drago (Workshop Labs — mission : « preventing human disempowerment from AI »), Anton Korinek (UVA — rigueur économique), Tom Davidson, Phil Trammell (Forethought/GPI) ; contrepoint sceptique : Daron Acemoglu.
- **Séquence de publication recommandée** : post Alignment Forum (feedback direct de la communauté ci-dessus) → preprint arXiv cs.CY ou cs.MA (horodatage public = antériorité) → conférence multi-agents (AAMAS) si les résultats tiennent. Note pratique : la première soumission arXiv d'un indépendant peut nécessiter un *endorsement* — le post Alignment Forum n'a aucune barrière et suffit à dater l'idée.
- **Fenêtre** : le déploiement de l'économie agentique (2025-2027) fournit les premières données réelles de compétition entre agents économiques IA — un modèle publié tôt peut énoncer des prédictions testables dessus. Kulveit et al. maintiennent une liste publique de « concrete research projects » : à vérifier en phase 0 pour ne pas dupliquer un chantier en cours.

## 4. Les dix lectures prioritaires

1. Kulveit et al., *Gradual Disempowerment* (2025) — arxiv.org/abs/2501.16946 — **[VÉRIFIÉ]**
2. Drago & Laine, *The Intelligence Curse* (2025) — intelligence-curse.ai — **[VÉRIFIÉ]**
3. Critch, *What Multipolar Failure Looks Like (RAAPs)* (2021) — Alignment Forum — **[VÉRIFIÉ]**
4. Christiano, *What Failure Looks Like* (2019) — Alignment Forum — **[VÉRIFIÉ]**
5. Hammond et al., *Multi-Agent Risks from Advanced AI* (2025) — arxiv.org/abs/2502.14143 — **[VÉRIFIÉ]**
6. Grossman & Stiglitz, *On the Impossibility of Informationally Efficient Markets* (1980) — *AER* 70(3):393-408 — **[VÉRIFIÉ]**
7. Korinek & Suh, *Scenarios for the Transition to AGI* (NBER WP 32255, 2024) — korinek.com — **[VÉRIFIÉ]**
8. Shalizi, *The Platform Socialist Calculation Problem* (2022) ; Brynjolfsson & Hitzig, *AI's Use of Knowledge in Society* (chapitre NBER, 2025) — **[VÉRIFIÉ]**
9. De Loecker & Eeckhout, *Global Market Power* (NBER WP 24768) — **[VÉRIFIÉ]**
10. Armstrong, Bostrom & Shulman, *Racing to the Precipice: a model of artificial intelligence development* (*AI & Society* 31:201-206, 2016) — **[VÉRIFIÉ]**
