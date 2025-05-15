import re

# Read the raw transcript file
with open("convo.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Remove timestamps like [00:12:45], (12:45), or variations
cleaned_text = re.sub(r'\[?\(?\d{1,2}:\d{2}(?::\d{2})?\)?\]?', '', raw_text)

# Regex pattern to match speaker labels and their statements
# Speaker name: 1-30 chars, letters, digits, spaces, hyphens, dots (to cover initials)
pattern = re.compile(
    r'([A-Za-z0-9 .\-]{1,30}):\s*(.*?)(?=(?:[A-Za-z0-9 .\-]{1,30}:)|$)', 
    re.DOTALL
)

# Find all speaker-statement pairs
matches = pattern.findall(cleaned_text)

formatted = ""
for speaker, statement in matches:
    speaker = speaker.strip().upper()
    statement = statement.strip()
    formatted += f"{speaker}:\n{statement}\n\n"

# Save formatted transcript
with open("formatted_transcript.txt", "w", encoding="utf-8") as f:
    f.write(formatted)

print("Formatted transcript saved as formatted_transcript.txt")