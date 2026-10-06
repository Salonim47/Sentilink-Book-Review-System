"""
Sentilink Enterprise — Executive Keynote Deck Generator
Autonomous Book Review Sentiment Analysis, Opinion Mining & Enterprise Decision Support System
BVDU DET CSBS: Enterprise Systems, ASTMA, IT Project Management

Completely unique, ultra-modern Cyber-Executive / Dark Glassmorphism aesthetic.
Distinct from the classmate's retro plum/pink presentation:
- Tech Palette: Obsidian Navy (#080c16), Slate Glass (#131c2e), Electric Cyan (#06b6d4),
  Cyber Indigo (#6366f1), Emerald Mint (#10b981), and Coral Rose (#f43f5e).
- Layout: Modern 16:9 widescreen, glowing category badges, tech card containers,
  accent top-stripes, metric stat blocks, and clean typographic hierarchy.
"""

import os
from reportlab.lib.pagesizes import landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Slide dimensions: 16:9 widescreen (1152 x 648 pt)
W, H = 1152, 648

# Color Palette — Cyber-Executive Modern Dark Theme
BG_DARK = colors.HexColor('#080d1a')          # Deep Obsidian Navy
BG_SLATE = colors.HexColor('#0f172a')         # Midnight Slate
CARD_BG = colors.HexColor('#131e33')          # Dark Glass Container
CARD_BORDER = colors.HexColor('#202e47')      # Subtle Slate Border
CARD_BORDER_HI = colors.HexColor('#334668')   # Active Slate Border

TEXT_WHITE = colors.HexColor('#f8fafc')       # Primary Crisp White
TEXT_MUTED = colors.HexColor('#94a3b8')       # Muted Slate
TEXT_SUBTLE = colors.HexColor('#64748b')      # Subtle Gray
TEXT_CODE = colors.HexColor('#cbd5e1')        # Code Monospace Text

CYAN = colors.HexColor('#06b6d4')             # Electric Cyan (ASTMA / NLP)
CYAN_GLOW = colors.HexColor('#22d3ee')
INDIGO = colors.HexColor('#6366f1')           # Cyber Indigo (ES / System)
INDIGO_LIGHT = colors.HexColor('#818cf8')
EMERALD = colors.HexColor('#10b981')          # Emerald Mint (Positive / ITPM)
EMERALD_LIGHT = colors.HexColor('#34d399')
ROSE = colors.HexColor('#f43f5e')             # Coral Rose (Negative / Risk)
AMBER = colors.HexColor('#f59e0b')            # Amber Gold (Neutral / Warning)
PURPLE = colors.HexColor('#a855f7')           # Royal Violet (Aspects)

# Register Crisp Windows TrueType Fonts
FONT_HEADING = 'Helvetica-Bold'
FONT_REGULAR = 'Helvetica'
FONT_BOLD = 'Helvetica-Bold'

fonts_dir = r'C:\Windows\Fonts'
if os.path.exists(os.path.join(fonts_dir, 'segoeuib.ttf')) and os.path.exists(os.path.join(fonts_dir, 'segoeui.ttf')):
    try:
        pdfmetrics.registerFont(TTFont('SegoeUI', os.path.join(fonts_dir, 'segoeui.ttf')))
        pdfmetrics.registerFont(TTFont('SegoeUI-Bold', os.path.join(fonts_dir, 'segoeuib.ttf')))
        FONT_REGULAR = 'SegoeUI'
        FONT_BOLD = 'SegoeUI-Bold'
        FONT_HEADING = 'SegoeUI-Bold'
    except Exception:
        pass


def top_y(dist):
    return H - dist


def draw_tech_background(c):
    c.saveState()
    # Dark Canvas
    c.setFillColor(BG_DARK)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Ambient Top Glow Accent Line
    c.setFillColor(INDIGO)
    c.rect(0, H - 4, W, 4, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.rect(0, H - 4, 380, 4, fill=1, stroke=0)

    # Subtle ambient circle glow in corner
    c.setFillColor(colors.HexColor('#0e172f'))
    c.circle(W - 40, H - 40, 220, fill=1, stroke=0)
    c.setFillColor(colors.HexColor('#0a1122'))
    c.circle(80, 40, 160, fill=1, stroke=0)

    # Bottom watermark footer
    c.setFillColor(TEXT_SUBTLE)
    c.setFont(FONT_REGULAR, 9)
    c.drawString(60, 22, "SENTILINK ENTERPRISE © 2026 • BVDU DET PUNE CSBS • ELECTIVE VI A · IV B · ITPM")
    c.drawRightString(W - 60, 22, "3-TIER MVC + SOA ARCHITECTURE • CONFIDENTIAL PROJECT REPORT")
    c.restoreState()


def draw_card(c, x, y, w, h, r=12, top_accent=None, bg=CARD_BG, border=CARD_BORDER):
    c.saveState()
    c.setFillColor(bg)
    c.setStrokeColor(border)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1)

    # Optional top accent bar
    if top_accent:
        c.setFillColor(top_accent)
        c.roundRect(x + 1, y + h - 5, w - 2, 4, 2, fill=1, stroke=0)
    c.restoreState()


def draw_badge(c, text, x, y, bg_col, text_col, font_size=10, px=10, py=5):
    c.saveState()
    c.setFont(FONT_BOLD, font_size)
    tw = c.stringWidth(text, FONT_BOLD, font_size)
    bw = tw + px * 2
    bh = font_size + py * 2
    c.setFillColor(bg_col)
    c.roundRect(x, y, bw, bh, bh / 2.0, fill=1, stroke=0)
    c.setFillColor(text_col)
    c.drawString(x + px, y + py, text)
    c.restoreState()
    return bw


def draw_slide_header(c, category, title, subtitle=None):
    c.saveState()
    # Category tag with cyan indicator dot
    c.setFillColor(CYAN)
    c.circle(65, top_y(54), 4, fill=1, stroke=0)
    c.setFont(FONT_BOLD, 11)
    c.drawString(76, top_y(58), category.upper())

    # Main Title
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 28)
    c.drawString(60, top_y(95), title)

    # Subtitle
    if subtitle:
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 13)
        c.drawString(60, top_y(122), subtitle)
    c.restoreState()


