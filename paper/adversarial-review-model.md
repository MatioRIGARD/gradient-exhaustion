# Revue adversariale — `model-notes.md` (§1–§5)

*Rôle : referee hostile mais rigoureux. Lecture seule. Objectif : trouver ce qui est FAUX, pas résumer. Priorité : (1) erreurs mathématiques, (2) tautologie cachée, (3) objections de fond, (4) sur-affirmations.*

---

## 1. Erreurs mathématiques

J'ai revérifié chaque pas de §2–§4 indépendamment. **Verdict : aucune erreur algébrique.** Toutes les formules sont correctes et coïncident, symbole par symbole, avec la re-dérivation aveugle (`rederivation-blind.md`).

Détail des vérifications :

- **Libre entrée / seuil (§2).** `gvμ_h/(Λ_h+Λ_a+θ)=c_h ⟹ Λ_h+Λ_a+θ=S≡gvμ_h/c_h`, d'où `Λ_h*=max(0, S−θ−Λ_a)` et `Λ̄=S−θ`. ✔
- **Revenus interieurs (§2, Result 2).** `κ_h*=(c_h/μ_h)(Λ̄−Λ_a)`, `κ_a*=(c_h/μ_h)Λ_a` (car `gv/S=c_h/μ_h`) ; total `κ_h+κ_a=gvΛ̄/S=gv(S−θ)/S` constant. ✔
- **Linéarité de π.** `π=κ_h/(κ_h+κ_a)=(Λ̄−Λ_a)/Λ̄=1−Λ_a/Λ̄`. ✔ Exactement linéaire — mais **par construction** (voir §2 ci-dessous), pas par surprise.
- **Critère γ (§3).** `γ=ηc_h/μ_h−δ`, `Λ̇_a=γΛ_a`. ✔
- **Temps d'exclusion.** `t*=(1/γ)ln(Λ̄/Λ_a(0))`. ✔
- **Point fixe post-exclusion.** `Λ_a**=ηgv/δ−θ`, et `Λ_a**>Λ̄ ⟺ η/δ>μ_h/c_h ⟺ γ>0`. ✔ L'équivalence est correcte.
- **Bande d'hystérésis (§4).** `Λ̄_exit−Λ̄_re=(1−β)(Λ̄_exit+θ)=(1−β)S(v_hi)` ; `Λ̄_re=βS(v_hi)−θ<Λ̄_exit ⟺ β<1` ; piège permanent `β≤θ/S(v_hi)`. ✔ Toutes cohérentes avec la re-dérivation.

**Deux imprécisions (non des erreurs de calcul) à corriger :**

