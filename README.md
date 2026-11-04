# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. Receives text and creator_id from /submit endpoint
2. Sends text to detector.model_signal, adds model_score from this signal call
3. Sends text to stylometry.style_signal, add style_score from this signal call
4. Sends both score to scoring.combine_signals, add confidence value from combined score
5. Sends combined score to scoring.score_to_label, add guess and label from combined score
6. Sends all of the information above to audit.log_decision, adds nothing, logs the submission

---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**

This measures how predictable the words used are.

**Why that might differ between human and AI writing:**

AI models uses probability to pick the next word so the text it writes are likely to be predictable where a human can use odd choices, go off on a tangent, use slangs.

**What it can't see:**

It can't see humans writers that write predictable words such as a foreigner/ESL using easier common words and strict semantics/grammar.

### Signal two — the style signal

**What it measures:**

This measures sentence length spread, unique word ratio, and punctuation density.

**Why that might differ between human and AI writing:**

AI models tend to write uniform, common repeating words choice where a human are less consistent on sentence length and punctuation, and using more unique/odd word choices due to pop culture or learning enivornments.

**What it can't see:**

It can't see edge cases/noises in each of these 3 metrics because it lacks context. I.E long research papers can have more repeating words.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**

Weighted average of the two scores, with 50% model and 50% style.

**The numbers:**

Model AI Score: 0.50
Style AI Score: 0.50

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**

 If there is a difference of 30% or more between model and style score, use a adjusted weighted average of 80% model and 20% style.

 Signal Split: Model Score - Style Score > 0.30
Model AI Score: 0.80
Style AI Score: 0.20

---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0 - 0.35 | This text has writing patterns common to AI-generated models. |
| unsure | 0.35 - 0.65 | This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person. |
| high-confidence AI | 0.65 - 1 | This text has distinct writing patterns written by a person. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

Simple and focus on the system not being able to make a determination.

---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json

```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json

```

---

## How I Used AI

**Moment 1**

- *What I asked for:*

My system allows this rate of wrongly flagging human writing as AI-generated, 2/10. Write the message a real writer would send me if they were one of the people that rate allows. Don't tell me whether my number is right.

- *What came back:*

Subject: Quick note on the flag

Hi,

I saw that my draft came back flagged as AI-generated. I wrote it myself, start to finish, over a couple of evenings last week. I can send you the Google Doc with its version history so you can see the drafts building up, along with my notes and the two earlier outlines I scrapped.

I know detectors aren’t perfect, and I’d guess some of the flagged passages are just the ones where I was trying to be clear and direct. I tend to write in short, tidy sentences, and that seems to be what trips these tools.

If it would help, I’m happy to talk through any section with you, explain why I made particular choices, or rewrite a paragraph live. I’d like to get this sorted out, so just tell me what you need from me.

Thanks for taking a look,
Dana

- *What I changed:*

Nothing.

**Moment 2**

- *What I asked for:*

Here are three labels a website might show on something I wrote. For each one, tell me what I would think it is saying about me and what I would do next. Answer as the writer, not as an engineer. Don't rewrite the labels.

1. This text was likely written by an AI model.
2. This text was likely written by a person.
3. The system cannot determine whether this text is written by AI model or a person.

- *What came back:*

**1. "This text was likely written by an AI model."**

You'd read this as an accusation, even though the word "likely" is in there. Your first reaction is probably a flash of defensiveness or embarrassment: *I wrote this. Does it sound robotic? What did I do wrong?* If you really did write it yourself, it feels like being called a liar by a machine that can't see you work. If you did use AI, you might feel caught, or wonder whether it's a problem.

What you do next depends on the stakes. If a teacher, editor, or client is going to see that label, you'd probably start gathering proof: version history, drafts, notes. You might also start rewriting to sound "more human," which usually means roughening your own style until the label goes away. Some people would just stop trusting the tool, or stop using the site.

**2. "This text was likely written by a person."**

You'd take this as a pass, and maybe a small compliment. There's relief if you were worried about being flagged, and mild satisfaction if you worked hard on the writing. You'd probably do nothing more with it. You'd keep going, submit it, or post it.

Two other reactions are possible. If you did use AI and got this label anyway, you might feel like you got away with something, and you'd start to wonder how much the label can be trusted. Or if you're a careful writer, you might wonder what the label is based on and whether it would hold up if challenged. "Likely" also leaves you slightly unsure whether it counts as a verdict.

**3. "The system cannot determine whether this text is written by AI model or a person."**

This is the most frustrating one. It doesn't clear you and it doesn't accuse you, so it doesn't help you at all. You'd probably think: *So what am I supposed to do with that?* You might feel a little suspicious, like being waved through security with a shrug, because anyone looking at it could take it either way.

Your next step is unclear, and that's the problem. Some people would shrug and move on. Others would worry the ambiguity will be read against them, since a reader who sees "can't determine" may assume the worst. You might edit the text to try to tip it toward "person," or you might wonder whether your writing is just plain or generic. Many people would also decide the tool is useless, since it didn't tell them anything they could act on.

**What the three share:** the writer's reaction is mostly about *what happens to them next*, not about the text itself. Labels 1 and 3 especially leave you without a way to respond, whether that's disputing the result, understanding it, or fixing anything. That's why people tend to respond by guessing at the system's rules instead of just writing normally.

- *What I changed:*

New labels:
AI: This text has writing patterns common to AI-generated models.
Human: This text has distinct writing patterns written by a person.
Unsure: This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
