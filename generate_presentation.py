"""
Sentilink Enterprise — Academic Project Presentation Deck
Smart Book Review Management & Customer Opinion Analytics
Theory behind the system: text mining, enterprise systems and IT project management
BVDU DET CSBS: ES, ASTMA, ITPM (Saloni Mahajan)

13 Clean, Pedagogical, High-Scoring Slides
- Elegant scholarly typography: Georgia-Bold titles, Segoe UI body
- High-contrast, easy-to-read cards, clean callouts, numbered step badges
- 100% Book Review domain content (crisp, grounded, non-exaggerated)
- Refined scholarly color scheme: Deep Navy (#0F172A), Royal Sapphire (#2563EB), Emerald (#059669)
"""

import os
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# 16:9 Widescreen slide dimensions
W, H = 1152, 648

# Scholarly Modern Palette
C_DARK_BG = colors.HexColor('#0F172A')       # Deep Oxford Navy for Slide 1 & 13
C_DARK_CARD = colors.HexColor('#1E293B')     # Charcoal Slate Container
C_LIGHT_BG = colors.HexColor('#F8FAFC')      # Crisp Light Slide Canvas (Slate 50)
C_WHITE = colors.HexColor('#FFFFFF')
C_CARD_BG = colors.HexColor('#FFFFFF')
C_CARD_TINT = colors.HexColor('#F1F5F9')     # Soft Tinted Container (Slate 100)
C_BORDER = colors.HexColor('#E2E8F0')        # Subtle Card Border (Slate 200)

# Typography Colors
C_TEXT_DARK = colors.HexColor('#0F172A')     # High-contrast charcoal heading (Slate 900)
C_TEXT_BODY = colors.HexColor('#334155')     # Slate-700 readable body text
C_TEXT_MUTED = colors.HexColor('#64748B')    # Slate-500 subtitle / caption
C_TEXT_WHITE = colors.HexColor('#FFFFFF')
C_TEXT_LIGHT_MUTED = colors.HexColor('#94A3B8')

