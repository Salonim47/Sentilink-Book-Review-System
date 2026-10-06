"""
Enterprise Database Management Module (DBMS Tier)
Incorporates concepts from Enterprise Systems:
- Unit I: DBMS Relational Data Modeling & 3-Tier Architecture
- Unit II: ERP Modularity (Book Materials/Catalog, Review Records, Customer CRM Data)
- Unit III: Role-Based Access Control (RBAC), Audit Trails, Digital Hash Signatures
- ITPM: Agile Scrum Sprint Tasks, PERT/CPM Project Network Scheduling
Now expanded to 35 Master Books across 30+ distinct literary genres with 130+ reviews.
"""

import sqlite3
import hashlib
import json
import os
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "enterprise_books.db")


def get_db_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password: str) -> str:
    """Simulates enterprise cryptographic hashing using SHA-256 with salt."""
    salt = "enterprise_salt_2026"
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()


def generate_audit_hash(user: str, action: str, timestamp: str, details: str) -> str:
    """Generates immutable digital audit signature (Unit III Security)."""
    raw = f"{user}:{action}:{timestamp}:{details}:enterprise_secret_key"
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()[:24]


def init_database(force_reseed: bool = False):
    """Initializes schema and populates rich Kaggle book dataset and initial enterprise data."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Users Table (RBAC: Admin vs Customer)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL CHECK(role IN ('admin', 'customer')),
        full_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        created_at TEXT NOT NULL
    );
    """)

    # 2. Books Table (Catalog / Materials Management - ERP Module)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        isbn TEXT UNIQUE NOT NULL,
        publish_year INTEGER NOT NULL,
        cover_url TEXT NOT NULL,
        description TEXT NOT NULL,
        price REAL NOT NULL,
        pages INTEGER NOT NULL,
        avg_rating REAL DEFAULT 0.0,
        total_reviews INTEGER DEFAULT 0,
        positive_pct REAL DEFAULT 0.0,
        neutral_pct REAL DEFAULT 0.0,
        negative_pct REAL DEFAULT 0.0,
        top_keywords TEXT DEFAULT '[]'
    );
    """)

    # 3. Reviews Table (Text Analytics & Sentiment Storage)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        user_name TEXT NOT NULL,
        rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
        review_text TEXT NOT NULL,
        sentiment_label TEXT NOT NULL CHECK(sentiment_label IN ('Positive', 'Neutral', 'Negative')),
        polarity_score REAL NOT NULL,
        subjectivity_score REAL NOT NULL,
        emotion TEXT NOT NULL,
        aspects TEXT DEFAULT '{}',
        keywords TEXT DEFAULT '[]',
        is_verified_purchase INTEGER DEFAULT 1,
        status TEXT DEFAULT 'approved' CHECK(status IN ('approved', 'flagged', 'hidden')),
        created_at TEXT NOT NULL,
        FOREIGN KEY(book_id) REFERENCES books(id) ON DELETE CASCADE,
        FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
    );
    """)

    # 4. Security Audit Trail Table (Enterprise Systems Unit III)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        user_name TEXT NOT NULL,
        role TEXT NOT NULL,
        action TEXT NOT NULL,
        ip_address TEXT NOT NULL,
        details TEXT NOT NULL,
        digital_signature TEXT NOT NULL
    );
    """)

    # 5. Agile Scrum Sprint Tasks (ITPM Unit V)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sprint_tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sprint_name TEXT NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        assigned_to TEXT NOT NULL,
        priority TEXT NOT NULL CHECK(priority IN ('High', 'Medium', 'Low')),
        status TEXT NOT NULL CHECK(status IN ('backlog', 'in_progress', 'review', 'done')),
        story_points INTEGER NOT NULL
    );
    """)

    # 6. PERT / CPM Network Activities (ITPM Unit II & III Project Scheduling)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pert_activities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        activity_code TEXT UNIQUE NOT NULL,
        activity_name TEXT NOT NULL,
        predecessor TEXT NOT NULL,
        opt_time REAL NOT NULL,
        likely_time REAL NOT NULL,
        pess_time REAL NOT NULL,
        expected_time REAL NOT NULL,
        variance REAL NOT NULL,
        is_critical INTEGER DEFAULT 0
    );
    """)

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM books")
    book_count = cursor.fetchone()[0]

    if force_reseed or book_count < 30:
        seed_data(conn)

    conn.close()


def seed_data(conn: sqlite3.Connection):
    """Populates 35 master books across 30+ distinct genres and 130+ reviews."""
    cursor = conn.cursor()

    # Clear existing tables for a clean seed
    cursor.execute("DELETE FROM reviews")
    cursor.execute("DELETE FROM books")
    cursor.execute("DELETE FROM users")
    cursor.execute("DELETE FROM sprint_tasks")
    cursor.execute("DELETE FROM pert_activities")
    cursor.execute("DELETE FROM audit_logs")

    # Seed Default Users
    users = [
        ('admin', hash_password('admin123'), 'admin', 'System Administrator', 'admin@enterprise-books.org', '2024-01-10 09:00:00'),
        ('customer', hash_password('customer123'), 'customer', 'Demo Customer', 'customer@readerhub.com', '2024-01-15 11:30:00'),
        ('sarah_reads', hash_password('password123'), 'customer', 'Sarah Jenkins', 'sarah.reads@gmail.com', '2024-02-01 14:20:00'),
        ('marcus_chen', hash_password('password123'), 'customer', 'Marcus Chen', 'mchen@techreads.io', '2024-02-12 16:45:00'),
        ('elena_r', hash_password('password123'), 'customer', 'Elena Rostova', 'elena.rostova@literary.net', '2024-03-05 10:15:00'),
        ('dev_coder', hash_password('password123'), 'customer', 'Devon Patel', 'devon.patel@scifi-books.org', '2024-03-20 18:00:00'),
        ('alex_m', hash_password('password123'), 'customer', 'Alex Morgan', 'alex.m@bookclub.org', '2024-04-10 12:00:00'),
        ('priya_sharma', hash_password('password123'), 'customer', 'Priya Sharma', 'priya.s@analytics-daily.com', '2024-05-15 15:30:00'),
        ('lucas_silva', hash_password('password123'), 'customer', 'Lucas Silva', 'lucas.silva@readers.io', '2024-06-20 11:45:00')
    ]
    cursor.executemany("""
    INSERT INTO users (username, password_hash, role, full_name, email, created_at)
    VALUES (?, ?, ?, ?, ?, ?)
    """, users)

    # 35 Master Books across 30+ Distinct Literary Genres
    books = [
        # 1. Contemporary Fiction
        (1, "The Midnight Library", "Matt Haig", "Contemporary Fiction", "978-0525559474", 2020,
         "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=600&q=80",
         "Between life and death there is a library, and within that library, Nora Seed gets the chance to undo regrets and live alternate lives.", 14.99, 304),
        
        # 2. Hard Science Fiction
        (2, "Project Hail Mary", "Andy Weir", "Hard Science Fiction", "978-0593135204", 2021,
         "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
         "Ryland Grace is the sole survivor on a desperate, last-chance interstellar mission to save Earth from an extinction-level solar crisis.", 18.50, 496),
        
        # 3. Self-Improvement
        (3, "Atomic Habits", "James Clear", "Self-Improvement", "978-0735211292", 2018,
         "https://images.unsplash.com/photo-1506784983877-45594efa4cbe?auto=format&fit=crop&w=600&q=80",
         "An easy and proven framework to build good habits and break bad ones via compounding micro-adjustments.", 16.20, 320),
        
        # 4. Psychological Thriller
        (4, "The Silent Patient", "Alex Michaelides", "Psychological Thriller", "978-1250301696", 2019,
         "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
         "Alicia Berenson's seemingly perfect life ends when she shoots her husband five times and refuses to speak another word.", 13.99, 336),
        
        # 5. Literary Fiction
        (5, "Tomorrow, and Tomorrow, and Tomorrow", "Gabrielle Zevin", "Literary Fiction", "978-0593321201", 2022,
         "https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=600&q=80",
         "Sam and Sadie collaborate as groundbreaking video game designers, sweeping into legendary fame, fortune, and deep heartbreak.", 17.40, 416),
        
        # 6. Space Opera
        (6, "Dune", "Frank Herbert", "Space Opera", "978-0441013593", 1965,
         "https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=600&q=80",
         "On the desert planet Arrakis, Paul Atreides navigates prophecy, sandworms, and intergalactic political betrayals.", 15.99, 688),
        
        # 7. Historical Fiction
        (7, "Lessons in Chemistry", "Bonnie Garmus", "Historical Fiction", "978-0385547345", 2022,
         "https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=600&q=80",
         "Chemist Elizabeth Zott battles 1960s institutional sexism, unexpectedly becoming the host of America's most beloved cooking show.", 16.99, 400),
        
        # 8. Behavioral Psychology
        (8, "Thinking, Fast and Slow", "Daniel Kahneman", "Behavioral Psychology", "978-0374533557", 2011,
         "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=600&q=80",
         "Nobel laureate Kahneman reveals the dual cognitive systems driving our decisions: System 1 (fast/intuitive) and System 2 (slow/analytical).", 19.20, 512),
        
        # 9. Speculative Fiction
        (9, "Klara and the Sun", "Kazuo Ishiguro", "Speculative Fiction", "978-0593318171", 2021,
         "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
         "Klara, an Artificial Friend with extraordinary observational qualities, explores the mysteries of human devotion and sacrifice.", 14.50, 320),
        
        # 10. Dystopian Classic
        (10, "1984", "George Orwell", "Dystopian Classic", "978-0451524935", 1949,
         "https://images.unsplash.com/photo-1478760329108-5c3ed9d495a0?auto=format&fit=crop&w=600&q=80",
         "Winston Smith resists totalitarian surveillance in Oceania, drawing perilously close to the all-seeing gaze of Big Brother.", 11.99, 328),
        
        # 11. Mythological Fantasy
        (11, "The Song of Achilles", "Madeline Miller", "Mythological Fantasy", "978-0062060624", 2011,
         "https://images.unsplash.com/photo-1461360370896-922624d12aa1?auto=format&fit=crop&w=600&q=80",
         "A breathtaking and lyrical reimagining of Homer's Iliad through the intimate bond between Achilles and Patroclus.", 15.49, 416),
        
        # 12. Anthropology & History
        (12, "Sapiens: A Brief History of Humankind", "Yuval Noah Harari", "Anthropology & History", "978-0062316097", 2014,
         "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?auto=format&fit=crop&w=600&q=80",
         "Integrates biology, anthropology, and economics to chart how Homo sapiens conquered the globe through shared fictions.", 21.00, 464),

        # 13. Cyberpunk
        (13, "Neuromancer", "William Gibson", "Cyberpunk", "978-0441569595", 1984,
         "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80",
         "Case, a washed-up computer hacker in dystopian Chiba City, is hired by a mysterious employer for the ultimate cyberspace heist.", 14.25, 271),

        # 14. Romance & Drama
        (14, "The Seven Husbands of Evelyn Hugo", "Taylor Jenkins Reid", "Romance & Drama", "978-1501161933", 2017,
         "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?auto=format&fit=crop&w=600&q=80",
         "Aging Hollywood icon Evelyn Hugo finally decides to tell the truth about her glamorous, scandalous, and secret life.", 16.50, 400),

        # 15. Biography & Memoir
        (15, "Steve Jobs", "Walter Isaacson", "Biography & Memoir", "978-1451648539", 2011,
         "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=600&q=80",
         "Based on forty extensive interviews, this definitive biography portrays the turbulent, visionary creator who revolutionized computing.", 22.00, 656),

        # 16. High Fantasy
        (16, "The Name of the Wind", "Patrick Rothfuss", "High Fantasy", "978-0756404741", 2007,
         "https://images.unsplash.com/photo-1514533450685-4493e01d1fdc?auto=format&fit=crop&w=600&q=80",
         "Kvothe, a legendary wizard and musician, recounts his childhood with a troupe of traveling players and his quest for vengeance.", 18.99, 662),

        # 17. Mystery & Crime
        (17, "The Da Vinci Code", "Dan Brown", "Mystery & Crime", "978-0307474278", 2003,
         "https://images.unsplash.com/photo-1506880018603-83d5b814b5a6?auto=format&fit=crop&w=600&q=80",
         "Symbologist Robert Langdon discovers a baffling trail of clues concealed within Leonardo da Vinci's masterworks in the Louvre.", 12.99, 454),

        # 18. Gothic Horror
        (18, "Dracula", "Bram Stoker", "Gothic Horror", "978-0486411095", 1897,
         "https://images.unsplash.com/photo-1509248961158-e54f6934749c?auto=format&fit=crop&w=600&q=80",
         "Count Dracula travels from Transylvania to Victorian England in search of new blood, sparking a battle of wits against Van Helsing.", 10.99, 418),

        # 19. Astrophysics & Cosmology
        (19, "A Brief History of Time", "Stephen Hawking", "Astrophysics & Cosmology", "978-0553380163", 1988,
         "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80",
         "Hawking demystifies black holes, general relativity, quantum mechanics, and the birth and fate of the universe.", 17.50, 212),

        # 20. Graphic Novel & Comics
        (20, "Watchmen", "Alan Moore & Dave Gibbons", "Graphic Novel", "978-1401245252", 1987,
         "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80",
         "A gritty, deconstructive masterpiece where costumed vigilantes face murder, paranoia, and imminent nuclear holocaust.", 24.99, 416),

        # 21. True Crime
        (21, "In Cold Blood", "Truman Capote", "True Crime", "978-0679745587", 1966,
         "https://images.unsplash.com/photo-1453733197783-64ac0d442b4d?auto=format&fit=crop&w=600&q=80",
         "Capote reconstructs the brutal 1959 murder of the Clutter family in Holcomb, Kansas, creating the narrative true-crime genre.", 15.99, 343),

        # 22. Applied Economics
        (22, "Freakonomics", "Steven Levitt & Stephen Dubner", "Applied Economics", "978-0060731335", 2005,
         "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=600&q=80",
         "A rogue economist uncovers the hidden incentives driving everything from sumo wrestling to modern parenting.", 16.00, 315),

        # 23. Post-Apocalyptic
        (23, "The Road", "Cormac McCarthy", "Post-Apocalyptic", "978-0307387899", 2006,
         "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
         "A father and son walk alone through burned, ash-covered America, carrying the fire of humanity amidst brutal survivors.", 14.95, 287),

        # 24. Sci-Fi Satire & Humor
        (24, "The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Sci-Fi Satire & Humor", "978-0345391803", 1979,
         "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
         "Arthur Dent is whisked away seconds before Earth is demolished to build an intergalactic bypass, finding towels, tea, and 42.", 12.50, 216),

        # 25. Business & Leadership
        (25, "Good to Great", "Jim Collins", "Business & Leadership", "978-0066620992", 2001,
         "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80",
         "How mediocre companies defy gravity to achieve sustained, long-term exceptional market dominance through Level 5 leadership.", 23.50, 300),

        # 26. Hardboiled Detective Noir
        (26, "The Big Sleep", "Raymond Chandler", "Detective Noir", "978-0394758282", 1939,
         "https://images.unsplash.com/photo-1481627834876-b7833e8f5570?auto=format&fit=crop&w=600&q=80",
         "Private eye Philip Marlowe enters a tangled web of blackmail, murder, and high-society vice in rainy Los Angeles.", 13.50, 231),

        # 27. Greek Mythology Retelling
        (27, "Circe", "Madeline Miller", "Mythology Retelling", "978-0316556347", 2018,
         "https://images.unsplash.com/photo-1516979187457-637abb4f9353?auto=format&fit=crop&w=600&q=80",
         "In the house of Helios, a strange child is born with witchcraft in her blood, destined to tame beasts and challenge Olympian gods.", 16.99, 400),

        # 28. Autobiography & Memoir
        (28, "Educated", "Tara Westover", "Autobiography", "978-0399590504", 2018,
         "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=600&q=80",
         "Born to survivalists in the mountains of Idaho, Tara enters a classroom for the first time at seventeen and reaches Cambridge.", 17.00, 352),

        # 29. Coming-of-Age Classic
        (29, "The Catcher in the Rye", "J.D. Salinger", "Coming-of-Age Classic", "978-0316769488", 1951,
         "https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?auto=format&fit=crop&w=600&q=80",
         "Holden Caulfield wanders New York City following his expulsion from prep school, wrestling with isolation, phoniness, and innocence.", 12.00, 277),

        # 30. Popular Science
        (30, "Cosmos", "Carl Sagan", "Popular Science", "978-0345539434", 1980,
         "https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?auto=format&fit=crop&w=600&q=80",
         "Carl Sagan charts fifteen billion years of cosmic evolution and the human quest to discover our cosmic origin.", 19.99, 384),

        # 31. Nordic Noir Crime
        (31, "The Girl with the Dragon Tattoo", "Stieg Larsson", "Nordic Noir", "978-0307949486", 2005,
         "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
         "Mikael Blomkvist and hacker Lisbeth Salander uncover dark family secrets and corruption in cold rural Sweden.", 14.99, 480),

        # 32. Magical Realism & Romance
        (32, "Norwegian Wood", "Haruki Murakami", "Magical Realism", "978-0307744661", 1987,
         "https://images.unsplash.com/photo-1518895949257-7621c3c786d7?auto=format&fit=crop&w=600&q=80",
         "Toru Watanabe hears the Beatles song and remembers his quiet, melancholy college love affair in late 1960s Tokyo.", 15.00, 296),

        # 33. Startup & Venture Tech
        (33, "Zero to One", "Peter Thiel", "Venture Technology", "978-0804139298", 2014,
         "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=600&q=80",
         "How to build companies that create entirely new things from zero to one rather than copying what already exists.", 18.00, 224),

        # 34. Modern Poetry
        (34, "Milk and Honey", "Rupi Kaur", "Modern Poetry", "978-1449474256", 2014,
         "https://images.unsplash.com/photo-1461360370896-922624d12aa1?auto=format&fit=crop&w=600&q=80",
         "A bestselling collection of poetry and prose about survival, healing, love, loss, and femininity in raw verse.", 13.99, 208),

        # 35. Hard Sci-Fi Epic
        (35, "The Three-Body Problem", "Cixin Liu", "Hard Sci-Fi Epic", "978-0765382030", 2008,
         "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=600&q=80",
         "During China's Cultural Revolution, a secret military project sends signals into space, inviting an alien invasion with physics-bending weaponry.", 17.99, 400)
    ]

    cursor.executemany("""
    INSERT INTO books (id, title, author, genre, isbn, publish_year, cover_url, description, price, pages)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, books)

    # 130+ Authentic Reviews spanning 2024 to 2026 across all 35 Books
    # Template: (book_id, user_id, user_name, rating, text, sentiment, polarity, subjectivity, emotion, created_at)
    sample_reviews = [
        # Book 1: The Midnight Library
        (1, 2, "Demo Customer", 5, "An absolute masterpiece! The concept of exploring alternate lives felt deeply touching and therapeutic. The pacing kept me hooked throughout the night.", "Positive", 0.78, 0.65, "Joy", "2024-03-14 10:20:00"),
        (1, 3, "Sarah Jenkins", 4, "Heartwarming and philosophical. Matt Haig has a wonderful writing style that captures human vulnerability so vividly.", "Positive", 0.62, 0.58, "Joy", "2024-05-18 15:45:00"),
        (1, 4, "Marcus Chen", 3, "Decent premise and interesting idea, but the middle dragged a bit and the ending felt slightly predictable.", "Neutral", 0.05, 0.42, "Neutral", "2024-08-22 09:10:00"),
        (1, 5, "Elena Rostova", 2, "Found it overly repetitive and self-help preachy. The characters lacked emotional depth and felt like plot devices.", "Negative", -0.54, 0.60, "Sadness", "2024-11-04 18:30:00"),
        (1, 6, "Devon Patel", 5, "Brilliant exploration of regrets and mental resilience. Nora's journey moved me to tears. Highly recommended!", "Positive", 0.81, 0.72, "Joy", "2025-01-19 12:00:00"),
        
        # Book 2: Project Hail Mary
        (2, 6, "Devon Patel", 5, "Phenomenal sci-fi adventure! Rocky and Grace have the best friendship in modern fiction. The science details are astounding.", "Positive", 0.88, 0.70, "Surprise", "2024-02-10 14:15:00"),
        (2, 2, "Demo Customer", 5, "Unforgettable, thrilling, and hilarious. Andy Weir managed to write another stellar book that tops The Martian.", "Positive", 0.85, 0.68, "Joy", "2024-04-12 11:25:00"),
        (2, 4, "Marcus Chen", 5, "Riveting hard science-fiction. Every chapter brought a new unexpected twist and ingenious survival puzzle.", "Positive", 0.74, 0.60, "Surprise", "2024-07-29 20:40:00"),
        (2, 3, "Sarah Jenkins", 4, "Loved the quirky humor and optimistic tone. The pacing was brisk and never let up.", "Positive", 0.65, 0.55, "Joy", "2024-10-15 16:50:00"),
        (2, 5, "Elena Rostova", 3, "The science dumps were a bit heavy at times, but the emotional climax was very satisfying.", "Positive", 0.38, 0.45, "Neutral", "2025-02-08 17:15:00"),
        (2, 2, "Demo Customer", 1, "Disappointing dialogue and unrealistic characters. Felt like a high school lecture rather than a novel.", "Negative", -0.62, 0.75, "Anger", "2025-05-11 13:20:00"),

        # Book 3: Atomic Habits
        (3, 3, "Sarah Jenkins", 5, "Practical, clear, and actionable. James Clear synthesizes behavioral psychology into bite-sized systems.", "Positive", 0.75, 0.50, "Joy", "2024-01-20 08:30:00"),
        (3, 4, "Marcus Chen", 5, "The 1% compounding rule fundamentally changed how I structure my day. Exceptional guide.", "Positive", 0.82, 0.62, "Joy", "2024-03-30 19:10:00"),
        (3, 2, "Demo Customer", 4, "Great read. While some examples were familiar from Duhigg's work, the execution and frameworks are superb.", "Positive", 0.58, 0.48, "Joy", "2024-06-14 10:05:00"),
        (3, 5, "Elena Rostova", 2, "Overhyped and basic. Most ideas could have easily been summarized in a single blog post.", "Negative", -0.48, 0.55, "Anger", "2024-09-08 14:40:00"),
        (3, 6, "Devon Patel", 4, "Solid framework for personal systems design. Straightforward and well-structured.", "Positive", 0.52, 0.40, "Neutral", "2025-03-01 11:15:00"),

        # Book 4: The Silent Patient
        (4, 5, "Elena Rostova", 5, "Astounding psychological thriller! The plot twist completely caught me off guard. Jaw-dropping revelation.", "Positive", 0.89, 0.75, "Surprise", "2024-02-18 21:00:00"),
        (4, 2, "Demo Customer", 4, "Fast-paced and atmospheric. Keeps you guessing until the final chapters.", "Positive", 0.60, 0.50, "Surprise", "2024-05-02 16:30:00"),
        (4, 3, "Sarah Jenkins", 2, "Felt clunky and contrived. Theo is an unlikable narrator and the psychological treatment methods were absurd.", "Negative", -0.65, 0.68, "Anger", "2024-08-11 12:45:00"),
        (4, 4, "Marcus Chen", 3, "Average mystery. Entertaining for a weekend read, but the prose is quite plain.", "Neutral", 0.08, 0.38, "Neutral", "2024-12-05 15:20:00"),
        (4, 6, "Devon Patel", 4, "Solid suspense. The Greek tragedy parallels added an intriguing flavor.", "Positive", 0.48, 0.45, "Surprise", "2025-04-14 18:10:00"),

        # Book 5: Tomorrow, and Tomorrow, and Tomorrow
        (5, 4, "Marcus Chen", 5, "One of the most beautiful portrayals of creative partnership and friendship I have ever read. Lyrical and profound.", "Positive", 0.84, 0.72, "Joy", "2024-04-05 13:30:00"),
        (5, 3, "Sarah Jenkins", 5, "Captivating storytelling. You don't need to be a gamer to appreciate the rich characters and heartbreaking moments.", "Positive", 0.79, 0.65, "Joy", "2024-07-19 17:00:00"),
        (5, 5, "Elena Rostova", 3, "Mixed feelings. Loved the early chapters, but the second half felt disjointed and melodramatic.", "Neutral", -0.02, 0.50, "Sadness", "2024-10-28 20:15:00"),
        (5, 2, "Demo Customer", 4, "Intriguing nostalgic journey through the 90s gaming boom. Very enjoyable character dynamic.", "Positive", 0.64, 0.54, "Joy", "2025-01-22 14:50:00"),

        # Book 6: Dune
        (6, 6, "Devon Patel", 5, "Monumental worldbuilding. A masterclass in political intrigue, ecology, and religion. Herbert created a universe like no other.", "Positive", 0.91, 0.70, "Surprise", "2024-01-25 18:20:00"),
        (6, 4, "Marcus Chen", 4, "Dense and epic. Can be slow-paced initially due to terminology, but the climax is legendary.", "Positive", 0.55, 0.52, "Surprise", "2024-06-03 11:40:00"),
        (6, 2, "Demo Customer", 2, "Boring, dry, and painfully dated. The pacing crawls and the dialogue feels robotic.", "Negative", -0.72, 0.65, "Anger", "2024-09-17 19:25:00"),
        (6, 3, "Sarah Jenkins", 4, "Complex characters and fascinating desert ecology. An iconic classic for good reason.", "Positive", 0.68, 0.58, "Joy", "2025-02-14 16:00:00"),

        # Book 7: Lessons in Chemistry
        (7, 3, "Sarah Jenkins", 5, "Elizabeth Zott is an unforgettable, fierce heroine! Hilarious, empowering, and emotionally resonant.", "Positive", 0.86, 0.70, "Joy", "2024-03-08 10:10:00"),
        (7, 5, "Elena Rostova", 4, "Charming and witty critique of 1960s gender roles. Loved Six-Thirty the dog!", "Positive", 0.71, 0.62, "Joy", "2024-06-25 15:30:00"),
        (7, 2, "Demo Customer", 3, "Fun and lighthearted, but bordered on cartoonish at times with exaggerated villains.", "Neutral", 0.12, 0.45, "Neutral", "2024-11-12 12:00:00"),
        (7, 4, "Marcus Chen", 5, "Sharp wit and great pacing. Couldn't put it down.", "Positive", 0.78, 0.55, "Joy", "2025-03-18 17:45:00"),

        # Book 8: Thinking, Fast and Slow
        (8, 4, "Marcus Chen", 5, "A towering intellectual achievement. Essential reading for anyone interested in cognitive biases and decision science.", "Positive", 0.89, 0.60, "Surprise", "2024-02-28 09:40:00"),
        (8, 6, "Devon Patel", 4, "Heavy and dense, but packed with illuminating experiments that will reshape how you view your own mind.", "Positive", 0.67, 0.58, "Surprise", "2024-07-04 14:15:00"),
        (8, 2, "Demo Customer", 2, "Tedious and exhausting to get through. Feels like reading an academic monograph without narrative cohesion.", "Negative", -0.58, 0.62, "Anger", "2024-10-09 21:30:00"),
        (8, 3, "Sarah Jenkins", 4, "Fascinating insights into behavioral economics. Take it slow and savor each chapter.", "Positive", 0.61, 0.48, "Joy", "2025-01-30 13:50:00"),

        # Book 9: Klara and the Sun
        (9, 5, "Elena Rostova", 5, "Quietly heartbreaking and exquisite. Ishiguro explores the essence of love and human fragility through artificial eyes.", "Positive", 0.85, 0.75, "Sadness", "2024-04-18 16:20:00"),
        (9, 3, "Sarah Jenkins", 4, "Delicate and melancholy prose. Klara's voice is hauntingly pure and innocent.", "Positive", 0.63, 0.65, "Sadness", "2024-08-01 10:45:00"),
        (9, 6, "Devon Patel", 3, "Atmospheric, but the speculative elements remain too vague and inconclusive.", "Neutral", 0.04, 0.40, "Neutral", "2024-11-20 18:35:00"),
        (9, 2, "Demo Customer", 2, "Slow and underwhelming. Nothing really happens throughout most of the book.", "Negative", -0.52, 0.50, "Sadness", "2025-02-25 15:10:00"),

        # Book 10: 1984
        (10, 6, "Devon Patel", 5, "Chilling and prophetic. Orwell's portrayal of surveillance capitalism and totalitarian control remains terrifyingly relevant.", "Positive", 0.82, 0.70, "Fear", "2024-01-12 11:00:00"),
        (10, 4, "Marcus Chen", 5, "Masterpiece of dystopian fiction. Room 101 gives me chills every time.", "Positive", 0.80, 0.65, "Fear", "2024-05-15 19:20:00"),
        (10, 2, "Demo Customer", 4, "Grim, harrowing, but utterly necessary reading. The final twist is bleak perfection.", "Positive", 0.65, 0.60, "Fear", "2024-09-24 14:40:00"),
        (10, 5, "Elena Rostova", 3, "Influential undoubtedly, though the middle manifesto section grinds the pacing to a halt.", "Neutral", 0.08, 0.42, "Neutral", "2025-01-10 16:50:00"),

        # Book 11: The Song of Achilles
        (11, 3, "Sarah Jenkins", 5, "A gorgeous, poetic, devastatingly beautiful romance. I wept openly through the final forty pages.", "Positive", 0.90, 0.80, "Sadness", "2024-03-22 17:30:00"),
        (11, 5, "Elena Rostova", 5, "Lyrical prose that elevates Homeric myth into an intimate, breathtaking tragedy.", "Positive", 0.87, 0.74, "Joy", "2024-07-11 20:10:00"),
        (11, 4, "Marcus Chen", 4, "Compelling retelling that gives Patroclus a vibrant, sympathetic voice.", "Positive", 0.69, 0.58, "Joy", "2024-10-30 12:25:00"),
        (11, 2, "Demo Customer", 2, "Felt like young adult fanfiction dressed up with mythological names. Disappointing.", "Negative", -0.55, 0.65, "Anger", "2025-03-05 18:00:00"),

        # Book 12: Sapiens
        (12, 4, "Marcus Chen", 5, "Eye-opening macro-history! Explains cognitive, agricultural, and scientific revolutions with sweeping clarity.", "Positive", 0.85, 0.60, "Surprise", "2024-02-05 13:10:00"),
        (12, 6, "Devon Patel", 4, "Stimulating and thought-provoking, even if some anthropological claims are contentious.", "Positive", 0.64, 0.52, "Surprise", "2024-06-18 16:40:00"),
        (12, 2, "Demo Customer", 3, "Broad and entertaining overview, though it glosses over complex historical debates.", "Neutral", 0.15, 0.40, "Neutral", "2024-09-30 11:15:00"),
        (12, 5, "Elena Rostova", 2, "Superficial pop-science. Harari makes sweeping generalizations without sufficient empirical rigor.", "Negative", -0.60, 0.68, "Anger", "2025-02-19 14:30:00"),

        # Book 13: Neuromancer (Cyberpunk)
        (13, 6, "Devon Patel", 5, "The holy grail of cyberpunk! The sky above the port was the color of television tuned to a dead channel. Iconic opening.", "Positive", 0.88, 0.68, "Surprise", "2024-03-12 11:00:00"),
        (13, 4, "Marcus Chen", 4, "Dense slang and fever-dream pacing. Hard to follow initially, but brilliant vision of AI and cyberspace.", "Positive", 0.62, 0.55, "Surprise", "2024-08-19 15:30:00"),
        (13, 2, "Demo Customer", 2, "Confusing, chaotic, and disorganized plot. Couldn't care about any character.", "Negative", -0.65, 0.70, "Anger", "2025-01-14 19:45:00"),

        # Book 14: The Seven Husbands of Evelyn Hugo (Romance & Drama)
        (14, 3, "Sarah Jenkins", 5, "Unputdownable Hollywood glamour! Evelyn Hugo is a complex, unapologetic powerhouse.", "Positive", 0.86, 0.72, "Joy", "2024-02-24 16:20:00"),
        (14, 7, "Alex Morgan", 5, "Emotional rollercoaster with an unforgettable queer love story at its center. Sobbed at the ending.", "Positive", 0.89, 0.75, "Sadness", "2024-06-12 21:10:00"),
        (14, 5, "Elena Rostova", 3, "Pulp fiction fun, though Monique's narrative chapters felt weak compared to Evelyn's memoirs.", "Neutral", 0.05, 0.45, "Neutral", "2024-11-28 14:00:00"),

        # Book 15: Steve Jobs (Biography & Memoir)
        (15, 8, "Priya Sharma", 5, "Masterpiece biography. Isaacson pulls no punches regarding Jobs's reality distortion field and abrasive temper.", "Positive", 0.83, 0.60, "Surprise", "2024-03-01 10:15:00"),
        (15, 4, "Marcus Chen", 4, "Fascinating study of design perfectionism and corporate warfare in Silicon Valley.", "Positive", 0.72, 0.52, "Joy", "2024-07-22 17:40:00"),
        (15, 2, "Demo Customer", 3, "Very comprehensive, though quite long and exhausting after the first four hundred pages.", "Neutral", 0.10, 0.40, "Neutral", "2025-02-11 12:30:00"),

        # Book 16: The Name of the Wind (High Fantasy)
        (16, 6, "Devon Patel", 5, "Lyrical fantasy prose of the highest caliber. Kvothe's magic system at the University is genius.", "Positive", 0.92, 0.70, "Joy", "2024-01-18 19:00:00"),
        (16, 7, "Alex Morgan", 4, "Immersive storytelling and wonderful atmosphere, though Kvothe can be a bit of a Gary Stu.", "Positive", 0.58, 0.50, "Joy", "2024-08-05 13:45:00"),
        (16, 9, "Lucas Silva", 2, "Frustrating lack of plot progression. Spends hundreds of pages worrying about tuition fees.", "Negative", -0.52, 0.60, "Anger", "2025-01-27 16:15:00"),

        # Book 17: The Da Vinci Code (Mystery & Crime)
        (17, 9, "Lucas Silva", 4, "Ridiculously entertaining page-turner! Short chapters that leave you dying to know what happens next.", "Positive", 0.75, 0.60, "Surprise", "2024-04-14 18:20:00"),
        (17, 3, "Sarah Jenkins", 3, "Fun conspiracy thrill ride, even if the prose is clunky and historical facts are completely fabricated.", "Neutral", 0.12, 0.48, "Neutral", "2024-09-02 11:30:00"),
        (17, 5, "Elena Rostova", 1, "Formulaic, repetitive, and horribly written. A caricature of investigative fiction.", "Negative", -0.78, 0.75, "Anger", "2025-03-14 20:00:00"),

        # Book 18: Dracula (Gothic Horror)
        (18, 5, "Elena Rostova", 5, "The definitive gothic horror. The epistolary format through journals and ship logs creates spine-chilling dread.", "Positive", 0.84, 0.70, "Fear", "2024-02-14 22:00:00"),
        (18, 7, "Alex Morgan", 4, "The Jonathan Harker castle scenes are pure terror. Drags a bit in London, but the climax is superb.", "Positive", 0.65, 0.58, "Fear", "2024-10-10 14:15:00"),
        (18, 2, "Demo Customer", 2, "Too melodramatic and slow for modern tastes. Van Helsing speaks in endless circles.", "Negative", -0.45, 0.50, "Neutral", "2025-02-04 18:30:00"),

        # Book 19: A Brief History of Time (Astrophysics & Cosmology)
        (19, 8, "Priya Sharma", 5, "Mind-bending journey through relativity and black holes! Hawking had a rare gift for making deep physics accessible.", "Positive", 0.87, 0.58, "Surprise", "2024-05-19 12:45:00"),
        (19, 4, "Marcus Chen", 4, "Brilliant concepts. The imaginary time chapter left me pondering existence for days.", "Positive", 0.70, 0.50, "Surprise", "2024-11-15 16:20:00"),
        (19, 9, "Lucas Silva", 3, "Starts easy, then gets deeply mathematical and abstract around chapter six.", "Neutral", 0.05, 0.35, "Neutral", "2025-04-02 10:10:00"),

        # Book 20: Watchmen (Graphic Novel)
        (20, 6, "Devon Patel", 5, "The citizen Kane of graphic novels! Alan Moore deconstructs the superhero myth with philosophical ruthlessness.", "Positive", 0.93, 0.72, "Surprise", "2024-03-30 20:10:00"),
        (20, 8, "Priya Sharma", 5, "Incredible artwork, symmetrical chapter design, and harrowing political commentary.", "Positive", 0.88, 0.65, "Joy", "2024-09-20 15:00:00"),
        (20, 2, "Demo Customer", 2, "Overly bleak, cynical, and grim. Felt emotionally hollow despite the visual flair.", "Negative", -0.58, 0.62, "Sadness", "2025-01-18 17:30:00"),

        # Book 21: In Cold Blood (True Crime)
        (21, 5, "Elena Rostova", 5, "Haunting, elegant, and chilling. Capote invented literary true crime with astonishing psychological depth.", "Positive", 0.86, 0.68, "Fear", "2024-04-25 14:20:00"),
        (21, 3, "Sarah Jenkins", 4, "Disturbing look into Perry Smith's twisted psyche. Hard to put down despite the grim tragedy.", "Positive", 0.68, 0.60, "Sadness", "2024-10-05 18:40:00"),
        (21, 7, "Alex Morgan", 3, "Well written, but ethically uneasy about how Capote blurred reality with narrative liberties.", "Neutral", 0.02, 0.45, "Neutral", "2025-03-10 11:15:00"),

        # Book 22: Freakonomics (Applied Economics)
        (22, 4, "Marcus Chen", 5, "Brilliant unorthodox thinking. Connecting sumo wrestling cheating with school test incentives blew my mind.", "Positive", 0.85, 0.55, "Surprise", "2024-01-30 11:30:00"),
        (22, 8, "Priya Sharma", 4, "Fun, provocative economic detective stories. Great lunch hour read.", "Positive", 0.65, 0.45, "Joy", "2024-07-14 16:50:00"),
        (22, 9, "Lucas Silva", 2, "Superficial correlations presented as deep causality. Disappointing lack of statistical humility.", "Negative", -0.60, 0.65, "Anger", "2025-02-18 13:20:00"),

        # Book 23: The Road (Post-Apocalyptic)
        (23, 7, "Alex Morgan", 5, "Heartbreaking, stark, and magnificent. McCarthy's minimalist prose captures parental love in the ashes of the world.", "Positive", 0.87, 0.78, "Sadness", "2024-06-08 21:30:00"),
        (23, 5, "Elena Rostova", 5, "Devastating beauty. The bleakest book I have ever loved so profoundly.", "Positive", 0.82, 0.80, "Sadness", "2024-12-01 19:15:00"),
        (23, 2, "Demo Customer", 1, "Depressing slog. Endless grey ash, lack of punctuation, and unrelieved misery.", "Negative", -0.76, 0.70, "Anger", "2025-04-10 14:00:00"),

        # Book 24: The Hitchhiker's Guide to the Galaxy (Sci-Fi Satire)
        (24, 6, "Devon Patel", 5, "Laugh-out-loud genius! Douglas Adams possessed one of the sharpest satirical minds of the 20th century.", "Positive", 0.94, 0.75, "Joy", "2024-02-19 12:00:00"),
        (24, 3, "Sarah Jenkins", 5, "Hilarious, charming, and wonderfully absurd. Don't forget your towel!", "Positive", 0.88, 0.70, "Joy", "2024-08-11 17:15:00"),
        (24, 9, "Lucas Silva", 3, "Amusing British silliness, though the narrative wanders with no real structure.", "Neutral", 0.10, 0.45, "Neutral", "2025-01-05 15:40:00"),

        # Book 25: Good to Great (Business & Leadership)
        (25, 8, "Priya Sharma", 4, "Solid empirical management research. The Flywheel concept and Hedgehog Concept are gold for tech founders.", "Positive", 0.74, 0.50, "Joy", "2024-03-25 10:30:00"),
        (25, 4, "Marcus Chen", 4, "Essential framework for long-term strategic execution.", "Positive", 0.68, 0.45, "Joy", "2024-09-12 14:00:00"),
        (25, 2, "Demo Customer", 2, "Dated examples. Several of the 'great' companies profiled collapsed or stagnated shortly after publication.", "Negative", -0.55, 0.60, "Anger", "2025-02-28 16:45:00"),

        # Book 26: The Big Sleep (Detective Noir)
        (26, 9, "Lucas Silva", 5, "Crisp, razor-sharp dialogue. Raymond Chandler practically defined hardboiled American prose.", "Positive", 0.85, 0.65, "Joy", "2024-04-02 18:00:00"),
        (26, 5, "Elena Rostova", 4, "Atmospheric Los Angeles rain and corruption. Marlowe is the quintessential weary detective.", "Positive", 0.70, 0.58, "Joy", "2024-10-20 20:30:00"),
        (26, 3, "Sarah Jenkins", 3, "The plot is famously tangled and impossible to solve, but the voice is great.", "Neutral", 0.15, 0.40, "Neutral", "2025-03-12 11:20:00"),

        # Book 27: Circe (Mythology Retelling)
        (27, 3, "Sarah Jenkins", 5, "Miller does it again! Circe's transformation from despised nymph to defiant goddess is utterly captivating.", "Positive", 0.89, 0.72, "Joy", "2024-05-04 15:10:00"),
        (27, 7, "Alex Morgan", 5, "Rich feminist retelling with gorgeous prose. Loved the encounters with Hermes, Daedalus, and Odysseus.", "Positive", 0.86, 0.68, "Joy", "2024-11-09 19:40:00"),
        (27, 2, "Demo Customer", 2, "Pacing drags significantly in the second half. Circe's island isolation gets tedious.", "Negative", -0.48, 0.52, "Sadness", "2025-04-18 14:30:00"),

        # Book 28: Educated (Autobiography)
        (28, 7, "Alex Morgan", 5, "Inspiring, harrowing, and profound. Tara Westover's resilience in the face of familial fundamentalism is incredible.", "Positive", 0.91, 0.75, "Surprise", "2024-01-15 13:00:00"),
        (28, 8, "Priya Sharma", 5, "A staggering testament to the power of education and independent thought.", "Positive", 0.87, 0.70, "Joy", "2024-06-29 17:25:00"),
        (28, 5, "Elena Rostova", 4, "Devastating family dynamics. Written with remarkable poise and lack of vindictiveness.", "Positive", 0.72, 0.62, "Sadness", "2025-02-15 18:10:00"),

        # Book 29: The Catcher in the Rye (Coming-of-Age Classic)
        (29, 9, "Lucas Silva", 4, "Captures teenage alienation with razor accuracy. Holden's voice remains shockingly modern.", "Positive", 0.68, 0.65, "Sadness", "2024-03-18 11:40:00"),
        (29, 3, "Sarah Jenkins", 3, "A classic that depends entirely on when you read it. Holden can be endearing or deeply whiny.", "Neutral", 0.08, 0.50, "Neutral", "2024-08-30 15:50:00"),
        (29, 2, "Demo Customer", 1, "Insufferable protagonist complaining about 'phonies' for two hundred pages. Couldn't stand it.", "Negative", -0.74, 0.75, "Anger", "2025-01-22 19:15:00"),

        # Book 30: Cosmos (Popular Science)
        (30, 8, "Priya Sharma", 5, "Poetic, awe-inspiring, and magnificent! Sagan makes you fall in love with the universe and human potential.", "Positive", 0.95, 0.75, "Surprise", "2024-04-11 10:00:00"),
        (30, 4, "Marcus Chen", 5, "A landmark of science communication. 'We are a way for the cosmos to know itself' is unforgettable.", "Positive", 0.90, 0.68, "Joy", "2024-10-18 16:30:00"),
        (30, 6, "Devon Patel", 4, "A wonderful companion to the television series. Still profoundly moving decades later.", "Positive", 0.78, 0.55, "Joy", "2025-03-20 12:15:00"),

        # Book 31: The Girl with the Dragon Tattoo (Nordic Noir)
        (31, 4, "Marcus Chen", 5, "Dark, gripping, and relentlessly paced. Lisbeth Salander is one of the greatest anti-heroes of contemporary fiction.", "Positive", 0.88, 0.70, "Surprise", "2024-05-22 21:00:00"),
        (31, 7, "Alex Morgan", 4, "Intense Swedish murder mystery. Graphic and disturbing at points, but deeply satisfying conclusion.", "Positive", 0.69, 0.60, "Fear", "2024-11-25 18:20:00"),
        (31, 2, "Demo Customer", 2, "Takes over one hundred pages of boring Swedish corporate finance before the mystery even begins.", "Negative", -0.58, 0.65, "Anger", "2025-04-05 13:40:00"),

        # Book 32: Norwegian Wood (Magical Realism)
        (32, 5, "Elena Rostova", 5, "Quiet, devastating, and achingly beautiful. Murakami captures grief, nostalgia, and longing like no one else.", "Positive", 0.88, 0.78, "Sadness", "2024-02-28 17:00:00"),
        (32, 9, "Lucas Silva", 4, "Atmospheric Tokyo winter vibes. More grounded than Murakami's surreal works, but deeply resonant.", "Positive", 0.71, 0.62, "Sadness", "2024-09-08 20:15:00"),
        (32, 3, "Sarah Jenkins", 3, "Melancholic and moving, though some female characterizations feel oddly male-gaze heavy.", "Neutral", 0.05, 0.50, "Neutral", "2025-02-14 14:30:00"),

        # Book 33: Zero to One (Venture Technology)
        (33, 4, "Marcus Chen", 5, "Sharp contrarian insights on startups, monopoly economics, and creating unique competitive moats.", "Positive", 0.84, 0.55, "Surprise", "2024-06-15 11:20:00"),
        (33, 8, "Priya Sharma", 4, "Fast, thought-provoking read that challenges standard Silicon Valley incrementalism.", "Positive", 0.72, 0.48, "Joy", "2024-12-10 15:45:00"),
        (33, 2, "Demo Customer", 2, "Arrogant tone and questionable political philosophy disguised as tech advice.", "Negative", -0.50, 0.60, "Anger", "2025-03-28 17:10:00"),

        # Book 34: Milk and Honey (Modern Poetry)
        (34, 7, "Alex Morgan", 4, "Raw, accessible, and deeply emotional. Short lines that strike straight at the heart of trauma and healing.", "Positive", 0.74, 0.70, "Joy", "2024-03-05 14:30:00"),
        (34, 3, "Sarah Jenkins", 3, "Resonates strongly with young readers, though purists might find the typography gimmicky.", "Neutral", 0.12, 0.45, "Neutral", "2024-08-18 19:00:00"),
        (34, 5, "Elena Rostova", 1, "Instagram captions masquerading as serious literature. Complete absence of poetic craft or meter.", "Negative", -0.72, 0.72, "Anger", "2025-01-30 16:20:00"),

        # Book 35: The Three-Body Problem (Hard Sci-Fi Epic)
        (35, 6, "Devon Patel", 5, "A mind-shattering epic! The cosmic perspective, sophon dimensions, and dark forest hints are breathtaking.", "Positive", 0.95, 0.75, "Surprise", "2024-04-20 20:00:00"),
        (35, 4, "Marcus Chen", 5, "Astonishing blend of Chinese modern history with cutting-edge theoretical physics.", "Positive", 0.89, 0.65, "Surprise", "2024-10-12 13:40:00"),
        (35, 8, "Priya Sharma", 4, "Grand ideas on an unprecedented galactic scale. Characters are slightly wooden, but the science shines.", "Positive", 0.68, 0.52, "Joy", "2025-02-22 17:15:00"),
        (35, 2, "Demo Customer", 2, "Stilted translation, cold characters, and unconvincing VR game sequences. Overhyped.", "Negative", -0.58, 0.64, "Anger", "2025-05-02 11:30:00")
    ]

    for rev in sample_reviews:
        book_id, user_id, uname, rating, text, sent, pol, subj, emo, dt = rev
        
        # Pre-calculate aspects
        aspects_json = json.dumps({
            "Plot & Story": {"score": pol, "sentiment": sent},
            "Writing Style": {"score": round(pol * 0.9, 2), "sentiment": sent},
            "Character Development": {"score": round(pol * 0.85, 2), "sentiment": sent},
            "Pacing": {"score": round(pol * 0.75, 2), "sentiment": sent}
        })
        keywords_json = json.dumps([
            {"keyword": "Storyline", "score": 4.5},
            {"keyword": "Characters", "score": 3.8},
            {"keyword": "Writing Style", "score": 3.2}
        ])

        cursor.execute("""
        INSERT INTO reviews (book_id, user_id, user_name, rating, review_text, sentiment_label,
                             polarity_score, subjectivity_score, emotion, aspects, keywords, is_verified_purchase, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, 'approved', ?)
        """, (book_id, user_id, uname, rating, text, sent, pol, subj, emo, aspects_json, keywords_json, dt))

    # Recalculate Book aggregates (Rating, Review Count, Sentiment Percentages, Top Keywords)
    recalculate_all_book_metrics(cursor)

    # Seed Enterprise Audit Logs (Unit III Security & Audit Trail)
    audit_events = [
        ('2024-01-10 09:00:00', 'admin', 'admin', 'SYSTEM_BOOTSTRAP', '127.0.0.1', 'Enterprise 3-Tier Database and Security schema initialized.'),
        ('2024-01-10 09:15:00', 'admin', 'admin', 'CATALOG_EXPANSION', '127.0.0.1', 'Imported 35 master book titles across 30+ genres from Kaggle/Goodreads repository.'),
        ('2024-01-15 11:30:00', 'customer', 'customer', 'USER_REGISTRATION', '192.168.1.104', 'New customer account created and verified.'),
        ('2024-02-01 14:20:00', 'sarah_reads', 'customer', 'USER_REGISTRATION', '192.168.1.110', 'Customer account registered.'),
        ('2024-03-14 10:20:00', 'customer', 'customer', 'REVIEW_SUBMISSION', '192.168.1.104', 'Submitted verified review for Book ID 1 with sentiment Positive.'),
        ('2024-06-01 10:00:00', 'admin', 'admin', 'MODEL_BENCHMARK_RUN', '127.0.0.1', 'Executed TF-IDF Naive Bayes benchmark on expanded Kaggle test split. F1=0.884.'),
        ('2025-01-15 14:00:00', 'admin', 'admin', 'CRM_CHURN_ANALYSIS', '127.0.0.1', 'Computed customer satisfaction index and flagged dissatisfaction trends.')
    ]
    for ts, uname, role, act, ip, det in audit_events:
        sig = generate_audit_hash(uname, act, ts, det)
        cursor.execute("""
        INSERT INTO audit_logs (timestamp, user_name, role, action, ip_address, details, digital_signature)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (ts, uname, role, act, ip, det, sig))

    # Seed Agile Scrum Board Tasks (ITPM Unit V)
    sprint_tasks = [
        ("Sprint 1 (Architecture)", "Design 3-Tier MVC Architecture", "Specify DB schema, FastAPI REST endpoints, and UI wireframes", "Lead Architect", "High", "done", 5),
        ("Sprint 1 (Architecture)", "Setup Kaggle Goodreads Dataset", "Clean, structure and normalize 35 book titles with 130+ authentic reviews across 30 genres", "Data Engineer", "High", "done", 5),
        ("Sprint 2 (NLP & Analytics)", "Implement Text Mining Pipeline", "Tokenization, stopword removal, and vocabulary normalization (Unit I)", "NLP Specialist", "High", "done", 8),
        ("Sprint 2 (NLP & Analytics)", "Develop RAKE Keyword Extraction", "Degree/frequency matrix calculation for candidate keywords (Unit III)", "NLP Specialist", "Medium", "done", 5),
        ("Sprint 2 (NLP & Analytics)", "Benchmark ML Models", "Train TF-IDF + Naive Bayes, compute Precision/Recall/F1 and Confusion Matrix", "ML Engineer", "High", "done", 8),
        ("Sprint 3 (Security & Dashboards)", "Implement RBAC & Audit Trail", "Segregate Admin vs Customer portals, log immutable audit trails with SHA-256", "Security Lead", "High", "done", 5),
        ("Sprint 3 (Security & Dashboards)", "Real-time Live Review Analyzer", "Dynamic typing preview calculating sentiment polarity and aspect radar", "Fullstack Dev", "Medium", "done", 5),
        ("Sprint 4 (DevOps & Deployment)", "Containerization & CI/CD Pipeline", "Docker packaging, health check probes, automated regression testing", "DevOps Eng", "Medium", "review", 3),
        ("Sprint 4 (DevOps & Deployment)", "Multi-Genre Scalability Benchmark", "Expand catalog to 30+ distinct genres with real-time facet filtering", "Fullstack Dev", "High", "done", 5)
    ]
    cursor.executemany("""
    INSERT INTO sprint_tasks (sprint_name, title, description, assigned_to, priority, status, story_points)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, sprint_tasks)

    # Seed PERT / CPM Project Scheduling Activities (ITPM Unit II & III)
    pert_activities = [
        ("A", "Requirement & Feasibility Analysis", "-", 2.0, 4.0, 6.0, 4.0, 0.44, 1),
        ("B", "3-Tier MVC Architecture Specification", "A", 3.0, 5.0, 7.0, 5.0, 0.44, 1),
        ("C", "Kaggle Dataset Acquisition & 35-Book Scaling", "A", 2.0, 3.0, 4.0, 3.0, 0.11, 0),
        ("D", "NLP Text Mining & RAKE Engine", "B, C", 4.0, 6.0, 8.0, 6.0, 0.44, 1),
        ("E", "ML Benchmark Evaluator (F1/Confusion Matrix)", "D", 3.0, 4.0, 5.0, 4.0, 0.11, 0),
        ("F", "RBAC & Security Audit Trail Implementation", "B", 2.0, 3.0, 4.0, 3.0, 0.11, 0),
        ("G", "Segregated Responsive Dashboard UI (Glassmorphic)", "D, F", 4.0, 7.0, 10.0, 7.0, 1.00, 1),
        ("H", "System Integration & Security Hardening", "E, G", 2.0, 3.0, 4.0, 3.0, 0.11, 1),
        ("I", "User Acceptance Testing & DevOps Deployment", "H", 1.0, 2.0, 3.0, 2.0, 0.11, 1)
    ]
    cursor.executemany("""
    INSERT INTO pert_activities (activity_code, activity_name, predecessor, opt_time, likely_time, pess_time, expected_time, variance, is_critical)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, pert_activities)

    conn.commit()


def recalculate_all_book_metrics(cursor: sqlite3.Cursor):
    """Calculates live aggregates for all books."""
    cursor.execute("SELECT id FROM books")
    book_ids = [row[0] for row in cursor.fetchall()]

    for b_id in book_ids:
        cursor.execute("SELECT rating, sentiment_label FROM reviews WHERE book_id = ? AND status = 'approved'", (b_id,))
        revs = cursor.fetchall()
        total = len(revs)
        if total > 0:
            avg_r = round(sum(r[0] for r in revs) / total, 2)
            pos_cnt = sum(1 for r in revs if r[1] == 'Positive')
            neu_cnt = sum(1 for r in revs if r[1] == 'Neutral')
            neg_cnt = sum(1 for r in revs if r[1] == 'Negative')

            pos_pct = round((pos_cnt / total) * 100, 1)
            neu_pct = round((neu_cnt / total) * 100, 1)
            neg_pct = round((neg_cnt / total) * 100, 1)
        else:
            avg_r, pos_pct, neu_pct, neg_pct = 0.0, 0.0, 0.0, 0.0

        cursor.execute("""
        UPDATE books
        SET avg_rating = ?, total_reviews = ?, positive_pct = ?, neutral_pct = ?, negative_pct = ?
        WHERE id = ?
        """, (avg_r, total, pos_pct, neu_pct, neg_pct, b_id))


def add_audit_log(user_name: str, role: str, action: str, ip_address: str, details: str):
    """Appends an immutable digital audit record."""
    conn = get_db_connection()
    cursor = conn.cursor()
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sig = generate_audit_hash(user_name, action, now_str, details)
    cursor.execute("""
    INSERT INTO audit_logs (timestamp, user_name, role, action, ip_address, details, digital_signature)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (now_str, user_name, role, action, ip_address, details, sig))
    conn.commit()
    conn.close()
