#!/usr/bin/env python3
"""
Generates a countdown SVG for the event starting Thursday 10:00 CEST (UTC+2).
To re-use for next year:
1) Update TARGET below.
2) GitHub -> Settings -> Developer settings -> Personal access tokens -> Fine-grained tokens -> create new token (or regenerate old one)
  Grant access to repository: vivmueller/egg-countdown
  Grant permission:           Actions: Read and write, Content: Read
  Expire date:                End of egg
  Copy the new token.
3) Update cron-job.org > egg-countdown > Details > Edit Cronjob > Advanced > Headers >  Key: Authorization, Value: token [insert token after 'token '] (it should look like: "token githubxxxx")
  Save, test run.
4) Embed in Wiki: {{ https://raw.githubusercontent.com/vivmueller/egg-countdown/main/countdown.svg }}

"""

from datetime import datetime, timezone

TARGET = datetime(2027, 5, 27, 8, 0, 0, tzinfo=timezone.utc)  # 10:00 CEST = 08:00 UTC
now = datetime.now(timezone.utc)
diff = TARGET - now

W, H = 400, 90

def block(x, value, label):
    val = str(value).zfill(2)
    return f"""
    <text x="{x}" y="60" font-family="Arial, Helvetica, sans-serif" font-size="24" font-weight="bold"
          fill="#000000" text-anchor="middle">{val}</text>
    <text x="{x}" y="74" font-family="Arial, Helvetica, sans-serif" font-size="11"
          fill="#333333" text-anchor="middle">{label}</text>"""

if diff.total_seconds() <= 0:
    countdown_svg = f"""
    <text x="{W//2}" y="70" font-family="Arial, Helvetica, sans-serif" font-size="22"
          fill="#000000" text-anchor="middle">The event has started!</text>"""
else:
    total_seconds = int(diff.total_seconds())
    days    = total_seconds // 86400
    hours   = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60

    countdown_svg = f"""
    {block(60,  days,    "DAYS")}
    <text x="130" y="60" font-family="Arial, sans-serif" font-size="32" fill="#555555">:</text>
    {block(200, hours,   "HOURS")}
    <text x="270" y="60" font-family="Arial, sans-serif" font-size="32" fill="#555555">:</text>
    {block(340, minutes, "MIN")}"""

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <!-- No background rect = transparent -->
  
<text x="{W//2}" y="25" font-family="Arial, Helvetica, sans-serif" font-size="16"
        fill="#555555" text-anchor="middle" letter-spacing="1">
    Countdown:
  </text>

  
  {countdown_svg}
</svg>"""

with open("countdown.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG written.")
