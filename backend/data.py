
from models import Nota, Tag, Task

task_dict: dict[int, Task] = {
    1: Task(
        titol="Task example",
        tipus=Tag.PROJECT,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
    2: Task(
        titol="Dummy 101",
        tipus=Tag.PERSONAL,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
    3: Task(
        titol="Test 123",
        tipus=Tag.OTHER,
        deadline=None,
        reminder=None,
        is_done=False,
    ),
    4: Task(
        titol="Test 456",
        tipus=Tag.OTHER,
        deadline=None,
        reminder=None,
        is_done=False,
    ),
    5: Task(
        titol="Task example",
        tipus=Tag.PROJECT,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
        6: Task(
        titol="Dummy 101",
        tipus=Tag.PERSONAL,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
        7: Task(
        titol="Test 123",
        tipus=Tag.OTHER,
        deadline=None,
        reminder=None,
        is_done=False,
    ),
        8: Task(
        titol="Task example",
        tipus=Tag.PROJECT,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
        9: Task(
        titol="Dummy 101",
        tipus=Tag.PERSONAL,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
        10: Task(
        titol="Test 123",
        tipus=Tag.OTHER,
        deadline=None,
        reminder=None,
        is_done=False,
    ),
       11: Task(
        titol="Task example",
        tipus=Tag.PROJECT,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
    12: Task(
        titol="Dummy 101",
        tipus=Tag.PERSONAL,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),
    13: Task(
        titol="Test 123",
        tipus=Tag.OTHER,
        deadline=None,
        reminder=None,
        is_done=False,
    ),
        14: Task(
        titol="Test 456",
        tipus=Tag.OTHER,
        deadline=None,
        reminder=None,
        is_done=False,
    ),
        15: Task(
        titol="Task example",
        tipus=Tag.PROJECT,
        deadline="2025-12-20T00:00:00",  # type: ignore  # noqa: PGH003
        reminder="2025-12-20T09:00:00",  # type: ignore  # noqa: PGH003
        is_done=False,
    ),

}


note_dict: dict[int, Nota] = {
    1: Nota(
        titol="Brainstorming Session Highlights",
        contingut="Capture your team's best ideas here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget augue ante. Integer hendrerit aliquam arcu at laoreet. Duis ac volutpat mi, porta laoreet lorem. Mauris et maximus nibh.",  # noqa: E501
        link="https://contoso.sharepoint.com/sites/Admins.... exemple link created",
        tasks_id=[1, 2, 3],
        num_links=3,
        tags=[Tag.PERSONAL, Tag.PROJECT],
        time="03:20 PM",
        notebook="NoteBook-01",
        has_alarm=True,
        is_shared=False,
        images=["livingroom.jpg"],
        last_edit="Dec 13, 2021",
    ),
    2: Nota(
        titol="Helping a local business",
        contingut="Amet minim mollit non deserunt illemco est Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget augue ante. Integer hendrerit aliquam arcu at laoreet. Duis ac volutpat mi, porta laoreet lorem. Mauris et maximus nibh.",  # noqa: E501
        link=None,
        tasks_id=[5, 6, 7],
        num_links=3,
        tags=[Tag.PROJECT, Tag.OTHER],
        time="11:24 AM",
        notebook="NoteBook-01",
        has_alarm=False,
        is_shared=False,
        images=["livingroom2.jpg"],
        last_edit="Dec 13, 2021",
    ),
    3: Nota(
        titol="Weekly Team Update",
        contingut="Document this week's accomplishments, challenges Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget augue ante. Integer hendrerit aliquam arcu at laoreet. Duis ac volutpat mi, porta laoreet lorem. Mauris et maximus nibh.",  # noqa: E501
        link="https://www.google.com/",
        tasks_id=[],
        num_links=0,
        tags=None,
        time="09:02 AM",
        notebook="NoteBook-01",
        has_alarm=False,
        is_shared=False,
        images=None,
        last_edit="Dec 13, 2021",
    ),
    4: Nota(
        titol="Streamline Your Workflow with a good environment",
        contingut="In today's fast-paced environment, staying organized is the key to succedd. Use this space to jot down important ideas, action plans, or meeting notes. With integrated task mangament, you can turn your thoughts into actionable steps with deadlines and labels. Keep your team aligned by sharing updates and progress in real-time. Stay ahead prioritizing what matters the most.",  # noqa: E501
        link="https://www.mozilla.org/es-ES/",
        tasks_id=[8, 9, 10],
        num_links=3,
        tags=[Tag.PERSONAL, Tag.OTHER],
        time="10:20 AM",
        notebook="NoteBook-01",
        has_alarm=True,
        is_shared=True,
        images=["livingroom.jpg"],
        last_edit="Dec 13, 2021",
    ),
    5: Nota(
        titol="Client Meeting Notes",
        contingut="Keep a record of all client interactions in one place. \n Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget augue ante. Integer hendrerit aliquam arcu at laoreet. Duis ac volutpat mi, porta laoreet lorem. Mauris et maximus nibh.",  # noqa: E501
        link=None,
        tasks_id=[11, 12],
        num_links=3,
        tags=[Tag.PERSONAL, Tag.OTHER],
        time="04:53 AM",
        notebook="NoteBook-01",
        has_alarm=False,
        is_shared=False,
        images=None,
        last_edit="Feb 23, 2022",
    ),
    6: Nota(
        titol="Project Kickoff Plan",
        contingut="Lay out the initial roadmap for your ner project. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget augue ante. Integer hendrerit aliquam arcu at laoreet. Duis ac volutpat mi, porta laoreet lorem. Mauris et maximus nibh.",  # noqa: E501
        link="https://www.mozilla.org/es-ES/",
        tasks_id=[13, 14, 15],
        num_links=0,
        tags=[Tag.PROJECT, Tag.OTHER],
        time="10:43 AM",
        notebook="NoteBook-01",
        has_alarm=False,
        is_shared=False,
        images=None,
        last_edit="Dec 13, 2021",
    ),
    7: Nota(
        titol="Ejemplo tasks",
        contingut="Ejemplo !!!!!!!!!!!!!!!!!!!. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget augue ante. Integer hendrerit aliquam arcu at laoreet. Duis ac volutpat mi, porta laoreet lorem. Mauris et maximus nibh.",  # noqa: E501
        link=None,
        tasks_id=[4],
        num_links=0,
        tags=[Tag.PROJECT],
        time="10:43 AM",
        notebook="NoteBook-01",
        has_alarm=False,
        is_shared=False,
        images=["livingroom2.jpg", "livingroom.jpg"],
        last_edit="Dec 13, 2021",
    ),
}