# Accents (Scholarly Royal Blue & Semantic Colors)
C_PRIMARY = colors.HexColor('#2563EB')       # Royal Sapphire Blue
C_PRIMARY_LIGHT = colors.HexColor('#60A5FA')
C_PRIMARY_BG = colors.HexColor('#EFF6FF')
C_GREEN = colors.HexColor('#059669')         # Positive Sentiment Accent (Emerald)
C_SLATE_BAR = colors.HexColor('#64748B')     # Neutral Sentiment Accent
C_RED_BAR = colors.HexColor('#DC2626')       # Negative Sentiment Accent (Crimson)
C_AMBER = colors.HexColor('#D97706')         # Warning / Highlight

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
    # Crisp Light Canvas Base
    c.setFillColor(C_LIGHT_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Title
    c.setFillColor(C_TEXT_DARK)
    c.setFont(FONT_TITLE, 38)
    c.drawString(70, top_y(90), title)

    # Subtitle
    if subtitle:
        c.setFillColor(C_TEXT_MUTED)
        c.setFont(FONT_BODY, 15)
        c.drawString(70, top_y(128), subtitle)

    c.restoreState()


# =========================================================================
# SLIDE 1: Cover Slide
# =========================================================================
def render_slide_1(c):
    c.saveState()
    # Dark Canvas
    c.setFillColor(C_DARK_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Elegant curved ambient shapes on right
    c.setFillColor(colors.HexColor('#1E293B'))
    c.circle(W - 60, H / 2 + 70, 240, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#1E3A8A'))
    c.circle(W + 20, H / 2 - 80, 220, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#172554'))
    c.circle(W - 160, H / 2 - 120, 150, fill=1, stroke=0)

    # Top tracker
    c.setFont(FONT_BOLD, 15)
    c.setFillColor(colors.HexColor('#60A5FA'))
    c.drawString(75, top_y(160), "E S   ·   I T P M   ·   A S T M A")

    # Main Title (3 lines)
    c.setFont(FONT_TITLE, 44)
    c.setFillColor(C_WHITE)
    c.drawString(75, top_y(240), "Smart Book Review")
    c.drawString(75, top_y(298), "Management & Customer")
    c.drawString(75, top_y(356), "Opinion Analytics")

    # Subtitle
    c.setFont(FONT_BODY, 16)
    c.setFillColor(C_TEXT_LIGHT_MUTED)
    c.drawString(75, top_y(415), "Theory behind the system: text mining, enterprise systems and IT project management")

    # Student & Department line
    c.setFont(FONT_BODY, 13)
    c.setFillColor(colors.HexColor('#64748B'))
    c.drawString(75, top_y(540), "Saloni Mahajan   |   B.Tech Computer Science & Business Systems   |   BVDU DET Pune")

    c.restoreState()


# =========================================================================
# SLIDE 2: One system, three subjects
# =========================================================================
def render_slide_2(c):
    draw_slide_header(
        c,
        "One system, three subjects",
        "The project turns raw customer reviews into business decisions by combining three coursework areas."
    )

    # 3 Cards
    card_w = 318
    card_h = 245
    card_y = top_y(395)
    gap = 28
    start_x = 70

    cards_data = [
        ("1", "ASTMA", "Applied Statistics & Text Mining. Preprocessing, sentiment analysis and opinion mining on book review text.", C_PRIMARY),
        ("2", "ES", "Enterprise Systems. Database, book catalog and review management, and the analytics dashboard.", C_PRIMARY),
        ("3", "ITPM", "IT Project Management. WBS, schedule, resources, cost and risk planning.", C_PRIMARY),
    ]

    for i, (num, title, body, badge_col) in enumerate(cards_data):
        cx = start_x + i * (card_w + gap)
        draw_card(c, cx, card_y, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)

        # Number Badge
        draw_circle_badge(c, cx + 38, card_y + card_h - 40, num, r=18, bg=badge_col)

        # Title
        c.setFont(FONT_TITLE, 22)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(cx + 72, card_y + card_h - 48, title)

        # Body
        draw_multiline(c, cx + 26, card_y + card_h - 90, body, FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 52)

    # Bottom Stat Row
    stat_y = top_y(510)
    stats = [
        ("124+", "reviews\nanalysed", C_PRIMARY),
        ("3", "sentiment\nclasses", C_PRIMARY),
        ("10", "opinion\naspects", C_PRIMARY),
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
# SLIDE 3: The text-mining pipeline
# =========================================================================
def render_slide_3(c):
    draw_slide_header(c, "The text-mining pipeline")

    # 6 pipeline stages
    stages = [
        ("Collect", "review CSVs", False),
        ("Prepare", "prepare_dataset.py", False),
        ("Preprocess", "preprocessing.py", True),
        ("Sentiment", "sentiment_analysis.py", True),
        ("Opinions", "opinion_mining.py", True),
        ("Dashboard", "server.py", False),
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
            c.setFont(FONT_BOLD, 16)
            c.setFillColor(C_WHITE)
            c.drawCentredString(bx + box_w / 2, box_y + box_h - 40, name)
            c.setFont(FONT_BODY, 11)
            c.setFillColor(C_TEXT_LIGHT_MUTED)
            c.drawCentredString(bx + box_w / 2, box_y + 30, script)
        else:
            draw_card(c, bx, box_y, box_w, box_h, r=12, bg=C_CARD_TINT, border=C_BORDER)
            c.setFont(FONT_BOLD, 16)
            c.setFillColor(C_TEXT_DARK)
            c.drawCentredString(bx + box_w / 2, box_y + box_h - 40, name)
            c.setFont(FONT_BODY, 11)
            c.setFillColor(C_TEXT_MUTED)
            c.drawCentredString(bx + box_w / 2, box_y + 30, script)

        # Arrow indicator between boxes
        if i < len(stages) - 1:
            c.setFont(FONT_BOLD, 22)
            c.setFillColor(C_PRIMARY)
            c.drawString(bx + box_w + 8, box_y + box_h / 2 - 6, "›")

    # Dark boxes note
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(70, top_y(300), "Dark boxes are the ASTMA stages.")

    # "Why this order?" Box
    callout_y = top_y(470)
    callout_h = 135
    callout_w = W - 140
    draw_card(c, 70, callout_y, callout_w, callout_h, r=14, bg=C_CARD_TINT, border=C_BORDER)

    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(100, callout_y + callout_h - 42, "Why this order?")

    body_text = "Each stage feeds the next. Clean, uniform data gives more reliable scores, and scores plus aspects power the dashboard KPIs."
    draw_multiline(c, 100, callout_y + callout_h - 78, body_text, FONT_BODY, 15, C_TEXT_BODY, 24, callout_w - 60)


# =========================================================================
# SLIDE 4: Text preprocessing
# =========================================================================
def render_slide_4(c):
    draw_slide_header(c, "Text preprocessing")

    # Left: 5 numbered steps
    steps = [
        ("1", "Lowercasing", "Masterpiece and masterpiece become one token"),
        ("2", "Noise removal", "Strip URLs, numbers, punctuation symbols"),
        ("3", "Tokenisation", "Split review text into word tokens"),
        ("4", "Stopword removal", "Drop the, is, and, but"),
        ("5", "Lemmatisation", "reading becomes read"),
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
    card_h = 420
    card_y = top_y(520)
    draw_card(c, card_x, card_y, card_w, card_h, r=16, bg=C_DARK_CARD, stroke=0)

    # BEFORE Section
    c.setFont(FONT_BOLD, 13)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(card_x + 40, card_y + card_h - 50, "B E F O R E")

    before_quote = "The novel has amazing character development, but the pacing made the middle chapters very boring!"
    draw_multiline(c, card_x + 40, card_y + card_h - 90, before_quote, FONT_BODY, 16, C_WHITE, 26, card_w - 80)

    # Subtle divider
    c.setStrokeColor(colors.HexColor('#334155'))
    c.setLineWidth(1)
    c.line(card_x + 40, card_y + card_h - 220, card_x + card_w - 40, card_y + card_h - 220)

    # AFTER Section
    c.setFont(FONT_BOLD, 13)
    c.setFillColor(colors.HexColor('#38BDF8'))
    c.drawString(card_x + 40, card_y + card_h - 255, "A F T E R")

    after_quote = "novel amazing character development pacing make middle chapter bore"
    draw_multiline(c, card_x + 40, card_y + card_h - 295, after_quote, FONT_BODY, 16, colors.HexColor('#BAE6FD'), 26, card_w - 80)


# =========================================================================
# SLIDE 5: Three ways to classify sentiment
# =========================================================================
def render_slide_5(c):
    draw_slide_header(c, "Three ways to classify sentiment")

    card_w = 318
    card_h = 420
    card_y = top_y(540)
    gap = 28
    start_x = 70

    # Card 1: Lexicon-based (Dark Card)
    cx1 = start_x
    draw_card(c, cx1, card_y, card_w, card_h, r=16, bg=C_DARK_CARD, stroke=0)

    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_WHITE)
    c.drawString(cx1 + 30, card_y + card_h - 50, "Lexicon-based")

    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_LIGHT_MUTED)
    draw_multiline(c, cx1 + 30, card_y + card_h - 95, "Scores words against a pre-rated dictionary.", FONT_BODY, 14, C_TEXT_LIGHT_MUTED, 22, card_w - 60)

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_PRIMARY_LIGHT)
    c.drawString(cx1 + 30, card_y + card_h - 180, "Strength: ")
    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_WHITE)
    c.drawString(cx1 + 100, card_y + card_h - 180, "Fast, no training")
    c.drawString(cx1 + 30, card_y + card_h - 204, "data, explainable")

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(colors.HexColor('#F87171'))
    c.drawString(cx1 + 30, card_y + card_h - 260, "Limit: ")
    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_WHITE)
    c.drawString(cx1 + 75, card_y + card_h - 260, "Weak on sarcasm and")
    c.drawString(cx1 + 30, card_y + card_h - 284, "context")

    c.setFont(FONT_BOLD, 15)
    c.setFillColor(colors.HexColor('#FACC15'))
    c.drawString(cx1 + 30, card_y + 40, "Used here: VADER")

    # Card 2: Machine learning (Light Card)
    cx2 = start_x + card_w + gap
    draw_card(c, cx2, card_y, card_w, card_h, r=16, bg=C_CARD_TINT, border=C_BORDER)

    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(cx2 + 30, card_y + card_h - 50, "Machine learning")

    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_BODY)
    draw_multiline(c, cx2 + 30, card_y + card_h - 95, "Trains Naive Bayes or SVM on labelled reviews.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_PRIMARY)
    c.drawString(cx2 + 30, card_y + card_h - 180, "Strength: ")
    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx2 + 100, card_y + card_h - 180, "Learns domain")
    c.drawString(cx2 + 30, card_y + card_h - 204, "wording")

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_RED_BAR)
    c.drawString(cx2 + 30, card_y + card_h - 260, "Limit: ")
    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx2 + 75, card_y + card_h - 260, "Needs labelled data")

    # Card 3: Deep learning (Light Card)
    cx3 = start_x + 2 * (card_w + gap)
    draw_card(c, cx3, card_y, card_w, card_h, r=16, bg=C_CARD_TINT, border=C_BORDER)

    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(cx3 + 30, card_y + card_h - 50, "Deep learning")

    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_BODY)
    draw_multiline(c, cx3 + 30, card_y + card_h - 95, "Transformers such as BERT learn context.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_PRIMARY)
    c.drawString(cx3 + 30, card_y + card_h - 180, "Strength: ")
    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx3 + 100, card_y + card_h - 180, "Best accuracy on")
    c.drawString(cx3 + 30, card_y + card_h - 204, "nuance")

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_RED_BAR)
    c.drawString(cx3 + 30, card_y + card_h - 260, "Limit: ")
    c.setFont(FONT_BODY, 14)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(cx3 + 75, card_y + card_h - 260, "Heavy compute and")
    c.drawString(cx3 + 30, card_y + card_h - 284, "data")