# =========================================================================
# SLIDE 1: Cover Keynote Slide
# =========================================================================
def render_slide_1(c):
    draw_tech_background(c)
    c.saveState()

    # Glowing Badge Top
    draw_badge(c, "ENTERPRISE AI PLATFORM • 2026 CAPSTONE EDITION", 70, top_y(160),
               colors.HexColor('#1e2942'), CYAN, font_size=11, px=14, py=6)

    # Primary Title
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 44)
    c.drawString(70, top_y(225), "SENTILINK ENTERPRISE")

    # Gradient-like Accent Subheading
    c.setFillColor(CYAN_GLOW)
    c.setFont(FONT_HEADING, 24)
    c.drawString(70, top_y(268), "Autonomous Book Review Sentiment Analysis & Reader Opinion Mining")

    # Long Executive Description
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 15)
    c.drawString(70, top_y(320), "A production 3-Tier MVC architecture unifying multi-method NLP text mining,")
    c.drawString(70, top_y(345), "real-time opinion extraction, and rigorous IT project delivery governance.")

    # 3 Subject Triad Chips at Bottom
    chips_y = top_y(460)
    chip_w = 320
    gap = 25

    chips = [
        ("ELECTIVE VI A", "Enterprise Systems", "SOA REST, Master Data, RBAC & 5-Yr TCO", INDIGO),
        ("ELECTIVE IV B", "Advanced Text Analytics", "VADER, RAKE, K-Means & Apriori Rules", CYAN),
        ("IT PROJECT MGMT", "ITPM Governance", "WBS, 16-Wk Plan, PERT CPM & ₹55k Cost", EMERALD)
    ]

    for i, (subj, title, desc, col) in enumerate(chips):
        cx = 70 + i * (chip_w + gap)
        draw_card(c, cx, chips_y, chip_w, 105, r=10, top_accent=col)

        c.setFillColor(col)
        c.setFont(FONT_BOLD, 10)
        c.drawString(cx + 18, chips_y + 76, subj)

        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_HEADING, 15)
        c.drawString(cx + 18, chips_y + 52, title)

        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(cx + 18, chips_y + 26, desc)

    # Institutional Tag
    c.setFillColor(TEXT_SUBTLE)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(70, top_y(545), "Bharati Vidyapeeth Deemed University (BVDU DET Pune) • Computer Science & Business Systems")

    c.restoreState()
    c.showPage()


# =========================================================================
# SLIDE 2: Executive Summary & Coursework Synthesis
# =========================================================================
def render_slide_2(c):
    draw_tech_background(c)
    draw_slide_header(c, "Executive Overview", "One Unified Platform • Three Core Subject Pillars",
                      "Bridging academic theory with enterprise production engineering across ES, ASTMA, and ITPM.")

    card_w = 325
    card_h = 320
    card_y = top_y(465)
    gap = 28
    start_x = 60

    pillars = [
        ("ASTMA", CYAN, "Text & Media Analytics", [
            ("Unsupervised Topics", "K-Means discovery of 4 latent themes"),
            ("Valence Scoring", "Dual VADER + Supervised Naive Bayes"),
            ("Keyphrase Mining", "RAKE word degree to frequency ratio"),
            ("Network Analytics", "Bipartite reader-book social graph")
        ]),
        ("ES", INDIGO, "Enterprise Systems", [
            ("3-Tier Architecture", "Presentation, SOA API, Relational DB"),
            ("Master Catalog", "36 books across 35 distinct genres"),
            ("RBAC Security", "Admin moderation vs Customer workflows"),
            ("Economic Modeling", "5-Year TCO: COTS vs Bespoke build")
        ]),
        ("ITPM", EMERALD, "Project Delivery", [
            ("Scope & WBS", "5 Work packages & 15 discrete tasks"),
            ("Schedule Control", "16-Week lifecycle & 7 stage-gates"),
            ("CPM / PERT", "Probabilistic expected duration & variance"),
            ("Cost Governance", "Bottom-up ₹55,000 budget tracking")
        ])
    ]

    for i, (pill_tag, col, title, bullets) in enumerate(pillars):
        cx = start_x + i * (card_w + gap)
        draw_card(c, cx, card_y, card_w, card_h, r=12, top_accent=col)

        draw_badge(c, pill_tag, cx + 22, card_y + card_h - 40, colors.HexColor('#1c2842'), col, font_size=11)

        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_HEADING, 19)
        c.drawString(cx + 22, card_y + card_h - 72, title)

        by = card_y + card_h - 110
        for b_head, b_desc in bullets:
            c.setFillColor(col)
            c.circle(cx + 26, by + 4, 3, fill=1, stroke=0)

            c.setFillColor(TEXT_WHITE)
            c.setFont(FONT_BOLD, 12)
            c.drawString(cx + 36, by, b_head)

            c.setFillColor(TEXT_MUTED)
            c.setFont(FONT_REGULAR, 11)
            c.drawString(cx + 36, by - 16, b_desc)
            by -= 44

    # Bottom Stat Counters
    stat_y = top_y(575)
    stat_w = 235
    stat_gap = 28
    stats = [
        ("124+ Stored Reviews", "Validated Corpus", CYAN),
        ("35 Master Genres", "Literature Diversity", INDIGO),
        ("10 Domain Aspects", "Opinion Dimensions", PURPLE),
        ("₹55,000 Budget", "Strict Financial Cap", EMERALD)
    ]

    for i, (val, label, col) in enumerate(stats):
        sx = start_x + i * (stat_w + stat_gap)
        draw_card(c, sx, stat_y, stat_w, 75, r=8, bg=colors.HexColor('#0c1424'))

        c.setFillColor(col)
        c.setFont(FONT_HEADING, 18)
        c.drawString(sx + 16, stat_y + 40, val)

        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(sx + 16, stat_y + 18, label)

    c.showPage()


# =========================================================================
# SLIDE 3: End-to-End System Architecture (3-Tier MVC + SOA)
# =========================================================================
def render_slide_3(c):
    draw_tech_background(c)
    draw_slide_header(c, "Enterprise Systems", "3-Tier MVC Architecture & Service-Oriented Framework",
                      "Clean separation of concerns with asynchronous REST contracts and relational ACID transactions.")

    # 3 Layers Stacked
    lx = 60
    layer_w = 640
    layer_h = 105
    gap = 20

    layers = [
        ("Presentation Layer (Client Tier)",
         "Tailwind CSS 3.0 • Vanilla JS (ES6+) • Chart.js 4.4 • Lucide Icons",
         "Responsive multi-view dashboard, live NLP typing feedback, category filters & modal inspectors.",
         CYAN),
        ("Business Logic Layer (Application Tier)",
         "FastAPI SOA Controller • Python 3.13 • Pydantic V2 • nlp_engine.py",
         "20+ REST endpoints, VADER valence calculation, RAKE keyphrase extractor, K-Means & Apriori.",
         INDIGO),
        ("Data Persistence Layer (Database Tier)",
         "SQLite 3.45 • B-Tree Indexing • Foreign Key Constraints • WAL Journaling",
         "Relational schema: books, reviews, users, audit_logs. Sub-5ms query lookups.",
         EMERALD)
    ]

    ly = top_y(175)
    for title, tech, desc, col in layers:
        ly -= layer_h
        draw_card(c, lx, ly, layer_w, layer_h, r=10, top_accent=col)

        c.setFillColor(col)
        c.setFont(FONT_BOLD, 11)
        c.drawString(lx + 24, ly + layer_h - 26, title.upper())

        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_HEADING, 15)
        c.drawString(lx + 24, ly + layer_h - 50, tech)

        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 12)
        c.drawString(lx + 24, ly + 20, desc)

        ly -= gap

    # Right Side: Architectural Quality Attributes
    rx = 730
    rw = 360
    rh = 365
    ry = top_y(515)
    draw_card(c, rx, ry, rw, rh, r=12, top_accent=PURPLE)

    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 20)
    c.drawString(rx + 24, ry + rh - 40, "Enterprise System Criteria")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(rx + 24, ry + rh - 64, "Key attributes ensuring production viability:")

    criteria = [
        ("Shared Single Source of Truth", "Catalog, reviews, and NLP predictions live on one synchronized platform."),
        ("Strict ACID Transactionality", "Atomic review submission with audit log triggers prevents state drift."),
        ("Role-Based Access Control", "Customer review submission vs Admin review moderation & book management."),
        ("Microservice Ready SOA", "Headless REST design allows hot-swapping NLP backends without UI disruption.")
    ]

    cy = ry + rh - 105
    for c_title, c_desc in criteria:
        c.setFillColor(PURPLE)
        c.circle(rx + 28, cy + 3, 3, fill=1, stroke=0)

        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 13)
        c.drawString(rx + 38, cy, c_title)

        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(rx + 38, cy - 16, c_desc[:48])
        c.drawString(rx + 38, cy - 30, c_desc[48:])
        cy -= 60

    c.showPage()


