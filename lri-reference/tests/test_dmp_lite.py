from storage.dmp_store import DMPStore
from services.dmp_writer import DMPWriter

def test_dmp_append(tmp_path):
    store = DMPStore(path=tmp_path / "dmp.jsonl")
    writer = DMPWriter(store)

    writer.record("A1", "explore", "move_forward")

    content = (tmp_path / "dmp.jsonl").read_text()
    assert "A1" in content
    assert "explore" in content
