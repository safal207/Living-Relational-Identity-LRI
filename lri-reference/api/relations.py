relations = []

def link_subject(subject_id1, subject_id2, relation_type):
    relations.append({"from": subject_id1, "to": subject_id2, "type": relation_type})
    return {"status": "linked"}

def unlink_subject(subject_id1, subject_id2, relation_type):
    global relations
    relations = [r for r in relations if not (r["from"]==subject_id1 and r["to"]==subject_id2 and r["type"]==relation_type)]
    return {"status": "unlinked"}

def list_relations(subject_id):
    return [r for r in relations if r["from"]==subject_id or r["to"]==subject_id]