# =========================================================================
# SLIDE 4: Complete Text Mining Pipeline
# =========================================================================
def render_slide_4(c):
    draw_tech_background(c)
    draw_slide_header(c, "ASTMA Pipeline", "6-Stage Asynchronous Text Mining & NLP Workflow",
                      "Sequential enrichment transforming raw unstructured customer reviews into actionable intelligence.")

    # 6 Step Blocks
    step_w = 160
    step_h = 170
    start_x = 60
    gap = 14
    sy = top_y(320)

    steps = [
        ("01", "INGESTION", "Multi-Source Feed", "Amazon, Kaggle & User Submitted Text", colors.HexColor('#334155')),
        ("02", "CLEANING", "Noise Strip", "URLs, HTML tags, special symbols & case fold", colors.HexColor('#334155')),
        ("03", "TOKENIZE", "Linguistic Split", "Atomic word tokens & stopword elimination", CYAN),
        ("04", "VALENCE", "VADER Scoring", "Compound [-1, +1] & punctuation boost", INDIGO),
        ("05", "ASPECTS", "Domain Regex", "10 Literary aspects & RAKE keyphrase tags", PURPLE),
        ("06", "EXECUTIVE", "BI Dashboard", "Real-time KPIs, CSAT gauge & visual charts", EMERALD)
    ]

    for i, (num, tag, title, desc, col) in enumerate(steps):
        sx = start_x + i * (step_w + gap)
        draw_card(c, sx, sy, step_w, step_h, r=10, top_accent=col)

        # Step Number
        c.setFillColor(col)
        c.setFont(FONT_HEADING, 24)
        c.drawString(sx + 16, sy + step_h - 35, num)

        # Stage Tag
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_BOLD, 9)
        c.drawString(sx + 16, sy + step_h - 55, tag)

        # Stage Title
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_HEADING, 13)
        c.drawString(sx + 16, sy + step_h - 80, title)

        # Description
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(sx + 16, sy + 38, desc[:22])
        c.drawString(sx + 16, sy + 22, desc[22:])

    # Pipeline Callout Card Below
    callout_y = top_y(540)
    callout_h = 165
    callout_w = W - 120
    draw_card(c, 60, callout_y, callout_w, callout_h, r=12, top_accent=CYAN)

    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 19)
    c.drawString(85, callout_y + callout_h - 38, "Architectural Pipeline Rationale")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 13)
    c.drawString(85, callout_y + callout_h - 70,
                 "1. Deterministic Sequential Ingestion: Raw reviews must undergo schema validation prior to tokenisation.")
    c.drawString(85, callout_y + callout_h - 95,
                 "2. VADER Raw Context Preservation: Unlike TF-IDF, VADER requires punctuation ('!') and capitalization for intensity scoring.")
    c.drawString(85, callout_y + callout_h - 120,
                 "3. Aspect-Polarity Decoupling: Extracting domain features independently allows negative sentiment to isolate specific flaws.")

    c.showPage()


