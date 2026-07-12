# Revue adversariale — `paper/paper.md`

> Referee hostile mais rigoureux. Sources de vérité : `paper/model-notes.md`,
> `sim/analysis/notes-production-v1.md`, `sim/analysis/notes-preliminary-e3.md`,
> `paper/predictions.md`, `docs/biblio-verification.md`. Lecture seule sauf ce fichier.
> Date de revue : 2026-07-12.

---

## 1. Traçabilité

Chaque nombre / claim mot-à-mot du papier confronté à sa source. Verdict : ✅ concorde,
⚠️ concorde mais à nuancer, ❌ ne concorde pas.

| Claim (papier) | Emplacement | Source | Verdict |
|---|---|---|---|
| « verified five ways » | Abstract | model-notes en-tête : **« Verified four ways »** (19 checks, re-dérivation aveugle, repro ABM V1 6/6, revue adversariale) | ❌ **MISMATCH** — la source dit explicitement *quatre*, pas cinq ; aucune énumération de cinq voies n'existe dans le papier |
| « verified five ways » — décompte des 19 checks | Abstract | log de vérif : C1-C3 = 12, C4 = 5, C5 = 2 → **19** | ✅ le total 19 est correct, mais rattaché à « four ways » |
| V1 « passes 6/6 at the stated tolerances (8-35% per test) » | §4.3 | model-notes log : « ✅ PASS (6/6 tests) … tolerances 8-35% as stated per test » | ✅ |
| τ* ≈ 0.917 | Abstract, §5.5, §8 | predictions E5.1 : τ*=1−δμ_h/(ηc_h) ≈ 0.917 ; notes-prod E5.1 | ✅ (recalculé : 0.9167) |
| ρ* ≈ 0.965 | Abstract, §5.5, §8 | predictions E4.4 ; notes-prod E4b | ✅ |
| t*(0.5)=8.3 (préd. 9.2), t*(0.8)=31.4 (préd. 33), « within 10% » | §5.5 | notes-prod E5.2 « écarts ≤10 % » | ⚠️ arithmétique OK (9.8 % et 4.8 %) MAIS la prédiction pré-enregistrée E5.2 portait une tolérance **±35 %**, pas 10 % — le « within 10% » est un resserrement *a posteriori* non signalé |
| π_total post-exclusion = τ exactement (0.50, 0.80), Δ=τ | §5.5 | notes-prod E5.3 ; predictions E5.3 | ✅ |
| E4b : t*=3.2, 7.9, 58.7 à ρ_d∈{0,0.5,0.9} ; ρ_d=1.0 → 6/6 seeds ; collusion → t*=3.2 | §5.5 | notes-prod E4b | ✅ |
| loop width +0.64±0.13 (K=0.05) vs −0.14±0.08 (linéaire), diff 0.78, IC disjoints | §5.3 | notes-prod (2026-07-13b) ; recalcul 0.64−(−0.14)=0.78 | ✅ |
| « 0.64 versus 0.95 » (narrower que la passe exploratoire) | §5.3 | notes-prod : « 0.64 vs 0.95 » | ✅ |
| fresh seeds 100-109, half ramp speed | §5.3 | predictions ADDENDUM 13b ; notes-prod | ✅ |
| E3.6 raideur : gap −0.17±0.12 | §5.3 | notes-prod E3.6 | ✅ |
| E6 négatif, lag-1 autocorr 0.64→0.65 | §5.6 | notes-prod E6 « piège : 0.64→0.65 » | ✅ |
| Baseline g=50, v=1, θ=2, μ_h=0.01, c_h=0.1 ⇒ S=5, Λ̄=3, γ=10η−δ | §5 | predictions ligne 12 | ✅ |
| E1.1 : γ<0 (η=0.003), π≈0.95 | §5.1 | notes-prod E1.1 ; γ recalculé = −0.02 | ✅ |
| β≤θ/S piège absolu ; θ/S=0.4 | §3.4 | model-notes §4 ; predictions E3.3 | ✅ |
| Λ̄_re = β(Λ̄_exit+θ)−θ ; largeur = (1−β)(Λ̄_exit+θ)=(1−β)S | §3.4 | model-notes §4 (lignes 102-106) | ✅ |
| Point fixe post-exclusion Λ_a**=ηgv/δ−θ ; β s'annule, condition reste γ>0 | §3.3 | model-notes §3 ligne 86 | ✅ |
| « confirms the exact phase boundary » | Abstract | notes-prod E2.1 : « bande de transition ≤ 1 cellule » ; §1(iii) papier : « to within a cell of the grid » | ⚠️ « exact » sur-vend « à ≤1 cellule près » — contradit son propre §1(iii) |
| Assad et al. 2024, JPE 132(3):723-771, marges ↑ stations non-monopolistiques | §2, §6, réfs | biblio-verification ligne 26 | ✅ |
| De Loecker & Eeckhout, markups 1.1→1.6 sur 1980-2016, NBER WP 24768, **sans** « superstar » | §2 | biblio ligne 19 (correction appliquée) | ✅ |
| Kulveit et al., PMLR 267:81678-81688 ; Hammond « seven risk factors » | §2, réfs | biblio lignes 11, 15 | ✅ |
| P(net>0)≈0.49 (marché perdant) / 0.59 (break-even) pour la règle d'apprentissage | §4.4 | **Aucune source fournie** | ⚠️ non traçable dans les fichiers de vérité ; sans doute issu du code, mais non vérifiable ici |
| Résultats V3 (invariance : permutation seeds, doublement réservoir, halving pas de temps) | §4.3 (promis) | Aucun verdict dans notes-prod ni ailleurs | ❌ promis en §4.3, **jamais rendu** en §5 |

