import re
import os

def remove_emojis(text):
    """Remove all emojis from text"""
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001F900-\U0001F9FF"  # supplemental symbols
        u"\U0001FA70-\U0001FAFF"  # symbols and pictographs extended-a
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

# Files to clean
files_to_clean = [
    'movielens_analysis.html',
    'MovieLens_Analysis_Report.html',
    'MovieLens_Analysis_Report.md',
    'analysis_simple.py',
    'run_analysis.py'
]

for filename in files_to_clean:
    if os.path.exists(filename):
        print(f"Cleaning {filename}...")
        
        # Read file
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove emojis
        clean_content = remove_emojis(content)
        
        # Write back
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        
        print(f"Cleaned {filename}")
    else:
        print(f"File {filename} not found")

print("All files cleaned of emojis")