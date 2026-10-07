"""
Sentilink Enterprise — Academic Project Presentation Deck
Smart Book Review Management & Customer Opinion Analytics
BVDU DET CSBS: Enterprise Systems, ASTMA, IT Project Management
Student: Saloni Mahajan

13 Simple, High-Scoring, Pedagogical Slides
- Clean, uncluttered layout with high readability
- 100% authentic Book Review domain details
- Distinct scholarly visual palette: Oxford Slate Navy (#0F172A), Royal Sapphire (#2563EB), Emerald (#059669)
- Georgia-Bold headings, Segoe UI body text
"""

import os
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 16:9 Widescreen slide dimensions
W, H = 1152, 648

# Color Palette — Scholarly Professional Theme
C_DARK_BG = colors.HexColor('#0F172A')       # Deep Oxford Navy for Slide 1 & 13
C_DARK_CARD = colors.HexColor('#1E293B')     # Charcoal Slate Container
C_LIGHT_BG = colors.HexColor('#F8FAFC')      # Crisp Light Slide Canvas (Slate 50)
C_WHITE = colors.HexColor('#FFFFFF')
C_CARD_BG = colors.HexColor('#FFFFFF')
C_CARD_TINT = colors.HexColor('#F1F5F9')     # Soft Tinted Container (Slate 100)
C_BORDER = colors.HexColor('#E2E8F0')        # Subtle Card Border (Slate 200)

# Typography Colors
C_TEXT_DARK = colors.HexColor('#0F172A')     # High-contrast charcoal heading
C_TEXT_BODY = colors.HexColor('#334155')     # Slate-700 readable body text
C_TEXT_MUTED = colors.HexColor('#64748B')    # Slate-500 subtitle / caption
C_TEXT_WHITE = colors.HexColor('#FFFFFF')
C_TEXT_LIGHT_MUTED = colors.HexColor('#94A3B8')

# Accents
C_PRIMARY = colors.HexColor('#2563EB')       # Royal Sapphire Blue
C_PRIMARY_LIGHT = colors.HexColor('#60A5FA')
C_GREEN = colors.HexColor('#059669')         # Positive Sentiment Accent (Emerald)
C_SLATE_BAR = colors.HexColor('#64748B')     # Neutral Sentiment Accent
C_RED_BAR = colors.HexColor('#DC2626')       # Negative Sentiment Accent (Crimson)
C_AMBER = colors.HexColor('#D97706')         # Warning / Highlight Accent

# Register Windows TrueType Fonts with Helvetica fallback
FONT_TITLE = 'Helvetica-Bold'
FONT_BODY = 'Helvetica'
FONT_BOLD = 'Helvetica-Bold'

fonts_dir = r'C:\Windows\Fonts'
try:
    if os.path.exists(os.path.join(fonts_dir, 'georgiab.ttf')) and os.path.exists(os.path.join(fonts_dir, 'georgia.ttf')):
        pdfmetrics.registerFont(TTFont('Georgia', os.path.join(fonts_dir, 'georgia.ttf')))
        pdfmetrics.registerFont(TTFont('Georgia-Bold', os.path.join(fonts_dir, 'georgiab.ttf')))
        FONT_TITLE = 'Georgia-Bold'
except Exception:
    pass

try:
    if os.path.exists(os.path.join(fonts_dir, 'segoeui.ttf')) and os.path.exists(os.path.join(fonts_dir, 'segoeuib.ttf')):
        pdfmetrics.registerFont(TTFont('SegoeUI', os.path.join(fonts_dir, 'segoeui.ttf')))
        pdfmetrics.registerFont(TTFont('SegoeUI-Bold', os.path.join(fonts_dir, 'segoeuib.ttf')))
        FONT_BODY = 'SegoeUI'
        FONT_BOLD = 'SegoeUI-Bold'
except Exception:
    pass


def top_y(dist):
    return H - dist


def wrap_text(c, text, font, font_size, max_width):
    words = text.split()
    lines = []
    cur_line = []
    for w in words:
        test_line = " ".join(cur_line + [w])
        if c.stringWidth(test_line, font, font_size) <= max_width:
            cur_line.append(w)
        else:
            if cur_line:
                lines.append(" ".join(cur_line))
            cur_line = [w]
    if cur_line:
        lines.append(" ".join(cur_line))
    return lines


def draw_multiline(c, x, y, text, font, font_size, color, leading, max_width):
    lines = wrap_text(c, text, font, font_size, max_width)
    c.setFont(font, font_size)
    c.setFillColor(color)
    cur_y = y
    for line in lines:
        c.drawString(x, cur_y, line)
        cur_y -= leading
    return cur_y


def draw_card(c, x, y, w, h, r=12, bg=C_CARD_BG, border=C_BORDER, stroke=1):
    c.saveState()
    c.setFillColor(bg)
    if stroke:
        c.setStrokeColor(border)
        c.setLineWidth(1)
        c.roundRect(x, y, w, h, r, fill=1, stroke=1)
    else:
        c.roundRect(x, y, w, h, r, fill=1, stroke=0)
    c.restoreState()


