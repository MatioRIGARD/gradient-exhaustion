# Audit externe pré-publication — session fraîche, 2026-07-13

> Auditeur : agent Fable 5 sans historique du projet, mandat hostile. Méthode : 6 volets
> (reproductibilité, intégrité épistémique, traçabilité, maths, code vs modèle, prêt-à-publier),
> avec deux sous-agents frais et indépendants pour les volets 4 (re-dérivation mathématique)
> et 5 (audit du code + contre-vérifications numériques). Le repo est la seule vérité terrain.
> Rien n'a été pushé. `predictions.md` et les tests n'ont pas été touchés.

---

## VERDICT GLOBAL : PUBLIABLE — OUI, conditionnel

**Le post Alignment Forum est publiable après deux corrections ciblées (M2 et M3 ci-dessous)
et l'exécution de l'étape 0 de la checklist (vérification croisée hors famille Claude, déjà
prévue mais jamais faite — M4).** Le papier arXiv demande en plus la remise en état de la
chaîne de reproductibilité des figures (M1).

Ce qui tient — et c'est le cœur : les maths de model-notes §2-§4 sont **correctes** (re-dérivées
intégralement par un référé frais, zéro erreur d'algèbre) ; le code implémente **fidèlement** le
modèle, sans aucun terme tautologique détecté (course de capture exacte et non biaisée — probe
numérique 20 000 pas —, libre entrée émergente, asymétries toutes déclarées ou de sens
anti-conclusion) ; `make setup && make ci` passe (lint propre, 14/14 tests),
`analytic_check.py` rend 19/19 PASS ; les pré-enregistrements précèdent topologiquement les
runs dans git pour les 4 vagues ; les deux revues adversariales sont réelles et substantielles
et **leurs 7 + 10 corrections exigées sont toutes effectivement appliquées** (vérifiées une à
une) ; les prédictions réfutées (E3.4, E3.6, E6) sont rapportées comme telles, ce qui est le
plus fort signal de bonne foi du dossier ; le résultat-phare de l'hystérésis (piège à demande
tardive K=0.05, rien en couplage linéaire) est **corroboré par une contre-vérification statique
indépendante de l'ABM** faite pendant cet audit.

---

## Findings

### Majeurs

**M1 — Les figures commitées ne sont pas régénérables par le code commité.**
PLAN.md:29 annonce « densification faite (E1/E4 : 30 seeds ; E2/E2b : 10 seeds — figures
régénérées et commitées) ». Les binaires densifiés ont bien été commités — mais dans
`c175bc1`, un commit dont le message ne parle que de l'objection juridictionnelle
(`git show --stat c175bc1` : f1, f2, f2b, f4 modifiées) — et **sans le code correspondant** :
les défauts de `sim/experiments/production_v1.py` sont restés `e1(seeds=10)`, `e2(3)`,
`e2b(3)`, `e4(10)` depuis leur création (`c717fec`), et le CLI n'a pas d'argument seeds.
Preuve visuelle : la F4 commitée montre ~30 points par colonne ; la régénération avec le code
commité en produit 10 (motif d'invariance identique dans les deux — pas de signal de
fabrication, les seeds 0-9 sont un sous-ensemble cohérent du nuage). Viole CLAUDE.md règle 6
(« tout chiffre cité est régénérable par une commande ») et le README (« every reported number
regenerates from a single documented command »). **À faire : committer les seeds densifiés en
défauts (ou en argument CLI documenté) et régénérer les figures depuis ce code.**

**M2 — Le chiffre central de l'hystérésis n'a aucun chemin de code.**
`sim/analysis/notes-production-v1.md:25` : gap(K=0.05) = +0.64±0.13, seeds 100-109,
t_leg=600, « Données : results/e3_confirmation.npz ». Or `results/` est gitignoré (données
absentes) et **aucun script commité ne produit ce protocole** : `--exp e3` régénère le
protocole exploratoire (seeds 0-2, t_leg=300 — celui dont le gap 0.95 était reconnu contaminé
par le lag de rampe). Le chiffre repris par l'abstract, §5.3 du papier et le post AF est donc
non régénérable. **À faire avant publication : ajouter `--exp e3conf` (seeds 100-109,
t_leg=600, β=0.6, n=8, K∈{0.05}, linéaire) reproduisant E3.9-E3.11.**