# =========================================================================
# SLIDE 6: How VADER scores a review
# =========================================================================
def render_slide_6(c):
    draw_slide_header(c, "How VADER scores a review")

    # Left: 5 heuristics
    heuristics = [
        ("1", "Punctuation", "!!! raises intensity"),
        ("2", "Capitalisation", "GREAT is stronger than great"),
        ("3", "Degree modifiers", "very, slightly"),
        ("4", "Negation", "not good flips polarity"),
        ("5", "Contrast", "but shifts weight to the end"),
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

    c.setFont(FONT_TITLE, 22)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(rx, top_y(180), "Compound score: -1 to +1")

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
    c.drawCentredString(rx + seg_w + seg_w / 2, bar_y + 18, "in between")

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

    call_text = "The output also includes pos, neu and neg proportions. Your code classifies using only the compound value."
    draw_multiline(c, rx + 30, call_y + call_h - 55, call_text, FONT_BODY, 15, C_TEXT_BODY, 26, rw - 60)


# =========================================================================
# SLIDE 7: Opinion mining: what is the review about? (Book Aspects)
# =========================================================================
def render_slide_7(c):
    draw_slide_header(
        c,
        "Opinion mining: what is the review about?",
        "A keyword dictionary maps each aspect to indicator words, matched with word-boundary regex. Simple, fast and explainable."
    )

    # 10 Book Aspect pills (2 rows of 5)
    row1 = ["plot", "characters", "pacing", "writing style", "ending"]
    row2 = ["world building", "emotion", "theme", "cover design", "price"]

    pill_w = 175
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
    c.drawString(card_x + 40, card_y + card_h - 45, "R E V I E W")

    rev_quote = "The novel has amazing character development but the pacing was slow and the ending was rushed."
    draw_multiline(c, card_x + 40, card_y + card_h - 85, rev_quote, FONT_BODY, 16, C_WHITE, 26, 480)

    # Right: ASPECTS DETECTED
    c.setFont(FONT_BOLD, 13)
    c.setFillColor(colors.HexColor('#94A3B8'))
    c.drawString(card_x + 560, card_y + card_h - 45, "A S P E C T S   D E T E C T E D")

    c.setFont(FONT_BODY, 16)
    c.setFillColor(colors.HexColor('#38BDF8'))
    c.drawString(card_x + 560, card_y + card_h - 85, "characters, pacing, ending")


# =========================================================================
# SLIDE 8: Enterprise system architecture (Books domain)
# =========================================================================
def render_slide_8(c):
    draw_slide_header(c, "Enterprise system architecture")

    # Left: 3 Tier layers
    lx = 75
    lw = 480

    # Layer 1: Presentation (Dark Card)
    y1 = top_y(260)
    draw_card(c, lx, y1, lw, 95, r=14, bg=C_DARK_CARD, stroke=0)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_WHITE)
    c.drawString(lx + 28, y1 + 55, "Presentation layer")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_LIGHT_MUTED)
    c.drawString(lx + 28, y1 + 25, "server.py & static web dashboard (HTML/CSS/JS)")

    # Layer 2: Business logic (Royal Blue Card)
    y2 = top_y(385)
    draw_card(c, lx, y2, lw, 95, r=14, bg=C_PRIMARY, stroke=0)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_WHITE)
    c.drawString(lx + 28, y2 + 55, "Business logic layer")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(colors.HexColor('#DBEAFE'))
    c.drawString(lx + 28, y2 + 25, "sentiment_analysis.py, opinion_mining.py")

    # Layer 3: Data layer (Light Card)
    y3 = top_y(510)
    draw_card(c, lx, y3, lw, 95, r=14, bg=C_CARD_TINT, border=C_BORDER)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(lx + 28, y3 + 55, "Data layer")
    c.setFont(FONT_BODY, 13)
    c.setFillColor(C_TEXT_MUTED)
    c.drawString(lx + 28, y3 + 25, "SQLite: books, users and reviews tables")

    # Right: What makes it an enterprise system
    rx = 620
    rw = 450
    c.setFont(FONT_TITLE, 24)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(rx, top_y(205), "What makes it an enterprise")
    c.drawString(rx, top_y(240), "system")

    bullets = [
        "Integrates data and processes on one shared platform",
        "Supports CRUD on books and reader reviews",
        "Turns stored data into decision support",
    ]

    by = top_y(300)
    for b in bullets:
        c.setFont(FONT_BOLD, 18)
        c.setFillColor(C_PRIMARY)
        c.drawString(rx, by, "•")

        draw_multiline(c, rx + 24, by, b, FONT_BODY, 15, C_TEXT_BODY, 24, rw - 30)
        by -= 68