# =========================================================================
# SLIDE 5: Dual Sentiment Classification (Lexicon vs Supervised ML)
# =========================================================================
def render_slide_5(c):
    draw_tech_background(c)
    draw_slide_header(c, "ASTMA Unit II", "Sentiment Classification: Rule-Based VADER vs Supervised ML",
                      "Production deployment of lexical heuristics benchmarked against TF-IDF Naive Bayes classification.")

    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: VADER Production Engine
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=CYAN)

    draw_badge(c, "PRODUCTION ENGINE", lx + 24, cy + ch - 38, colors.HexColor('#162b3d'), CYAN, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(lx + 24, cy + ch - 70, "VADER Lexicon & Rule Engine")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(lx + 24, cy + ch - 94, "Gold-standard valence dictionary optimized for micro-text and consumer reviews.")

    vader_rules = [
        ("Punctuation Intensity", "Repeated exclamation marks ('Must read!!!') increase polarity weight."),
        ("Capitalisation Booster", "ALL-CAPS words ('AMAZING worldbuilding') amplify positive valence."),
        ("Degree Adverb Modifiers", "'deeply touching' boosts score; 'slightly predictable' dampens score."),
        ("Polarity Flipping Negation", "'not gripping' or 'never connected' inverts positive word polarity."),
        ("Contrastive 'BUT' Conjunction", "Shifts emotional weight to the trailing clause: 'Pacing was slow, BUT loved it.'")
    ]

    vy = cy + ch - 130
    for r_head, r_desc in vader_rules:
        c.setFillColor(CYAN)
        c.circle(lx + 28, vy + 3, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(lx + 38, vy, r_head)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(lx + 38, vy - 15, r_desc)
        vy -= 44

    # Right: Supervised ML Benchmark
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=INDIGO)

    draw_badge(c, "ACADEMIC BENCHMARK", rx + 24, cy + ch - 38, colors.HexColor('#242147'), INDIGO, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(rx + 24, cy + ch - 70, "TF-IDF + Multinomial Naive Bayes")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(rx + 24, cy + ch - 94, "Supervised classification model trained on n-gram frequency matrices.")

    # Metrics Box
    mb_y = cy + ch - 195
    draw_card(c, rx + 24, mb_y, cw - 48, 85, r=8, bg=colors.HexColor('#0c1424'))

    metrics = [
        ("Accuracy", "89.2%", EMERALD),
        ("Precision", "0.884", CYAN),
        ("Recall", "0.879", INDIGO),
        ("F1-Score", "0.881", PURPLE)
    ]
    for i, (m_name, m_val, m_col) in enumerate(metrics):
        mx = rx + 36 + i * 110
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(mx, mb_y + 52, m_name)
        c.setFillColor(m_col)
        c.setFont(FONT_HEADING, 22)
        c.drawString(mx, mb_y + 18, m_val)

    # Qualitative comparison bullets
    my = mb_y - 35
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_BOLD, 13)
    c.drawString(rx + 24, my, "Core Trade-off Analysis:")

    tradeoffs = [
        ("Explainability", "VADER is 100% white-box; every word delta can be traced in real time."),
        ("Latency Footprint", "VADER executes in <2ms per review; zero model loading or GPU dependency."),
        ("Domain Sensitivity", "Supervised ML excels on genre jargon but suffers from out-of-vocabulary drift.")
    ]
    ty = my - 26
    for t_head, t_desc in tradeoffs:
        c.setFillColor(INDIGO)
        c.circle(rx + 28, ty + 3, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(rx + 38, ty, t_head)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(rx + 38, ty - 15, t_desc)
        ty -= 38

    c.showPage()


# =========================================================================
# SLIDE 6: Fine-Grained Opinion Mining (10 Aspects & RAKE)
# =========================================================================
def render_slide_6(c):
    draw_tech_background(c)
    draw_slide_header(c, "ASTMA Unit III", "Aspect-Based Opinion Mining & RAKE Keyphrase Extraction",
                      "Deconstructing document-level sentiment into 10 literary dimensions with candidate co-occurrence scoring.")

    # 10 Aspect Cards Grid (2 rows x 5 cols)
    aspects = [
        ("Plot & Story", "Narrative arc, suspense, mystery, storyline"),
        ("Writing Style", "Prose quality, poetic voice, author craft"),
        ("Character Dev.", "Protagonist growth, flawed motives, depth"),
        ("Pacing", "Page-turner tempo, slow middle, dragged chapters"),
        ("Emotional Depth", "Heartwarming, tear-jerker, vulnerability"),
        ("Worldbuilding", "Sci-fi lore, fantasy realm, immersion"),
        ("Dialogue", "Witty banter, realistic conversation, voice"),
        ("Ending & Climax", "Shocking twist, cliffhanger, resolution"),
        ("Originality", "Unique premise, trope subversion, fresh ideas"),
        ("Price & Value", "Paperback quality, audio length, affordability")
    ]

    card_w = 196
    card_h = 95
    start_x = 60
    gap_x = 12
    gap_y = 12
    sy = top_y(160)

    for i, (name, keywords) in enumerate(aspects):
        col = i % 5
        row = i // 5
        cx = start_x + col * (card_w + gap_x)
        cy = sy - row * (card_h + gap_y)

        draw_card(c, cx, cy, card_w, card_h, r=8, top_accent=PURPLE)

        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_HEADING, 13)
        c.drawString(cx + 12, cy + card_h - 24, name)

        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(cx + 12, cy + 35, keywords[:24])
        c.drawString(cx + 12, cy + 20, keywords[24:])

    # Real-World Review Inspector Box Below
    demo_y = top_y(540)
    demo_h = 190
    demo_w = W - 120
    draw_card(c, 60, demo_y, demo_w, demo_h, r=12, top_accent=CYAN)

    c.setFillColor(CYAN)
    c.setFont(FONT_BOLD, 11)
    c.drawString(85, demo_y + demo_h - 30, "LIVE SYSTEM INFERENCE PREVIEW")

    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 16)
    c.drawString(85, demo_y + demo_h - 58,
                 "“The writing style is breathtaking and the emotional depth kept me hooked through chapter ten,")
    c.drawString(85, demo_y + demo_h - 82,
                 "however the pacing dragged in the middle and the character development felt rushed.”")

    # Metrics Row
    my = demo_y + 25
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_BOLD, 12)
    c.drawString(85, my + 38, "DETECTED ASPECTS:")
    draw_badge(c, "Writing Style (+0.82)", 230, my + 32, colors.HexColor('#162b3d'), CYAN, font_size=10)
    draw_badge(c, "Emotional Depth (+0.75)", 390, my + 32, colors.HexColor('#162b3d'), CYAN, font_size=10)
    draw_badge(c, "Pacing (-0.45)", 570, my + 32, colors.HexColor('#3d1624'), ROSE, font_size=10)
    draw_badge(c, "Character Dev. (-0.38)", 690, my + 32, colors.HexColor('#3d1624'), ROSE, font_size=10)

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_BOLD, 12)
    c.drawString(85, my + 6, "RAKE KEYPHRASES:")
    draw_badge(c, "Breathtaking Writing Style (9.0)", 230, my, colors.HexColor('#241938'), PURPLE, font_size=10)
    draw_badge(c, "Rushed Character Development (9.0)", 465, my, colors.HexColor('#241938'), PURPLE, font_size=10)
    draw_badge(c, "Emotional Depth (4.0)", 730, my, colors.HexColor('#241938'), PURPLE, font_size=10)

    c.showPage()


