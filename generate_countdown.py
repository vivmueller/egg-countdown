#!/usr/bin/env python3
"""Generates a countdown SVG for the event on June 4, 2026 at 14:00 CEST (UTC+2)."""

from datetime import datetime, timezone, timedelta

TARGET = datetime(2026, 6, 4, 12, 0, 0, tzinfo=timezone.utc)  # 14:00 CEST = 12:00 UTC
now = datetime.now(timezone.utc)
diff = TARGET - now

W, H = 520, 110

def block(x, value, label):
    val = str(value).zfill(2)
    return f"""
    <text x="{x}" y="72" font-family="Georgia, serif" font-size="42" font-weight="bold"
          fill="#f0e6d3" text-anchor="middle" letter-spacing="-1">{val}</text>
    <text x="{x}" y="90" font-family="Georgia, serif" font-size="9"
          fill="#c8a96e" text-anchor="middle" letter-spacing="2" opacity="0.75">{label}</text>"""

if diff.total_seconds() <= 0:
    countdown_svg = f"""
    <text x="{W//2}" y="62" font-family="Georgia, serif" font-size="26"
          fill="#f0e6d3" text-anchor="middle" letter-spacing="1">
      The event has started!
    </text>"""
else:
    total_seconds = int(diff.total_seconds())
    days    = total_seconds // 86400
    hours   = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    countdown_svg = f"""
    {block(60,  days,    "DAYS")}
    <text x="178" y="68" font-family="Georgia,serif" font-size="36" fill="#c8a96e">:</text>
    {block(205, hours,   "HOURS")}
    <text x="323" y="68" font-family="Georgia,serif" font-size="36" fill="#c8a96e">:</text>
    {block(350, minutes, "MIN")}
    <text x="468" y="68" font-family="Georgia,serif" font-size="36" fill="#c8a96e">:</text>
    {block(495, seconds, "SEC")}"""

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#1a1008"/>
      <stop offset="100%" stop-color="#2e1f05"/>
    </linearGradient>
  </defs>

  <rect width="{W}" height="{H}" rx="10" ry="10" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" rx="10" ry="10"
        fill="none" stroke="#c8a96e" stroke-width="1.5" opacity="0.6"/>

  <text x="{W//2}" y="22" font-family="Georgia, serif" font-size="12"
        fill="#c8a96e" text-anchor="middle" letter-spacing="3" opacity="0.85">
    COUNTDOWN TO EVENT · 4 JUNE 2026 · 14:00
  </text>
  <line x1="20" y1="28" x2="{W-20}" y2="28" stroke="#c8a96e" stroke-width="0.5" opacity="0.4"/>

  {countdown_svg}
</svg>"""

with open("countdown.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("SVG written.")
