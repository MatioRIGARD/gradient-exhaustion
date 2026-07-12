# Pack de vérification croisée (pour Mathieu — aucune compétence math requise)

> **But** : faire dériver le modèle à l'aveugle par un modèle d'IA d'une AUTRE famille que Claude (GPT, Gemini, DeepSeek…), pour éliminer l'hypothèse « erreurs corrélées entre instances Claude ». **Mode d'emploi** : (1) colle la PARTIE A telle quelle dans le modèle tiers, sans rien d'autre ; (2) compare sa réponse à la grille de la PARTIE B, symbole à symbole ; (3) tout écart → colle la transcription complète dans une session Opus avec : « Compare cette dérivation à paper/model-notes.md §2-3, identifie qui a raison, explique-moi en français simple. » Concordance = un check indépendant de plus (à noter dans le journal de vérification de model-notes.md). Fais-le idéalement avec DEUX modèles tiers différents.

---

## PARTIE A — à coller telle quelle dans le modèle tiers

You are a careful applied mathematician / economic theorist. Derive everything from scratch, showing your work. Simplify expressions fully.

**The model.** Time is continuous.
- Profit opportunities arrive as a Poisson process with rate g > 0. Each is worth v > 0 to whoever captures it first. An uncaptured opportunity expires at rate θ > 0 (exponential lifetime).
- Human agents: an unbounded pool of identical potential participants. A participating human pays flow cost c_h > 0 and detects any given live opportunity at Poisson rate μ_h > 0 (independent across opportunities and agents). Free entry and exit, outside option 0: humans participate while expected net flow income is positive; participation adjusts fast relative to any other dynamics.
- AI side: an aggregate detection intensity Λ_a ≥ 0 competing in the same races.
- The first detector of a live opportunity captures its value v. With total human intensity Λ_h = n_h·μ_h, all detection/expiry clocks are independent exponentials.

**Questions.**
1. For fixed Λ_a: derive the stationary free-entry level Λ_h*(Λ_a), the income flows κ_h and κ_a, and the human share π = κ_h/(κ_h+κ_a). Describe exactly how each behaves as Λ_a rises, including any critical values.
2. Let dΛ_a/dt = η·κ_a − δ·Λ_a (η, δ > 0), humans always at their fast free-entry response. Under what exact parameter condition does Λ_a grow vs decay while humans participate? If it grows, what happens and in what time? What are the long-run attractors?
3. Make v endogenous: v = v_hi while humans participate at free-entry scale, v = β·v_hi (0 < β < 1) when humans are fully excluded. Ramp Λ_a slowly up then down: is the system reversible? Compute the threshold(s) and the size of any irreversibility as a function of β.
4. Sanity: (a) Λ_a = 0; (b) Λ_a frozen with η = 0; (c) replace the AI by a second identical free-entry human population — does any population get excluded in each case?

---

## PARTIE B — grille de correction (NE PAS montrer au modèle tiers avant sa réponse)

Le modèle tiers doit retrouver (notations équivalentes acceptées ; seul le contenu compte) :

| # | Quantité | Réponse attendue |
|---|---|---|
| 1a | Niveau d'entrée libre | Λ_h* = max(0, g·v·μ_h/c_h − θ − Λ_a) — décroît **linéairement**, atteint 0 exactement à Λ̄ = g·v·μ_h/c_h − θ |
| 1b | Revenus (régime intérieur) | κ_h = g·v − (θ+Λ_a)·c_h/μ_h (linéaire ↓) ; κ_a = Λ_a·c_h/μ_h (linéaire ↑) ; total constant |
| 1c | Part humaine | π = 1 − Λ_a/Λ̄ (exactement linéaire), π = 0 au-delà de Λ̄ |
| 2a | Condition de croissance | croissance ssi **η·c_h/μ_h > δ** (sinon Λ_a → 0 et π → 1) |
| 2b | Temps d'exclusion | t* = ln(Λ̄/Λ_a(0)) / (η·c_h/μ_h − δ), fini |
| 2c | Attracteur post-exclusion | Λ_a** = η·g·v/δ − θ, avec Λ_a** > Λ̄ ⟺ condition 2a (exclusion absorbante) |
| 3a | Seuils d'hystérésis | sortie à Λ̄(v_hi) = g·v_hi·μ_h/c_h − θ ; ré-entrée à β·g·v_hi·μ_h/c_h − θ |
| 3b | Largeur du piège | (1−β)·g·v_hi·μ_h/c_h ; **piège permanent si β < θ·c_h/(g·v_hi·μ_h)** |
| 4 | Sanity | (a) et (b) : coexistence stable, aucune exclusion ; (c) : aucune population éliminée (partage indéterminé) — l'exclusion exige le canal d'accumulation |

**Verdict à consigner** : si 1a-1c, 2a-2c et 4 concordent → le cœur (§2-3 du papier) est validé par une famille de modèles indépendante. 3a-3b concordants → le §4 aussi. Tout écart → session Opus pour arbitrage (voir mode d'emploi).
