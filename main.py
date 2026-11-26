import os

# Roast the Smart Fridge: one line, best laugh wins.
# The roast: the fridge push-notifies you about your own midnight snacking.
ENTRY = "My smart fridge sent me a push notification at 3 a.m.: 'You have opened me 14 times today. I am not a therapist. Please go to bed.'"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# Write exactly one line, no trailing newline.
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
