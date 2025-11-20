# uvicorn main:app --reload  # noqa: INP001


from typing import List

from data import note_dict, task_dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Nota

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:3000"] si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/notes")
async def get_notes() -> dict[int, Nota]:
    return note_dict


@app.get("/notes/{note_id}")
async def get_note(note_id: int) -> Nota | None:
    return note_dict.get(note_id)


@app.get("/notes/{note_id}/tasks")
def get_tasks_for_note(note_id: int) -> List[dict]:
    note = note_dict.get(note_id)
    if not note:
        return []

    result = []
    for taskid in note.tasks_id:
        if taskid in task_dict:
            task = task_dict[taskid]
            task_data = task.model_dump()  # para que sea un dict
            task_data['id'] = taskid  # Usar la key del diccionario como id
            result.append(task_data)

    return result
