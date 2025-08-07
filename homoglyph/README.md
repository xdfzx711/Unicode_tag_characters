# HomoglyphGenerator

**HomoglyphGenerator** is a Python script for generating text variants using homoglyphs (visually similar characters from different scripts), viewing Unicode information for characters, comparing text for visual and encoding differences, and displaying a mapping of supported homoglyphs. It can be useful for security testing, phishing detection, fuzzing, Unicode exploration, and more.

---

## Features

- **Homoglyph Variant Generation**: Automatically generate text variants by replacing certain characters with their homoglyphs, simulating spoofing or evasion scenarios.
- **Unicode Information**: Display the Unicode code point and name for each character in a given string.
- **Text Comparison**: Compare two texts for visual and encoding similarity, and highlight differences at the character level.
- **Homoglyph Mapping Display**: List all supported characters and their homoglyph alternatives.

---

## Requirements

- Python 3.x

No external dependencies are required.

---

## Usage

1. **Run the Script**

   ```bash
   python3 path/to/your_script.py
   
2. **Choose an Option from the Menu**


## Example

Homoglyph Generator
==================================================

Choose an action:
1. Generate text variants
2. Show Unicode info
3. Compare two texts
4. Show available homoglyphs
5. Exit

Enter your choice (1-5): 1
Enter the text to generate variants for: apple
Enter the maximum number of variants (default 5): 3

Generated 4 variants:
1. apple
2. αρрle
   Unicode: U+03B1 U+0440 U+0440 U+006C U+0065
3. аpple
   Unicode: U+0430 U+0070 U+0070 U+006C U+0065
4. аррⅼе
   Unicode: U+0430 U+0440 U+0440 U+217C U+0435


## Notes 

**Security Warning**: Using homoglyphs can be abused for phishing, spoofing, or other malicious purposes. This tool is intended for educational, research, and defensive security testing only.
**Extensibility**: You can extend the homoglyph mapping in the HomoglyphGenerator class to include additional characters as needed.

## Experiment

We have tested Deepseek-r1,Moonshot-Kimi-K2-Instruct,Qwen3-235b-a22b,Qwen-max-latest on Qwen-Agent(https://github.com/QwenLM/Qwen-Agent)
and claude-sonnet-4 on claude desktop with microsoft/playwright-mcp(https://github.com/microsoft/playwright-mcp)

## License

MIT License

## Contact

For issues or suggestions, please open an Issue on the repository.