# =========================================================================
# SLIDE 7: Unsupervised Discovery (K-Means Clustering & Apriori Rules)
# =========================================================================
def render_slide_7(c):
    draw_tech_background(c)
    draw_slide_header(c, "ASTMA Unit IV", "Unsupervised Machine Learning & Latent Theme Mining",
                      "K-Means TF-IDF vector clustering ($K=4$) and market-basket Apriori association rule discovery.")

    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: K-Means Clustering
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=CYAN)

    draw_badge(c, "UNSUPERVISED CLUSTERING", lx + 24, cy + ch - 38, colors.HexColor('#162b3d'), CYAN, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 20)
    c.drawString(lx + 24, cy + ch - 70, "K-Means Latent Theme Discovery")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(lx + 24, cy + ch - 94, "Discovers natural semantic groupings without supervision (K=4 in TF-IDF space).")

    clusters = [
        ("Cluster 1: Cosmic Sci-Fi & Worldbuilding", "77.4% of corpus • 'science, fiction, atmospheric, universe'"),
        ("Cluster 2: Emotional Drama & Resonance", "9.7% of corpus • 'pacing, tone, vulnerability, touching'"),
        ("Cluster 3: Behavioral Science & Habit", "8.9% of corpus • 'prose, habits, mindset, behavioral, daily'"),
        ("Cluster 4: Psychological Suspense & Thriller", "4.0% of corpus • 'mystery, twist, psychological, climax'")
    ]

    ky = cy + ch - 135
    for c_title, c_desc in clusters:
        draw_card(c, lx + 20, ky - 36, cw - 40, 52, r=6, bg=colors.HexColor('#0c1424'))
        c.setFillColor(CYAN)
        c.circle(lx + 35, ky - 10, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(lx + 46, ky - 7, c_title)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(lx + 46, ky - 24, c_desc)
        ky -= 62

    # Right: Apriori Association Rules
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=PURPLE)

    draw_badge(c, "ASSOCIATION MINING", rx + 24, cy + ch - 38, colors.HexColor('#241938'), PURPLE, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 20)
    c.drawString(rx + 24, cy + ch - 70, "Apriori Co-occurrence Rules")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(rx + 24, cy + ch - 94, "Identifies high-confidence aspect relationships: Antecedent → Consequent.")

    rules = [
        ("Emotional Depth → Writing Style", "Support: 31.5% • Confidence: 82.4% • Lift: 1.45"),
        ("Pacing Friction → Ending Disappointment", "Support: 18.2% • Confidence: 74.1% • Lift: 1.88"),
        ("Worldbuilding → Originality Acclaim", "Support: 24.6% • Confidence: 89.0% • Lift: 1.62"),
        ("Price Critique → Negative CSAT", "Support: 14.3% • Confidence: 91.2% • Lift: 2.14")
    ]

    ry_item = cy + ch - 135
    for r_title, r_desc in rules:
        draw_card(c, rx + 20, ry_item - 36, cw - 40, 52, r=6, bg=colors.HexColor('#0c1424'))
        c.setFillColor(PURPLE)
        c.circle(rx + 35, ry_item - 10, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(rx + 46, ry_item - 7, r_title)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(rx + 46, ry_item - 24, r_desc)
        ry_item -= 62

    c.showPage()


# =========================================================================
# SLIDE 8: Enterprise Systems: RBAC & ERP Materials Management
# =========================================================================
def render_slide_8(c):
    draw_tech_background(c)
    draw_slide_header(c, "Enterprise Systems", "Role-Based Access Control & Master Data Management",
                      "Operational enterprise integrity separating administrative moderation from customer interactions.")

    # Two Main Cards
    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: RBAC Model
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=INDIGO)

    draw_badge(c, "SECURITY ARCHITECTURE", lx + 24, cy + ch - 38, colors.HexColor('#1a1e3d'), INDIGO, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(lx + 24, cy + ch - 70, "RBAC Security & Audit Trails")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(lx + 24, cy + ch - 94, "Enforces strict authorization boundaries with transactional audit logging.")

    # Role comparison
    draw_card(c, lx + 20, cy + 140, cw - 40, 100, r=8, bg=colors.HexColor('#0c1424'))
    draw_badge(c, "ADMIN ROLE", lx + 36, cy + 210, colors.HexColor('#2c163b'), PURPLE, font_size=9)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_BOLD, 12)
    c.drawString(lx + 120, cy + 214, "Product registration, delete reviews, ITPM plan view")
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 11)
    c.drawString(lx + 36, cy + 188, "• Access to PERT crashing tools, Scrum boards, and ERP TCO projections.")
    c.drawString(lx + 36, cy + 168, "• Review moderation authority and direct database deletion rights.")

    draw_card(c, lx + 20, cy + 25, cw - 40, 100, r=8, bg=colors.HexColor('#0c1424'))
    draw_badge(c, "CUSTOMER ROLE", lx + 36, cy + 95, colors.HexColor('#162b29'), EMERALD, font_size=9)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_BOLD, 12)
    c.drawString(lx + 145, cy + 99, "Catalog browsing, review submission, live NLP feedback")
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 11)
    c.drawString(lx + 36, cy + 73, "• Live NLP feedback typing card (instant VADER score & RAKE tags).")
    c.drawString(lx + 36, cy + 53, "• Read-only access to community reviews and individual book metrics.")

    # Right: ERP Materials Catalog
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=EMERALD)

    draw_badge(c, "ERP MATERIALS MODULE", rx + 24, cy + ch - 38, colors.HexColor('#142b26'), EMERALD, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(rx + 24, cy + ch - 70, "Master Catalog & Data Models")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(rx + 24, cy + ch - 94, "Enterprise Materials Master: 36 verified books spanning 35 genres.")

    cat_specs = [
        ("Entity Integrity", "Foreign key constraints link reviews to verified book IDs and user IDs."),
        ("B-Tree Optimization", "Indexed queries on genre, rating, and sentiment execute in <5ms."),
        ("Audit Trail Ledger", "Every login, submission, and moderation writes to audit_logs table."),
        ("Batch ETL Capabilities", "Paginated streaming handles 100k+ reviews without memory exhaustion.")
    ]

    ey = cy + ch - 130
    for e_head, e_desc in cat_specs:
        c.setFillColor(EMERALD)
        c.circle(rx + 28, ey + 3, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 13)
        c.drawString(rx + 38, ey, e_head)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(rx + 38, ey - 16, e_desc)
        ey -= 56

    c.showPage()


# =========================================================================
# SLIDE 9: ERP 5-Year Total Cost of Ownership (TCO Model)
# =========================================================================
def render_slide_9(c):
    draw_tech_background(c)
    draw_slide_header(c, "Enterprise Systems", "5-Year Total Cost of Ownership (TCO): COTS vs Bespoke",
                      "Evaluating economic trade-offs between commercial SaaS packages and custom FastAPI NLP architecture.")

    # Top Comparative Cards
    cw = 495
    ch = 180
    cy = top_y(290)

    # COTS Box
    draw_card(c, 60, cy, cw, ch, r=12, top_accent=ROSE)
    draw_badge(c, "COMMERCIAL OFF-THE-SHELF (COTS)", 85, cy + ch - 35, colors.HexColor('#3d1624'), ROSE, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 22)
    c.drawString(85, cy + ch - 68, "5-Year Cumulative: ₹1,85,000")
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(85, cy + 60, "• High recurring SaaS license fees per seat per year.")
    c.drawString(85, cy + 40, "• Rigid customization lock-in; cannot tune internal NLP algorithms.")
    c.drawString(85, cy + 20, "• Expensive third-party connector fees for external CRM/ERP sync.")

    # Bespoke Box
    draw_card(c, 595, cy, cw, ch, r=12, top_accent=EMERALD)
    draw_badge(c, "SENTILINK BESPOKE BUILD (CHOSEN)", 620, cy + ch - 35, colors.HexColor('#142b26'), EMERALD, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 22)
    c.drawString(620, cy + ch - 68, "5-Year Cumulative: ₹82,000 (56% Savings)")
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(620, cy + 60, "• Upfront CapEx of ₹55,000 with nominal annual cloud hosting (₹6,000/yr).")
    c.drawString(620, cy + 40, "• Complete ownership of NLP intellectual property and fine-tuning rules.")
    c.drawString(620, cy + 20, "• Breakeven achieved by Month 14 of commercial deployment.")

    # 5-Year Projection Table Below
    tbl_y = top_y(540)
    tbl_h = 220
    tbl_w = W - 120
    draw_card(c, 60, tbl_y, tbl_w, tbl_h, r=12, top_accent=INDIGO)

    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 17)
    c.drawString(85, tbl_y + tbl_h - 32, "Cumulative Cost Projection Table (₹ INR)")

    # Table Header
    headers = ["Cost Category", "Year 1 (Capex)", "Year 2", "Year 3", "Year 4", "Year 5", "5-Yr Total"]
    col_w = [260, 115, 115, 115, 115, 115, 145]
    th_y = tbl_y + tbl_h - 65

    c.setFillColor(colors.HexColor('#1a263d'))
    c.rect(80, th_y, tbl_w - 40, 24, fill=1, stroke=0)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_BOLD, 11)
    tx = 90
    for h_txt, w in zip(headers, col_w):
        c.drawString(tx, th_y + 6, h_txt)
        tx += w

    # Rows
    rows_data = [
        ("COTS SaaS Package (e.g. Brand24 / Sprinklr)", "₹45,000", "₹35,000", "₹35,000", "₹35,000", "₹35,000", "₹1,85,000", ROSE),
        ("Sentilink Bespoke Architecture (Built)", "₹55,000", "₹6,000", "₹7,000", "₹7,000", "₹7,000", "₹82,000", EMERALD),
        ("Net Enterprise Cost Benefit (Savings)", "- ₹10,000", "+ ₹29,000", "+ ₹28,000", "+ ₹28,000", "+ ₹28,000", "+ ₹1,03,000", CYAN)
    ]

    ry_pos = th_y - 28
    for r_title, y1, y2, y3, y4, y5, tot, c_col in rows_data:
        c.setFillColor(TEXT_WHITE if c_col != CYAN else CYAN)
        c.setFont(FONT_BOLD if c_col != TEXT_MUTED else FONT_REGULAR, 11)
        tx = 90
        c.drawString(tx, ry_pos, r_title)
        tx += col_w[0]
        for val in [y1, y2, y3, y4, y5]:
            c.drawString(tx, ry_pos, val)
            tx += col_w[1]
        c.setFillColor(c_col)
        c.drawString(tx, ry_pos, tot)
        ry_pos -= 26

    c.showPage()


