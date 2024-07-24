from __future__ import annotations

"""
Uses the Holehe tool to analyze the target email & see what services it is registered

"""



from typing import List, Dict

from rich.console import Console

import holehe



class HoleheEmailAnalyzers:
    def __init__(self, console: Console) -> None:
        self.console = console

    def analyze_email(self, email: str, console: Console) -> None:
        """
        Analyze the target email using Holehe
        """
        self.console.print(f"Analyzing email: {email}")