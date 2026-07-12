# Note d'analyse — Première passe de production E1-E4 (2026-07-13)

> Script : `sim/experiments/production_v1.py`. Données : `results/e*.npz`. Figures : `paper/figures/f*.png`. Verdicts rendus contre `paper/predictions.md` (pré-enregistré). **Statut : première passe — seeds réduits (3-10) ; la densification (n≥30) et la confirmation des découvertes exploratoires sur seeds frais sont des tâches de suivi (voir §Suites).**

## E1 — Dynamique de π vs vitesse IA (F1)

- **E1.1 CONFIRMÉE** : γ<0 (η=0.003) → π se maintient ≈0.95 sur tout l'horizon.
- **E1.2 CONFIRMÉE** : γ>0 → déclin « lent puis brutal », exclusion complète peu après t*, avec le lag d'ajustement attendu. Ordre des effondrements strictement monotone en η.
- **E1.3 qualitativement confirmée** (doublement de η ⇒ effondrement ~2× plus tôt) ; vérification chiffrée à faire au run densifié.
- Caveat : transitoire de construction initial (π monte de ~0.3 à ~0.9 pendant les 3 premières unités — démarrage à participation nulle) ; le run final devrait partir de l'équilibre.

## E2 — Diagramme de phase η×δ (F2)

- **E2.1 CONFIRMÉE, spectaculairement** : frontière nette collée à la ligne prédite δ=10η sur toute la grille ; bande de transition ≤ 1 cellule ; pas de bande intermédiaire stable.
- **E2.3 non évaluée** (3 seeds moyennés — la bimodalité near-boundary demande le run densifié).

## E2b — Coexistence sous saturation de capacité (F2b)

- **E2.2 CONFIRMÉE** : pour Λmax < Λ̄, π_final suit la droite analytique 1−Λmax/Λ̄ point par point ; π≈0 au-delà. **La région de coexistence existe** : l'exclusion n'est pas universelle dans le modèle — résultat d'honnêteté à mettre en avant.

## E3 — Hystérésis et forme de la réponse de demande (F3)

- **E3.5 CONFIRMÉE** : réponse linéaire → pas de boucle (gap +0.12±0.35, compatible 0) ; exclusion vers Λ_a ≈ βS−θ (≈1), conforme.
- **E3.6 RÉFUTÉE TELLE QU'ÉNONCÉE** : la *raideur* n seule ne crée pas la boucle (n=8, K=0.5 : gap −0.17±0.12 ; l'aire mesurée au premier passage était un artefact de lag de rampe, cf. correctif du script). Le paramètre décisif est la *position* K de la réponse — une demande qui ne réagit que tard (K→0 : elle « tient » tant que le revenu humain n'a pas presque disparu — épargne, crédit, rigidités) crée une boucle nette.
- **CONFIRMATION (2026-07-13b, protocole pré-enregistré E3.9-E3.11)** : seeds neufs 100-109, rampes 2× plus lentes (t_leg=600) → gap(linéaire) = −0.14±0.08 (E3.10 ✓ compatible zéro), gap(K=0.05) = +0.64±0.13 (E3.9 ✓), différence 0.78 avec IC disjoints (E3.11 ✓). **Les trois prédictions confirmées ; le résultat n'est plus exploratoire.** (Le gap plus faible qu'au premier passage — 0.64 vs 0.95 — reflète la réduction du lag de rampe : 0.64 est plus proche de la vraie largeur de bistabilité.) Données : `results/e3_confirmation.npz`.
- **E3.7 partiellement soutenue** (convergence vers la limite deux-états visible dans la direction K→0) ; **E3.8 non testée**.
- **Lecture économique** (rejoint le prior n°2 de Mathieu, `docs/decisions.md`) : *si la consommation suit le revenu en douceur, l'effondrement est précoce mais réversible ; si elle tient (épargne/crédit/transferts) puis cède, il est tardif mais piégeant.* Implication à traiter avec précaution dans le papier : une politique de soutien de la demande retarde l'exclusion ET élargit la fenêtre du piège si elle cède.

## E4 — Nombre d'opérateurs (F4)

- **E4.1 CONFIRMÉE exactement** : t* identique pour N ∈ {1,2,5,20} à capacité agrégée constante (trajectoires appariées par seed superposées). Le résultat nul est propre : sans dissipation de rentes, la concurrence entre opérateurs ne change rien. **E4.2 (conditionnelle, dissipation) en attente de T3.8.**

## E5 — Redistribution comme frein endogène (F5) — *ajout 13/07c*

