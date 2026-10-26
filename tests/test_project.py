"""Offline structural and renderer smoke tests; no real or invented people."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile
from docx import Document

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class ProjectTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'templates/evidence_template.json').read_text(encoding='utf-8'))

    def test_entrypoint(self):
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(skill.startswith('---\nname: sl-mapping\n'))
        self.assertIn('description:', skill.split('---')[1])
        for name in ('references/research_protocol.md', 'references/network_and_communication.md', 'templates/report_outline.md'):
            self.assertTrue((ROOT / name).is_file())

    def test_empty_template_word(self):
        with tempfile.TemporaryDirectory() as temp:
            path = load('build_report').render(self.data, temp)
            doc = Document(path)
            text = '\n'.join(p.text for p in doc.paragraphs)
            self.assertIn('医生公开学术信息简报', text)
            self.assertIn('0/5', text)
            self.assertIn('未绘制网络图', text)

    def test_unknown_source_rejected(self):
        self.data['basic'][0]['sources'] = ['MISSING']
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'Unknown source'):
                load('build_report').render(self.data, temp)

    def test_unverified_source_rejected(self):
        self.data['basic'][0]['sources'] = ['S1']
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'Unverified'):
                load('build_report').render(self.data, temp)

    def test_duplicate_sources_rejected(self):
        self.data['sources'].append(copy.deepcopy(self.data['sources'][0]))
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, 'Duplicate source'):
                load('build_report').render(self.data, temp)

    def test_package_allowlist(self):
        with tempfile.TemporaryDirectory() as temp:
            path = load('package_skill').package(Path(temp) / 'skill.zip')
            with ZipFile(path) as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn('SKILL.md', archive.namelist())
                self.assertNotIn('.github/workflows/ci.yml', archive.namelist())
                self.assertFalse(any(n.endswith('.docx') for n in archive.namelist()))

if __name__ == '__main__':
    unittest.main()