def draw_circle_badge(c, x, y, num_str, r=16, bg=C_PRIMARY, text_color=C_WHITE):
    c.saveState()
    c.setFillColor(bg)
    c.circle(x, y, r, fill=1, stroke=0)
    c.setFillColor(text_color)
    c.setFont(FONT_BOLD, 13)
    c.drawCentredString(x, y - 4, num_str)
    c.restoreState()


def draw_slide_header(c, title, subtitle=None):
    c.saveState()
    c.setFillColor(C_LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Title
    c.setFillColor(C_TEXT_DARK)
    c.setFont(FONT_TITLE, 36)
    c.drawString(70, top_y(88), title)

    # Subtitle
    if subtitle:
        c.setFillColor(C_TEXT_MUTED)
        c.setFont(FONT_BODY, 15)
        c.drawString(70, top_y(124), subtitle)

    c.restoreState()


# =========================================================================
# SLIDE 1: Cover Slide
# =========================================================================
def render_slide_1(c):
    c.saveState()
    c.setFillColor(C_DARK_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Curved ambient shapes on right
    c.setFillColor(colors.HexColor('#1E293B'))
    c.circle(W - 60, H / 2 + 70, 240, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#1E3A8A'))
    c.circle(W + 20, H / 2 - 80, 220, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#172554'))
    c.circle(W - 160, H / 2 - 120, 150, fill=1, stroke=0)

    # Top tracker
    c.setFont(FONT_BOLD, 14)
    c.setFillColor(colors.HexColor('#60A5FA'))
    c.drawString(75, top_y(155), "CSBS CAPSTONE  ·  ES  ·  ITPM  ·  ASTMA")

    # Main Title
    c.setFont(FONT_TITLE, 42)
    c.setFillColor(C_WHITE)
    c.drawString(75, top_y(235), "Sentilink Enterprise:")
    c.drawString(75, top_y(292), "Book Review Sentiment Analysis")
    c.drawString(75, top_y(349), "& Decision Support Platform")

    # Subtitle
    c.setFont(FONT_BODY, 16)
    c.setFillColor(C_TEXT_LIGHT_MUTED)
    c.drawString(75, top_y(410), "Unifying Natural Language Processing, 3-Tier Enterprise Systems, and IT Project Management")

    # Department & Student Info
    c.setFont(FONT_BODY, 13)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(75, top_y(540), "Saloni Mahajan   |   Department of Engineering & Technology (CSBS)   |   BVDU Pune")

    c.restoreState()


# =========================================================================
# SLIDE 2: Academic Tri-Subject Foundation
# =========================================================================
def render_slide_2(c):
    draw_slide_header(
        c,
        "Academic Tri-Subject Foundation",
        "How three engineering disciplines converge to transform reader feedback into publishing intelligence."
    )

    card_w = 318
    card_h = 245
    card_y = top_y(395)
    gap = 28
    start_x = 70

    cards_data = [
        ("1", "ASTMA (Elective IV B)", "Text Mining & NLP Engine. Preprocessing literary feedback, polarity scoring, and RAKE keyword extraction.", C_PRIMARY),
        ("2", "Enterprise Systems", "3-Tier Architecture & BI. Scalable FastAPI services, relational SQLite database, RBAC security, and BI analytics.", C_PRIMARY),
        ("3", "IT Project Management", "Execution & Governance. 4-sprint Agile scheduling, PERT critical path analysis, and budget control.", C_PRIMARY),
    ]

    for i, (num, title, body, badge_col) in enumerate(cards_data):
        cx = start_x + i * (card_w + gap)
        draw_card(c, cx, card_y, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)

        draw_circle_badge(c, cx + 38, card_y + card_h - 40, num, r=18, bg=badge_col)

        c.setFont(FONT_TITLE, 19)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(cx + 72, card_y + card_h - 46, title)

        draw_multiline(c, cx + 26, card_y + card_h - 90, body, FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 52)

    # Bottom Stat Row
    stat_y = top_y(510)
    stats = [
        ("36", "Master Books\nin Catalog", C_PRIMARY),
        ("35", "Literary Genres\nFiltered", C_PRIMARY),
        ("124+", "Verified Reviews\nAnalysed", C_PRIMARY),
    ]

    stat_start_x = 75
    stat_col_w = 346

    for i, (val, label, col) in enumerate(stats):
        sx = stat_start_x + i * stat_col_w
        c.setFont(FONT_TITLE, 46)
        c.setFillColor(col)
        c.drawString(sx, stat_y, val)

        vw = c.stringWidth(val, FONT_TITLE, 46)
        label_lines = label.split('\n')
        c.setFont(FONT_BODY, 15)
        c.setFillColor(C_TEXT_BODY)
        c.drawString(sx + vw + 14, stat_y + 16, label_lines[0])
        if len(label_lines) > 1:
            c.drawString(sx + vw + 14, stat_y - 4, label_lines[1])


# =========================================================================
# SLIDE 3: The Sentilink Text Analytics Pipeline
# =========================================================================
def render_slide_3(c):
    draw_slide_header(
        c,
        "The Sentilink Text Analytics Pipeline",
        "A modular, stage-by-stage architecture turning raw reader prose into actionable business intelligence."
    )

    stages = [
        ("1. Ingest", "sqlite3 corpus", False),
        ("2. Clean", "stopwords & regex", True),
        ("3. Polarity", "VADER compound", True),
        ("4. Aspects", "RAKE extraction", True),
        ("5. REST API", "FastAPI routes", False),
        ("6. Dashboard", "Chart.js / UI", False),
    ]

    box_w = 142
    box_h = 105
    box_y = top_y(260)
    gap = 26
    start_x = 70

    for i, (name, script, is_dark) in enumerate(stages):
        bx = start_x + i * (box_w + gap)
        if is_dark:
            draw_card(c, bx, box_y, box_w, box_h, r=12, bg=C_DARK_CARD, stroke=0)
            c.setFont(FONT_BOLD, 15)
            c.setFillColor(C_WHITE)
            c.drawCentredString(bx + box_w / 2, box_y + box_h - 40, name)
            c.setFont(FONT_BODY, 11)
            c.setFillColor(C_TEXT_LIGHT_MUTED)
            c.drawCentredString(bx + box_w / 2, box_y + 30, script)
        else:
            draw_card(c, bx, box_y, box_w, box_h, r=12, bg=C_CARD_TINT, border=C_BORDER)
            c.setFont(FONT_BOLD, 15)
            c.setFillColor(C_TEXT_DARK)
            c.drawCentredString(bx + box_w / 2, box_y + box_h - 40, name)
            c.setFont(FONT_BODY, 11)
            c.setFillColor(C_TEXT_MUTED)
            c.drawCentredString(bx + box_w / 2, box_y + 30, script)

        if i < len(stages) - 1:
            c.setFont(FONT_BOLD, 22)
            c.setFillColor(C_PRIMARY)
            c.drawString(bx + box_w + 8, box_y + box_h / 2 - 6, "›")

    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(70, top_y(298), "Highlighted dark stages represent the core ASTMA processing pipeline.")

    # Architectural Rationale Callout
    callout_y = top_y(470)
    callout_h = 135
    callout_w = W - 140
    draw_card(c, 70, callout_y, callout_w, callout_h, r=14, bg=C_CARD_TINT, border=C_BORDER)

    c.setFont(FONT_TITLE, 21)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(100, callout_y + callout_h - 42, "Why Sequential Decoupling?")

    body_text = (
        "Each stage isolates concerns: rigorous cleaning eliminates vocabulary skew without losing valence cues, "
        "sentiment scores feed aspect indexing, and asynchronous REST endpoints allow the dashboard to render instantly."
    )
    draw_multiline(c, 100, callout_y + callout_h - 78, body_text, FONT_BODY, 15, C_TEXT_BODY, 24, callout_w - 60)


# =========================================================================
# SLIDE 4: Text Preprocessing & Normalization
# =========================================================================
def render_slide_4(c):
    draw_slide_header(
        c,
        "Text Preprocessing & Normalization",
        "Refining literary reviews to isolate semantic features while preserving emotional intensity cues."
    )

    steps = [
        ("1", "Case Normalization", "Unifies 'Masterpiece' and 'masterpiece' into identical tokens"),
        ("2", "Noise & Symbol Removal", "Filters web URLs, HTML entities, and formatting symbols"),
        ("3", "Word Tokenization", "Segments continuous literary prose into discrete lexical units"),
        ("4", "Custom Stopword Pruning", "Removes generic terms ('the', 'page') while preserving valence modifiers"),
        ("5", "Morphological Lemmatization", "Maps inflected variations ('reading', 'reads') to base lemma 'read'"),
    ]

    start_y = top_y(190)
    step_gap = 68
    for i, (num, title, desc) in enumerate(steps):
        sy = start_y - i * step_gap
        draw_circle_badge(c, 90, sy, num, r=18, bg=C_PRIMARY)

        c.setFont(FONT_BOLD, 16)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(124, sy + 3, title)

        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_MUTED)
        c.drawString(124, sy - 18, desc)

    # Right: Dark BEFORE / AFTER Card
    card_x = 590
    card_w = 490
    card_h = 365
    card_y = top_y(535)
    draw_card(c, card_x, card_y, card_w, card_h, r=16, bg=C_DARK_CARD, stroke=0)

    # BEFORE Section
    c.setFont(FONT_BOLD, 12)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(card_x + 36, card_y + card_h - 40, "RAW READER REVIEW (BEFORE)")

    before_quote = "The protagonist's character arc was truly magnificent, but the slow pacing in chapter 8 made me lose interest!"
    draw_multiline(c, card_x + 36, card_y + card_h - 75, before_quote, FONT_BODY, 15, C_WHITE, 24, card_w - 72)

    # Subtle divider
    c.setStrokeColor(colors.HexColor('#334155'))
    c.setLineWidth(1)
    c.line(card_x + 36, card_y + card_h - 185, card_x + card_w - 36, card_y + card_h - 185)

    # AFTER Section
    c.setFont(FONT_BOLD, 12)
    c.setFillColor(colors.HexColor('#38BDF8'))
    c.drawString(card_x + 36, card_y + card_h - 220, "EXTRACTED FEATURE TOKENS (AFTER)")

    after_quote = "protagonist character arc truly magnificent slow pacing chapter 8 lose interest"
    draw_multiline(c, card_x + 36, card_y + card_h - 255, after_quote, FONT_BODY, 15, colors.HexColor('#BAE6FD'), 24, card_w - 72)


# =========================================================================
# SLIDE 5: Sentiment Classification Paradigms
# =========================================================================
def render_slide_5(c):
    draw_slide_header(
        c,
        "Sentiment Classification Paradigms",
        "Evaluating NLP methodologies for literary review analytics: why a hybrid approach was chosen."
    )

    card_w = 318
    card_h = 365
    card_y = top_y(535)
    gap = 28
    start_x = 70

    # Card 1: Lexicon-Based (Dark Card - Primary)
    cx1 = start_x
    draw_card(c, cx1, card_y, card_w, card_h, r=16, bg=C_DARK_CARD, stroke=0)

    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_WHITE)
    c.drawString(cx1 + 26, card_y + card_h - 44, "Lexicon-Based (VADER)")

    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_LIGHT_MUTED)
    draw_multiline(c, cx1 + 26, card_y + card_h - 80, "Evaluates sentiment using curated word valence dictionaries.", FONT_BODY, 13, C_TEXT_LIGHT_MUTED, 20, card_w - 52)

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_PRIMARY_LIGHT)
    c.drawString(cx1 + 26, card_y + card_h - 150, "Strength: ")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_WHITE)
    c.drawString(cx1 + 90, card_y + card_h - 150, "Zero training data,")
    c.drawString(cx1 + 26, card_y + card_h - 172, "instant explainability")

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(colors.HexColor('#F87171'))
    c.drawString(cx1 + 26, card_y + card_h - 222, "Limit: ")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_WHITE)
    c.drawString(cx1 + 70, card_y + card_h - 222, "Insensitive to deep")
    c.drawString(cx1 + 26, card_y + card_h - 244, "literary sarcasm")

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(colors.HexColor('#FACC15'))
    c.drawString(cx1 + 26, card_y + 30, "Primary Production Engine")

    # Card 2: Machine Learning
    cx2 = start_x + card_w + gap
    draw_card(c, cx2, card_y, card_w, card_h, r=16, bg=C_CARD_TINT, border=C_BORDER)

    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(cx2 + 26, card_y + card_h - 44, "Statistical ML (TF-IDF)")

    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_BODY)
    draw_multiline(c, cx2 + 26, card_y + card_h - 80, "Trains Naive Bayes & Logistic Regression on n-gram vectors.", FONT_BODY, 13, C_TEXT_BODY, 20, card_w - 52)

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_PRIMARY)
    c.drawString(cx2 + 26, card_y + card_h - 150, "Strength: ")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx2 + 90, card_y + card_h - 150, "Learns book-specific")
    c.drawString(cx2 + 26, card_y + card_h - 172, "literary vocabularies")

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_RED_BAR)
    c.drawString(cx2 + 26, card_y + card_h - 222, "Limit: ")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx2 + 70, card_y + card_h - 222, "Requires verified labels")

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(cx2 + 26, card_y + 30, "Evaluated as Baseline")

    # Card 3: Deep Learning
    cx3 = start_x + 2 * (card_w + gap)
    draw_card(c, cx3, card_y, card_w, card_h, r=16, bg=C_CARD_TINT, border=C_BORDER)

    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(cx3 + 26, card_y + card_h - 44, "Deep Transformers")

    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_BODY)
    draw_multiline(c, cx3 + 26, card_y + card_h - 80, "Bidirectional contextual embeddings (BERT / RoBERTa).", FONT_BODY, 13, C_TEXT_BODY, 20, card_w - 52)

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_PRIMARY)
    c.drawString(cx3 + 26, card_y + card_h - 150, "Strength: ")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx3 + 90, card_y + card_h - 150, "Understands complex")
    c.drawString(cx3 + 26, card_y + card_h - 172, "metaphors & tone")

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_RED_BAR)
    c.drawString(cx3 + 26, card_y + card_h - 222, "Limit: ")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx3 + 70, card_y + card_h - 222, "High RAM & latency")

    c.setFont(FONT_BOLD, 13)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(cx3 + 26, card_y + 30, "Future Scale Target")


