# Note d'analyse — E3 préliminaire (2026-07-13, run de dérisquage, PAS le run de production)

Script : `sim/analysis/preliminary_e3.py`. Protocole : Λ_a contrôlé, rampe lente 0→4.5→0 (300 unités par branche), demande **continue** (DemandPool : v ∝ β + (1−β)·κ_h/κ_ref, couplage linéaire au revenu instantané lissé). Seuil de mesure : Λ_h croise 0.3.

## Résultats bruts

| β | sortie (montée) | ré-entrée (descente) | largeur de boucle |
|---|---|---|---|
| 0.6 | Λ_a ≈ 0.77 | Λ_a ≈ 0.87 | ≈ 0 (−0.11, bruit) |
| 1.0 | Λ_a ≈ 2.52 | Λ_a ≈ 3.03 | ≈ 0 (−0.51, artefacts) |

## Verdicts contre paper/predictions.md (E3)

- **E3.1-E3.3 : NON TESTÉES** — elles portent sur le protocole *deux états* ; ce run a utilisé le couplage continu. À tester telles quelles en production.
- **E3.4 : INFIRMÉE pour le couplage linéaire.** « La boucle persiste en continu (largeur ≤ (1−β)S) » — mesuré : largeur ≈ 0. Le gain de boucle du couplage linéaire est < 1 : pas de bistabilité (exactement la condition pointée par la revue adversariale, model-notes §5 ligne A8, ajoutée *avant* ce run).

## Analyse (vérifiée analytiquement à la main)

Avec v = [β + (1−β)·κ_h/κ_ref]·v_hi et κ_h = (c_h/μ_h)·Λ_h, l'équilibre auto-cohérent donne
Λ_h·(1 − (1−β)·S₀·c_h/(μ_h·κ_ref)) = β·S₀ − θ − Λ_a, soit avec les paramètres de base : **participation nulle dès Λ_a = β·S₀ − θ = 1.0** (β=0.6) — cohérent avec la mesure 0.77 (lag de rampe + bruit). Deux implications :
1. **Le couplage linéaire avance l'exclusion** (seuil β·S−θ au lieu de S−θ) **mais la rend réversible** (v suit le revenu symétriquement dans les deux sens).
2. **Le cliquet exige une non-linéarité** : réponse de la demande sigmoïde/à seuil, ou rigidité (v lié à l'état de participation plutôt qu'au revenu instantané — c'est ce que fait la version deux-états de model-notes §4, qui est une non-linéarité en marche d'escalier).

Artefacts de mesure identifiés (pour le protocole de production) : (a) le franchissement Λ_h=0.3 correspond en théorie à Λ_a = Λ̄−0.3, pas Λ̄ ; (b) sur la branche descendante, le burst d'entrée (excès de signal transitoire) fait un overshoot qui biaise le point de ré-entrée vers le haut ; utiliser plutôt l'aire de boucle sur tout le cycle et des rampes plus lentes.

## Conséquences pour la suite

- **E3 production (T4.3)** : ajouter un paramètre de non-linéarité de la demande (exposant de Hill n sur κ_h/κ_ref, n=1 = linéaire) et cartographier la bistabilité dans le plan (β × n) + protocole deux-états pour E3.1-3. Pré-enregistrer les prédictions de cette extension AVANT les runs (amender predictions.md par AJOUT daté, jamais par modification).
- **Papier / post AF** : présenter §4 ainsi — l'exclusion est robuste ; son *irréversibilité* dépend de la forme de la réponse de la demande : linéaire ⇒ effondrement plus précoce mais réversible ; le piège exige rigidité ou non-linéarité. C'est plus fin, plus honnête, et falsifiable empiriquement (la rigidité des ajustements de demande est mesurable).
