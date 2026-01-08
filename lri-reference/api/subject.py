subjects = {}

def create_subject(subject_id, data):
    if subject_id in subjects:
        return {"error": "Subject already exists"}
    subjects[subject_id] = data
    return {"status": "created", "subject": subjects[subject_id]}

def get_subject(subject_id):
    return subjects.get(subject_id, {"error": "Subject not found"})

def update_subject(subject_id, data):
    if subject_id not in subjects:
        return {"error": "Subject not found"}
    subjects[subject_id].update(data)
    return {"status": "updated", "subject": subjects[subject_id]}

def delete_subject(subject_id):
    if subject_id in subjects:
        del subjects[subject_id]
        return {"status": "deleted"}
    return {"error": "Subject not found"}