# =========================================================================
# SLIDE 10: IT Project Management: WBS & 16-Week Schedule
# =========================================================================
def render_slide_10(c):
    draw_tech_background(c)
    draw_slide_header(c, "IT Project Management", "Work Breakdown Structure (WBS) & 16-Week Schedule",
                      "Structured project delivery decomposing capstone scope into 5 work packages and 15 trackable activities.")

    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: WBS Hierarchy
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=EMERALD)

    draw_badge(c, "WBS SCOPE HIERARCHY", lx + 24, cy + ch - 38, colors.HexColor('#142b26'), EMERALD, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 20)
    c.drawString(lx + 24, cy + ch - 70, "Work Breakdown Structure")

    wbs_pkgs = [
        ("WP 1.0: Initiation & Architecture", "Scope charter, literature survey, 3-tier MVC blueprint"),
        ("WP 2.0: Data Ingestion & Storage", "SQLite schema design, Kaggle ETL pipeline, data cleaning"),
        ("WP 3.0: Core NLP Engineering", "VADER rule adaptation, RAKE extractor, K-Means clustering"),
        ("WP 4.0: Dashboard & Web UI", "Chart.js analytics, role toggles, live typing inference card"),
        ("WP 5.0: QA, Testing & Deployment", "Unit test suites, syllabus report generation, UAT sign-off")
    ]

    wy = cy + ch - 120
    for wp_name, wp_desc in wbs_pkgs:
        draw_card(c, lx + 20, wy - 32, cw - 40, 48, r=6, bg=colors.HexColor('#0c1424'))
        c.setFillColor(EMERALD)
        c.circle(lx + 35, wy - 8, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(lx + 46, wy - 5, wp_name)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(lx + 46, wy - 22, wp_desc)
        wy -= 56

    # Right: 16-Week Schedule & Milestones
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=CYAN)

    draw_badge(c, "TIMELINE & STAGE-GATES", rx + 24, cy + ch - 38, colors.HexColor('#162b3d'), CYAN, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 20)
    c.drawString(rx + 24, cy + ch - 70, "16-Week Delivery Lifecycle")

    milestones = [
        ("M1 (Week 2): Project Charter Signed", "Scope baseline approved by academic mentors"),
        ("M2 (Week 5): Database Schema Live", "Books and reviews tables populated with seed data"),
        ("M3 (Week 8): NLP Algorithm Alpha", "VADER compound & RAKE keyphrase engine operational"),
        ("M4 (Week 11): REST API Interoperability", "FastAPI Swagger endpoints fully integrated with UI"),
        ("M5 (Week 13): Advanced Analytics Lab", "K-Means clusters, Apriori rules & social graphs live"),
        ("M6 (Week 16): Final Defense & Handoff", "Full code repository, documentation & live demonstration")
    ]

    my = cy + ch - 115
    for m_title, m_desc in milestones:
        c.setFillColor(CYAN)
        c.circle(rx + 28, my + 3, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(rx + 38, my, m_title)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(rx + 38, my - 14, m_desc)
        my -= 44

    c.showPage()


# =========================================================================
# SLIDE 11: ITPM CPM/PERT Critical Path & Activity Crashing
# =========================================================================
def render_slide_11(c):
    draw_tech_background(c)
    draw_slide_header(c, "IT Project Management", "CPM / PERT Critical Path & Activity Crashing Analysis",
                      "Three-time probabilistic estimation ($T_e$) identifying project bottlenecks and optimal crashing slopes.")

    # Two Cards
    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: PERT Formula & Critical Path
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=CYAN)

    draw_badge(c, "PROBABILISTIC NETWORK", lx + 24, cy + ch - 38, colors.HexColor('#162b3d'), CYAN, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(lx + 24, cy + ch - 70, "PERT Expected Time Formula")

    # Formula Box
    f_box_y = cy + ch - 160
    draw_card(c, lx + 24, f_box_y, cw - 48, 75, r=8, bg=colors.HexColor('#0c1424'))
    c.setFillColor(CYAN_GLOW)
    c.setFont(FONT_HEADING, 18)
    c.drawCentredString(lx + cw / 2.0, f_box_y + 42, "T_e = (a + 4m + b) / 6")
    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 11)
    c.drawCentredString(lx + cw / 2.0, f_box_y + 18, "a = Optimistic Time • m = Most Likely Time • b = Pessimistic Time")

    # Critical Path Callout
    cp_y = f_box_y - 80
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_BOLD, 14)
    c.drawString(lx + 24, cp_y + 50, "Critical Path Identification:")

    c.setFillColor(ROSE)
    c.setFont(FONT_HEADING, 17)
    c.drawString(lx + 24, cp_y + 24, "A  →  C  →  F  →  G  →  H  (16.0 Weeks)")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(lx + 24, cp_y - 2, "• Zero float activities; any delay in these directly delays project completion.")
    c.drawString(lx + 24, cp_y - 20, "• Total Project Variance: σ² = 1.34 weeks (Std Dev: 1.16 weeks).")
    c.drawString(lx + 24, cp_y - 38, "• 95% Confidence Interval for completion: 14.8 to 17.2 weeks.")

    # Right: Activity Crashing Analysis
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=ROSE)

    draw_badge(c, "SCHEDULE OPTIMIZATION", rx + 24, cy + ch - 38, colors.HexColor('#3d1624'), ROSE, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(rx + 24, cy + ch - 70, "Crashing Cost Slope Analysis")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(rx + 24, cy + ch - 94, "Crash Cost Slope = (Crash Cost - Normal Cost) / (Normal Time - Crash Time)")

    crash_data = [
        ("Task C: NLP Pipeline Dev.", "Normal: 4 wks → Crash: 3 wks", "Slope: ₹2,000/wk", "Priority 1 Crash candidate"),
        ("Task F: Dashboard Visuals", "Normal: 3 wks → Crash: 2 wks", "Slope: ₹2,500/wk", "Priority 2 Crash candidate"),
        ("Task G: Integration QA", "Normal: 2 wks → Crash: 1 wk", "Slope: ₹3,000/wk", "Priority 3 Crash candidate"),
        ("Task H: Final UAT Sign-off", "Normal: 2 wks → Crash: 1.5 wks", "Slope: ₹4,000/wk", "High cost; avoid crashing")
    ]

    cry = cy + ch - 135
    for t_name, t_times, t_slope, t_prio in crash_data:
        draw_card(c, rx + 20, cry - 38, cw - 40, 52, r=6, bg=colors.HexColor('#0c1424'))
        c.setFillColor(ROSE)
        c.circle(rx + 35, cry - 10, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(rx + 46, cry - 7, t_name)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(rx + 46, cry - 24, f"{t_times}  •  {t_slope}  ({t_prio})")
        cry -= 62

    c.showPage()


# =========================================================================
# SLIDE 12: ITPM Budget Allocation & Risk Governance Matrix
# =========================================================================
def render_slide_12(c):
    draw_tech_background(c)
    draw_slide_header(c, "IT Project Management", "Budget Breakdown (₹55,000 Cap) & Risk Register",
                      "Bottom-up cost accounting and quantitative risk management with proactive mitigation protocols.")

    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: Budget Allocation Chart
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=EMERALD)

    draw_badge(c, "FINANCIAL GOVERNANCE", lx + 24, cy + ch - 38, colors.HexColor('#142b26'), EMERALD, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(lx + 24, cy + ch - 70, "₹55,000 Bottom-Up Budget")

    c.setFillColor(TEXT_MUTED)
    c.setFont(FONT_REGULAR, 12)
    c.drawString(lx + 24, cy + ch - 94, "Strict capital expenditure cap verified against deliverable heads:")

    cost_heads = [
        ("Software Engineering & Architecture", 25000, "45.5%", EMERALD),
        ("Cloud Infrastructure & DB Storage", 10000, "18.2%", CYAN),
        ("Quality Assurance & Benchmark QA", 8000, "14.5%", INDIGO),
        ("Miscellaneous & Contingency Buffer", 7000, "12.7%", AMBER),
        ("Technical Documentation & Reports", 5000, "9.1%", PURPLE)
    ]

    by = cy + ch - 130
    for name, amt, pct, col in cost_heads:
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(lx + 24, by, name)

        c.setFillColor(col)
        c.drawRightString(lx + cw - 24, by, f"₹{amt:,} ({pct})")

        # Visual progress bar
        draw_card(c, lx + 24, by - 16, cw - 48, 8, r=4, bg=colors.HexColor('#0c1424'))
        bar_fill = ((amt) / 25000.0) * (cw - 48)
        c.setFillColor(col)
        c.roundRect(lx + 24, by - 16, bar_fill, 8, 4, fill=1, stroke=0)

        by -= 48

    # Right: Risk Register Table
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=ROSE)

    draw_badge(c, "RISK MITIGATION", rx + 24, cy + ch - 38, colors.HexColor('#3d1624'), ROSE, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(rx + 24, cy + ch - 70, "Risk Governance Register")

    risks = [
        ("Review Noise & Spam", "Med", "High", "Automated regex cleaning & duplicate token pruning"),
        ("VADER Sarcasm Misses", "Med", "Med", "Dual Naive Bayes fallback & compound threshold tuning"),
        ("Database Data Drift", "Low", "High", "Daily automated SQLite snapshots & foreign key constraints"),
        ("Schedule Overrun", "Med", "High", "CPM/PERT critical path tracking & crash candidate C"),
        ("API Contract Mismatch", "Med", "Med", "Pydantic V2 schema validation & Swagger documentation")
    ]

    ry = cy + ch - 120
    for r_name, prob, imp, mit in risks:
        draw_card(c, rx + 20, ry - 36, cw - 40, 52, r=6, bg=colors.HexColor('#0c1424'))
        c.setFillColor(ROSE if imp == "High" else AMBER)
        c.circle(rx + 35, ry - 10, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 12)
        c.drawString(rx + 46, ry - 7, r_name)
        c.setFillColor(ROSE if imp == "High" else AMBER)
        c.setFont(FONT_BOLD, 10)
        c.drawRightString(rx + cw - 35, ry - 7, f"P:{prob} | I:{imp}")
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 10)
        c.drawString(rx + 46, ry - 24, mit)
        ry -= 60

    c.showPage()


# =========================================================================
# SLIDE 13: Live System Verification & Academic Compliance Matrix
# =========================================================================
def render_slide_13(c):
    draw_tech_background(c)
    draw_slide_header(c, "Verification & Results", "System Verification & Academic Syllabus Compliance",
                      "100% formal compliance across all required BVDU CSBS syllabus units and live operational metrics.")

    # 4 Metric Cards Across
    stat_w = 235
    stat_gap = 28
    start_x = 60
    top_stat_y = top_y(220)

    stats = [
        ("< 10 ms", "API Latency SLA", "FastAPI Asynchronous Engine", CYAN),
        ("89.2%", "Supervised Accuracy", "TF-IDF + Naive Bayes Benchmark", INDIGO),
        ("10 / 10", "Aspect Coverage", "Complete Domain Literary Reach", PURPLE),
        ("₹0 Cost Drift", "Budget Variance", "Exact ₹55,000 Cap Maintained", EMERALD)
    ]

    for i, (val, title, sub, col) in enumerate(stats):
        sx = start_x + i * (stat_w + stat_gap)
        draw_card(c, sx, top_stat_y, stat_w, 95, r=10, top_accent=col)

        c.setFillColor(col)
        c.setFont(FONT_HEADING, 22)
        c.drawString(sx + 16, top_stat_y + 55, val)

        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 11)
        c.drawString(sx + 16, top_stat_y + 34, title)

        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 9)
        c.drawString(sx + 16, top_stat_y + 16, sub)

    # Compliance Matrix Table Below
    tbl_y = top_y(540)
    tbl_h = 300
    tbl_w = W - 120
    draw_card(c, 60, tbl_y, tbl_w, tbl_h, r=12, top_accent=CYAN)

    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 18)
    c.drawString(85, tbl_y + tbl_h - 35, "BVDU DET CSBS Academic Syllabus Compliance Matrix")

    headers = ["Subject", "Syllabus Unit / Concept", "Practical System Implementation", "Verification Status"]
    col_w = [140, 260, 430, 150]
    th_y = tbl_y + tbl_h - 68

    c.setFillColor(colors.HexColor('#1a263d'))
    c.rect(80, th_y, tbl_w - 40, 24, fill=1, stroke=0)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_BOLD, 11)
    tx = 90
    for h_txt, w in zip(headers, col_w):
        c.drawString(tx, th_y + 6, h_txt)
        tx += w

    matrix_rows = [
        ("ASTMA", "Unit I: Text Preprocessing", "Noise stripping, tokenisation, stopwords, lemmatisation pipeline", "Verified (100%)", EMERALD),
        ("ASTMA", "Unit II: Sentiment Analysis", "VADER rule heuristics + supervised TF-IDF Naive Bayes benchmark", "Verified (100%)", EMERALD),
        ("ASTMA", "Unit III: Keyphrase Extraction", "RAKE word degree to frequency co-occurrence matrix", "Verified (100%)", EMERALD),
        ("ASTMA", "Unit IV: Unsupervised Topics", "K-Means TF-IDF space clustering (K=4) & Apriori association rules", "Verified (100%)", EMERALD),
        ("Enterprise Systems", "Unit I-II: 3-Tier MVC Architecture", "FastAPI SOA REST gateway + Vanilla JS UI + SQLite persistence", "Verified (100%)", EMERALD),
        ("Enterprise Systems", "Unit III-IV: RBAC & TCO", "Admin vs Customer role segregation & 5-Year COTS vs Bespoke model", "Verified (100%)", EMERALD),
        ("IT Project Mgmt", "Units I-VI: Project Controls", "WBS, 16-Wk Plan, ₹55k Cost, Risk Register, CPM/PERT Crashing", "Verified (100%)", EMERALD)
    ]

    ry_pos = th_y - 26
    for subj, concept, impl, status, col in matrix_rows:
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 10)
        tx = 90
        c.drawString(tx, ry_pos, subj)
        tx += col_w[0]
        c.setFont(FONT_REGULAR, 10)
        c.drawString(tx, ry_pos, concept)
        tx += col_w[1]
        c.drawString(tx, ry_pos, impl)
        tx += col_w[2]
        c.setFillColor(col)
        c.setFont(FONT_BOLD, 10)
        c.drawString(tx, ry_pos, status)
        ry_pos -= 26

    c.showPage()


