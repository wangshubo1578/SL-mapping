"""Create an allowlisted Skill archive; never include research outputs."""
import argparse
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "SKILL.md", "README.md", "LICENSE", "requirements.txt",
    "references/research_protocol.md", "references/network_and_communication.md",
    "templates/report_outline.md", "templates/evidence_template.json",
    "scripts/build_report.py", "scripts/README.md",
]

def package(destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        if not (ROOT / name).is_file():
            raise FileNotFoundError(name)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(ROOT / name, name)
    return destination

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="dist/sl-mapping.zip")
    print(package(parser.parse_args().out))
