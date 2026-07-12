# T1.2 — Brouillons de mails (à envoyer par Mathieu)

> Deux mails courts, personnalisés, en anglais. **Avant d'envoyer : publie le post AF (`paper/af-post-minimal-model.md`) et remplace `[AF-POST-LINK]` par son URL** — un lien vers un post public vaut mieux qu'une pièce jointe (et si tu n'as pas encore publié, garde la pièce jointe `docs/pi-definition.en.md` en PDF/gist et supprime la phrase du lien). Envoie tel quel ou ajuste le ton — mais **n'allonge pas** : les chercheurs répondent aux mails courts avec une question précise. Adresses : cherche leurs pages personnelles (Kulveit : ACS Research Prague ; Drago & Laine : Workshop Labs / leurs Substacks acceptent les DM).

---

## Mail 1 — Jan Kulveit (ACS Research, Prague)

**Subject:** Formalizing gradual disempowerment — feedback on a participation index?

Hi Jan,

I'm an independent developer working on what I believe is a missing piece downstream of your Gradual Disempowerment paper: a formal multi-agent model of the economic channel — the economy as a stream of profit opportunities captured competitively by human agents and AI operators, with closed-form exclusion thresholds and first simulation results (phase boundary, coexistence region, and a demand-side irreversibility condition). I've just written it up here: [AF-POST-LINK]

In the interest of full disclosure: I'm an embedded-systems engineer, not an economist, and I built this with heavy AI assistance — the model, derivations and code, under my direction and independently cross-checked several ways. That's a large part of why I'd value a domain expert's eye on it, and on one design choice in particular: the operational definition of a "human economic participation index" (π) that the whole model rests on — 2 pages attached. The specific question is the two-channel accounting at the end (§7): the demand side treats all human income as source-agnostic (a dividend spent = a wage spent), while the headline index counts only *self-enforcing* participation — passive capital income is tracked but excluded, on the grounds that a claim enforced by institutions is only as secure as the institutions' alignment, which is the variable under study. Does that split seem right to you? And does this overlap with anything already in progress in your group's "concrete research projects" list?

Any pointer, even one line, would be very useful.

Best,
Mathieu [nom complet]

---

## Mail 2 — Luke Drago & Rudolf Laine (Workshop Labs)

**Subject:** A formal model of the intelligence curse's economic mechanism — quick sanity check?

Hi Luke, hi Rudolf,

The Intelligence Curse describes powerful actors losing their incentive to invest in people. I'm an independent developer trying to formalize the micro-mechanism underneath: a multi-agent model where profit opportunities ("gradients") are captured in a race between human agents and AI operators whose capability compounds with reinvested income. First results (closed-form exclusion threshold, phase diagram matching it exactly, and a finding on when exclusion becomes irreversible) are written up here: [AF-POST-LINK]

Full disclosure: I'm an embedded-systems engineer, not an economist, and this was built with heavy AI assistance under my direction (and cross-checked several independent ways) — which is exactly why a sanity check from your side would help. Attached (2 pages): the operational definition of the participation index the model tracks. If you have 10 minutes, I'd value your read on it — especially the two-channel split at the end (§7): demand counts all human income regardless of source, but the headline index counts only self-enforcing participation, so passive AI-capital income is tracked separately rather than counted as "being in the loop". That seemed consistent with your rentier framing — a rentier's claim is only as good as the institutions enforcing it — but it is the design choice I'm least certain about.

Happy to share the model notes as they mature.

Best,
Mathieu [nom complet]

---

*Après envoi : cocher T1.2 dans PLAN.md, noter les dates d'envoi ici. Les réponses ne sont pas bloquantes.*