**M3 — Sur-interprétation d'E3.6 : « la raideur n seule ne crée pas le piège » est plus forte
que ce que la mesure autorise.** Contre-vérification indépendante de l'ABM (sous-agent volet 5) :
la carte d'équilibres statique du couplage de demande — résoudre la libre entrée auto-cohérente
Λ_h + Λ_a + θ = S·m(Λ_h/Λ̄), m = β + (1−β)·Hill(n, K) — montre une **bande bistable réelle à
K=0.5, n=8 (Λ_a ∈ [0.06, 0.84], largeur 0.78)**, là où l'ABM mesure gap = −0.17±0.12 et où les
notes concluent « n ne compte pas ». Explication : le métrique `crossing_gap`
(production_v1.py:219, seuil fixe Λ_h=0.5) ne détecte que le piège *proche de l'exclusion* ;
la bistabilité à K médian vit à Λ_a bas / Λ_h haut et s'échappe par le bruit de population
finie. La phrase du papier §5.3 et du post AF (« What restores the trap is the response's
lateness ») doit être requalifiée : *vrai pour le piège près de l'exclusion mesuré par ce
métrique*, pas comme propriété générale du modèle. **Contrepartie décisive : le même calcul
corrobore le résultat-phare** (bande statique [0.94, 2.71] à K=0.05, ≈ la limite deux-états ;
aucune multi-stabilité en linéaire) — la conclusion centrale tient, c'est sa généralisation
qui déborde.