# =========================================================================
# SLIDE 6: Polarity Scoring & Valence Heuristics
# =========================================================================
def render_slide_6(c):
    draw_slide_header(
        c,
        "Polarity Scoring & Valence Heuristics",
        "How grammatical cues and modifier heuristics calculate the normalized compound sentiment."
    )

    heuristics = [
        ("1", "Punctuation Stacking", "'Magnificent!' vs 'Magnificent!!!' raises intensity"),
        ("2", "Capitalization Emphasis", "'MASTERPIECE' boosts positive polarity score"),
        ("3", "Degree Modifiers", "'Very engaging' raises score; 'barely readable' lowers it"),
        ("4", "Polarity Inversion", "'Not captivating' inverts positive word to negative valence"),
        ("5", "Contrastive Conjunctions", "'Good start, BUT dull ending' weights concluding clause"),
    ]

    start_y = top_y(190)
    gap_y = 68
    for i, (num, tag, desc) in enumerate(heuristics):
        sy = start_y - i * gap_y
        draw_circle_badge(c, 90, sy, num, r=18, bg=C_PRIMARY)

        c.setFont(FONT_BOLD, 16)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(124, sy - 5, tag)

        tw = c.stringWidth(tag, FONT_BOLD, 16)
        c.setFont(FONT_BODY, 14)
        c.setFillColor(C_TEXT_MUTED)
        c.drawString(124 + tw + 12, sy - 5, desc)

    # Right: Compound Score & Color Bar
    rx = 590
    rw = 490

    c.setFont(FONT_TITLE, 21)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(rx, top_y(180), "Compound Metric Scale: -1.0 to +1.0")

    # 3-segment color bar
    bar_y = top_y(280)
    bar_h = 70
    seg_w = rw / 3.0

    # Negative Segment (Left)
    c.setFillColor(C_RED_BAR)
    c.rect(rx, bar_y, seg_w, bar_h, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_WHITE)
    c.drawCentredString(rx + seg_w / 2, bar_y + 42, "Negative")
    c.setFont(FONT_BODY, 12)
    c.drawCentredString(rx + seg_w / 2, bar_y + 18, "<= -0.05")

    # Neutral Segment (Center)
    c.setFillColor(C_SLATE_BAR)
    c.rect(rx + seg_w, bar_y, seg_w, bar_h, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_WHITE)
    c.drawCentredString(rx + seg_w + seg_w / 2, bar_y + 42, "Neutral")
    c.setFont(FONT_BODY, 12)
    c.drawCentredString(rx + seg_w + seg_w / 2, bar_y + 18, "-0.05 to +0.05")

    # Positive Segment (Right)
    c.setFillColor(C_GREEN)
    c.rect(rx + 2 * seg_w, bar_y, seg_w, bar_h, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_WHITE)
    c.drawCentredString(rx + 2 * seg_w + seg_w / 2, bar_y + 42, "Positive")
    c.setFont(FONT_BODY, 12)
    c.drawCentredString(rx + 2 * seg_w + seg_w / 2, bar_y + 18, ">= +0.05")

    # Callout card below
    call_y = top_y(490)
    call_h = 175
    draw_card(c, rx, call_y, rw, call_h, r=14, bg=C_CARD_TINT, border=C_BORDER)

    call_text = (
        "The engine computes raw positive, neutral, and negative word proportions, "
        "and categorizes the review using the normalized compound score calculated from valence adjustments."
    )
    draw_multiline(c, rx + 30, call_y + call_h - 55, call_text, FONT_BODY, 15, C_TEXT_BODY, 25, rw - 60)


