with open('generate_mini_project_reports.py', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all Rupee symbols
text = text.replace('\u20b9', 'Rs. ')
text = text.replace('■', 'Rs. ')

# Align ITPM index
text = text.replace('(5, "Results", 14),\n        (6, "Conclusion", 16),\n        (7, "References", 17)',
                    '(5, "Results", 13),\n        (6, "Conclusion", 14),\n        (7, "References", 14)')

# Align ES index
text = text.replace('(2, "Literature Survey", 8),\n        (3, "System Design & Architecture", 9),\n        (4, "Implementation", 12),\n        (5, "Results", 14),\n        (6, "Conclusion", 16),\n        (7, "References", 17)',
                    '(2, "Literature Survey", 7),\n        (3, "System Design & Architecture", 8),\n        (4, "Implementation", 10),\n        (5, "Results", 11),\n        (6, "Conclusion", 13),\n        (7, "References", 13)')

# Align ASTMA index
text = text.replace('(4, "Implementation", 11),\n        (5, "Results", 13),\n        (6, "Conclusion", 15),\n        (7, "References", 16)',
                    '(4, "Implementation", 10),\n        (5, "Results", 11),\n        (6, "Conclusion", 12),\n        (7, "References", 12)')

with open('generate_mini_project_reports.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("generate_mini_project_reports.py patched successfully!")