- **M-a. Point fixe post-exclusion incohérent avec §4.** §3 calcule `Λ_a**=ηgv/δ−θ` avec `v` exogène constant et déclare l'exclusion « absorbing state ». Mais dès qu'on active la demande endogène (§4), après exclusion `v→v_lo=βv_hi`, donc le point de repos pertinent est `Λ_a**(v_lo)=ηgβv_hi/δ−θ`. La conclusion « absorbant » **survit** (`Λ_a**(v_lo)>Λ̄_re ⟺ γ>0`, que j'ai vérifié), mais §3 ne fait pas ce raccord et énonce l'état absorbant sur un point fixe qui n'est plus le bon une fois §4 en jeu. À recomposer explicitement.
- **M-b. Genericité r=0.** Le cas `γ=0` produit un continuum non-générique de points fixes (signalé dans la re-dérivation, flag 5). §3 le range en douce sous « γ≤0 → π→1 », ce qui est faux au sens strict à `γ=0` (marginal, pas convergence vers π=1). Cosmétique mais à noter.

Conclusion front 1 : **le squelette mathématique est solide.** L'attaque doit porter ailleurs.

---

## 2. Tautologie cachée — VERDICT DIFFÉRENCIÉ

Il faut séparer deux résultats, car ils n'ont pas le même statut.

### 2.a Exclusion (§2–§3) : **NON — émergent (sur un jeu de dés pipé)**

L'exclusion **n'est pas** vraie par construction, et je le concède parce que les preuves l'exigent :
- Elle est **conditionnelle à γ>0**. Si `γ≤0`, l'IA décroît et `π→1` (Result 4). Un régime documenté où le mécanisme *ne* produit *pas* d'exclusion existe.
- Les trois checks §2.4 sont valides : IA gelée → coexistence stable ; seconde population à libre entrée → partage indéterminé, aucune force d'exclusion ; `η=0` → rien. Ce sont de vrais garde-fous : ce n'est pas l'étiquette « IA » qui exclut.

**Mais** la note anti-tautologie (ligne 30) sur-vend « le mécanisme, pas les étiquettes ». La véritable asymétrie n'est pas seulement A7 (compounding). C'est **A9 dédoublée** : (i) les humains sont en libre entrée → rente nette nulle → *rien à réinvestir* ; (ii) l'IA réinvestit son revenu **brut** *sans aucune discipline concurrentielle de profit nul*. La re-dérivation le dit crûment (§Q4). C'est reconnu (A9), donc pas caché — mais l'ampleur l'est : **deux** asymétries empilées, pas une.

Ce qui, lui, **échappe au périmètre A7/A9** : le modèle analytique **interdit par construction qu'un humain possède le canal qui compound** (posséder Λ_a). Un « humain » est un travailleur à `(μ_h,c_h)` figés en libre entrée, point. Or `pi-definition.md` (cas centaure, série ρ, DEC-001) *sait* qu'un humain peut louer/posséder de la capacité IA — mais la **dynamique** de §3 ne l'autorise jamais. Si les humains peuvent acheter Λ_a, « exclusion humaine » devient une erreur de catégorie (le revenu échoit à des propriétaires humains). §5 ne flague pas cette exclusion-par-construction du canal de propriété. **À ajouter à l'audit.**

Verdict 2.a : **émergent, conditionnel, honnête sur γ — mais les dés sont pipés par A9, et le canal « humain propriétaire de l'IA » est retiré du modèle analytique sans que §5 le dise.**

### 2.b Hystérésis / cliquet (§4) : **OUI — largement construit par A8**

Ici je suis moins clément. Le résultat-vedette « la dépendance de la demande au revenu humain rend l'exclusion irréversible » (Result 6, revendiqué « nouveau ») est une **conséquence algébrique directe de poser `v_lo=βv_hi`**. Dès qu'on postule deux états de `v` indexés sur la présence humaine avec `v_lo<v_hi`, deux seuils distincts et une bande bistable de largeur `(1−β)S` sont *forcés*. Ce n'est pas émergent, c'est l'énoncé de l'hypothèse relu à l'envers.

Pire, **une asymétrie load-bearing y est cachée et non flaggée en §5** : A8 pose demande = `β·(autonome)` + `(1−β)·(nourrie par le revenu humain gagné)`. **Le revenu gagné par l'IA n'apparaît nulle part comme source de demande.** Quand les humains sortent, la fraction `(1−β)` s'évapore *alors même que l'IA encaisse désormais ce revenu*. Autrement dit A8 suppose que **le revenu humain est générateur de demande et le revenu IA ne l'est pas** (hors la part exogène et fixe β). C'est précisément le moteur du cliquet, et c'est une hypothèse d'étiquette (« humain » vs « IA »), pas un fait dérivé. Si le revenu IA recirculait symétriquement, `v` ne s'effondrerait pas et il n'y aurait pas de cliquet. De plus β est **fixe et exogène** : même quand la richesse IA explose post-exclusion, la demande autonome reste plafonnée à `βv_hi` — la collapse est cablée en dur.

§5 range A8 en « Simplification » et affirme « l'hystérésis qualitative survit avec `v(κ_h)` continu (argument de bifurcation standard) ». **C'est faux comme énoncé général** : une rétroaction *continue* `v(κ_h)` ne donne bistabilité que si le gain de boucle dépasse 1 ; ce n'est pas automatique. Le pli net est un artefact de la fonction en escalier. §5 ne couvre donc PAS ce point ; il l'esquive.

Verdict 2.b : **OUI, l'hystérésis est essentiellement construite** (conditionnelle à β<1, donc pas tautologie *logique* pure, mais l'énoncé « nouveau » n'apporte rien au-delà de son hypothèse, et repose sur une asymétrie de génération de demande humain/IA non déclarée).

**Verdict global tautologie : l'exclusion est émergente (2.a) ; le cliquet est construit (2.b). La phrase « le mécanisme, pas les étiquettes, produit *chaque* résultat ci-dessous » (ligne 30) est donc fausse pour §4.**

---

## 3. Objections de fond, classées (les 5 plus fortes)

1. **Pas d'équilibre général ; opportunités = manne ; revenu IA non recirculé ; régénération schumpétérienne absente.** `g` et `v` sont exogènes (sauf le §4 grossier). L'économie qui *engendre* les opportunités n'est pas modélisée. Un économiste type Korinek attaque ça en premier : en EG, l'abondance IA fait monter revenus et demande, ouvre de nouvelles niches → `g` croissant avec la capacité, ce qui peut soutenir indéfiniment une frange humaine. Le modèle fige `g` et refuse à l'IA tout rôle de demandeur. **Statut : (a) fatal à la généralité de la conclusion / (b) adressable en ABM (g endogène, consommation IA) — mais l'adresser risque de renverser à la fois l'exclusion et le cliquet.** C'est la plus forte.

2. **Les humains ne peuvent ni acheter ni posséder la capacité IA.** Dans le modèle un « humain » est un travailleur `(μ_h,c_h)` figé. Le résident résiduel humain qui *possède* Λ_a n'existe pas dans la dynamique. « Exclusion humaine » devient alors une question de *distribution entre humains* (propriétaires vs non-propriétaires), un problème différent — et sans doute plus réel. **Statut : (b) adressable en ABM (canal de propriété), mais dissout ou reformule le résultat.** L'accounting (ρ, centaure) est prêt dans `pi-definition.md` ; la dynamique ne l'est pas.

3. **Zéro option extérieure ⇒ l'exclusion est vide de contenu welfare.** Libre entrée + option extérieure = 0 ⟹ **surplus net humain identiquement nul dans tout le régime A** (la re-dérivation l'établit, A9/welfare note l'admet). Donc le passage `Λ_a:0→Λ̄` fait chuter π de 1 à 0 mais change le bien-être humain de *exactement zéro*. Le modèle ne peut structurellement pas représenter le mal qu'il prétend diagnostiquer ; toute la charge normative repose sur une hypothèse non modélisée (« ne pas participer est pire », subsistance négative). **Statut : (c) limitation à énoncer explicitement** — corrigeable par une option extérieure positive/subsistance, ce qui déplacerait les seuils. Objection conceptuelle sérieuse.

4. **Aucun marché du travail, aucun prix, aucun salaire.** « Revenu » = flux de capture ; la libre entrée à profit nul est un ersatz brutal de marché du travail. Pas de prix des facteurs, pas de réallocation. Un referee EG demandera où sont les prix. **Statut : (c) limitation à énoncer / partiellement (b).**

5. **θ exogène et faisant le gros du travail ; pas de création de niches.** `θ` (décroissance des gradients) est exogène, indépendant de qui chasse, et porte les seuils (précondition `S>θ`, tous les `Λ̄`). Pourquoi un `θ` fixe ? Et l'abondance IA ne crée aucune niche nouvelle (couplé à l'objection 1). **Statut : (b)/(c).**

