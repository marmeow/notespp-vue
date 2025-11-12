<script setup>
import MyButton from './MyButton.vue';
import FilterBar from './FilterBar.vue';


//VIRTUAL SCROLL 
</script>


<template>

    <section id="note-list">

        <div class="new-note flex">
            <h2>Notes</h2>
            <MyButton bg="white" color="var(--color-primary)" border="var(--border)" width="fit-content"><i
                    class="fa fa-plus fa-sm"></i><span class="create"> Create New</span></MyButton>
        </div>


        <div class="notes-info flex">
            <p><span class="num-notes">0</span> Notes</p>
            <FilterBar/>
            
        </div>


        <div class="notes-categories flex">
            <p class="all">All</p>
            <p class="reminder">Reminder</p>
        </div>


    </section>

</template>


<style scoped>
#note-list {
    grid-area: note-list;
    display: flex;
    flex-direction: column;
    min-width: 0;
    max-width: 100%;
    height: 100%;
    color: black;
    background-color: rgba(128, 128, 128, 0.267);
}


.new-note {
    border-bottom: var(--border);
    padding: 1.5625rem;
    display: flex;
    align-items: center;
    gap: 1.25rem;
}

*::-webkit-scrollbar {
    display: none;
}


h2 {
    color: var(--color-accent);
    padding-right: 1.875rem;
    border-right: var(--border);
    margin: 0;
}


.sort-date {
    gap: 0.625rem;
}

.notes-info {
    justify-content: space-around;
    font-weight: 600;
    font-size: 0.9375rem;
    border-bottom: var(--border);
    color: var(--color-secondary);
    padding: 0.625rem;
    flex-wrap: wrap;

}

.num-notes {
    color: var(--color-accent);
}

.num-notes {
    font-weight: bold;
}

.notes-categories {
    justify-content: center;
    align-items: flex-end;
    border-bottom: var(--border);
    font-size: 1rem;
    font-weight: 600;
    color: var(--color-secondary);
    text-align: center;
    padding: 1.25rem 1.25rem 0px 1.25rem;
    cursor: pointer;
}

.all {
    color: var(--color-primary);
    border-bottom: 3px solid var(--color-primary);
    width: 50%;
    padding-bottom: 0.75rem;
    font-weight: bold;
}

.reminder {
    width: 50%;
    padding-bottom: 0.75rem;
    border-bottom: 3px solid transparent;
}


</style>