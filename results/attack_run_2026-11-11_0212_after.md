# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 02:12
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e14806f0-bd52-4a2a-9e86-de7ed068c07f` | unsure | 0.372 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `29805144-af51-4097-a4be-10283af59686` | unsure | 0.501 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `7e732d26-f35e-4726-83e2-7115dba4ac28` | unsure | 0.601 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `c17f50f5-340e-4da5-973e-1127fa785230` | unsure | 0.554 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `93affdae-efd9-4ec4-817c-32c875341905` | human | 0.277 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `e7140123-6840-4b05-9e08-482c95618668` | unsure | 0.424 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `1da8ed3a-356d-4efe-90ee-b38cd1a7ebe5` | unsure | 0.577 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `26f1b844-eba6-4016-8e24-31f57e2e56b5` | unsure | 0.402 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `4c58ab32-484b-431e-9d94-e4aef308ffc7` | unsure | 0.578 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `14aea645-a8dd-4199-81a1-08c4c8bac46e` | ai | 0.843 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ba04827b-3c0b-4179-9c3d-5836005fb162` | unsure | 0.588 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `7f4af379-c46b-41d6-968f-d09239dee0f9` | ai | 0.703 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `793ec748-a9fc-4d78-910b-6aa175bd1d22` | ai | 0.712 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `838b094b-8b9f-4650-9906-0f9c2ac2e393` | ai | 0.703 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `424f2a94-9d0c-4ebf-a999-abdabf753b72` | ai | 0.743 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `1526d08e-fcc3-40ad-ad61-c54340ef0395` | ai | 0.809 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a1226b22-f266-40d2-a738-87cf544715b5` | ai | 0.805 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `4ed3691b-4dfc-4c9a-a79b-356a77966e20` | unsure | 0.403 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `05b8f259-c686-4c13-99f4-455c7631d275` | unsure | 0.426 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `2fd663ba-bfdf-4039-9c5e-16b17bbb2651` | human | 0.222 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `f0bc0736-a846-4886-95f6-029cd4248c09` | unsure | 0.514 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `99468ad3-2171-4236-9eaa-ae2b75233cc6` | unsure | 0.521 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `976c118b-db14-4ae4-aa94-33ebfbaee93d` | unsure | 0.567 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `df502af6-e0e6-4219-9f47-fe1ac3238741` | unsure | 0.562 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 429 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 429 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a30e860d-621d-4fd2-922d-dda266ca58f2` | unsure | 0.364 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `01d84faf-2a8c-405b-b1d3-8278678e3568` | unsure | 0.364 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1baae1ec-08eb-40cb-a997-43cac607d056` | unsure | 0.364 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a75ef137-f385-4fcc-9f14-ece6f4cd9a60` | unsure | 0.364 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fa2bb68b-f008-402c-8468-95e740d48147` | unsure | 0.364 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "e14806f0-bd52-4a2a-9e86-de7ed068c07f",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.3717619577805506,
  "model_score": 0.1635,
  "style_score": 0.5800239155611012,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "29805144-af51-4097-a4be-10283af59686",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5010725243583697,
  "model_score": 0.5943,
  "style_score": 0.12816262179184776,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "7e732d26-f35e-4726-83e2-7115dba4ac28",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.6005091770827693,
  "model_score": 0.6662,
  "style_score": 0.3377458854138468,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "c17f50f5-340e-4da5-973e-1127fa785230",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5538590226344116,
  "model_score": 0.6114,
  "style_score": 0.4963180452688231,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "93affdae-efd9-4ec4-817c-32c875341905",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.27654063170844967,
  "model_score": 0.3212,
  "style_score": 0.2318812634168993,
  "label": "This text has distinct writing patterns written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "e7140123-6840-4b05-9e08-482c95618668",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.42385,
  "model_score": 0.5727,
  "style_score": 0.275,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "1da8ed3a-356d-4efe-90ee-b38cd1a7ebe5",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.577120618556701,
  "model_score": 0.5862,
  "style_score": 0.568041237113402,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "26f1b844-eba6-4016-8e24-31f57e2e56b5",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.40188932188134524,
  "model_score": 0.2452,
  "style_score": 0.5585786437626905,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "4c58ab32-484b-431e-9d94-e4aef308ffc7",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5781588625915497,
  "model_score": 0.7042,
  "style_score": 0.45211772518309945,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "14aea645-a8dd-4199-81a1-08c4c8bac46e",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8430468493862999,
  "model_score": 0.9792,
  "style_score": 0.7068936987725998,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "ba04827b-3c0b-4179-9c3d-5836005fb162",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.588063253603414,
  "model_score": 0.6175,
  "style_score": 0.5586265072068279,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "7f4af379-c46b-41d6-968f-d09239dee0f9",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.7026837335139462,
  "model_score": 0.7387,
  "style_score": 0.6666674670278925,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "793ec748-a9fc-4d78-910b-6aa175bd1d22",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7120690453501433,
  "model_score": 0.8051,
  "style_score": 0.6190380907002864,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "838b094b-8b9f-4650-9906-0f9c2ac2e393",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.7034566208854142,
  "model_score": 0.8329,
  "style_score": 0.5740132417708284,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "424f2a94-9d0c-4ebf-a999-abdabf753b72",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7431709916185398,
  "model_score": 0.8005,
  "style_score": 0.6858419832370797,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "1526d08e-fcc3-40ad-ad61-c54340ef0395",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.8091411008567619,
  "model_score": 0.8814,
  "style_score": 0.5201055042838101,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "a1226b22-f266-40d2-a738-87cf544715b5",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.8047310972173868,
  "model_score": 0.8816,
  "style_score": 0.4972554860869334,
  "label": "This text has writing patterns common to AI-generated models.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "4ed3691b-4dfc-4c9a-a79b-356a77966e20",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4028968245269452,
  "model_score": 0.3223,
  "style_score": 0.48349364905389036,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "05b8f259-c686-4c13-99f4-455c7631d275",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.42558635146947765,
  "model_score": 0.4625,
  "style_score": 0.3886727029389553,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "2fd663ba-bfdf-4039-9c5e-16b17bbb2651",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.22183383843818835,
  "model_score": 0.2044,
  "style_score": 0.2392676768763767,
  "label": "This text has distinct writing patterns written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "f0bc0736-a846-4886-95f6-029cd4248c09",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5144168381934249,
  "model_score": 0.5943,
  "style_score": 0.43453367638684964,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "99468ad3-2171-4236-9eaa-ae2b75233cc6",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.5213118241471012,
  "model_score": 0.4998,
  "style_score": 0.5428236482942024,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "976c118b-db14-4ae4-aa94-33ebfbaee93d",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.5669395479208968,
  "model_score": 0.6401,
  "style_score": 0.27429773960448417,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "df502af6-e0e6-4219-9f47-fe1ac3238741",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5615971566223728,
  "model_score": 0.5583,
  "style_score": 0.5648943132447454,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 429,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "a30e860d-621d-4fd2-922d-dda266ca58f2",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.36434999999999995,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "01d84faf-2a8c-405b-b1d3-8278678e3568",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.36434999999999995,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "1baae1ec-08eb-40cb-a997-43cac607d056",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.36434999999999995,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "a75ef137-f385-4fcc-9f14-ece6f4cd9a60",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.36434999999999995,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "fa2bb68b-f008-402c-8468-95e740d48147",
  "creator_id": "attacker_flood",
  "guess": "unsure",
  "confidence": 0.36434999999999995,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "This text has mixed writing patterns and/or style common with AI-generated models and naturally written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
