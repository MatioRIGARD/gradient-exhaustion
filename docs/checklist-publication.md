# Checklist de publication — actions de Mathieu, dans l'ordre

> Écrit le 13/07/2026 au soir. Fable indisponible après le 14/07 14h ; tout ce qui suit est exécutable sans lui (les prompts Opus sont fournis). Cocher au fur et à mesure.

## Étape 0 — Vérification croisée (ce soir ou demain matin, ~20 min)

- [ ] Ouvre `docs/verification-pack.md`. Colle la **Partie A** telle quelle dans un modèle non-Claude (GPT, Gemini…). Compare sa réponse à la grille **Partie B**, ligne par ligne.
- [ ] Idéalement, refais-le avec un second modèle d'une autre famille.
- [ ] Concordance → note-le (une ligne dans le journal de vérification de `paper/model-notes.md`, ou demande à Opus). Écart → colle la transcription dans Opus : *« Compare cette dérivation à paper/model-notes.md §2-3, identifie qui a raison, explique-moi en français simple. »*

## Étape 1 — Relecture du post (~30-45 min)

- [ ] Fichier : `paper/af-post-minimal-model.md` (~2600 mots). Si besoin, prompt Opus :
  > Lis paper/af-post-minimal-model.md et traduis-le moi en français simple, section par section. Signale : (a) toute affirmation qui te semble plus forte que ce que paper/model-notes.md et sim/analysis/notes-production-v1.md justifient ; (b) tout ce qu'un commentateur hostile attaquerait en premier.
- [ ] Ton droit de veto porte sur : le titre, le ton, toute phrase que tu ne te sens pas capable d'assumer en commentaire.

## Étape 2 — Compte et publication (~30 min)

- [ ] **Crée un compte sur LessWrong** (lesswrong.com) dès maintenant — les nouveaux comptes passent par une modération légère, autant lancer l'horloge. (L'Alignment Forum est sur invitation ; la voie normale : publier sur LessWrong avec les tags IA, les modérateurs promeuvent vers l'AF si pertinent. Le post est écrit pour ce public.)
- [ ] Nouveau post → colle le markdown du fichier. Les maths `$...$` sont supportées (activer l'éditeur markdown dans les settings du compte).
- [ ] Aux 5 emplacements `[Figure: fX_….png]` : upload l'image correspondante depuis `paper/figures/`.
- [ ] Tags suggérés : AI, AI Risk, Economics. Titre : celui du fichier.
- [ ] Publie. **Copie l'URL.**

## Étape 3 — Les mails (~10 min)

- [ ] Dans `docs/outreach-emails.md` : remplace les 3 occurrences de `[AF-POST-LINK]` par l'URL.
- [ ] Envoie le mail 1 (Kulveit) et le mail 2 (Drago & Laine). Adresses : leurs pages personnelles / Substack DM.
- [ ] Note la date d'envoi dans le fichier.

## Étape 4 — Repo public (~10 min, peut attendre un jour ou deux)

- [ ] `gh auth login` puis, depuis `~/workspace/gradient-exhaustion` :
  `gh repo create gradient-exhaustion --public --source=. --push`
- [ ] Ajoute l'URL du repo en commentaire du post (ou édite le post pour le lier).

## Étape 5 — Après publication (routine Opus, une tâche par session)

- [ ] Chaque réponse de chercheur / commentaire substantiel → prompt **P4** de `docs/prompts-opus.md` (il te traduit, trie, et draft la réponse).
- [ ] Chaque résultat d'expérience restante → prompt **P3**.
- [ ] File d'attente des tâches restantes (aucune ne bloque quoi que ce soit) : relecture du papier long (voir ci-dessous), E3.8, E6 retravaillé, calibration du niveau learning, balayage β×K, E7 (juridictions), conversion LaTeX (T5.4 : installer pandoc — `sudo apt install pandoc` — ou faire faire à Opus), soumission arXiv (T5.5, après retours sur le post ; l'endorsement peut se demander à Kulveit/Laine s'ils ont répondu).

## Papier long (T5.1) — état

Le draft complet de `paper/paper.md` a été rédigé dans la nuit du 13 au 14/07 (agent) puis relu par Fable et passé au référé hostile (T5.2) si le temps l'a permis — **vérifier l'état d'avancement dans les derniers commits (`git log --oneline -5`)**. C'est le candidat arXiv ; il attend tes retours après la publication du post, pas avant.

## Rappels

- Le repo est la mémoire : toute décision → `docs/decisions.md`, tout résultat → note d'analyse committée.
- Personne ne te demande de certifier les maths : le post EST une demande de vérification, et la pile (4 vérifications internes + vérification croisée inter-modèles + publication) est au-dessus des standards du genre.