**Bilan traçabilité :** un seul vrai ❌ chiffré (« five ways » vs « four ways »), un ❌
structurel (V3 promis non rendu), trois ⚠️ (« exact » boundary, « within 10% » vs
±35 % pré-enregistré, chiffres d'apprentissage non sourcés). Tout le reste — et
c'est l'essentiel, les t*, τ*, ρ*, largeurs de boucle, seuils — concorde au chiffre près.

---

## 2. Sur-affirmations (citations)

1. **Abstract : « A minimal analytic model, verified five ways »**
   La source (`model-notes.md`, en-tête) dit « Verified four ways ». Le papier gonfle
   le décompte d'une unité dans la phrase la plus lue du document. Aucune énumération
   des cinq voies n'est fournie nulle part. Sur-affirmation nette et facile à corriger.

2. **Abstract : « it quantifies three policy levers, finding that redistribution
   prevents exclusion only above a near-confiscatory threshold (τ*≈0.917) … »**
   Ces chiffres proviennent d'une **première passe de production à seeds réduits (3-10)**
   (§5 en-tête l'énonce clairement : « This is a *first production pass* on reduced seed
   counts (3-10) »). L'abstract présente τ*, ρ* et les t* comme des acquis sans jamais
   porter ce caveat. Ce n'est pas faux (τ*/ρ* sont des seuils *analytiques* encadrés par
   la sim), mais l'abstract sur-vend la solidité empirique.

3. **Abstract : « confirms the exact phase boundary »**
   Le corps du papier (§1 iii, §5.2) et les notes disent « à ≤1 cellule de grille près ».
   « exact » est plus fort que ce que le §5 a mesuré et se contredit avec son propre §1(iii).