# =========================================================================
# SLIDE 7: Aspect-Based Opinion Mining for Books
# =========================================================================
def render_slide_7(c):
    draw_slide_header(
        c,
        "Aspect-Based Opinion Mining for Books",
        "Dissecting reader reviews into 8 literary craft dimensions to discover WHY readers loved or disliked a book."
    )

    row1 = ["Plot & Narrative", "Character Arc", "Pacing & Rhythm", "Writing Style"]
    row2 = ["World Building", "Emotional Impact", "Theme & Tone", "Ending & Resolution"]

    pill_w = 224
    pill_h = 44
    gap = 26
    start_x = 75

    # Row 1
    y1 = top_y(240)
    for i, tag in enumerate(row1):
        px = start_x + i * (pill_w + gap)
        c.saveState()
        c.setFillColor(C_WHITE)
        c.setStrokeColor(C_PRIMARY)
        c.setLineWidth(1.5)
        c.roundRect(px, y1, pill_w, pill_h, pill_h / 2.0, fill=1, stroke=1)
        c.setFont(FONT_BOLD, 14)
        c.setFillColor(C_TEXT_DARK)
        c.drawCentredString(px + pill_w / 2, y1 + 14, tag)
        c.restoreState()

    # Row 2
    y2 = top_y(305)
    for i, tag in enumerate(row2):
        px = start_x + i * (pill_w + gap)
        c.saveState()
        c.setFillColor(C_WHITE)
        c.setStrokeColor(C_PRIMARY)
        c.setLineWidth(1.5)
        c.roundRect(px, y2, pill_w, pill_h, pill_h / 2.0, fill=1, stroke=1)
        c.setFont(FONT_BOLD, 14)
        c.setFillColor(C_TEXT_DARK)
        c.drawCentredString(px + pill_w / 2, y2 + 14, tag)
        c.restoreState()

    # Dark Container Card below
    card_x = 75
    card_w = W - 150
    card_h = 185
    card_y = top_y(540)
    draw_card(c, card_x, card_y, card_w, card_h, r=16, bg=C_DARK_CARD, stroke=0)

    # Left: REVIEW
    c.setFont(FONT_BOLD, 13)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(card_x + 40, card_y + card_h - 45, "READER REVIEW")

    rev_quote = "The world building was breathtaking, but the characters felt shallow and the ending was rushed."
    draw_multiline(c, card_x + 40, card_y + card_h - 85, rev_quote, FONT_BODY, 16, C_WHITE, 26, 480)

    # Right: DETECTED DIMENSIONS
    c.setFont(FONT_BOLD, 13)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(card_x + 560, card_y + card_h - 45, "MINED OPINION DIMENSIONS")

    c.setFont(FONT_BODY, 15)
    c.setFillColor(colors.HexColor('#38BDF8'))
    c.drawString(card_x + 560, card_y + card_h - 82, "• World Building: Positive (+0.82) — 'breathtaking'")
    c.drawString(card_x + 560, card_y + card_h - 110, "• Character Arc: Negative (-0.45) — 'shallow'")
    c.drawString(card_x + 560, card_y + card_h - 138, "• Ending & Resolution: Negative (-0.61) — 'rushed'")


