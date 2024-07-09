import sys
from time import sleep

def lyrics():
  # Tyler, The Creator - I Thought You Wanted To Dance
  lines = [
    ("What makes you think", 0.08),
    ("I'm not in love?", 0.10),
    ("How could you know", 0.10),
    ("What's best for us?", 0.10),
    ("Why am I here", 0.10),
    ("Standing alone?", 0.10),
    ("Cause I thought,", 0.07),
    ("I thought you wanted to dance", 0.055),
    ("yeah", 0.05),
  ]

  delays = [1.8, 1.5, 1.9, 1.8, 2.15, 1.75, 1.7, 1.5, 1.0]

  # print each line with a delay
  # when line is done, print a new line with a delay from the delays list
  for line, delay in lines:
    # Get each character in the line
    for char in line:
      print(char, end='', flush=True)
      sleep(delay)
    # Print a new line
    print()
    # Sleep for the delay
    sleep(delays.pop(0))

if __name__ == "__main__":
  lyrics()
  sys.exit(0)