# =========================================================================
# SLIDE 9: Data layer and business intelligence (Books domain)
# =========================================================================
def render_slide_9(c):
    draw_slide_header(c, "Data layer and business intelligence")

    card_w = 480
    card_h = 165
    gap_x = 40

    x1 = 75
    x2 = x1 + card_w + gap_x
    y_row1 = top_y(330)
    y_row2 = top_y(530)

    # 1. Relational database
    draw_card(c, x1, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row1 + card_h - 38, "1", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row1 + card_h - 44, "Relational database")
    draw_multiline(c, x1 + 30, y_row1 + card_h - 82, "Books and reviews tables with CRUD operations in SQLite.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 2. Indexing
    draw_card(c, x2, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row1 + card_h - 38, "2", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row1 + card_h - 44, "Indexing")
    draw_multiline(c, x2 + 30, y_row1 + card_h - 82, "Indexes on sentiment, genre, rating, and book title speed up filters.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 3. Chunked processing
    draw_card(c, x1, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row2 + card_h - 38, "3", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row2 + card_h - 44, "Chunked processing")
    draw_multiline(c, x1 + 30, y_row2 + card_h - 82, "Reviews load in batches so entire corpus fits in memory efficiently.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 4. BI dashboard
    draw_card(c, x2, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row2 + card_h - 38, "4", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 20)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row2 + card_h - 44, "BI dashboard")
    draw_multiline(c, x2 + 30, y_row2 + card_h - 82, "KPIs, distributions and aspect charts, cached for 5 minutes.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)


# =========================================================================
# SLIDE 10: IT project management
# =========================================================================
def render_slide_10(c):
    draw_slide_header(c, "IT project management")

    # Left: 6 numbered steps
    items = [
        ("1", "WBS", "Break the project into work packages"),
        ("2", "Schedule", "16 weeks with a Gantt-style view"),
        ("3", "Milestones", "Eight checkpoints, week 1 to 16"),
        ("4", "Resources", "Roles allocated by percentage"),
        ("5", "Cost", "Bottom-up budget estimate"),
        ("6", "Risk", "Rate, then mitigate"),
    ]

    start_y = top_y(190)
    gap_y = 56
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

    # Right: Horizontal bar chart
    rx = 560

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(rx + 90, top_y(175), "Cost estimate by component (INR)")

    bars = [
        ("Software Development", 25000, "25,000"),
        ("Database & Cloud", 10000, "10,000"),
        ("Testing", 8000, "8,000"),
        ("Miscellaneous", 7000, "7,000"),
        ("Documentation", 5000, "5,000"),
    ]

    by = top_y(235)
    bar_max_val = 28000
    bar_max_w = 210

    for name, val, val_str in bars:
        # Category label
        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_BODY)
        c.drawRightString(rx + 155, by + 4, name)

        # Grey axis separator line
        c.setStrokeColor(colors.HexColor('#CBD5E1'))
        c.setLineWidth(1)
        c.line(rx + 165, by - 12, rx + 165, by + 24)

        # Bar
        bw = (val / bar_max_val) * bar_max_w
        c.setFillColor(C_PRIMARY)
        c.rect(rx + 166, by, bw, 22, fill=1, stroke=0)

        # Value label
        c.setFont(FONT_BODY, 13)
        c.setFillColor(C_TEXT_DARK)
        c.drawString(rx + 166 + bw + 10, by + 4, val_str)

        by -= 48

    # Total Cost Callout
    tot_y = top_y(540)
    c.setFont(FONT_BOLD, 36)
    c.setFillColor(C_PRIMARY)
    c.drawString(rx + 10, tot_y, "Rs. 55,000")

    tw = c.stringWidth("Rs. 55,000", FONT_BOLD, 36)
    c.setFont(FONT_BODY, 15)
    c.setFillColor(C_TEXT_BODY)
    c.drawString(rx + 10 + tw + 12, tot_y + 4, "total estimated cost")


# =========================================================================
# SLIDE 11: Risk register
# =========================================================================
def render_slide_11(c):
    draw_slide_header(c, "Risk register")

    # Clean Table
    tx = 75
    ty = top_y(530)
    tw = W - 150
    th = 380

    col_widths = [300, 110, 110, 482]
    headers = ["Risk", "Probability", "Impact", "Mitigation"]

    rows = [
        ("Poor review data quality", "Medium", "High", "Clean and validate review data"),
        ("Incorrect sentiment classification", "Medium", "Medium", "Test NLP model with sample reviews"),
        ("Database failure", "Low", "High", "Maintain database backup"),
        ("Project schedule delay", "Medium", "High", "Track schedule and milestones"),
        ("Integration problems", "Medium", "Medium", "Test modules independently first"),
        ("Insufficient testing", "Low", "Medium", "Prepare test cases"),
    ]

    # Header Row
    c.setFillColor(C_DARK_CARD)
    c.rect(tx, ty + th - 48, tw, 48, fill=1, stroke=0)

    c.setFont(FONT_BOLD, 14)
    c.setFillColor(C_WHITE)
    cur_x = tx + 20
    for j, h_text in enumerate(headers):
        c.drawString(cur_x, ty + th - 32, h_text)
        cur_x += col_widths[j]

    # Data Rows
    row_h = 52
    for i, row in enumerate(rows):
        ry = ty + th - 48 - (i + 1) * row_h

        # Alternating background
        if i % 2 == 1:
            c.setFillColor(colors.HexColor('#F8FAFC'))
            c.rect(tx, ry, tw, row_h, fill=1, stroke=0)

        # Thin border bottom
        c.setStrokeColor(C_BORDER)
        c.setLineWidth(0.8)
        c.line(tx, ry, tx + tw, ry)

        # Row Text
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
# SLIDE 12: Limitations to acknowledge
# =========================================================================
def render_slide_12(c):
    draw_slide_header(c, "Limitations to acknowledge")

    card_w = 480
    card_h = 165
    gap_x = 40

    x1 = 75
    x2 = x1 + card_w + gap_x
    y_row1 = top_y(330)
    y_row2 = top_y(530)

    # 1. Preprocessing clashes with VADER
    draw_card(c, x1, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row1 + card_h - 38, "1", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row1 + card_h - 35, "Preprocessing clashes with")
    c.drawString(x1 + 68, y_row1 + card_h - 58, "VADER")
    draw_multiline(c, x1 + 30, y_row1 + card_h - 96, "Removing stopwords and punctuation strips negation and emphasis cues.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 2. Document-level sentiment
    draw_card(c, x2, y_row1, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row1 + card_h - 38, "2", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row1 + card_h - 44, "Document-level sentiment")
    draw_multiline(c, x2 + 30, y_row1 + card_h - 85, "One score per review, so aspects are detected but not scored separately.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 3. Keyword matching
    draw_card(c, x1, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x1 + 38, y_row2 + card_h - 38, "3", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x1 + 68, y_row2 + card_h - 44, "Keyword matching")
    draw_multiline(c, x1 + 30, y_row2 + card_h - 85, "Misses synonyms and context; a word like good fits many aspects.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)

    # 4. No ground truth check
    draw_card(c, x2, y_row2, card_w, card_h, r=14, bg=C_CARD_TINT, border=C_BORDER)
    draw_circle_badge(c, x2 + 38, y_row2 + card_h - 38, "4", r=16, bg=C_PRIMARY)
    c.setFont(FONT_TITLE, 19)
    c.setFillColor(C_TEXT_DARK)
    c.drawString(x2 + 68, y_row2 + card_h - 44, "No ground truth check")
    draw_multiline(c, x2 + 30, y_row2 + card_h - 85, "Labels are not yet compared with star ratings.", FONT_BODY, 14, C_TEXT_BODY, 22, card_w - 60)


# =========================================================================
# SLIDE 13: Conclusion and future work
# =========================================================================
def render_slide_13(c):
    c.saveState()
    # Dark Canvas
    c.setFillColor(C_DARK_BG)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Title
    c.setFont(FONT_TITLE, 40)
    c.setFillColor(C_WHITE)
    c.drawString(75, top_y(100), "Conclusion and future work")

    col_w = 460
    col_y = top_y(200)

    # Column 1: What we built
    c.setFont(FONT_TITLE, 24)
    c.setFillColor(C_PRIMARY_LIGHT)
    c.drawString(75, col_y, "What we built")

    built_bullets = [
        "End-to-end pipeline from raw reviews to dashboard",
        "VADER sentiment plus aspect detection",
        "Enterprise data layer for books and reviews",
        "Planned and tracked with ITPM tools",
    ]

    by = col_y - 45
    for b in built_bullets:
        c.setFont(FONT_BOLD, 18)
        c.setFillColor(C_WHITE)
        c.drawString(75, by, "•")

        draw_multiline(c, 100, by, b, FONT_BODY, 16, C_WHITE, 26, col_w - 30)
        by -= 68

    # Column 2: Next steps
    cx2 = 600
    c.setFont(FONT_TITLE, 24)
    c.setFillColor(C_PRIMARY_LIGHT)
    c.drawString(cx2, col_y, "Next steps")

    next_bullets = [
        "Aspect-based sentiment analysis (ABSA)",
        "Transformer models such as BERT",
        "Evaluate with precision, recall and F1",
        "Skip heavy cleaning before VADER",
    ]

    by2 = col_y - 45
    for b in next_bullets:
        c.setFont(FONT_BOLD, 18)
        c.setFillColor(C_WHITE)
        c.drawString(cx2, by2, "•")

        draw_multiline(c, cx2 + 25, by2, b, FONT_BODY, 16, C_WHITE, 26, col_w - 30)
        by2 -= 68

    c.restoreState()


# =========================================================================
# MASTER GENERATION FUNCTION
# =========================================================================
def generate_deck(output_filename="Sentilink_Book_Review_Presentation.pdf"):
    print(f"Generating clean, pedagogical presentation deck: {output_filename} ...")
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
