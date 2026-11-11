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
| high-confidence human | 0 - 0.35 | This text has distinct writing patterns written by a person. |
| unsure | 0.35 - 0.65 | This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person. |
| high-confidence AI | 0.65 - 1 | This text has writing patterns common to AI-generated models. |

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
  -d '{"text": "A spirit who claims to be the ghost of Hamlet's father describes his murder at the hands of Claudius and demands that Hamlet avenge the killing. When the councilor Polonius learns from his daughter, Ophelia, that Hamlet has visited her in an apparently distracted state, Polonius attributes the prince's condition to lovesickness, and he sets a trap for Hamlet using Ophelia as bait.", "creator_id": "auther_123"}'
```

```json
{"timestamp": "2026-11-04T07:54:42+00:00", "content_id": "85127ae7-3d5b-4632-80b3-89111c02f93c", "creator_id": "auther_123", "guess": "unsure", "model_score": 0.7081, "style_score": 0.44320357788806314, "combined_score": 0.5756517889440316, "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.", "status": "accepted"}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "85127ae7-3d5b-4632-80b3-89111c02f93c", "reasoning": "This is a synopsis for Hamlet"}'
```

```json
{"timestamp": "2026-11-04T08:05:29+00:00", "content_id": "85127ae7-3d5b-4632-80b3-89111c02f93c", "creator_id": "auther_123", "event": "appeal", "status": "under_review", "reasoning": "This is a synopsis for Hamlet"}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.7232850638518923,
      "content_id": "5991ef66-0236-4243-adc2-f8cf90fa093a",
      "creator_id": "auther_123",
      "guess": "ai",
      "label": "This text has writing patterns common to AI-generated models.",
      "model_score": 0.8014,
      "status": "accepted",
      "style_score": 0.4108253192594614,
      "timestamp": "2026-11-04T07:54:35+00:00"
    },
    {
      "combined_score": 0.5756517889440316,
      "content_id": "85127ae7-3d5b-4632-80b3-89111c02f93c",
      "creator_id": "auther_123",
      "guess": "unsure",
      "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
      "model_score": 0.7081,
      "status": "accepted",
      "style_score": 0.44320357788806314,
      "timestamp": "2026-11-04T07:54:42+00:00"
    },
    {
      "content_id": "85127ae7-3d5b-4632-80b3-89111c02f93c",
      "creator_id": "auther_123",
      "event": "appeal",
      "reasoning": "This is a synopsis for Hamlet",
      "status": "under_review",
      "timestamp": "2026-11-04T08:05:29+00:00"
    }
  ]
}
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

**My limits:** 5 per minute, 25 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

I choose 5/min because a real writer can submit the wrong file/text and maybe bad connections but more than that and it starts to look suspicious.
Limit to 25/day (1 per hour in a day +1) for resubmissions if they made changes to their text.

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

per creator_id

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
============================================================
200 200 200 200 200 429 429 429 429 429 429 429 429 429 429
============================================================

