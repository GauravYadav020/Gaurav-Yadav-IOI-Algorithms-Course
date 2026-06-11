# Module 7 Lesson 3: After-Class Project
# Project Name: RegEx Text Pipeline Engine Markdown to HTML Converter

import re

class MarkdownCompilationEngine:
    def render_html_blocks(self, raw_markdown_text):
        # Convert header structural markers securely
        compiled_step = re.sub(r'^##\s(.*)$', r'<h2>\1</h2>', raw_markdown_text, flags=re.MULTILINE)
        compiled_step = re.sub(r'^#\s(.*)$', r'<h1>\1</h1>', compiled_step, flags=re.MULTILINE)
        # Convert bold markers inline text strings
        compiled_final = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', compiled_step)
        return compiled_final

if __name__ == "__main__":
    compiler = MarkdownCompilationEngine()
    md = "# IOI Syllabus\n## Section 1\n**Dynamic Programming** rules are active."
    print(compiler.render_html_blocks(md))