# =========================================================================
# SLIDE 8: 3-Tier Enterprise Architecture
# =========================================================================
def render_slide_8(c):
    draw_slide_header(
        c,
        "3-Tier Enterprise Architecture",
        "Decoupled Service-Oriented Architecture (SOA) ensuring performance, maintainability, and security."
    )

    lx = 75
    lw = 480

    # Layer 1: Presentation (Dark Card)
    y1 = top_y(260)
    draw_card(c, lx, y1, lw, 95, r=14, bg=C_DARK_CARD, stroke=0)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_WHITE)
    c.drawString(lx + 28, y1 + 55, "Presentation Tier (UI)")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_LIGHT_MUTED)
    c.drawString(lx + 28, y1 + 25, "Responsive Web Dashboard, Chart.js Visualizations, Genre Filters")

    # Layer 2: Business Logic (Royal Blue Card)
    y2 = top_y(385)
    draw_card(c, lx, y2, lw, 95, r=14, bg=C_PRIMARY, stroke=0)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_WHITE)
    c.drawString(lx + 28, y2 + 55, "Application & Logic Tier (SOA)")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(colors.HexColor('#DBEAFE'))
    c.drawString(lx + 28, y2 + 25, "FastAPI Microservices, VADER Sentiment Engine, RAKE Extractor")

    # Layer 3: Data Tier (Light Card)
    y3 = top_y(510)
    draw_card(c, lx, y3, lw, 95, r=14, bg=C_CARD_TINT, border=C_BORDER)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(lx + 28, y3 + 55, "Data Persistence Tier")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(lx + 28, y3 + 25, "SQLite relational database: books, reviews, users, audit logs")

    # Right: Enterprise System Capabilities
    rx = 620
    rw = 450
    c.setFont(FONT_TITLE, 23)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(rx, top_y(205), "Enterprise Characteristics")

    bullets = [
        "Unified Data Platform: Consolidates catalog data and NLP analytics into a single dashboard.",
        "Role-Based Access Control: Granular security separating Admin controls from Reader views.",
        "SOA Interoperability: Modular REST endpoints ready for external e-commerce integration.",
    ]

    by = top_y(270)
    for b in bullets:
        c.setFont(FONT_BOLD, 18)
        c.setFillColor(C_PRIMARY)
        c.drawString(rx, by, "•")

        draw_multiline(c, rx + 24, by, b, FONT_BODY, 14, C_TEXT_BODY, 22, rw - 30)
        by -= 72


