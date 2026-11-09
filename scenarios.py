"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "Given 10 human written text submission, at most 2 submission can be falsely labelled AI.",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I think you'll know this style of trading, long term, elliot wave theory, and this guy does very good analysis of companies imo",
            "Amazon Prime Uber Eats promo + Popeye buy 1 get 1 free. 6 sandwich, 12 wings, 1 drink for $12 😂",
            "Omg. When did iPads get so expensive?! I remember getting one like 5 years ago for $400! They're like $1000 now!",
            "I think that's better, i rather have roster bound gems and higher level gems for progression than char gems\nchar gems is ass/aids\ngem atleast is straight forward progression, not these shitty ass systems",
            "They will expand ocean content with the new region called \"Sea of Aldebaran\". This region comes with 17 new Islands and 4 new Adventure Islands. Existing Adventure Islands will be retired (no longer part of the rotation, the places still exist). They're also planning to allow players to play certain PvP islands such as Snowpang with AI companions.",
            "i think the problem was eman was helping 2 ppl at the same time\ncuz from what i heard, it sounded like you two were slightly off in which part you guys were doing so when he said something you thought he was talking to you but he wasn't",
            "lol i thought that was yours when you opened it but that's DISGUSTING",
            "they were like always together in daycare\nwe do have the parent's contact info, we were suppose to have a playdate but ended up not happening\ni don't think they really remember each other anymore lol\nthe kids i mean",
            "I think better animation would be sword the guard with the shield behind it pushing against the sword",
            "It's turn-based and each character gets 2 actions. if you move within the blue range, it counts as 1 action and you can either attack or stop there. Otherwise you  can use 2 move actions.\nEach dino has a different set of skills. The little yellow one can hack doors open, the triceratops can do a charge attack move where he dashes. There's a sniper and an assasin that spits venom\nright now there is 1 mission where you have to escape past the guards. If you kill them all or run past them, but they can call reinforcements. IF they catch one of your guys, The next mission will be an optional rescue mission where you rescue your teammate"
        ],
    },
    {
        "name": "The combine score difference between AI and human have a gap of at least 0.30.",
        "criterion": 2,
        "texts": [
            "In today’s rapidly evolving digital landscape, it is important to note that the tapestry of human creativity continues to be woven together with the transformative power of artificial intelligence. Whether you’re a seasoned professional or just beginning your journey, delving into this multifaceted realm can unlock a wealth of exciting possibilities. It’s worth noting that navigating these waters requires a delicate balance of innovation and responsibility, ensuring that we harness technology’s potential while remaining mindful of its limitations.",  # AI
            "Omg. When did iPads get so expensive?! I remember getting one like 5 years ago for $400! They're like $1000 now!"  # Human
        ],
    },
    {
        "name": "All three labels: AI, Human, Unsure, must be reachable at least once.",
        "criterion": 3,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "In today’s rapidly evolving digital landscape, it is important to note that the tapestry of human creativity continues to be woven together with the transformative power of artificial intelligence. Whether you’re a seasoned professional or just beginning your journey, delving into this multifaceted realm can unlock a wealth of exciting possibilities. It’s worth noting that navigating these waters requires a delicate balance of innovation and responsibility, ensuring that we harness technology’s potential while remaining mindful of its limitations.",
            "Omg. When did iPads get so expensive?! I remember getting one like 5 years ago for $400! They're like $1000 now!",
            "The quick brown fox jumps over the lazy dog.",
        ],
    },
    {
        "name": "All appeal must be 100% recorded.",
        "criterion": 4,
        "texts": [
            "Simple text to manually test appeal path for this criteria."
        ],
    },
    # A bad-input criterion looks like this. Uncomment and adjust if that's one
    # of your five — these are raw request bodies, sent exactly as written.
    {
        "name": "A bad input, such as missing text or creator_id, should 100% return an error response.",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },

    # TODO: add what your remaining criteria need.
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