*(Objections déjà couvertes, non comptées : IA agrégée unique A6 → E4 ; humains homogènes A4 → front, pas falaise ; concurrence d'opérateurs érodant η → E4/A9.)*

---

## 4. Sur-affirmations (citations)

- **Ligne 88 :** « Neither malice nor strategy appears anywhere; **competition + compounding suffice.** » — Sous-déclaré : il faut aussi (i) libre entrée à rente retenue nulle côté humain, (ii) réinvestissement *brut* IA sans discipline de profit nul (A9), (iii) revenu IA non générateur de demande (A8). « competition + compounding suffice » masque A9 et l'asymétrie de demande.
- **Ligne 108 :** « the more the economy's demand depends on human income, the **more irreversible** exclusion becomes… **Counterintuitive and, we believe, novel as a formal statement.** » — Sur-vente : identité algébrique directe de `v_lo=βv_hi`. « nouveau » habille une hypothèse ; le « we believe » n'est pas vérifié.
- **Ligne 30 :** « the mechanism, not the labels, drives **every** result below. » — Faux pour §4 : le cliquet repose sur une asymétrie d'étiquette (revenu humain nourrit la demande, revenu IA non).
- **Ligne 126 (§5) :** « **qualitative hysteresis survives** (standard bifurcation argument — verify numerically) » — Affirmé, non dérivé, et conditionnellement faux : la bistabilité en `v(κ_h)` continu exige un gain de boucle > 1.
- **Ligne 86 :** « exclusion is an **absorbing state** as long as parameters don't change » — Établi avec `v` constant ; sous §4 (v→v_lo) il faut recomposer le point fixe (M-a). La conclusion tient mais n'est pas montrée.
- **Ligne 128 (§5) :** « the model is falsifiable through its parameters, **hence not a tautology.** » — Auto-complaisant : la falsifiabilité du critère d'exclusion (γ) ne blanchit pas la construction en escalier de A8 ni l'asymétrie de demande.

---

## 5. Verdict final

**Publiable comme post court après corrections mineures : OUI** — conditionnellement. Le cœur mathématique (§2–§3) est correct, indépendamment reproduit, et l'exclusion y est présentée honnêtement comme *conditionnelle* (γ>0) avec des sanity checks valides. Ce sont des mérites réels et rares. Aucune objection n'est fatale *à un post court qui cadre honnêtement sa portée*. Mais le §4 sur-vend un résultat construit, et une asymétrie load-bearing n'est pas déclarée.

**Corrections EXIGÉES avant publication :**

1. **Déclarer l'asymétrie de génération de demande de A8** : le revenu humain nourrit la demande, le revenu IA non (β exogène fixe). C'est le vrai moteur du cliquet. À ajouter à l'audit §5 comme hypothèse load-bearing, pas comme « simplification ».
2. **Rétrograder Result 6** : retirer « novel/counterintuitive » ou le requalifier « conséquence de l'hypothèse à deux états » ; remplacer « l'hystérésis qualitative survit avec v continu » par la condition explicite (gain de boucle > 1 ; sinon pas de pli).
3. **Neutralité welfare de l'exclusion** : énoncer en clair que, l'option extérieure étant nulle, le surplus net humain est identiquement nul dans tout le régime A — donc π mesure la présence, pas le bien-être, et la charge normative requiert une hypothèse de subsistance non modélisée.
4. **Ajouter à l'audit** l'exclusion-par-construction du canal « humain propriétaire/acheteur de Λ_a » (présent dans `pi-definition.md`, absent de la dynamique) comme limitation de la phase analytique, à lever en ABM.
5. **Corriger ligne 30** : « le mécanisme, pas les étiquettes » ne vaut que pour §2–§3, pas pour §4.
6. **Raccorder M-a** : recalculer le point fixe post-exclusion sous `v_lo` et montrer que l'état absorbant tient (`Λ_a**(v_lo)>Λ̄_re ⟺ γ>0`).
7. Adoucir les sur-affirmations des lignes 88 et 128.

Corrections **recommandées** (non bloquantes) : traiter le knife-edge γ=0 (M-b) ; annoncer l'objection EG/manne (front 3.1) comme la limitation numéro un en section limites.