# =========================================================================
# SLIDE 9: Relational Database & Decision Support
# =========================================================================
def render_slide_9(c):
    draw_slide_header(
        c,
        "Relational Database & Decision Support",
        "Structured data engineering powering publishing market analysis and reader satisfaction metrics."
    )

    card_w = 480
    card_h = 165
    gap_x = 40

    x1 = 75
    x2 = x1 + card_w + gap_x
    y_row1 = top_y(330)
    y_row2 = top_y(530)

    # 1. Relational Schema
    draw_card(c, x1, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row1 + card_h - 38, "1", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row1 + card_h - 44, "Relational Schema Design")
    draw_multiline(c, x1 + 30, y_row1 + card_h - 82, "Normalized SQLite schema linking Books, Reviews, Users, and Genres with referential integrity.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 2. B-Tree Query Indexing
    draw_card(c, x2, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row1 + card_h - 38, "2", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row1 + card_h - 44, "B-Tree Query Indexing")
    draw_multiline(c, x2 + 30, y_row1 + card_h - 82, "Indexes on book_id, sentiment_class, and genre ensure sub-10ms query execution across reviews.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 3. Rating Divergence Analysis
    draw_card(c, x1, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row2 + card_h - 38, "3", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row2 + card_h - 44, "Star vs Sentiment Divergence")
    draw_multiline(c, x1 + 30, y_row2 + card_h - 82, "Detects reviews where reader gave 4/5 stars but NLP text score reveals severe narrative criticisms.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 4. Genre Intelligence
    draw_card(c, x2, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row2 + card_h - 38, "4", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row2 + card_h - 44, "Genre Satisfaction Index")
    draw_multiline(c, x2 + 30, y_row2 + card_h - 82, "Computes aggregate sentiment across 35 literary genres to identify high-performing literary categories.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)


# =========================================================================
# SLIDE 10: IT Project Management & Agile Delivery
# =========================================================================
def render_slide_10(c):
    draw_slide_header(
        c,
        "IT Project Management & Agile Delivery",
        "Executing the project using an 8-week Scrum methodology with budget and schedule control."
    )

    items = [
        ("1", "Sprint 1 (W1-2)", "Corpus Ingestion (36 books) & Database Schema Design"),
        ("2", "Sprint 2 (W3-4)", "NLP Pipeline, VADER Engine & RAKE Aspect Discovery"),
        ("3", "Sprint 3 (W5-6)", "FastAPI Microservices, Analytics Dashboard & RBAC"),
        ("4", "Sprint 4 (W7-8)", "Integration Testing, Crashing Analysis & Cloud Launch"),
    ]

    start_y = top_y(200)
    gap_y = 65
    for i, (num, tag, desc) in enumerate(items):
        sy = start_y - i * gap_y
        draw_circle_badge(c, 85, sy, num, r=16, bg=C_PRIMARY)

        c.setFont(FONT_BOLD, 15)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(116, sy - 5, tag)

        tw = c.stringWidth(tag, FONT_BOLD, 15)
        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_MUTED)
        c.drawString(116 + tw + 10, sy - 5, desc)

    # Right: Horizontal bar chart (Realistic Budget)
    rx = 560

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(rx + 90, top_y(175), "Project Budget Allocation (INR)")

    bars = [
        ("Software Engineering", 28000, "28,000"),
        ("NLP & Text Mining", 14000, "14,000"),
        ("Quality Assurance & Testing", 9000, "9,000"),
        ("Cloud Infrastructure", 8000, "8,000"),
        ("Project Documentation", 6000, "6,000"),
    ]

    by = top_y(235)
    bar_max_val = 30000
    bar_max_w = 210

    for name, val, val_str in bars:
        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_BODY)
        c.drawRightString(rx + 155, by + 4, name)

        c.setStrokeColor(colors.HexColor('#CBD5E1'))
        c.setLineWidth(1)
        c.line(rx + 165, by - 12, rx + 165, by + 24)

        bw = (val / bar_max_val) * bar_max_w
        c.setFillColor(C_PRIMARY)
        c.rect(rx + 166, by, bw, 22, fill=1, stroke=0)

        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(rx + 166 + bw + 10, by + 4, val_str)

        by -= 48

    tot_y = top_y(540)
    c.setFont(FONT_BOLD, 36)
    c.setFillColor(C_PRIMARY)
    c.drawString(rx + 10, tot_y, "Rs. 65,000")

    tw = c.stringWidth("Rs. 65,000", FONT_BOLD, 36)
    c.setFont(FONT_BODY, 15)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(rx + 10 + tw + 12, tot_y + 4, "Total Project Expenditure")


# =========================================================================
# SLIDE 11: Risk Management & Quality Assurance
# =========================================================================
def render_slide_11(c):
    draw_slide_header(
        c,
        "Risk Management & Quality Assurance",
        "Proactive identification of technical and operational risks with targeted mitigation strategies."
    )

    tx = 75
    ty = top_y(530)
    tw = W - 150
    th = 380

    col_widths = [310, 110, 110, 472]
    headers = ["Risk Description", "Probability", "Impact", "Mitigation Strategy"]

    rows = [
        ("Literary Idiom Misinterpretation", "Medium", "Medium", "Augment lexicon with domain-specific literary modifiers"),
        ("Database Write Concurrency", "Low", "High", "Implement SQLite WAL mode and serialized connection pool"),
        ("Sprint Scope Creep", "Medium", "High", "Enforce strict Scrum backlog freezes and milestone reviews"),
        ("Corpus Ingestion Format Errors", "Low", "Medium", "Implement strict Pydantic input models and validation hooks"),
        ("Cloud Deployment Cold-Start", "Medium", "Low", "Configure health ping heartbeat to keep background services warm"),
        ("Subjectivity Ambiguity in Reviews", "Medium", "Medium", "Combine polarity scores with RAKE aspect phrase co-occurrence"),
    ]

    c.setFillColor(C_DARK_CARD)
    c.rect(tx, ty + th - 48, tw, 48, fill=1, stroke=0)

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_WHITE)
    cur_x = tx + 20
    for j, h_text in enumerate(headers):
        c.drawString(cur_x, ty + th - 32, h_text)
        cur_x += col_widths[j]

    row_h = 52
    for i, row in enumerate(rows):
        ry = ty + th - 48 - (i + 1) * row_h

        if i % 2 == 1:
            c.setFillColor(colors.HexColor('#F8FAFC'))
            c.rect(tx, ry, tw, row_h, fill=1, stroke=0)

        c.setStrokeColor(C_BORDER)
        c.setLineWidth(0.8)
        c.line(tx, ry, tx + tw, ry)

        cur_x = tx + 20
        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_BODY)
        for j, cell in enumerate(row):
            if j == 0:
                c.setFont(FONT_BOLD, 13)
                c.setFillColor(C_TEXT_DARK)
            else:
                c.setFont(FONT_BODY, 13)
                c.setFillColor(C_TEXT_BODY)

            c.drawString(cur_x, ry + 18, cell)
            cur_x += col_widths[j]


