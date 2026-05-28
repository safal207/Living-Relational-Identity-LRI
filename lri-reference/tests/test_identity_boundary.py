"""
Identity boundary enforcement tests.

Validates that LRI protocol schemas, reference implementation,
and documentation maintain the boundary between human-boundary
protocol and identity platform.
"""

from pathlib import Path

import pytest
import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
FIXTURES_DIR = PROJECT_ROOT / "docs" / "fixtures" / "identity_boundary"
PROTOCOL_DIR = PROJECT_ROOT / "protocol" / "lri"
REFERENCE_DIR = PROJECT_ROOT / "lri-reference"
DOCS_DIR = PROJECT_ROOT / "docs"


def _load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _load_fixture(name):
    return _load_yaml(FIXTURES_DIR / name)


@pytest.fixture(scope="module")
def prohibited_patterns():
    return _load_fixture("prohibited_patterns.yaml")


@pytest.fixture(scope="module")
def boundary_rules():
    return _load_fixture("identity_boundary_rules.yaml")


class TestProhibitedSchemaFields:
    """Protocol schemas must not contain prohibited identity-platform fields."""

    def _collect_schema_files(self):
        schema_files = []
        schema_dir = PROTOCOL_DIR / "schema"
        if schema_dir.exists():
            for f in schema_dir.rglob("*.yaml"):
                schema_files.append(f)
        return schema_files

    def _collect_field_names(self, schema_data):
        """Recursively extract all field names from a schema."""
        fields = set()
        if isinstance(schema_data, dict):
            for key in schema_data:
                fields.add(key)
                fields.update(self._collect_field_names(schema_data[key]))
        elif isinstance(schema_data, list):
            for item in schema_data:
                fields.update(self._collect_field_names(item))
        return fields

    def test_no_prohibited_fields_in_schemas(self, prohibited_patterns):
        prohibited = set(prohibited_patterns["prohibited_schema_fields"])
        schema_files = self._collect_schema_files()
        violations = []

        for path in schema_files:
            data = _load_yaml(path)
            fields = self._collect_field_names(data)
            found = fields & prohibited
            if found:
                violations.append((str(path.relative_to(PROJECT_ROOT)), found))

        assert not violations, f"Prohibited schema fields found: {violations}"

    def test_no_prohibited_endpoints_in_reference(self, prohibited_patterns):
        prohibited = set(prohibited_patterns["prohibited_api_endpoints"])
        main_path = REFERENCE_DIR / "main.py"
        if not main_path.exists():
            pytest.skip("main.py not found")

        content = main_path.read_text(encoding="utf-8")
        violations = []
        for endpoint in prohibited:
            if endpoint in content:
                violations.append(endpoint)

        assert not violations, f"Prohibited API endpoints in main.py: {violations}"


class TestProhibitedFramingInDocs:
    """Documentation must not contain prohibited framing."""

    def _collect_doc_files(self):
        doc_files = []
        for ext in ("*.md", "*.rst", "*.txt"):
            for f in DOCS_DIR.rglob(ext):
                doc_files.append(f)
        return doc_files

    def test_no_prohibited_phrases_in_docs(self, prohibited_patterns):
        prohibited = prohibited_patterns["prohibited_phrases"]
        doc_files = self._collect_doc_files()

        # Files where prohibited phrases appear in negative/scope-boundary context
        # (what LRI is NOT) — these are allowed
        allowlist = {
            "NON_CLAIMS.md",
            "GLOSSARY.md",
            "REVIEWER_PATH.md",
            "PORTFOLIO_RELATIONSHIP.md",
            "GRANT_EVIDENCE.md",
            "identity_freezing_examples.md",
            "silent_authorship.md",
            "lri_vs_privacy_consent.md",
            "consent_drift_scenario.md",
            "identity_governance_threat_model.md",
        }

        violations = []

        for path in doc_files:
            if path.name in allowlist:
                continue
            content = path.read_text(encoding="utf-8").lower()
            for phrase in prohibited:
                if phrase.lower() in content:
                    violations.append((str(path.relative_to(PROJECT_ROOT)), phrase))

        assert not violations, f"Prohibited phrases in docs (outside allowlist): {violations}"

    def test_no_prohibited_terms_in_code_comments(self, prohibited_patterns):
        prohibited = set(prohibited_patterns["prohibited_terms"])
        code_files = list(REFERENCE_DIR.rglob("*.py"))
        violations = []

        for path in code_files:
            content = path.read_text(encoding="utf-8")
            for line_num, line in enumerate(content.splitlines(), 1):
                stripped = line.strip()
                if stripped.startswith("#"):
                    comment_text = stripped.lstrip("#").strip().lower()
                    for term in prohibited:
                        if term.replace("_", " ") in comment_text:
                            violations.append((str(path.relative_to(PROJECT_ROOT)), line_num, term))

        assert not violations, f"Prohibited terms in code comments: {violations}"


