# Définition de l'indice π — participation économique humaine (T1.1)

> Draft de travail (🤖+👤). Traite explicitement **Q2** (la demande humaine est-elle porteuse ?) et **Q3** (qu'est-ce qui compte comme « humain dans la boucle » et comment le mesurer ?) de `docs/research-program.md` §2. Objectif : **une** définition opérationnelle de π, calculable dans le modèle *et* approximable dans des données réelles, avec tous les cas ambigus tranchés. Le §7 liste le seul arbitrage de fond que je te laisse confirmer. Langue : français (le doc sera traduit en anglais pour la relecture externe, T1.2).

---

## 1. Principe directeur (trois décisions de conception)

π mesure **la part du *flux* économique qui passe par des humains en tant qu'agents économiques**. Trois choix fixent tout le reste :

1. **Un flux, pas un stock, pas une tête.** π est une part de *valeur qui circule par unité de temps* (revenus), pas une part de richesse accumulée, pas une fraction de population. Le diagnostic D1 porte sur la *boucle* économique (qui capte les gradients, qui décide, qui travaille), pas sur qui détient un patrimoine hérité ni sur combien d'humains sont nominalement « actifs ».
2. **Attribution au demandeur résiduel (residual claimant), pas à l'outil.** Un revenu est « humain » si c'est un **agent humain** qui en est le bénéficiaire résiduel et qui porte le coût de participation — quel que soit l'outil (y compris une IA) qu'il utilise. Un humain qui *loue* de la capacité IA reste humain ; c'est la **marge nette** qu'il conserve qui est comptée côté humain, la redevance versée à l'opérateur étant comptée côté IA (cf. §4, cas « humain assisté »).
3. **Un ratio, robuste au sort de la demande.** π est une *part* (numérateur/dénominateur), délibérément. Ainsi π est bien défini que le flux total Y s'effondre (crise de réalisation de Korinek) ou se maintienne via une demande inter-IA autoporteuse (Q2a). Le sort de Y est un *paramètre du modèle* (part de la demande émanant des opérateurs), pas un ingrédient de la définition de π.

**Garde-fou anti-tautologie.** « Humain » et « IA » ne désignent dans le modèle que deux **jeux de paramètres** (latence, coût d'information, plafond de capacité, vitesse d'apprentissage), jamais des règles spéciales. Rien dans la définition de π ne force π_humain > 0 ou → 0 : ce sont les paramètres et la dynamique qui décident.

---

## 2. Canaux de valeur et définition formelle

À chaque pas de temps, le modèle produit un flux de valeur captée. On le ventile par **bénéficiaire** (humains `h` / opérateurs IA `a`) et par **canal** :

| Canal | Symbole (humains) | Description |
|---|---|---|
| **Capture** | κ_h | revenu tiré de la saisie de gradients « ouverts » (arbitrage, entrepreneuriat, décision d'allocation) |
| **Travail** | λ_h | capture des gradients étiquetés « exigent une présence humaine » — fraction non automatisable, **décroissante et endogène** (l'IA peut finir par les capter aussi : λ_a ≥ 0, aucune protection ad hoc) |
| **Transferts** | T_h | redistribution politique : UBI, impôt→transfert |
| **Capital passif** | R_h | dividendes/rente versés à des humains qui n'opèrent pas — **série de sortie séparée**, hors des indices de tête (DEC-001) |

Notations agrégées : revenu **gagné** (pré-transfert) humain `E_h = κ_h + λ_h`, IA `E_a = κ_a + λ_a` ; flux gagné total `E = E_h + E_a`. Les transferts redistribuent E sans le créer (le flux total post-transfert reste E).

**Indice de marché (earned) :**
$$\pi_{\text{marché}} = \frac{E_h}{E} = \frac{\kappa_h + \lambda_h}{\kappa_h + \lambda_h + \kappa_a + \lambda_a}$$
→ part du revenu **gagné** qui revient aux humains. C'est l'indice principal, celui dont on étudie la dynamique (F1) et les seuils (F2/F3).

**Indice total (livelihood) :**
$$\pi_{\text{total}} = \frac{E_h + T_h}{E} = \frac{\kappa_h + \lambda_h + T_h}{E}$$
→ part du flux qui **soutient** des humains une fois comptés redistribution et claims passifs.

**Écart de perfusion :**
$$\Delta = \pi_{\text{total}} - \pi_{\text{marché}} = \frac{T_h}{E}$$
→ **c'est lui-même un résultat, pas un déchet de calcul** : la part de la subsistance humaine qui n'est plus *gagnée dans la boucle* mais *versée hors boucle* par redistribution. Un régime « π_marché → 0, π_total élevé, Δ grand » est précisément la fin de partie du diagnostic : *les humains ne vivent plus que de perfusion*, hors de la boucle productive.

**Série de capital passif (séparée, DEC-001) :**
$$\rho = \frac{R_h}{E}$$
→ part du flux versée à des humains **propriétaires mais non opérants** (rente de capital IA). Reportée **à part** dans chaque expérience : elle n'entre ni dans π_marché ni dans Δ, pour laisser **les indices de tête inchangés** tout en gardant analysable la question « la propriété du capital IA protège-t-elle ? ». Lecture étendue disponible si on veut la tester : π_total⁺ = π_total + ρ (jamais l'indice par défaut).

Ces grandeurs sont des **ratios de compteurs tenus par le simulateur** → calculables sans ambiguïté et reproductibles (critère « calculable dans le modèle » ✔).

---

## 3. Traitement de Q2 et Q3

**Q2 — la demande humaine est-elle porteuse ou décorative ?**
- (a) *Demande inter-IA autoporteuse ?* Traitée comme **paramètre du modèle** (part de la demande finale émanant des opérateurs, §2.3 de l'archi), pas comme définition. π étant un ratio (décision §1.3), il reste interprétable dans les deux régimes : si la demande inter-IA soutient Y malgré des revenus humains nuls, alors « π_marché → 0 » est un état *stable* et non auto-corrigé — ce qui est justement le point. La définition n'a donc pas à trancher Q2a ; elle doit seulement y être **robuste**, ce que le choix du ratio garantit.
- (b) *UBI = dans la boucle ou perfusion ?* **Tranché** : la redistribution est le canal T, comptée dans **π_total uniquement**, jamais dans π_marché. On ne choisit pas entre les deux lectures — on **rapporte les deux** et l'écart Δ mesure explicitement la « perfusion ». (Voir §4.)

**Q3 — qu'est-ce qui compte comme « humain dans la boucle » et comment le mesurer ?**
- *Ce qui compte* : la **participation active** = capture (κ_h) + travail (λ_h). Détenir un patrimoine ou toucher un transfert n'est pas participer (→ canal T, π_total). Décider/arbitrer/entreprendre/travailler, oui (→ E_h, π_marché).
- *Comment le mesurer* : par ratios de flux (§2) dans le modèle ; par un indice construit à partir de proxys dans les données réelles (§5).
- π_marché **est** la « variable d'état centrale » que Q3 réclame. Un indicateur secondaire de *décision* (part des événements de capture initiés par des agents humains) est conservé comme diagnostic complémentaire mais **pas** comme π principal (raison en §6, alternative rejetée n°3).

---

## 4. Cas ambigus — tous tranchés

| Cas | Décision | Où il tombe | Signature attendue |
|---|---|---|---|
| **UBI / redistribution** | Revenu non gagné dans la boucle → canal T | π_total seulement (dans Δ) | π_marché↓ mais π_total soutenu, Δ↑ = économie de perfusion |
| **Humain assisté par IA** (« centaure ») | Attribué au demandeur résiduel humain. Modélisé comme agent humain louant de la capacité : sa **marge nette** (valeur − redevance) est κ_h ; la redevance est κ_a | π_marché (la marge) + π_marché IA (la redevance) | quand les opérateurs captent tout le surplus, la marge humaine → 0 *même si « un humain est impliqué »* — le mécanisme rendu mesurable |
| **Actionnaire passif** (humain vivant de dividendes d'une firme-IA, sans opérer) | Revenu de capital **sans participation** → hors π_marché ; **série séparée ρ** (ni dans π_marché ni dans Δ), DEC-001 | série ρ (indices de tête inchangés) | « classe de rentiers de l'IA » : π_marché→0 alors que ρ reste positif — la série ρ *montre* si posséder protège, au lieu de le décréter |

Le principe unificateur : **on compte la participation, pas la propriété ni la perfusion.** Un euro n'entre dans π_marché que s'il est *gagné* par un agent humain qui capte un gradient ou fournit du travail.

---

## 5. Correspondance avec les données réelles (approximabilité)

Aucune source unique ne donne π directement ; π_marché est un **indice construit**. Correspondances :

- **λ_h (travail)** ≈ **labor share** des comptes nationaux (mesurée, en baisse — mais confondue par la mondialisation et le pouvoir de marché, cf. De Loecker & Eeckhout ; d'où l'insuffisance de la seule labor share, §6-1).
- **κ_h (capture/entrepreneuriat humain)** ≈ revenu des indépendants + valeur créée par les nouvelles firmes fondées et opérées *sans IA frontale* ; **laboratoire le plus pur** : gains mission par mission sur les plateformes de freelance avant/après LLM (piste C, jeu 1).
- **Δ (perfusion)** ≈ part des transferts sociaux dans le revenu disponible des ménages + revenu de capital des ménages non tiré d'une activité propre.
- **Proxy de décision** ≈ part des transactions (e-commerce, finance) initiées par des agents autonomes (piste C, jeu 3) ; `1 −` cette part approxime la décision humaine.

Une sous-économie (une plateforme freelance) fournit un π_marché sectoriel calculable mission par mission : c'est l'instanciation empirique la plus propre pour la piste C.

---

## 6. Trois définitions alternatives rejetées

1. **Labor share seule** (π := revenu du travail / revenu national). *Rejetée* : (a) ignore la capture/l'entrepreneuriat humains (κ_h), pourtant au cœur de D1 — un monde où les humains ne gagnent rien en salaire mais captent encore des gradients comme entrepreneurs n'est pas un désempowerment ; (b) la labor share décline déjà pour des raisons étrangères à l'IA (pouvoir de marché), donc elle *confond*. On la garde comme **proxy empirique de λ_h**, pas comme π.
2. **Taux d'emploi / part de population active** (π := fraction d'humains employés). *Rejetée* : c'est le cadrage « population » que le programme abandonne explicitement (background §2.4). On peut « employer » des humains dans du make-work pendant que toute la valeur allocative file vers l'IA ; inversement une poignée d'humains peut capter énormément. π doit être une part de **flux de valeur**, pas une tête.
3. **Part des droits de décision** (π := fraction des décisions d'allocation prises par des humains). *Rejetée comme définition principale* : conceptuellement la plus pure, mais **non mesurée et mal définie** (qu'est-ce qu'« une décision » ? comment la pondérer ?) — inapproximable dans les données et ambiguë dans le modèle. On choisit la **calculabilité** : elle survit comme *indicateur secondaire* (part des captures initiées par des humains), pas comme π.

*(Variante voisine également écartée : la **part de richesse** détenue par des humains — un stock, pas un flux ; un rentier détient un stock tout en apportant zéro au flux de la boucle. On mesure le flux.)*

---

## 7. Arbitrage tranché (DEC-001, affiné par DEC-002)

**L'actionnaire passif** est traité « hors boucle » : le revenu de capital passif est **hors de π_marché** et **reporté en série séparée ρ** (ni fusionné dans Δ, ni dans les indices de tête). La question « la propriété du capital IA protège-t-elle ? » reste ainsi analysable dans les figures (série ρ, lecture étendue π_total⁺) sans charger la définition. Décision et justification complètes : `docs/decisions.md` → DEC-001.

**Affinement DEC-002 (objection de Mathieu, intégrée)** : le lien revenu→consommation est indifférent à la source — un dividende dépensé nourrit la demande comme un salaire dépensé. Le modèle en tient compte en séparant deux canaux : **la demande est agnostique à la source** (tout revenu humain disponible — gagné, transféré, ou de capital — l'alimente identiquement, cf. DemandPool à partir de T3.8), tandis que **π mesure le canal participation** : un flux auto-exécutoire (couper un salaire arrête la production) vs un claim qui ne tient que par l'enforcement institutionnel (couper un dividende n'arrête rien). Le dividende garde l'humain économiquement *en vie* (canal demande, mesuré) ; π mesure s'il reste *nécessaire* (canal participation, indice de tête). La section limites du papier présentera les deux lectures avec la série ρ à l'appui.

---

*Références : `docs/research-program.md` §2 (Q2, Q3), §3 (piste C) ; `docs/simulation-architecture.md` §2.5. Implémentation : `sim/metrics/indices.py` (T3.9), qui doit calculer π_marché, π_total et Δ exactement comme ci-dessus (traçabilité doc ↔ code).*
