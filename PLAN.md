# PLAN — De zéro à l'article publié

> **Mode d'emploi (pour Mathieu).** Ce plan est découpé en tâches atomiques exécutables par un agent (Opus) en une session courte chacune. Donne à l'agent UNE tâche à la fois, par son ID (« fais T2.1 »), avec ce fichier et les docs référencés en contexte. Chaque tâche a des critères d'acceptation vérifiables : ne passe à la suivante que s'ils sont remplis. Les **GATES** entre phases sont des points de décision qui t'appartiennent — un agent ne doit jamais les franchir seul. Les critères d'abandon K1-K4 sont dans `docs/research-program.md` §4 : relis-les à chaque gate.

**Objectif final** : un article (« première formalisation multi-agents du désempowerment économique, avec seuils critiques ») publié en post Alignment Forum + preprint arXiv, appuyé sur la simulation de ce repo.

**Colonne « Qui »** : 🤖 = agent seul ; 🤖+👤 = agent produit, Mathieu relit et tranche ; 👤 = Mathieu (éventuellement aidé).

---

## État d'avancement (2026-07-13, nuit de drive Fable)

- ✅ **Phase 0** complète (T0.1-T0.3, GATE 0 franchie : terrain libre).
- ✅ **T1.1** (définition de π, DEC-001 tranché) ; **T1.2** : brouillons prêts dans `docs/outreach-emails.md` → **à envoyer par Mathieu**.
- ✅ **T2.1-T2.3** : modèle formalisé et résolu (`paper/model-notes.md`) — seuil d'exclusion Λ̄, critère γ, temps t*, hystérésis ∝ (1−β). **Triple vérification** : dérivation + 18 checks numériques (`sim/analysis/analytic_check.py`) + contre-dérivation aveugle par agent indépendant (`paper/rederivation-blind.md`) — concordance totale.
- 🟡 **T2.4** : premier passage fait (audit A1-A9 dans model-notes §5) ; **reste la relecture adversariale par session fraîche** avant de considérer la phase 2 close.
- ✅ **T3.1-T3.4** : cœur du simulateur + ancre analytique V1 (6/6 tests). Leçons de conception documentées dans les docstrings (signal d'épaisseur de marché, comptabilité par agent avec patience, réponse symétrique anti-rectification).
- ✅ **T3.5, T3.6, T3.9** : V2 sanity + V3 invariances + métriques (12/12 tests verts). ✅ **T4.0** : prédictions pré-enregistrées (`paper/predictions.md`).
- ✅ **Relecture adversariale** faite (`paper/adversarial-review-model.md`) : verdict « publiable après corrections » — **les 7 corrections sont appliquées** dans model-notes rev. 2. Statut épistémique acté : §2-3 (exclusion) émergent et vérifié ; §4 (cliquet) conditionnel à A8, présenté comme tel.
- ✅ **E3 préliminaire** (`sim/analysis/notes-preliminary-e3.md`) : E3.4 INFIRMÉE pour couplage linéaire — l'hystérésis exige une demande non-linéaire/rigide ; l'exclusion, elle, tient (et arrive plus tôt). À intégrer au design d'E3 production.
- ✅ **GATE 2 : FRANCHIE le 13/07/2026** (délégué par Mathieu, conditions du dossier remplies : relecture adversariale passée, corrections appliquées). Périmètre de publication acté : §2-3 en résultat principal, §4 en résultat conditionnel avec la découverte E3-préliminaire.
- ✅ **Phase 4, première passe (13/07 soir)** : E1-E4 exécutées contre les prédictions pré-enregistrées, figures F1-F4 dans `paper/figures/`, verdicts dans `sim/analysis/notes-production-v1.md`. Résultats : frontière de phase **exactement** sur δ=10η (E2.1) ; région de coexistence confirmée sur la droite analytique (E2.2) ; invariance exacte au nombre d'opérateurs (E4.1) ; E3.6 **réfutée telle qu'énoncée** et découverte exploratoire : le piège d'irréversibilité exige une réponse de demande **tardive** (K bas — épargne/crédit), largeur 0.95±0.03 à K=0.05, monotone vers la limite (1−β)S.
- ✅ **Post AF rédigé et mis à jour** (`paper/af-post-minimal-model.md`, ~2500 mots) : relu par Fable, intègre les résultats de production. **Prêt pour relecture finale par Mathieu puis publication** (avec les figures F1-F4 aux emplacements marqués [Figure: …]).
- ✅ **Confirmation K sur seeds neufs** (E3.9-E3.11 pré-enregistrées, toutes confirmées) : le résultat « le piège exige une demande tardive » n'est plus exploratoire.
- ✅ **T3.7** : règles de décision interchangeables — replicator (ancre V1) + best_response validées (tests) ; niveau « learning » implémenté mais descopé honnêtement (inférence individuelle non informative en régime d'income lumpy — voir docstring ; suivi).
- ✅ **T3.8** : redistribution (taxe τ→transferts, DEC-002 câblé : la demande reçoit capture+transferts), dissipation de rentes entre opérateurs, drapeau collusion. π_total implémenté.
- ✅ **E5 et E4b** (prédictions 13/07c pré-enregistrées, toutes confirmées) : la redistribution ne préserve la participation qu'à taux quasi confiscatoire (τ*≈0.92 ; π_total=τ exactement après exclusion) ; la concurrence entre IA ne protège qu'à dissipation quasi totale (ρ*≈0.97) et **la collusion éteint exactement la protection**. Figures F5, F4b.
- �Ⓝ **E6 première passe négative** (pas d'early warnings détectables avec l'estimateur naïf) — documenté, à retravailler, ne pas revendiquer dans le papier.
- ⬜ Restent : densification n≥30 (cosmétique papier), E3.8, E6 retravaillé, calibration du niveau learning, balayage β×K ; puis phase 5 (papier long, LaTeX, arXiv). Le post AF est prêt et n'attend rien de tout ça.

---

## Phase 0 — Fondations (≈ 1-2 sessions agent)

| ID | Tâche | Livrable | Critères d'acceptation | Qui |
|---|---|---|---|---|
| T0.1 | **Vérifier la bibliographie.** Vérifier une par une les références de `docs/background.md` §4 et les ⚠️ : URL existe, auteurs/année/titre exacts, la thèse résumée correspond au contenu réel. Corriger `background.md`, marquer `[VÉRIFIÉ]` ou `[INTROUVABLE]`. | `background.md` corrigé + `docs/biblio-verification.md` (tableau) | Les 10 lectures prioritaires toutes vérifiées ; plus aucun ⚠️ non statué | 🤖 |
| T0.2 | **Fiches de lecture.** Pour les références 1-5 de `background.md` §4 : fiche d'une page chacune (thèse, modèle s'il y en a un, ce que notre projet ajoute, risque de recouvrement). Vérifier en particulier la liste « Gradual Disempowerment: Concrete Research Projects » (Alignment Forum) : l'un des chantiers listés est-il notre sujet ? | `docs/fiches-lecture.md` | 5 fiches ; section finale « recouvrements » explicite avec verdict (libre / à ajuster / occupé) | 🤖 |
| T0.3 | **Setup du repo.** pyproject.toml (Python 3.12, numpy, scipy, matplotlib, pytest, ruff), Makefile (`setup`, `test`, `lint`, `format`), CI locale simple, arborescence `sim/` conforme à `docs/simulation-architecture.md` §4 (fichiers vides + docstrings). | Repo qui passe `make test` (0 tests) et `make lint` | Commandes documentées dans le README ; `make setup` fonctionne sur machine vierge | 🤖 |
| **GATE 0** | **Décision : le terrain est-il libre ?** Si T0.2 révèle qu'une équipe a déjà publié un modèle formel équivalent → pivot (répliquer + étendre au lieu de créer). Sinon, continuer. | | | 👤 |

## Phase 1 — L'indice π (≈ 1 session agent + relecture)

| ID | Tâche | Livrable | Critères d'acceptation | Qui |
|---|---|---|---|---|
| T1.1 | **Draft de la définition de π** (participation économique humaine). Traiter explicitement Q2 et Q3 de `docs/research-program.md` §2 : que compte-t-on (revenu de capture, travail, transferts — séparés en π_marché / π_total), pourquoi ces choix, quelles données réelles existantes s'en approchent (labor share, etc.). Inclure 3 définitions alternatives rejetées avec raisons. | `docs/pi-definition.md` (2-3 pages) | π est calculable dans le modèle ET approximable dans des données réelles ; les cas ambigus (UBI, humain assisté par IA, actionnaire passif) sont tous tranchés | 🤖+👤 |
| T1.2 | **Relecture externe du draft** : envoyer `pi-definition.md` (traduit en anglais par l'agent) à 1-2 personnes de `background.md` §3 avec un message court. Objectif secondaire : premier contact avec la communauté. | Email/DM envoyé | Message parti (la réponse n'est pas bloquante pour la suite) | 👤 |

## Phase 2 — Modèle minimal analytique (≈ 1-2 semaines — incompressible sous ~1 semaine : les passes de vérification doivent être espacées et faites par des sessions fraîches) — **le cœur du projet**

| ID | Tâche | Livrable | Critères d'acceptation | Qui |
|---|---|---|---|---|
| T2.1 | **Formaliser le marché des gradients.** Poser mathématiquement : processus d'apparition des opportunités (taux g, valeurs v, difficultés k, durées de vie d), règle de capture (course détection/latence), deux populations (humains : coûts/latences fixes ; IA : décroissants avec le réinvestissement). Écrire les équations du revenu de chaque population. Base : `docs/research-program.md` §3 piste A et `docs/simulation-architecture.md` §2. | `paper/model-notes.md` (formalisme complet) | Toutes les variables définies, toutes les hypothèses numérotées (A1, A2…) et justifiées en une ligne chacune | 🤖+👤 |
| T2.2 | **Résoudre le cas dégénéré** (2 agents, opportunités homogènes, capacité IA gelée) : revenu stationnaire de chaque population en fonction des paramètres. Solution fermée ou quasi-fermée. | Section « solution » de `model-notes.md` + script `sim/analysis/analytic_check.py` qui trace la solution | La solution est vérifiée numériquement par le script (accord < 1 %) | 🤖 |
| T2.3 | **Dynamique avec réinvestissement IA** : capacité IA endogène (revenu → réinvestissement → coût/latence ↓). Chercher : condition pour revenu humain → 0, existence d'un seuil, existence d'hystérésis dans ce cadre simple. | Section « dynamique » de `model-notes.md` | Un théorème (même modeste) OU un contre-exemple documenté ; conditions exprimées en paramètres interprétables | 🤖+👤 |
| T2.4 | **Test anti-tautologie du modèle.** Rédiger la liste des hypothèses A1-An avec, pour chacune : « si on la retire, la conclusion tient-elle ? ». Identifier celles qui portent la conclusion. | Section « robustesse » de `model-notes.md` | Aucune hypothèse du type « les humains ne peuvent pas X » sans justification empirique ; la conclusion ne repose pas sur une seule hypothèse fragile | 🤖+👤 |
| **GATE 2** | **Décision K1 (`research-program.md` §4) : le mécanisme sort-il du modèle sans être forcé ?** Si non → retravailler le diagnostic avant toute simulation. Si oui → optionnel mais recommandé : publier dès maintenant un post court Alignment Forum avec le modèle minimal (occupe le terrain, récolte du feedback, date l'antériorité). | | | 👤 |

## Phase 3 — Simulation v1 (≈ 1-2 semaines en sessions agent)

Suivre `docs/simulation-architecture.md` (architecture, principes anti-tautologie, populations vectorisées numpy). Ordre strict : les tests de validation V1-V3 **avant** toute expérience.

| ID | Tâche | Livrable | Critères d'acceptation | Qui |
|---|---|---|---|---|
| T3.1 | `sim/core/opportunities.py` + tests unitaires (génération, vieillissement, pool de demande §2.3) | Module + tests verts | Distributions paramétrables ; demande endogène branchable/débranchable par config | 🤖 |
| T3.2 | `sim/core/agents.py` + `sim/core/capture.py` + tests (populations en arrays ; mécanisme de course §2.1-2.2) | Modules + tests verts | Humains et IA ne diffèrent QUE par des paramètres (revue de code explicite sur ce point) | 🤖 |
| T3.3 | `sim/core/dynamics.py` (boucle, réinvestissement, entrée/sortie endogène) + config YAML | Boucle complète qui tourne | Run reproductible par seed ; aucun nombre magique hors config | 🤖 |
| T3.4 | **Test V1 (accord analytique)** : `tests/test_analytic.py` — le simulateur reproduit la solution de T2.2 sur le cas dégénéré | Test vert en CI | Écart < tolérance chiffrée et justifiée | 🤖 |
| T3.5 | **Tests V2 (anti-tautologie)** : sans IA → marché stationnaire équitable ; IA à capacité gelée → π se stabilise > 0 | `tests/test_sanity.py` vert | Si V2 échoue, INTERDICTION de continuer : corriger le cœur | 🤖 |
| T3.6 | **Tests V3 (invariances)** : stabilité sous seeds (n≥30), taille de population ×2, pas de temps ÷2 | `tests/test_invariance.py` vert | Intervalles de confiance systématiques dans les sorties | 🤖 |
| T3.7 | `sim/strategies/` : les 3 niveaux de rationalité (réplicateur, meilleure réponse, apprentissage) derrière une interface commune (§2.6) | Modules + tests | Les 3 niveaux passent V1-V3 ; interchangeables par config | 🤖 |
| T3.8 | Stratégies riches : collusion, sortie/autarcie, redistribution paramétrique (§2.4) | Modules + tests | Chaque stratégie activable indépendamment par config (pour les ablations E5) | 🤖 |
| T3.9 | `sim/metrics/indices.py` : π_marché, π_total (selon `docs/pi-definition.md`), Gini, durée de vie des niches, indicateurs d'alerte précoce (variance glissante, autocorrélation lag-1) | Module + tests | π implémenté exactement comme défini en T1.1 (traçabilité doc ↔ code) | 🤖 |
| **GATE 3** | Revue complète : V1-V3 verts sur les 3 niveaux de rationalité ; relecture du cœur par un second agent en mode adversarial (« trouve le terme qui force la conclusion ») | | | 👤 (orchestration) |

## Phase 4 — Expériences et figures (≈ 1 semaine : runs en heures, analyse en sessions)

Protocole détaillé : `docs/simulation-architecture.md` §3.2. Une tâche = une expérience = une figure.

| ID | Tâche | Livrable | Critères d'acceptation | Qui |
|---|---|---|---|---|
| T4.0 | **Pré-enregistrement** : avant de lancer E2/E3, écrire les prédictions du modèle (fichier daté, commité) | `paper/predictions.md` | Commité AVANT les runs de production (l'historique git fait foi) | 🤖+👤 |
| T4.1 | E1 → figure F1 (dynamique de π vs vitesse du progrès IA) | `experiments/configs/e1.yaml` + figure + note d'analyse | 30 seeds, IC affichés, ablation des 3 rationalités en annexe | 🤖 |
| T4.2 | E2 → F2 (diagramme de phase 2D : vitesse IA × régénération de niches) | idem | Frontière détectée par méthode documentée (bimodalité), pas à l'œil | 🤖 |
| T4.3 | E3 → F3 (protocole d'hystérésis aller-retour) | idem | Aire de la boucle quantifiée + significativité vs bruit | 🤖 |
| T4.4 | E4 → F4 (1 vs N opérateurs IA à capacité agrégée constante — Q5) | idem | Réponse nette à « la compétition est-elle nécessaire ? » | 🤖 |
| T4.5 | E5 → F5 (matrice d'ablations collusion/sortie/redistribution) | idem | Tableau « quelle conclusion survit à quoi » | 🤖 |
| T4.6 | E6 → F6 (early warnings sur les trajectoires d'E3) | idem | Indicateurs calculés AVANT le point de bascule uniquement | 🤖 |
| **GATE 4** | **Décision K2 : y a-t-il un seuil ?** Oui → papier « transition de phase ». Non → repositionner sur « déclin graduel : conditions et paramètres » (toujours publiable). Vérifier K3/K4 à la lumière des données empiriques disponibles. | | | 👤 |

## Phase 5 — Article et publication (≈ 1-2 semaines + latences extérieures incompressibles : réponses des contacts, endorsement arXiv, commentaires AF)

| ID | Tâche | Livrable | Critères d'acceptation | Qui |
|---|---|---|---|---|
| T5.1 | Compléter `paper/paper.md` (squelette déjà en place) : intro, related work (à partir des fiches T0.2), modèle (T2), simulation (T3), résultats (F1-F6), limites, prédictions | `paper/paper.md` complet (anglais) | Chaque claim adossé à une figure ou une référence vérifiée ; section limites écrite « contre nous » | 🤖+👤 |
| T5.2 | **Relecture adversariale** par agent : jouer le referee hostile (économiste sceptique + modélisateur pointilleux), lister les objections, corriger | Rapport de review + corrections | Les 5 objections les plus fortes ont une réponse dans le texte | 🤖 |
| T5.3 | Version post Alignment Forum (plus courte, moins formelle, avec liens repo) | `paper/af-post.md` | Autonome, lisible sans le papier | 🤖+👤 |
| T5.4 | Conversion LaTeX (pandoc + template arXiv standard) + `make paper` qui régénère figures et PDF de zéro | `paper/latex/` + PDF | Compile sans erreur ; figures reproduites from scratch | 🤖 |
| T5.5 | **Publication** : (1) rendre le repo GitHub public (licence MIT déjà en place) ; (2) poster sur Alignment Forum ; (3) soumettre le preprint arXiv (cs.CY ou cs.MA ; si endorsement requis, le demander à un des contacts de la phase 1 — c'est une demande banale) ; (4) envoyer aux contacts de `background.md` §3 | Post + preprint en ligne | L'horodatage public existe = antériorité établie. C'est ça, la « protection » de la propriété intellectuelle : personne ne peut plus publier l'idée sans te citer | 👤 (guidé par agent) |

---

## Règles permanentes pour les agents exécutants

1. **Une tâche = une session.** Ne pas déborder sur la tâche suivante ; terminer par un résumé de ce qui est fait/resté.
2. **Les critères d'acceptation sont contractuels.** Une tâche dont les critères ne sont pas remplis est déclarée « bloquée », pas « faite ».
3. **Anti-tautologie partout** : ne jamais introduire de terme, règle ou paramètre qui traite les humains différemment autrement que par des valeurs de paramètres. Tout ce qui force la conclusion est un bug, même si « ça donne le bon résultat ».
4. **Jamais conclure au-delà des ablations.** Toute phrase de résultat précise les conditions sous lesquelles elle tient.
5. **Pas de mention de cryptomonnaie/token/blockchain** dans ce repo — le projet est 100 % scientifique.
6. **Français avec Mathieu, anglais dans `paper/`** et dans le code (identifiants, docstrings).
7. **Reproductibilité** : tout résultat cité doit être régénérable par une commande unique documentée.