4. **§5.5 : « within 10% (E5.2) »**
   La prédiction E5.2 pré-enregistrée était « ±35% ». Le papier remplace silencieusement
   la tolérance annoncée par une tolérance mesurée plus serrée. Techniquement honnête
   (l'écart réel est ~10 %), mais présenté d'une façon qui masque que la barre
   pré-enregistrée était bien plus lâche. À rendre transparent.

Les verdicts §5 (« CONFIRMED, sharply », « CONFIRMED exactly ») reproduisent fidèlement
le ton des notes (« CONFIRMÉE, spectaculairement / exactement ») : pas de sur-affirmation
là. Le §5.6 (early warnings négatif) et le §7 (limites) sont, eux, honnêtes voire
sous-vendus.

---

## 3. Cohérence interne

- **Figures :** les 8 figures référencées (F1, F2, F2b, F3, F4, F4b, F5, F6) existent
  dans `paper/figures/`. La checklist finale coche F1-F5+F4b et laisse F6 à ☐ (« negative
  first pass »), cohérent avec §5.6. ✅ Aucune figure manquante, aucune orpheline.

- **Collision de notation ρ :** `ρ` désigne (i) la série de revenu de capital passif /
  propriété (DEC-001, §4.2 et §7) ET (ii) via `ρ_d`/`ρ*` la dissipation de rentes
  (§5.5, §8). Un lecteur peut confondre « ρ series » (propriété) et « ρ* ≈ 0.965 »
  (dissipation). À désambiguïser (renommer la série de propriété, p.ex. `ω`).

- **Audit §3.5 vs ce que §5 teste :** cohérent. A7′ (saturation) → testé §5.2 (E2b) ✅ ;
  A8 (demande) → testé §5.3 (E3) ✅ ; A9/A6 (concurrence opérateurs, discipline de rente)
  → testés §5.4-5.5 (E4/E4b) ✅ ; A10 (équilibre général) explicitement non testé, énoncé
  comme limite ✅ ; A11 (propriété) rapporté à part, non testé, cohérent avec §3.5.

- **Protocole de validation V1-V3 (§4.3) vs Résultats :** V1 rendu (6/6). V2 invoqué
  qualitativement. **V3 (invariance) n'a aucun verdict rapporté.** Le §4.3 le présente
  comme une couche de garde-fou de premier ordre ; le §5 ne dit jamais si elle a passé.
  Incohérence à combler.

- **Décompte « verified five ways » :** ni le papier, ni model-notes n'énumèrent cinq
  voies ; le log de vérif a 6 lignes qui se regroupent en 4 méthodes distinctes. Le
  « five » ne correspond à aucun regroupement naturel. (Voir §1, §2.1.)

- **Paramètre de raideur sigmoïde :** le §5.3 parle de « steepness » et de « lateness K »
  mais n'introduit jamais le symbole `n` (l'exposant de Hill) qui porte la raideur dans
  predictions/notes. Le lecteur du seul papier ne sait pas ce qu'est « steepness ».
  Défaut mineur (voir §5).

---

## 4. Objections non couvertes par §7

### Fatales
Aucune. Le §7 est inhabituellement complet (il désamorce lui-même l'équilibre partiel,
le caractère value-laden de π, la variante capital-funded, l'économie parallèle, la course
juridictionnelle). Rien qui invalide la publication en working paper.

### Adressables (à traiter avant/dans la v suivante)
1. **Sensibilité aux propres boutons de réglage de l'ABM.** Le §4.1 introduit grubstake
   (patience×cost), `entry_rate`, terme `explore`, cap de dépletion — tous des paramètres
   libres du simulateur. Aucun balayage de sensibilité n'est rapporté. Un méthodologue ABM
   attaquera : les t*, τ*, ρ* dépendent-ils de ces réglages ? §7 ne dit rien. À montrer,
   au moins qualitativement, que les résultats headline sont invariants sur une plage.
2. **Seeds réduits (3-10) pour des estimations à 3 chiffres significatifs.** Rapporter
   « t*=31.4 » ou « t*=58.7 » à partir de ≤10 seeds, sans IC, prête le flanc. E2.3
   (bimodalité) est « non évaluée ». Le §5 le signale mais l'abstract et §8 propagent les
   points. À encadrer d'IC ou à dégrader en « ordre de grandeur » tant que le run densifié
   (n≥30, déjà planifié) n'a pas eu lieu.
3. **Résultats V3 absents** (cf. §3) — un reviewer ABM demandera la preuve d'invariance
   avant de croire l'équilibre de libre-entrée émergent.

### À mentionner
4. **Le saut « économique → contrôle institutionnel ».** La thèse-mère (Kulveit et al.)
   porte sur l'érosion du *contrôle humain* (vote, loi, culture) ; ce papier ne modélise
   que la *part de flux économique* π. Qu'un commentateur AF pointera : π_market→0
   n'établit pas, à lui seul, la perte de contrôle — c'est le pari, non démontré, que
   l'un entraîne l'autre. Le papier se présente honnêtement comme « une pièce », mais le
   pont n'est jamais argumenté ; une phrase le reconnaissant explicitement manque.
5. **Tension titre/welfare.** Le titre « Priced Out by Machines » et le mot
   « disempowerment » suggèrent un préjudice de bien-être que le modèle admet ne pas
   pouvoir représenter (net rent = 0 partout ; π mesure la *présence*, pas le welfare —
   §1 non-claims, §7). Un économiste Korinek-style relèvera que l'objet mesuré est
   welfare-muet alors que le framing promet du welfare. À désamorcer d'une ligne dans
   l'intro, pas seulement au §7.
