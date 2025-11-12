<script setup>



</script>
<template>
    <aside id="first-sidebar">
        <nav>
            <ul class="flex">
                <li><a href="#" aria-label="Icona"><i class="fa-solid fa-link fa-xl text-primary"></i></a></li>
                <li><a href="#" aria-label="Recordatoris"><i class="bi bi-grid-1x2-fill text-primary fa-xl"></i></a>
                </li>
                <li><a href="#" aria-label="Fitxers"><i class="fa-solid fa-folder-open fa-xl text-primary"></i></a>
                </li>
                <li><a href="#" aria-label="Correu"><i class="fa-solid fa-envelope fa-xl text-primary"></i></a></li>
                <li><a href="#" aria-label="Usuari"><i class="fa-solid fa-circle-user fa-xl text-primary"></i></a>
                </li>
                <li><a href="#" class="active-first-sidebar" aria-label="Notes"><i
                            class="fa-solid fa-file fa-xl text-primary"></i></a></li>
                <li><a href="#" aria-label="Tasques"><i class="fa-brands fa-trello fa-xl text-primary"></i></a></li>
                <li><a href="#" aria-label="Calendari"><i class="fa-solid fa-calendar-days fa-xl text-primary"></i></a>
                </li>
                <li><a href="#" aria-label="Meetings"><i class="fa-solid fa-video fa-xl text-primary"></i></a></li>
            </ul>
        </nav>
    </aside>
</template>
<style scoped>
#first-sidebar {
    grid-area: first-sidebar;
}

nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

nav a {
    font-size: 1rem;
}

nav ul {
    padding-top: 1.25rem;
    flex-direction: column;
    grid-area: first-sidebar;
}

nav li {
    margin-bottom: 1.75rem;
}


.fa-link {
    margin-bottom: 2rem;
}

.active-first-sidebar {
    border: 3px solid var(--color-primary);
    padding: 1.250rem 0.3125rem;
    border-radius: var(--btn-radius);
    background-color: var(--color-bg-light);
    display: flex;
    align-items: center;
}

.fa-xl {
    font-size: 1.5rem;
    line-height: .04167em;
    vertical-align: -5px;
}
</style>