class TestBoundaryRulesEnforced:
    """Identity boundary rules from fixtures must be structurally enforced."""

    def test_non_claims_doc_exists(self):
        non_claims = DOCS_DIR / "NON_CLAIMS.md"
        assert non_claims.exists(), "docs/NON_CLAIMS.md must exist"

    def test_non_claims_contains_prohibited_list(self):
        non_claims = DOCS_DIR / "NON_CLAIMS.md"
        content = non_claims.read_text(encoding="utf-8")

        required_entries = [
            "identity classification",
            "personality scoring",
            "profiling",
            "diagnosis",
            "therapy",
            "mental-health assessment",
            "social credit",
            "risk scoring",
            "automated decisioning",
            "true self",
        ]

        for entry in required_entries:
            assert entry in content, f"NON_CLAIMS.md must mention '{entry}'"

    def test_required_disclaimers_present(self, boundary_rules):
        for disclaimer in boundary_rules["required_disclaimers"]:
            location = PROJECT_ROOT / disclaimer["location"]
            assert location.exists(), f"Disclaimer location {disclaimer['location']} missing"

            content = location.read_text(encoding="utf-8").lower()
            assert disclaimer["text"].lower() in content, (
                f"Required disclaimer missing from {disclaimer['location']}: " f"{disclaimer['text']}"
            )

    def test_allowed_capabilities_are_protective(self, boundary_rules):
        """All allowed capabilities must be protective, not classificatory."""
        protective_keywords = [
            "track",
            "detect",
            "record",
            "enforce",
            "simulate",
            "generate",
            "write",
        ]

        for cap in boundary_rules["allowed_capabilities"]:
            assert any(kw in cap for kw in protective_keywords), (
                f"Capability '{cap}' does not appear protective. "
                f"Allowed capabilities must be protective, not classificatory."
            )

    def test_prohibited_behaviors_not_in_reference(self, boundary_rules):
        prohibited = boundary_rules["prohibited_behaviors"]
        py_files = list(REFERENCE_DIR.rglob("*.py"))
        violations = []

        for path in py_files:
            content = path.read_text(encoding="utf-8").lower()
            for behavior in prohibited:
                snake_case = behavior.replace("_", " ")
                if snake_case in content:
                    violations.append((str(path.relative_to(PROJECT_ROOT)), behavior))

        assert not violations, f"Prohibited behaviors referenced in reference implementation: {violations}"


class TestIdentityAuthorityPreserved:
    """Identity authority must remain with the subject, not the system."""

    def test_subject_endpoints_exist(self):
        main_path = REFERENCE_DIR / "main.py"
        content = main_path.read_text(encoding="utf-8")

        assert "/subject" in content, "Subject endpoints must exist for identity authority"

    def test_authority_check_exists(self):
        main_path = REFERENCE_DIR / "main.py"
        content = main_path.read_text(encoding="utf-8")

        assert "authority" in content.lower(), "Authority check must exist for identity authority"

    def test_observer_is_read_only(self):
        """Observer must not have write access to identity state."""
        main_path = REFERENCE_DIR / "main.py"
        content = main_path.read_text(encoding="utf-8")

        observer_routes = [
            line for line in content.splitlines() if "/observer" in line and ("@app" in line or "def " in line)
        ]

        for route in observer_routes:
            assert "post" not in route.lower(), f"Observer route must not be POST (write): {route}"
