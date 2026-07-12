# Prompts prêts à l'emploi pour les sessions Opus

> Copie-colle tel quel, un prompt par session, `/clear` entre deux. Chaque prompt est autonome (l'agent retrouve tout dans le repo). Si l'agent pose une question d'arbitrage : réponds « applique docs/decisions.md et continue ».

---

## P1 — Reprendre le fil (à utiliser en début de toute session floue)

> Lis CLAUDE.md, PLAN.md (section « État d'avancement ») et docs/decisions.md. Dis-moi en 5 lignes où en est le projet et quelle est la prochaine tâche recommandée. N'exécute rien encore.

## P2 — Exécuter une tâche du plan

> Lis CLAUDE.md et PLAN.md, puis exécute la tâche **T&lt;ID&gt;** exactement selon ses critères d'acceptation. Une seule tâche. À la fin : lance `make ci`, committe si vert, et donne-moi un résumé en français simple (5-10 lignes) : ce qui est fait, ce qui a été décidé (DEC-00N le cas échéant), ce qui reste.

## P3 — Interpréter des résultats d'expérience (à utiliser après chaque E1-E6)

> Lis paper/predictions.md et le dossier de résultats de l'expérience E&lt;N&gt;. Rends un verdict CONFIRMÉ / INFIRMÉ / PARTIEL pour chaque prédiction numérotée de cette expérience, en citant les chiffres. Puis explique-moi en français simple, sans jargon (je ne suis pas économiste) : qu'est-ce que ça veut dire pour la thèse du papier, et qu'est-ce que ça change à la suite ? Si un résultat INFIRME une prédiction : ne corrige RIEN dans le modèle — documente l'écart dans le fichier d'analyse de l'expérience et propose-moi 2 explications candidates.

## P4 — Interpréter une réponse de chercheur (mails T1.2)

> Voici la réponse de &lt;NOM&gt; à mon mail (collée ci-dessous). Contexte : docs/outreach-emails.md (mon mail), docs/pi-definition.md et paper/model-notes.md (ce sur quoi je demandais un avis). Explique-moi en français simple : (1) ce qu'il/elle dit vraiment, point par point ; (2) ce qui est une critique à prendre au sérieux vs une remarque de forme ; (3) ce que ça change à notre plan, le cas échéant (référence PLAN.md) ; (4) un brouillon de réponse courte en anglais, dans le même ton que le mail d'origine. Ne modifie aucun fichier sans mon accord, sauf pour consigner les critiques importantes dans paper/model-notes.md §5 (audit) si elles sont nouvelles.
>
> --- RÉPONSE REÇUE ---
> [coller ici]

## P5 — Post court Alignment Forum (après GATE 2)

> Lis paper/model-notes.md (avec son journal de vérification), paper/adversarial-review-model.md, docs/pi-definition.md et docs/background.md §3. Rédige `paper/af-post-minimal-model.md` : un post Alignment Forum court (~1500-2500 mots) en anglais présentant le modèle minimal. Structure : le gap (gradual disempowerment sans modèle formel) ; le modèle en langage simple + les 4 résultats (seuil, déclin linéaire, critère γ, hystérésis par la demande) ; les hypothèses porteuses A7/A9 présentées comme LA question ouverte, pas comme un détail ; ce qui vient ensuite (ABM, expériences pré-enregistrées — lien vers predictions.md) ; appel à critique. Ton : sobre, falsifiable, zéro sensationnalisme, aucun mot sur les cryptos. Les affirmations doivent rester strictement dans les limites de ce qui est dérivé et vérifié. Je relirai avant publication.

## P6 — Suite de la phase 3 (rationalités et stratégies)

> Lis CLAUDE.md, PLAN.md et docs/simulation-architecture.md §2.4-2.6, puis exécute T3.7 (trois niveaux de rationalité interchangeables derrière une interface commune ; les tests V1-V3 doivent passer avec chacun). Attention : le niveau « réplicateur » actuel est l'implémentation entry/exit existante dans sim/core/agents.py — il s'agit de la factoriser derrière l'interface, pas de la réécrire. Committe si `make ci` vert. Ensuite STOP (T3.8 sera une autre session).

## P7 — Lancer une expérience de production

> Lis PLAN.md (phase 4), paper/predictions.md et docs/simulation-architecture.md §3.2. Exécute T4.&lt;N&gt; : écris la config YAML dans sim/experiments/configs/, implémente ce qui manque du runner (multi-seeds n≥30, IC systématiques, résultats horodatés + config embarquée), lance les runs, produis la figure F&lt;N&gt; et une note d'analyse avec le verdict vs predictions.md (format du prompt P3). Committe le tout. Ne lance JAMAIS une expérience dont la prédiction n'est pas déjà dans predictions.md — si elle n'y est pas, demande-moi d'abord.

## Règle de décision pour toi (Mathieu)

- L'agent te propose quelque chose qui **change le périmètre, le positionnement public, ou contredit une GATE** → refuse et demande-lui de s'en tenir à PLAN.md.
- L'agent rend un verdict INFIRMÉ → c'est normal et intéressant : demande P3 point (4), les deux explications candidates, et on en reparle ensemble à la session suivante.
- Tu ne comprends pas une sortie → « explique-moi ça comme à un développeur qui n'a jamais fait d'économie, avec une analogie logicielle ».
