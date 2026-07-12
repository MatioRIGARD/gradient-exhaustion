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
- **E3.6 RÉFUTÉE TELLE QU'ÉNONCÉE** : la *raideur* n seule ne crée pas la boucle (n=8, K=0.5 : gap −0.17±0.12 ; l'aire mesurée au premier passage était un artefact de lag de rampe, cf. correctif du script). **Découverte exploratoire (non pré-enregistrée, à confirmer)** : le paramètre décisif est la *position* K de la réponse — une demande qui ne réagit que tard (K→0 : elle « tient » tant que le revenu humain n'a pas presque disparu — épargne, crédit, rigidités) crée une boucle nette : gap = 0.95±0.03 à K=0.05, monotone en 1/K, tendant vers la limite deux-états (1−β)S=2.
- **E3.7 partiellement soutenue** (convergence vers la limite deux-états visible dans la direction K→0) ; **E3.8 non testée**.
- **Lecture économique** (rejoint le prior n°2 de Mathieu, `docs/decisions.md`) : *si la consommation suit le revenu en douceur, l'effondrement est précoce mais réversible ; si elle tient (épargne/crédit/transferts) puis cède, il est tardif mais piégeant.* Implication à traiter avec précaution dans le papier : une politique de soutien de la demande retarde l'exclusion ET élargit la fenêtre du piège si elle cède.

## E4 — Nombre d'opérateurs (F4)

- **E4.1 CONFIRMÉE exactement** : t* identique pour N ∈ {1,2,5,20} à capacité agrégée constante (trajectoires appariées par seed superposées). Le résultat nul est propre : sans dissipation de rentes, la concurrence entre opérateurs ne change rien. **E4.2 (conditionnelle, dissipation) en attente de T3.8.**

## Suites (tâches à donner à Opus)

1. **Run densifié** : n≥30 seeds pour E1/E2/E2b/E4 ; bimodalité E2.3 ; départ à l'équilibre pour E1. (Config à formaliser en YAML par la même occasion.)
2. **Confirmation K** : pré-enregistrer quantitativement la prédiction K (ajout daté dans predictions.md : gap(K) croissant vers (1−β)S quand K→0, gap(K=0.05)∈[0.7,1.3]), puis run sur seeds NEUFS (≥10, seeds 100+) et rampes 2× plus lentes (contrôle du lag).
3. **E3.8** (piège permanent β<θ/S à K bas) et balayage β×K complet.
4. **E6** (early warnings sur les trajectoires K bas vs linéaire — la prédiction E6.3 discrimine maintenant les régimes par K, pas par n).