6. **Légitimité de l'abstraction « gradient ».** Réduire arbitrage + innovation + travail
   à un unique flux poissonien de valeur homogène v est une réduction forte ; §6 admet
   des proxies « confounded » mais ne défend pas la validité externe du noyau. Korinek-style
   objection à anticiper.

---

## 5. Défauts de présentation

1. **`n` (raideur de Hill) jamais introduit dans le corps du papier** alors que §5.3
   raisonne sur « steepness ». Le lecteur du seul papier ne peut pas rattacher « steepness »
   à un paramètre. Introduire le symbole ou dire « exposant de la réponse sigmoïde ».
2. **Collision ρ / ρ_d / ρ*** (cf. §3) — friction de lecture réelle.
3. **V3 promis puis muet** — le lecteur attend un verdict d'invariance qui ne vient pas.
4. **Abstract dense d'une seule phrase-fleuve** (la 4e phrase fait ~8 lignes). Découper.
5. **« within 10% » vs « ±35% » pré-enregistré** — sans note, un lecteur attentif qui
   ouvre predictions.md croira à une incohérence. Une demi-phrase (« l'écart mesuré,
   ≤10 %, est très en-deçà de la tolérance pré-enregistrée de ±35 % ») transformerait un
   soupçon en point fort.
6. **Chiffres de la règle d'apprentissage (0.49/0.59) non sourcés** dans les fichiers
   fournis — au minimum renvoyer au script qui les produit.
7. Redondance mineure : la liste « ce qui falsifie » apparaît trois fois quasi
   identique (§3.5, fin §7, §8). Acceptable dans un working paper, mais compressible.

---

## 6. Verdict final

**Publiable comme working paper (arXiv register) après corrections mineures : OUI.**

Le cœur — modèle analytique fermé, triple-vérifié, et ABM pré-enregistré qui reproduit
puis étend — est solide, honnête, et traçable au chiffre près sur l'écrasante majorité des
claims. Les défauts sont de calibrage rédactionnel et de complétude de reporting, non de
fond. Le point le plus grave est purement cosmétique (« five » au lieu de « four »), le
plus substantiel est un trou de reporting (V3) et un manque de caveat sur les seeds réduits.

### Corrections exigées (numérotées)

1. **Abstract : « verified five ways » → « verified four ways »** (ou énumérer
   explicitement cinq voies distinctes si l'auteur en revendique cinq). Aligner sur
   `model-notes.md`.
2. **Abstract : ajouter le caveat « première passe de production, seeds réduits (3-10) »**
   présent au §5, avant d'énoncer τ*, ρ* et les t* comme acquis.
3. **Abstract : « exact phase boundary » → « à une cellule de grille près »** (aligner sur
   §1 iii et §5.2).
4. **Rapporter les résultats V3 (invariance) au §5**, ou retirer la promesse du §4.3.
5. **Désambiguïser la notation ρ** : la série de propriété passive (DEC-001) et la
   dissipation de rentes (ρ_d, ρ*) partagent la lettre ρ ; renommer l'une.
6. **§5.5 : rendre explicite** que le « within 10% » est plus serré que la tolérance
   pré-enregistrée ±35 % (E5.2), plutôt que de substituer silencieusement la barre.
7. **Introduire le paramètre de raideur (`n`/exposant de Hill) dans le corps** avant de
   raisonner sur « steepness » au §5.3.
8. **Sourcer les chiffres de la règle d'apprentissage** (P(net>0)≈0.49/0.59, §4.4) —
   renvoi au script, faute de quoi ils sont non vérifiables.
9. **Ajouter au §7 (ou en intro) une ligne** reconnaissant (a) que π→0 ne démontre pas à
   lui seul la perte de contrôle institutionnel — le pont vers la thèse Kulveit reste un
   pari — et (b) la tension titre/welfare (π est welfare-muet).
10. **Signaler l'absence de balayage de sensibilité aux paramètres propres de l'ABM**
    (grubstake, entry_rate, explore) comme limite ouverte au §7.

Corrections 1-3 et 6 sont triviales (mots/chiffres). 4, 5, 7-10 demandent quelques
paragraphes. Aucune ne touche un résultat.