# =========================================================================
# SLIDE 14: Conclusion & Future Research Roadmap
# =========================================================================
def render_slide_14(c):
    draw_tech_background(c)
    draw_slide_header(c, "Conclusion & Roadmap", "Project Achievements & Next-Generation Research Directions",
                      "Summary of engineering milestones achieved and future technological enhancements for 2026-2027.")

    cw = 495
    ch = 390
    cy = top_y(520)

    # Left: What We Built & Delivered
    lx = 60
    draw_card(c, lx, cy, cw, ch, r=12, top_accent=EMERALD)

    draw_badge(c, "DELIVERED VALUE", lx + 24, cy + ch - 38, colors.HexColor('#142b26'), EMERALD, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(lx + 24, cy + ch - 70, "Engineering Deliverables")

    delivered = [
        ("Full-Stack Enterprise Web Application", "Production-grade 3-Tier MVC with FastAPI REST backend and responsive Chart.js dashboard."),
        ("Multi-Method NLP Opinion Engine", "Real-time VADER valence scoring, RAKE keyphrase mining, and 10 literary aspect detectors."),
        ("Unsupervised Knowledge Discovery", "K-Means semantic topic discovery (K=4), Apriori association rules, and reader bipartite graphs."),
        ("Rigorous ITPM Governance Framework", "On-time 16-week delivery, probabilistic PERT critical path, and exact ₹55,000 budget adherence.")
    ]

    dy = cy + ch - 120
    for d_title, d_desc in delivered:
        c.setFillColor(EMERALD)
        c.circle(lx + 28, dy + 3, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 13)
        c.drawString(lx + 38, dy, d_title)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(lx + 38, dy - 16, d_desc[:52])
        c.drawString(lx + 38, dy - 30, d_desc[52:])
        dy -= 60

    # Right: Future Research Roadmap
    rx = 595
    draw_card(c, rx, cy, cw, ch, r=12, top_accent=CYAN)

    draw_badge(c, "FUTURE HORIZON", rx + 24, cy + ch - 38, colors.HexColor('#162b3d'), CYAN, font_size=10)
    c.setFillColor(TEXT_WHITE)
    c.setFont(FONT_HEADING, 21)
    c.drawString(rx + 24, cy + ch - 70, "Next-Gen Research Roadmap")

    roadmap = [
        ("Fine-Tuned Transformer Models", "Deploy domain-specific Book-BERT or RoBERTa microservices for literary subtext and irony."),
        ("Sentence-Level ABSA", "Syntactic dependency parsing to isolate multi-aspect polarities within complex compound sentences."),
        ("Vector Embeddings & Semantic Search", "Vector database integration (FAISS / ChromaDB) for semantic recommendation search."),
        ("PostgreSQL Enterprise Clustering", "Scale from SQLite to distributed multi-master database clusters with read replicas.")
    ]

    ry = cy + ch - 120
    for r_title, r_desc in roadmap:
        c.setFillColor(CYAN)
        c.circle(rx + 28, ry + 3, 3, fill=1, stroke=0)
        c.setFillColor(TEXT_WHITE)
        c.setFont(FONT_BOLD, 13)
        c.drawString(rx + 38, ry, r_title)
        c.setFillColor(TEXT_MUTED)
        c.setFont(FONT_REGULAR, 11)
        c.drawString(rx + 38, ry - 16, r_desc[:52])
        c.drawString(rx + 38, ry - 30, r_desc[52:])
        ry -= 60

    c.showPage()


def build_deck(filename="Sentilink_Book_Review_Presentation.pdf"):
    c = canvas.Canvas(filename, pagesize=(W, H))

    render_slide_1(c)
    render_slide_2(c)
    render_slide_3(c)
    render_slide_4(c)
    render_slide_5(c)
    render_slide_6(c)
    render_slide_7(c)
    render_slide_8(c)
    render_slide_9(c)
    render_slide_10(c)
    render_slide_11(c)
    render_slide_12(c)
    render_slide_13(c)
    render_slide_14(c)

    c.save()
    print(f"Successfully generated custom executive keynote: {filename} ({os.path.getsize(filename):,} bytes)")


if __name__ == '__main__':
    build_deck()
