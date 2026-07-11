# Vérification bibliographique — T0.1

> Vérification une par une des références de `background.md` §4 (10 lectures prioritaires) et de tous les marqueurs ⚠️ du document. Date : 2026-07-12. Méthode : `WebFetch`/`WebSearch` sur URL et métadonnées, contrôle de la thèse résumée contre l'abstract/contenu réel. Verdict `[VÉRIFIÉ]` = existe + métadonnées exactes (ou corrigées) + thèse fidèle ; `[INTROUVABLE]` = introuvable / faux non réconciliable.
>
> **Bilan : 10/10 lectures vérifiées, 3/3 ⚠️ statués (tous vérifiés), 0 introuvable.** Aucune référence ne remet en cause l'argument « terrain libre » de GATE 0 (voir §fin).

## 1. Les 10 lectures prioritaires (`background.md` §4)

| # | Référence (telle que citée) | URL / état | Auteurs · Année · Titre — exact ? | Thèse fidèle ? | Verdict | Correction appliquée |
|---|---|---|---|---|---|---|
| 1 | Kulveit et al., *Gradual Disempowerment* (2025), arxiv 2501.16946 | arXiv:2501.16946 OK ; version ICML : PMLR 267:81678-81688 OK | Auteurs exacts (Kulveit, Douglas, Ammann, Turan, Krueger, Duvenaud). Titre exact pour la version arXiv. **La version ICML 2025 porte un titre différent** : « Position: Humanity Faces Existential Risk from Gradual Disempowerment » | Oui (érosion incrémentale de l'influence humaine sur économie/État/culture) | **[VÉRIFIÉ]** | §2.1 : ajout du titre exact de la version ICML/PMLR |
| 2 | Drago & Laine, *The Intelligence Curse* (2025), intelligence-curse.ai | Site OK | Luke Drago & Rudolf Laine, 2025, série d'essais. Sous-titre « How AGI Makes Us All Obsolete » présent dans les notes brutes mais **non affiché sur le site** (série d'essais, cadre Avert/Diffuse/Democratize) | Oui (analogie État rentier / resource curse confirmée mot pour mot) | **[VÉRIFIÉ]** | Aucune (ne pas citer le sous-titre non confirmé) |
| 3 | Critch, *What Multipolar Failure Looks Like (RAAPs)* (2021), Alignment Forum | AF OK (déc. 2021) | Andrew Critch, 2021, titre exact « What Multipolar Failure Looks Like, and Robust Agent-Agnostic Processes (RAAPs) » | Oui (processus agent-agnostiques robustes, échec multipolaire sans agent unique responsable) | **[VÉRIFIÉ]** | Aucune |
| 4 | Christiano, *What Failure Looks Like* (2019), Alignment Forum | AF OK (17 mars 2019) | Paul Christiano, 2019, titre exact | Oui (Part I « going out with a whimper » = déclin par proxies mesurables ; Part II « with a bang ») | **[VÉRIFIÉ]** | Aucune |
| 5 | Hammond et al., *Multi-Agent Risks from Advanced AI* (2025), arxiv 2502.14143 | arXiv:2502.14143 OK | 1er auteur Lewis Hammond, 2025, titre exact. **51 auteurs, pas ~47** | Oui (3 modes d'échec : miscoordination, conflit, collusion ; 7 facteurs de risque) | **[VÉRIFIÉ]** | §2.2 : « ~47 auteurs » → « ~50 auteurs » |
| 6 | Grossman & Stiglitz, *On the Impossibility of Informationally Efficient Markets* (1980) | AER OK | Grossman & Stiglitz, 1980, *American Economic Review* 70(3):393-408 | Oui (l'efficience informationnelle parfaite s'auto-détruit : plus de rente info → plus d'incitation à s'informer) | **[VÉRIFIÉ]** | Aucune (réf de canon) |
| 7 | Korinek (NBER 2024-2025), scénarios de transition AGI, korinek.com | NBER + korinek.com OK | Korinek & Suh, « Scenarios for the Transition to AGI », NBER WP 32255 (2024) ; aussi « Economic Policy Challenges for the Age of AI », NBER WP 32980 (2024) | Oui (si automatisation complète + complexité des tâches humaines bornée → effondrement des salaires) | **[VÉRIFIÉ]** | Aucune (« 2024-2025 » couvre bien les WP + révisions) |
| 8 | Shalizi, *The Platform Socialist Calculation Problem* (2022) ; Brynjolfsson & Hitzig, *AI's Use of Knowledge in Society* (2025) ⚠️ | Shalizi : blog Conflated Automatons OK (3 juil. 2022). B&H : NBER OK (sept. 2025) | Shalizi 2022, titre exact. Brynjolfsson & Hitzig (Erik B. & Zoë Hitzig), 2025, chapitre du volume NBER *The Economics of Transformative AI* (Univ. Chicago Press) | Oui (réévaluation de Hayek / problème du calcul face à l'IA transformative) | **[VÉRIFIÉ]** | ⚠️ levé (voir §2) |
| 9 | De Loecker & Eeckhout, *Global Market Power* | NBER WP w24768 OK (2018, rév. 2021) | De Loecker & Eeckhout, titre exact | Partiellement : hausse des markups (moy. mondiale 1,1→1,6 entre 1980 et 2016) = leur résultat. Le cadrage « firmes superstars » est plutôt Autor et al. ; la concentration est discutée mais « superstar » n'est pas leur terme | **[VÉRIFIÉ]** | §2.3 : « concentrée sur les firmes superstars (De Loecker & Eeckhout) » → attribuer la hausse des markups à De Loecker & Eeckhout sans leur imputer le terme « superstar » |
| 10 | Armstrong, Bostrom & Shulman, *Racing to the Precipice* (2016) | Springer OK | Armstrong, Bostrom & Shulman, « Racing to the precipice: a model of artificial intelligence development », *AI & Society* 31:201-206, 2016 | Oui (course au développement IA ; sacrifice de la sécurité ; plus d'infos entre équipes = plus de risque) | **[VÉRIFIÉ]** | Aucune |

## 2. Marqueurs ⚠️ statués

| Emplacement | Claim de background.md | Vérification | Verdict | Correction appliquée |
|---|---|---|---|---|
| §2.2 | « marché allemand de l'essence, Assad et al. ⚠️ chiffres » | Assad, Clark, Ershov & Xu, « Algorithmic Pricing and Competition: Empirical Evidence from the German Retail Gasoline Market », *Journal of Political Economy* 132(3):723-771 (2024) ; CESifo WP 2020. Résultat : l'adoption du pricing algorithmique **augmente les marges, mais seulement pour les stations non-monopolistiques**. background ne cite aucun chiffre précis (rien de faux à corriger). Nuance : la « convergence spontanée vers la collusion sans communication » est surtout le résultat **expérimental** de Calvano et al. ; Assad et al. est la preuve **empirique de terrain** (marges ↑) | **[VÉRIFIÉ]** | §2.2 : ⚠️ retiré ; reformulation pour distinguer Calvano (expérimental) d'Assad (empirique, hausse des marges) |
| §2.3 | « compression des spreads et fenêtres d'arbitrage sous le trading algorithmique ⚠️ » | Phénomène documenté (synthèse multi-sources, pas une citation unique) : les fenêtres d'arbitrage ont fortement décliné (≈80-90 % disparaissent en <1 s dès 2010, marché FX/EBS) ; les spreads effectifs se sont resserrés avec le HFT (Hasbrouck & Saar 2013). background ne cite aucun chiffre précis | **[VÉRIFIÉ]** | §2.3 : ⚠️ retiré (claim qualitatif soutenu ; ancres possibles pour le papier : Hasbrouck & Saar 2013 ; littérature sur le déclin des fenêtres d'arbitrage FX) |
| §4.8 | Brynjolfsson & Hitzig ⚠️ | Voir ligne 8 ci-dessus : chapitre NBER, sept. 2025, réel | **[VÉRIFIÉ]** | §4 item 8 : ⚠️ → [VÉRIFIÉ] |

## 3. Vérifications secondaires (bonus, hors périmètre contractuel)

| Réf inline | Vérification | Verdict |
|---|---|---|
| §2.2 — stéganographie, arXiv:2402.07510 | « Secret Collusion among AI Agents: Multi-Agent Deception via Steganography », Motwani, Baranchuk, Strohmeier, Bolina, Torr, Hammond, Schroeder de Witt, 2024 | **[VÉRIFIÉ]** |
| §2.4 — MAIM, Hendrycks, Schmidt & Wang (2025) | « Superintelligence Strategy », arXiv:2503.05628, 2025. MAIM = *Mutual Assured AI Malfunction*. **3ᵉ auteur = Alexandr Wang** (préciser le prénom en citation) | **[VÉRIFIÉ]** |

## 4. Corrections portées à `background.md`

1. §2.1 — ajout du titre exact de la version ICML/PMLR de Gradual Disempowerment (le titre cité est celui de la version arXiv).
2. §2.2 — nombre d'auteurs de Hammond et al. : « ~47 » → « ~50 » (réel : 51).
3. §2.2 — ⚠️ Assad retiré + distinction Calvano (expérimental) / Assad (empirique).
4. §2.3 — ⚠️ arbitrage/spreads retiré (claim qualitatif vérifié).
5. §2.3 — markups : ne plus imputer le terme « firmes superstars » à De Loecker & Eeckhout.
6. §4 — tag `[VÉRIFIÉ]` sur les 10 lectures ; ⚠️ de l'item 8 remplacé par `[VÉRIFIÉ]`.

## 5. Références restées `[INTROUVABLE]`

Aucune.

## 6. Impact sur GATE 0 (« le terrain est-il libre ? »)

Rien dans cette vérification ne contredit le diagnostic central de `background.md` §2.1 : les travaux fondateurs (Gradual Disempowerment, Intelligence Curse, RAAPs, What Failure Looks Like) existent bien et sont **qualitatifs** ; aucun ne propose de modèle formel multi-agents ni de simulation. La vérification de l'antériorité formelle (recherche active d'un modèle équivalent déjà publié) relève de **T0.2** (fiches de lecture + liste « Concrete Research Projects » de Kulveit et al.) et non de T0.1. GATE 0 reste ouverte, décision de Mathieu.