**M4 — La vérification hors famille Claude n'existe pas (encore).**
Toutes les vérifications du journal de model-notes sont intra-Claude ou numériques : les
19 checks et la re-dérivation aveugle (authentique — contenu excédentaire propre, notation
indépendante — mais même famille de modèles). Aucun fichier de résultats d'une dérivation
par un modèle tiers n'existe **ni dans l'arbre ni dans aucun des 35 commits de l'historique**
(vérifié). Ce qui existe : `docs/verification-pack.md` (prêt à l'emploi) et l'étape 0 de
`docs/checklist-publication.md`, **non cochée**. « Triple/quadruple-vérifié » doit se lire
« vérifié plusieurs fois au sein de la même famille » tant que l'étape 0 n'est pas faite —
le repo le reconnaît d'ailleurs lui-même en ayant créé le pack. Si tu pensais ce résultat
déjà acquis : il ne l'est pas.

### Mineurs

**m5 — Incohérence sur les seeds entre papier et figures.** L'abstract et le §5 disent
« first production pass at reduced seed counts (3-10) » alors que les F1/F2/F2b/F4 commitées
sont les versions densifiées (30/10 seeds). Un référé qui compte ~30 points dans F4 conclura
à une incohérence. Se résout avec M1 (aligner texte, code et figures).

**m6 — Convention « configs YAML » violée.** `sim/experiments/configs/` ne contient qu'un
`.gitkeep` ; tous les paramètres sont en dur dans `production_v1.py` (contra CLAUDE.md et
simulation-architecture) ; le dict BASE est dupliqué à l'identique dans 5 fichiers et
`LAMBDA_BAR = 3.0` est en dur en 4 endroits alors qu'il dérive de BASE. Reconnu dans
notes-production §Suites, mais le README du repo bientôt public affirme « experiment configs
are versioned » — faux aujourd'hui.

**m7 — README périmé.** « Status: Early stage — model formalization in progress » à la veille
de publier des résultats complets. À réécrire avant `gh repo create` (étape 4 checklist).

**m8 — Une règle asymétrique non ablatée : le plafond de richesse humain.**
`sim/core/agents.py:79-84` : `credit()` écrête la richesse humaine à `patience × cost`
(« consume the surplus »). C'est une *règle* sans analogue côté IA, de sens pro-conclusion
(interdit de banquer la chance passée → sorties plus rapides). Déclarée en docstring et bornée
par l'ancre V1, mais jamais ablatée. Ablation recommandée (cap → ∞) pour montrer
l'insensibilité des seuils.

**m9 — Biais O(dt) du signal d'entrée humain.** `sim/core/dynamics.py:152` : le signal de
richesse de marché est mesuré après le retrait des opportunités du pas (~−2,5 % au baseline) ;
seuls les humains le consomment → sous-entrée humaine (sens pro-conclusion). Couvert par
`test_timestep_invariance` mais à tolérance large (~20 %). À noter dans les limites ABM.

**m10 — Deux « confirmations » sont vraies par construction.** E5.3 (π_total = τ exactement
post-exclusion) est une identité comptable de l'implémentation (dynamics.py:143-144), et
E4.1 (invariance en N) découle de la linéarité exacte de la réinvestion agrégée
(agents.py:160-162). Les présenter comme checks d'implémentation, pas comme découvertes —
le ton « CONFIRMÉE au centième / exactement » sur-vend.

**m11 — π_market est calculé avec κ_a NET de taxe et de dissipation** (indices.py, choix
documenté) : à τ>0 ou ρ_d>0 le dénominateur rétrécit et gonfle mécaniquement la part humaine.
Sans effet au baseline, mais à défendre explicitement dans le papier pour E5/E4b.

**m12 — « tolerances 8-35% » optimiste sur un point.** `test_analytic.py:53` : tolérance
libre-entrée 0.45 *absolu*, soit 45 % relatif au point Λ_a=2. Les autres tolérances annoncées
sont conformes ; les assertions restent non triviales.

**m13 — Erreur de bord γ=0 (corrigée sur branche).** « γ ≤ 0 ⇒ π → 1 » est strictement faux à
γ = 0 (Λ_a reste figé ; ligne de points fixes neutres — la re-dérivation aveugle le traitait
correctement, model-notes non ; flaggé « recommandé non bloquant » par la revue du modèle,
jamais appliqué). Corrigé dans model-notes.md, paper.md et af-post sur la branche
`audit-fix/gamma-zero-edge`. **`predictions.md:17` porte le même lapsus mais est gelé par
politique — à mentionner d'une note dans le papier, pas à réécrire.** Même famille :
le domaine de t* (0 < Λ_a(0) < Λ̄) et l'« annulation de β » (suppose β > 0) méritent
une demi-ligne chacun.

### Notes

**n14 — Dates.** Tous les commits sont du 2026-07-12 (+0700) alors que PLAN/notes/checklist
parlent des 13-14/07. L'*ordre* topologique (qui seul fait foi pour le pré-enregistrement) est
cohérent ; les dates absolues ne le sont pas. Sans gravité — l'antériorité publique viendra de
la publication — mais à savoir si quelqu'un inspecte l'historique.

**n15 — Force probante du pré-enregistrement.** Les 4 vagues de prédictions précèdent leurs
runs de 5 à 17 minutes, même acteur, même session. En soi, cela ne prouve pas grand-chose
(l'ordre des commits ne prouve pas l'ordre d'exécution). Ce qui porte réellement la crédibilité :
trois prédictions **réfutées** et rapportées comme telles (E3.4, E3.6, E6), et l'ancrage
analytique indépendant des chiffres confirmés. Présenter le pré-enregistrement comme discipline
d'honnêteté, pas comme preuve forte.

**n16 — E4.4 : la formule η(1−ρ_d(1−1/N)) est une spécification de la couche T3.8, pas un
théorème du modèle §1-§4 ; predictions.md la présente dans le même registre que les prédictions
dérivées. L'arithmétique (ρ* ≈ 0.965) est exacte.**

**n17 — Piège absolu strict/large incohérent entre documents** : β ≤ θ/S (model-notes:112),
β < θ/S (log de vérification), β < β_crit (rederivation-blind) — le log affirme pourtant une
concordance « symbol for symbol ». Sans conséquence (convention d'entrée au break-even).

**n18 — Détails production_v1.py** : `loop_area` est du code mort ; les `np.convolve(...,
"same")` paddent en zéros aux bords (sans effet ici, fragile) ; dans `e6`, `np.argmax(<0.3)`
rend 0 silencieusement si aucune sortie.

**n19 — `test_no_ai`** : l'assertion π > 0.999 est vraie par construction (κ_a ≡ 0 sans IA) ;
le contenu réel du test est la stationnarité. Le reste de test_sanity contraint authentiquement
(le plancher de coexistence 0.1 vaut ~5× le niveau atteignable par pure exploration) ; le
fichier n'a **jamais été affaibli** (2 commits, aucun après sa création).

**n20 — Volet 6 (prêt-à-publier) : conforme.** La checklist est exécutable telle quelle
(P3/P4 existent dans prompts-opus.md ; les 5 emplacements [Figure: …] du post correspondent) ;
le post AF est autoporteur (toutes les maths inline, chiffres tracés — 19 checks, 0.64±0.13,
τ*≈0.92, ρ*≈0.97 — tous conformes aux sources) ; les mails sont cohérents avec le post et
n'affirment rien que le repo ne soutient. Biblio : 10/10 vérifiées, 0 introuvable ; les
références du papier recoupent docs/biblio-verification.md.

---

## Corrections appliquées vs escaladées

**Appliquée (1)** — branche `audit-fix/gamma-zero-edge`, commit `ddfb42a` : le bord γ=0
(m13) dans model-notes.md, paper.md, af-post-minimal-model.md. Non pushée, à merger par
Mathieu.

**Escaladées (tout le reste)** — non triviales ou touchant du contenu gelé : M1-M4, m5-m12,
et la note sur predictions.md:17. Priorité suggérée : M2 (script e3conf) → M3 (requalifier la
phrase « lateness » dans paper §5.3 + af-post) → M4 (étape 0 checklist) → M1/m5 (seeds) →
m7 (README) avant le repo public.

**Non touchés, conformément au mandat** : predictions.md, tous les tests, les figures
(régénérées transitoirement pour comparaison puis restaurées via `git checkout`),
GATES, aucun push.

---

## MISE À JOUR post-audit (même session, sur mandat de Mathieu)

Mathieu a levé le gel des corrections après lecture du rapport. État révisé :

- **M4 — clos hors repo** : Mathieu indique avoir exécuté lui-même la vérification croisée
  hors famille Claude (étape 0 de la checklist) avec concordance, sans en committer la trace.
  Décision : on n'en revendique rien de plus que ce que le post dit déjà (« four ways »,
  toutes intra-famille) ; une ligne au journal de vérification de model-notes reste
  souhaitable si la date et le modèle tiers sont retrouvés.
- **m13 — mergé** : branche `audit-fix/gamma-zero-edge` dans master.
- **M2 — corrigé** : `--exp e3conf` ajouté à `production_v1.py` (protocole exact E3.9-E3.11 :
  seeds 100-109, t_leg=600, verdicts imprimés, données `results/e3_confirmation.npz`) ;
  run de re-vérification consigné dans l'addendum de notes-production-v1.
- **M1/m5 — corrigés** : seeds densifiés commis en défauts (E1/E4 : 30 ; E2/E2b : 10),
  figures régénérées depuis ce code, texte du papier aligné (abstract + en-tête §5).
- **M3 — corrigé** : requalification « lateness » dans paper §5.3 et le post AF, adossée au
  script commité `sim/analysis/static_demand_map.py` (re-dérivation indépendante des bandes
  du sous-agent, reproduites au centième : aucune en linéaire ; [0.06, 0.84] à K=0.5, n=8 ;
  [0.93, 2.71] à K=0.05).
- **m10 — corrigé** : E4.1 et E5.3 requalifiées dans le papier en checks de cohérence
  d'implémentation.
- **m7 — corrigé** : README réécrit (statut à jour, claim « configs versionnées » remplacé
  par l'état réel, note sur les docs en français).
- **Décision repo (post force-push d'identité)** : Mathieu garde le repo GitHub actuel pour
  la publication, en connaissance du résidu (anciens commits accessibles par SHA côté
  GitHub). Risque accepté.
- **Traduction** : recommandation rendue — traduire seulement la chaîne de preuve
  (notes-production-v1, les deux revues adversariales, decisions.md) en `.en.md` à côté des
  originaux, verbatim, par un agent séparé ; le reste demeure en français.
- **Restent ouverts** : m6 (extraction YAML), m8 (ablation du plafond de richesse), m9
  (biais O(dt) du signal d'entrée), m11 (défense d'une ligne du π net-de-taxe en §7), m12
  (tolérance V1 à 45 % sur un point), n16-n19.

---

## Résumé en français simple (ce que je changerais avant publication)

1. **Rends le chiffre-clé refabricable** : le « 0.64 ± 0.13 » de l'irréversibilité n'a aujourd'hui aucun script — ajoute la commande qui le régénère, sinon c'est parole contre parole.
2. **Adoucis une phrase** : « seule une demande tardive crée le piège » va plus loin que ta mesure ; dis « dans le régime proche de l'exclusion que nous mesurons » — ton résultat principal, lui, est solide (on l'a re-vérifié par un calcul indépendant).
3. **Fais l'étape 0 de ta checklist** (coller le pack de vérification dans GPT/Gemini) AVANT de publier : c'est ta seule vérification hors famille Claude, et elle n'a jamais été faite.
4. **Aligne code, figures et texte sur les seeds** (le papier dit 3-10, les figures en montrent 30) et mets à jour le README avant de rendre le repo public.
5. Merge la petite correction mathématique (cas limite γ=0) que j'ai laissée sur la branche `audit-fix/gamma-zero-edge`.