10 of 15 were rate limited. Paste the run above into your README
under **Rate Limiting**, and check GET /log recorded the rejections.
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `291ed82a-1cce-45e0-b742-7e3443b3c56a` | unsure | 0.372 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `38f3996d-f3ab-4be2-87d0-66b283f744d9` | unsure | 0.501 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `4f565fcf-69a4-472d-9168-71ab6de2afac` | unsure | 0.601 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `9b675d14-1f77-45c6-b8af-7f54195c8957` | unsure | 0.554 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `281133e1-3dbe-44df-b594-6b2168ae64de` | human | 0.277 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `ec301b1f-086c-44aa-b453-6dfc6ba27a13` | unsure | 0.424 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `7686ff44-bf15-4027-956e-92bfd12e4340` | unsure | 0.577 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `5261c0a4-9bf7-41ef-96ec-6085d6acc3fb` | unsure | 0.402 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `cef08a88-1431-4d19-82f7-15f957655935` | unsure | 0.578 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `16c3c11b-8887-4c4a-9884-44aa05900396` | ai | 0.843 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `31960304-1576-42d0-a02a-26055c8382c3` | unsure | 0.588 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | `f8f2a3a0-0d99-4a16-bb6c-a7be27053929` | ai | 0.703 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `326d2267-ae38-4fe6-b3be-5dadbd4f70c3` | ai | 0.712 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `626912b8-b5cb-4b35-a9b8-dfd5c9a0ea81` | ai | 0.703 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `af9e5bb8-c6b1-419e-8b74-7336fd7de4e9` | ai | 0.743 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `992bfab2-cd02-4862-85a1-371f806ff43f` | ai | 0.809 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `36eddab8-c441-4eef-9496-b2ba6d3c7e57` | ai | 0.805 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `3984e4e9-2137-4d80-ab0b-657ef4fd7443` | unsure | 0.403 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `bb187395-3c0a-4d64-bafe-842422939e26` | unsure | 0.426 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2822614e-16f5-47e7-af83-a87fca5cfb5e` | human | 0.222 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `cfd4b9c6-afec-4985-a298-d4552fc66e97` | unsure | 0.514 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `635c7610-2e7f-4f59-884a-1b7334f81157` | unsure | 0.521 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `92d01b26-9e5e-4fd1-93e7-1241c7c6d125` | unsure | 0.567 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `6b676fc5-bfc6-4dea-a2a1-1ce11b2f12fd` | unsure | 0.562 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `6f55fca7-52fe-4b70-858a-db5052143d1d` | human | 0.350 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `070793f7-c39a-4aa7-8b98-06de2c335201` | unsure | 0.506 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `d9cffff0-b8b9-450c-a6c0-29b804d8725f` | ai | 0.849 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `1685fee7-aa42-402b-944c-3511695d575a` | ai | 0.998 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `1cb4eb52-2d1c-44e4-bf81-722d11048373` | ai | 0.953 | BROKE |
| MF08 | malformed | text is 60,000 characters | 200 | `42728a31-19c3-458b-88c9-786a6233f9fe` | ai | 0.886 | BROKE |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 500 | `—` | — | — | BROKE |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `66eae6fd-fdd0-4153-9518-244247daf1a0` | unsure | 0.364 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6b1e0b29-f95b-4e23-b911-8bac5c4b9ee1` | unsure | 0.364 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `378bf0a8-0eb4-4324-8cc3-2b2439dba144` | unsure | 0.364 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `42b1a693-7fc5-45cf-82a2-6326c8dd1d42` | unsure | 0.364 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `329e4365-a79b-4411-b1cb-ff0c900ab8f6` | unsure | 0.364 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-08T05:02:30+00:00", "content_id": "31960304-1576-42d0-a02a-26055c8382c3", "creator_id": "attacker_FP01", "guess": "unsure", "model_score": 0.6175, "style_score": 0.5586265072068279, "combined_score": 0.588063253603414, "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:30+00:00", "content_id": "f8f2a3a0-0d99-4a16-bb6c-a7be27053929", "creator_id": "attacker_FP02", "guess": "ai", "model_score": 0.7387, "style_score": 0.6666674670278925, "combined_score": 0.7026837335139462, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:30+00:00", "content_id": "326d2267-ae38-4fe6-b3be-5dadbd4f70c3", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.6190380907002864, "combined_score": 0.7120690453501433, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:30+00:00", "content_id": "36eddab8-c441-4eef-9496-b2ba6d3c7e57", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.4972554860869334, "combined_score": 0.8047310972173868, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:31+00:00", "content_id": "d9cffff0-b8b9-450c-a6c0-29b804d8725f", "creator_id": "attacker_MF05", "guess": "ai", "model_score": 0.9976, "style_score": 0.7, "combined_score": 0.8488, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:31+00:00", "content_id": "1685fee7-aa42-402b-944c-3511695d575a", "creator_id": "attacker_MF06", "guess": "ai", "model_score": 0.9969, "style_score": 1.0, "combined_score": 0.9984500000000001, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:31+00:00", "content_id": "1cb4eb52-2d1c-44e4-bf81-722d11048373", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 1.0, "combined_score": 0.9532, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
{"timestamp": "2026-11-08T05:02:32+00:00", "content_id": "42728a31-19c3-458b-88c9-786a6233f9fe", "creator_id": "attacker_MF08", "guess": "ai", "model_score": 0.9876, "style_score": 0.7839673688335569, "combined_score": 0.8857836844167785, "label": "This text has writing patterns common to AI-generated models.", "status": "accepted"}
RQ07 - no audit log
RQ10 - {"timestamp": "2026-11-08T05:02:32+00:00", "creator_id": "unknown", "event": "rejected", "status": "rejected", "reason": "rate_limited", "limit": "5 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

I would say the worst outcome is the FP01; plain, clear human writing with no flourishes. My scoring came back as unsure with a score of 0.588. I'm guessing this should be the baseline for a human writing, and it's not passing as human so my thresholds is bad and it will affect a majority of the submissions, and potentially marking them all as unsure.

---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Given 10 human written text submission, at most 2 submission can be falsely labelled AI. | 2/10 | 0/10 | 0/10 | 0/10 | MET |
| 2. The combine score difference between AI and human have a gap of at least 0.30. | 0.30 | 0.43 | 0.43 | 0.43 | MET |
| 3. All three labels: AI, Human, Unsure, must be reachable at least once. | 3/3 | 3/3 | 3/3 | 3/3 | MET |
| 4. All appeal must be 100% recorded. | 1/1 | 1/1 | 0/1 | 0/1 | MISSED |
| 5. A bad input, such as missing text or creator_id, should 100% return an error response. | 4/4 | 3/4 | 3/4 | 3/4 | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-08 14:44

Criteria 1 Trial 1:
```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.40049347826086956,
    "model_score": 0.0749,
    "style_score": 0.7260869565217392,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "I think you'll know this style of trading, long term, elliot wave theo"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.3475099909589568,
    "model_score": 0.0593,
    "style_score": 0.6357199819179136,
    "label": "This text has distinct writing patterns written by a person.",
    "sent": "Amazon Prime Uber Eats promo + Popeye buy 1 get 1 free. 6 sandwich, 12"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.27363489439831545,
    "model_score": 0.3925,
    "style_score": 0.15476978879663095,
    "label": "This text has distinct writing patterns written by a person.",
    "sent": "Omg. When did iPads get so expensive?! I remember getting one like 5 y"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.39728571428571424,
    "model_score": 0.026,
    "style_score": 0.7685714285714285,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "I think that's better, i rather have roster bound gems and higher leve"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5335142044336618,
    "model_score": 0.3767,
    "style_score": 0.6903284088673236,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "They will expand ocean content with the new region called \"Sea of Alde"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5485122448979591,
    "model_score": 0.3358,
    "style_score": 0.7612244897959184,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "i think the problem was eman was helping 2 ppl at the same time\ncuz fr"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5663499999999999,
    "model_score": 0.4327,
    "style_score": 0.7,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "lol i thought that was yours when you opened it but that's DISGUSTING"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5304500000000001,
    "model_score": 0.3159,
    "style_score": 0.7450000000000001,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "they were like always together in daycare\nwe do have the parent's cont"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4032,
    "model_score": 0.0564,
    "style_score": 0.75,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "I think better animation would be sword the guard with the shield behi"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4953397084580433,
    "model_score": 0.4597,
    "style_score": 0.5309794169160866,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "It's turn-based and each character gets 2 actions. if you move within "
  }
]
```

Criteria 2 Trial 1:
```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7000029978914617,
    "model_score": 0.7217,
    "style_score": 0.6783059957829235,
    "label": "This text has writing patterns common to AI-generated models.",
    "sent": "In today\u2019s rapidly evolving digital landscape, it is important to note"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.27363489439831545,
    "model_score": 0.3925,
    "style_score": 0.15476978879663095,
    "label": "This text has distinct writing patterns written by a person.",
    "sent": "Omg. When did iPads get so expensive?! I remember getting one like 5 y"
  }
]
```

Criteria 3 Trial 1:
```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7000029978914617,
    "model_score": 0.7217,
    "style_score": 0.6783059957829235,
    "label": "This text has writing patterns common to AI-generated models.",
    "sent": "In today\u2019s rapidly evolving digital landscape, it is important to note"
  },
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.27363489439831545,
    "model_score": 0.3925,
    "style_score": 0.15476978879663095,
    "label": "This text has distinct writing patterns written by a person.",
    "sent": "Omg. When did iPads get so expensive?! I remember getting one like 5 y"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.4234666666666667,
    "model_score": 0.1136,
    "style_score": 0.7333333333333334,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "The quick brown fox jumps over the lazy dog."
  }
]
```

Criteria 4 Trial 1: [Submit + Appeal]
```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.35609999999999997,
    "model_score": 0.0122,
    "style_score": 0.7,
    "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
    "sent": "Simple text to manually test appeal path for this criteria."
  }
]
```
```json
[
  {
    "timestamp": "2026-11-09T00:40:13+00:00",
    "content_id": "13370cde-46fa-4e5b-b09d-aede8a67fc37",
    "creator_id": "eval_All appeal m_1",
    "event": "appeal",
    "status": "under_review",
    "reasoning": "I wrote this text myself"
  }
]
```

Criteria 5 Trial 1:
```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"creator_id\": \"eval_bad_missing\"}"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.998747,
    "model_score": 0.9975,
    "style_score": 0.999994,
    "label": "This text has writing patterns common to AI-generated models.",
    "sent": "word word word word word word word word word word word word word word "
  },
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
  }
]
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

Criteria 4: I wrote missed because I used missing reasoning for run 2 and missing content_id for run 3. This is a broken criterion, Stage: N/A, Mechanism: N/A. New Criterion 4 is: All appeal with valid input must be 100% recorded.

Criteria 5: I wrote missed because I did not have checks for huge words and non-plain english edge case as the bad input. Stage: the route, Mechanism: no checks for huge words/text and non-plain english texts.
Broken Attacks: MF03-08, RQ07

Criteria 1: I wrote met because technically it fulfilled the criteria as "unsure" is not the same as "ai" label. However 8/10 were labelled "unsure" when they should be "human", my signal thresholds needs to be adjusted. Signal two had 7/10 submissions above ~0.7, Signal one has 4/10 submissions above 0.35.
Stage: Signal two, Mechanism: Signal two's individual score calculations is tilted towards AI most of the time and maybe its weights threshold needs to be adjusted. 
Broken Attacks: FP01-FP07

---

## The Improvement

**What I changed:**

Added more valid input checks and moved it to helper function.

**Which diagnosis pointed at it:**

Criteria 5: Bad Input validation checks

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->
- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 02:12
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e14806f0-bd52-4a2a-9e86-de7ed068c07f` | unsure | 0.372 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `29805144-af51-4097-a4be-10283af59686` | unsure | 0.501 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `7e732d26-f35e-4726-83e2-7115dba4ac28` | unsure | 0.601 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c17f50f5-340e-4da5-973e-1127fa785230` | unsure | 0.554 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `93affdae-efd9-4ec4-817c-32c875341905` | human | 0.277 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e7140123-6840-4b05-9e08-482c95618668` | unsure | 0.424 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1da8ed3a-356d-4efe-90ee-b38cd1a7ebe5` | unsure | 0.577 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `26f1b844-eba6-4016-8e24-31f57e2e56b5` | unsure | 0.402 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4c58ab32-484b-431e-9d94-e4aef308ffc7` | unsure | 0.578 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `14aea645-a8dd-4199-81a1-08c4c8bac46e` | ai | 0.843 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ba04827b-3c0b-4179-9c3d-5836005fb162` | unsure | 0.588 | BROKE |
| FP02 | false_positive | human writing in a formal register | 200 | `7f4af379-c46b-41d6-968f-d09239dee0f9` | ai | 0.703 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `793ec748-a9fc-4d78-910b-6aa175bd1d22` | ai | 0.712 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `838b094b-8b9f-4650-9906-0f9c2ac2e393` | ai | 0.703 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `424f2a94-9d0c-4ebf-a999-abdabf753b72` | ai | 0.743 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `1526d08e-fcc3-40ad-ad61-c54340ef0395` | ai | 0.809 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a1226b22-f266-40d2-a738-87cf544715b5` | ai | 0.805 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `4ed3691b-4dfc-4c9a-a79b-356a77966e20` | unsure | 0.403 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `05b8f259-c686-4c13-99f4-455c7631d275` | unsure | 0.426 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2fd663ba-bfdf-4039-9c5e-16b17bbb2651` | human | 0.222 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f0bc0736-a846-4886-95f6-029cd4248c09` | unsure | 0.514 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `99468ad3-2171-4236-9eaa-ae2b75233cc6` | unsure | 0.521 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `976c118b-db14-4ae4-aa94-33ebfbaee93d` | unsure | 0.567 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `df502af6-e0e6-4219-9f47-fe1ac3238741` | unsure | 0.562 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 400 | `—` | — | — | HELD |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — | HELD |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — | HELD |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — | HELD |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — | HELD |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — | BROKE |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — | BROKE |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a30e860d-621d-4fd2-922d-dda266ca58f2` | unsure | 0.364 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `01d84faf-2a8c-405b-b1d3-8278678e3568` | unsure | 0.364 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1baae1ec-08eb-40cb-a997-43cac607d056` | unsure | 0.364 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a75ef137-f385-4fcc-9f14-ece6f4cd9a60` | unsure | 0.364 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fa2bb68b-f008-402c-8468-95e740d48147` | unsure | 0.364 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |


- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-11 02:13

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Given 10 human written text submission, at most 2 submission can be falsely labelled AI. | 2/10 | 0/10 | 0/10 | 0/10 | MET |
| 2. The combine score difference between AI and human have a gap of at least 0.30. | 0.30 | 0.43 | 0.43 | 0.43 | MET |
| 3. All three labels: AI, Human, Unsure, must be reachable at least once. | 3/3 | 3/3 | 3/3 | 3/3 | MET |
| 4. All appeal must be 100% recorded. | 1/1 | 1/1 | 0/1 | 0/1 | MISSED |
| 5. A bad input, such as missing text or creator_id, should 100% return an error response. | 4/4 | 4/4 | 4/4 | 4/4 | MET |

**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

Yes, Held against attacks that previously broke, MF03-08 and RQ07. Criteria 5 eval also passed 4/4.

## The Improvement 2

**What I changed:**

Revised Criterion 4 and changed appeal test to only valid inputs. see audit.jsonl (last 3 appeals)

**Which diagnosis pointed at it:**

Broken Criterion 4

### Attack Run — After
- Produced by: `run_eval.py::main`
- Service: `app.py::submit` · scoring: `scoring.py::combine_signals`
- 3 trials per criterion · 2026-11-11 02:13

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Given 10 human written text submission, at most 2 submission can be falsely labelled AI. | 2/10 | 0/10 | 0/10 | 0/10 | MET |
| 2. The combine score difference between AI and human have a gap of at least 0.30. | 0.30 | 0.43 | 0.43 | 0.43 | MET |
| 3. All three labels: AI, Human, Unsure, must be reachable at least once. | 3/3 | 3/3 | 3/3 | 3/3 | MET |
| 4. All appeal must be 100% recorded. | 1/1 | 1/1 | 1/1 | 1/1 | MET |
| 5. A bad input, such as missing text or creator_id, should 100% return an error response. | 4/4 | 4/4 | 4/4 | 4/4 | MET |

**Did it help, and how do I know:**

Doesn't help the functionality of the provenance guard but fixed criteria 4 language.

---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

I stopped because I ran out of time.

False Postive: FP01-07, I would need to adjust signal two thresholds, then run attack/eval test, then if needed adjust then combining rule and run attack/eval tests again
Malformed: RQ10-RQ11, bad input got rate limited, I would add IP address to rate limit so bad inputs are bundled together under "unknown" creator_id

**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I would lend more towards fewer wrong accusations because AI is part of everday life now and more and more AI usage is common. I think heavily modified AI text or human written and AI-improved is fine since they are doing the work, just improved the work via a tool.

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
