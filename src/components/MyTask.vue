<script setup>
import { useNoteStore } from '../stores/NoteStore'

const props = defineProps({
    taskId: {
        type: Number,
        required: true
    },
    noteId: {
        type: Number,
    },
    titol: {
        type: String,
        required: true
    },
    isDone: {
        type: Boolean,
        required: true
    },
    deadline: {
        type: String,
        default: null
    },
    reminder: {
        type: String,
        default: null
    },
    tipus: {
        type: String,
    }
})

const noteStore = useNoteStore()



const toggleTask = async (event) => {
    const newValue = event.target.checked
    // Necesitas pasar el noteId también
    await noteStore.updateTask(noteStore.selectedNoteId, props.taskId, newValue)
}
</script>

<template>
    <div class="task-wrapper ">
        <i class="icono bi bi-grip-vertical"></i>
        <div class="task-nota" :data-task-id="taskId">
            <div class="task-title flex">
                <label class="check" :class="tipus.toLowerCase() + '-check'">
                    <input type="checkbox" :checked="isDone" @change="toggleTask" />
                    <span class="checkmark"></span>
                    {{ titol }}
                </label>

            </div>
            <div class="deadline-info flex">
                <div class="flex">
                    <div class="flex" v-if="deadline"><i class="fa-solid fa-flag-checkered fa-sm text-secondary"></i>
                        <p class="deadline">Deadline <span class="date-deadline">{{ deadline }}</span></p>
                    </div>
                    <div class="flex alarm" v-if="reminder"><i class="fa-solid fa-alarm-clock fa-sm text-secondary"></i>
                        <p class="alarm-day">{{ reminder }}</p>
                    </div>

                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>
.check {
    display: block;
    position: relative;
    padding-left: 2.1875rem;
    margin-bottom: 0.3125rem;
    cursor: pointer;
    font-size: 1.125rem;
    user-select: none;
    color: var(--color-accent);
    font-weight: 600;
}

.check input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    height: 0;
    width: 0;
}

.checkmark {
    position: absolute;
    top: 0;
    left: 0;
    height: 1.375rem;
    width: 1.375rem;
    border-radius: 0.3125rem;
    background-color: var(--color-bg-light);
}

.project-check .checkmark {
    border: 3px solid var(--color-project-lbl);
}

.personal-check .checkmark {
    border: 3px solid var(--color-personal-lbl);
}

.other-check .checkmark {
    border: 3px solid var(--color-primary);
}

.project-check:hover input~.checkmark {
    background-color: var(--bg-project-lbl);
}

.personal-check:hover input~.checkmark {
    background-color: var(--bg-personal-lbl);
}

.other-check:hover input~.checkmark {
    background-color: #0859bc66;
}

.project-check input:checked~.checkmark {
    background-color: var(--color-project-lbl);
}

.personal-check input:checked~.checkmark {
    background-color: var(--color-personal-lbl);
}

.other-check input:checked~.checkmark {
    background-color: var(--color-primary);
}

.checkmark:after {
    content: "";
    position: absolute;
    display: none;
}

.check input:checked~.checkmark:after {
    display: block;
}

.check .checkmark:after {
    left: 0.4375rem;
    top: 0.1875rem;
    width: 0.3125rem;
    height: 0.625rem;
    border: solid white;
    border-width: 0 3px 3px 0;
    transform: rotate(45deg);
}

.deadline-info {
    justify-content: space-between;
    margin-left: 2.1875rem;
}

.deadline-info p {
    margin-left: 0.3125rem;
    font-size: 0.875rem;
}

.tasks-nota {
    margin: 1.875rem 0 6.25rem 0;
}

.tasks-nota .btn {
    background-color: transparent;
    color: #0859bc;
    font-size: 18px;
    padding: 0;
}


.tasks-nota .btn:hover {
    background-color: transparent !important;
    color: #0859bc;
    font-size: 18px;
    padding: 0;
}

.task-title {
    justify-content: space-between;
}

.task-title span {

    font-size: 28px;
    font-weight: bold;
    color: var(--color-accent);
    cursor: pointer;
    transition: color 0.3s;
}

.task-nota {
    border-bottom: var(--border);
    padding: 1rem;
}

.selected .task-nota {
    border: var(--border);
    border-radius: var(--btn-radius);
    background-color: var(--color-bg-light);
}

.task-header {
    display: flex;
    align-items: center;
    gap: 0.625rem;
}

.task-wrapper {
    position: relative;
    cursor: pointer;
}

.task-wrapper .icono {
    position: absolute;
    left: -35px;
    top: 0;
    bottom: 0;
    display: none;
    align-items: center;
    font-size: 24px;
    color: var(--color-secondary);
    cursor: grab;
    pointer-events: none;
}

.task-wrapper.selected .icono {
    display: flex;
}

.edit-tools .fa-solid {
    margin-left: 0.625rem;
}

.alarm {
    border: var(--border);
    padding: 0.3125rem 0.625rem;
    border-radius: 0.9375rem;
    background-color: white;
    margin-left: 1.25rem;
}
</style>