- **E5.1 CONFIRMÉE** : exclusion à τ∈{0, 0.5, 0.8}, prévention à τ=0.95 (π_market stationnaire = 1.0) ; seuil analytique τ*≈0.917 encadré.
- **E5.2 CONFIRMÉE** : t*(0.5)=8.3 (préd. 9.2), t*(0.8)=31.4 (préd. 33) — écarts ≤10 %.
- **E5.3 CONFIRMÉE au centième** : π_total post-exclusion = τ exactement (0.50, 0.80). Le régime « maintenus en vie, hors de la boucle » est mesuré : Δ = τ.
- Lecture : à ces paramètres, **la redistribution ne préserve la participation qu'à taux quasi confiscatoire** (>92 %) — le frein doit battre une croissance exponentielle. En dessous, elle achète du délai et de la survie (π_total), pas de la participation.

## E4b — Dissipation de rentes et collusion (F4b) — *ajout 13/07c*

- **E4.4 CONFIRMÉE** : exclusion à ρ_d∈{0, 0.5, 0.9} (t*=3.2, 7.9, 58.7 — divergence près de ρ*≈0.965), prévention à ρ_d=1.0 (6/6 seeds).
- **E4.5 CONFIRMÉE exactement** : collusion à ρ_d=1.0 → t*=3.2, identique au cas sans dissipation. **La collusion éteint intégralement la protection concurrentielle.**

## E6 — Signaux d'alerte précoce (F6) — *ajout 13/07c*

- **Première passe NÉGATIVE / non concluante** : l'autocorrélation lag-1 de Λ_h reste plate à l'approche de la sortie dans les deux régimes (piège : 0.64→0.65). E6.2 infirmée en l'état ; caveat : l'estimateur naïf sur série brute (jitter d'entrée/sortie, forçage rapide) peut masquer le ralentissement critique — la littérature EWS exige détrendage et forçage lent. À retravailler (suite n°4) avant toute conclusion ; en l'état, **ne pas revendiquer d'early warnings dans le papier**.

## ADDENDUM 2026-07-13 — audit de session fraîche (voir `docs/audit-fable-clean-2026-07-13.md`)

1. **La confirmation E3.9-E3.11 a maintenant un chemin de code commité** : `uv run python
   sim/experiments/production_v1.py --exp e3conf` (seeds 100-109, t_leg=600 — le run original
   avait été exécuté avec du code non commité, finding M2 de l'audit). Re-run du 13/07 :
   gap(K=0.05) = **+0.64 ± 0.06 (SE)**, IC 95 % [+0.51, +0.76] ; gap(linéaire) = **−0.14 ± 0.04**,
   IC 95 % [−0.22, −0.07] ; différence 0.78, IC disjoints — **E3.9, E3.10, E3.11 re-PASS**,
   moyennes identiques au run original (dont les ±0.13/±0.08 se lisent comme des IC 95 %).
   Données : `results/e3_confirmation.npz`.
2. **Requalification d'E3.6** (finding M3) : la carte de points fixes *statique* du couplage
   de demande (`sim/analysis/static_demand_map.py`, indépendante de l'ABM) montre une bande
   bistable aussi pour la réponse raide à K médian (n=8, K=0.5 : Λ_a ∈ [0.06, 0.84]) — bande
   située loin de la frontière d'exclusion, que le métrique `crossing_gap` (seuillé près de
   l'exclusion) ne mesure pas et que l'ABM à population finie quitte par bruit démographique.
   Lecture corrigée : **« près de la frontière d'exclusion, à ces tailles de population, le
   piège exige une réponse tardive »** — la raideur seule ouvre une fenêtre bistable ailleurs
   dans la carte déterministe sans produire de piège mesurable ici. La même carte corrobore
   indépendamment le résultat-phare : bande [0.93, 2.71] à K=0.05 (≈ la limite deux-états 2.0),
   aucune bande en linéaire.
3. **E4.1 et E5.3 requalifiées** en checks de cohérence d'implémentation (l'invariance en N
   découle de la linéarité exacte de la réinvestion agrégée ; π_total = τ post-exclusion est
   une identité comptable du canal de transfert) — le papier le dit désormais explicitement.
4. **Seeds densifiés commis en défauts** (E1/E4 : 30 ; E2/E2b : 10) et figures F1/F2/F2b/F4
   régénérées depuis ce code — chaque figure du papier est reproductible par la commande
   `--exp` correspondante (finding M1 clos).

## Suites (tâches à donner à Opus)

1. **Run densifié** : n≥30 seeds pour E1/E2/E2b/E4 ; bimodalité E2.3 ; départ à l'équilibre pour E1. (Config à formaliser en YAML par la même occasion.)
2. **Confirmation K** : pré-enregistrer quantitativement la prédiction K (ajout daté dans predictions.md : gap(K) croissant vers (1−β)S quand K→0, gap(K=0.05)∈[0.7,1.3]), puis run sur seeds NEUFS (≥10, seeds 100+) et rampes 2× plus lentes (contrôle du lag).
3. **E3.8** (piège permanent β<θ/S à K bas) et balayage β×K complet.
4. **E6** (early warnings sur les trajectoires K bas vs linéaire — la prédiction E6.3 discrimine maintenant les régimes par K, pas par n).