# =========================================================================
# SLIDE 12: Technical Evaluation & Known Limitations
# =========================================================================
def render_slide_12(c):
    draw_slide_header(
        c,
        "Technical Evaluation & Known Limitations",
        "Academic honesty: examining current design trade-offs and algorithmic constraints."
    )

    card_w = 480
    card_h = 165
    gap_x = 40

    x1 = 75
    x2 = x1 + card_w + gap_x
    y_row1 = top_y(330)
    y_row2 = top_y(530)

    # 1. Document-Level Blending
    draw_card(c, x1, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row1 + card_h - 38, "1", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row1 + card_h - 44, "Document-Level Aggregation")
    draw_multiline(c, x1 + 30, y_row1 + card_h - 85, "Each review produces one compound score, which blends mixed aspect opinions into an average.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 2. Sarcasm Detection
    draw_card(c, x2, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row1 + card_h - 38, "2", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row1 + card_h - 44, "Irony & Sarcasm Boundaries")
    draw_multiline(c, x2 + 30, y_row1 + card_h - 85, "Subtle literary sarcasm (e.g. 'What a joy to read 500 pages of filler') requires attention transformers.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 3. Era & Genre Variance
    draw_card(c, x1, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row2 + card_h - 38, "3", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row2 + card_h - 44, "Classical Prose Vocabulary")
    draw_multiline(c, x1 + 30, y_row2 + card_h - 85, "Standard modern lexicons occasionally misread archaic 19th-century adjectives in classical fiction.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 4. Proxy Ground Truth
    draw_card(c, x2, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row2 + card_h - 38, "4", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row2 + card_h - 44, "Proxy Star-Rating Validation")
    draw_multiline(c, x2 + 30, y_row2 + card_h - 85, "Validation relies on star ratings as proxy ground truth rather than crowd-annotated sentiment tags.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)


# =========================================================================
# SLIDE 13: Project Conclusion & Future Roadmap
# =========================================================================
def render_slide_13(c):
    c.saveState()
    c.setFillColor(C_DARK_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    c.setFont(FONT_TITLE, 38)
    c.setFillColor(C_WHITE)
    c.drawString(75, top_y(95), "Project Conclusion & Future Roadmap")

    col_w = 460
    col_y = top_y(195)

    # Column 1: Delivered Capabilities
    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_PRIMARY_LIGHT)
    c.drawString(75, col_y, "Delivered Capabilities")

    built_bullets = [
        "End-to-end 3-Tier Enterprise system deployed live with FastAPI and SQLite",
        "Dual sentiment engine combining VADER polarity and RAKE aspect extraction",
        "Interactive BI dashboard cataloging 36 books across 35 literary genres",
        "Managed under Agile Scrum with CPM activity crashing and budget tracking",
    ]

    by = col_y - 45
    for b in built_bullets:
        c.setFont(FONT_BOLD, 18)
        c.setFillColor(C_WHITE)
        c.drawString(75, by, "•")

        draw_multiline(c, 100, by, b, FONT_BODY, 15, C_WHITE, 25, col_w - 30)
        by -= 72

    # Column 2: Future Roadmap
    cx2 = 600
    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_PRIMARY_LIGHT)
    c.drawString(cx2, col_y, "Future Engineering Roadmap")

    next_bullets = [
        "Fine-tune domain-specific BERT / DeBERTa models for sentence-level ABSA",
        "Mobile barcode scanner integration for in-store instant book sentiment lookups",
        "Reader personalization engine combining sentiment profiles with collaborative filtering",
        "Cross-lingual sentiment mining for regional Indian and translated literature",
    ]

    by2 = col_y - 45
    for b in next_bullets:
        c.setFont(FONT_BOLD, 18)
        c.setFillColor(C_WHITE)
        c.drawString(cx2, by2, "•")

        draw_multiline(c, cx2 + 25, by2, b, FONT_BODY, 15, C_WHITE, 25, col_w - 30)
        by2 -= 72

    c.restoreState()


# =========================================================================
# MASTER GENERATION FUNCTION
# =========================================================================
def generate_deck(output_filename="Sentilink_Book_Review_Presentation.pdf"):
    print(f"Generating clean, original presentation deck: {output_filename} ...")
    c = canvas.Canvas(output_filename, pagesize=(W, H))

    renderers = [
        render_slide_1,
        render_slide_2,
        render_slide_3,
        render_slide_4,
        render_slide_5,
        render_slide_6,
        render_slide_7,
        render_slide_8,
        render_slide_9,
        render_slide_10,
        render_slide_11,
        render_slide_12,
        render_slide_13,
    ]

    for i, renderer in enumerate(renderers, 1):
        renderer(c)
        c.showPage()
        print(f"Rendered slide {i}/13.")

    c.save()
    print(f"Presentation successfully saved to {output_filename} ({os.path.getsize(output_filename):,} bytes).")


if __name__ == "__main__":
    generate_deck()
