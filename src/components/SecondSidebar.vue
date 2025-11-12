<script setup>
import MyButton from './MyButton.vue';
import UploadButton from './UploadButton.vue';
</script>

<template>

    <aside id="second-sidebar">
        <button class="closebtn"> <i class="fa-solid fa-xmark x-icon"></i></button>
        <div class="sidebar-upload">
        <UploadButton />
        
        </div>
        <nav>
            <h4 class="sidebar-heading">Quick links</h4>
            <ul class="sidebar-quick-links">
                <li><a href="#"><i class="bi bi-journals"></i> All Notes</a></li>
                <li><a href="#"><i class="bi bi-pin-angle-fill"></i> Pinned</a></li>
                <li><a href="#"><i class="fa fa-solid fa-clipboard-check"></i> Task</a></li>
            </ul>
            <h4 class="sidebar-heading">Notes</h4>
            <ul class="sidebar-notes-links">
                <li><a href="#"><i class="bi bi-stickies-fill"></i> Sticky Notes</a></li>
                <li class="active"><a href="#"><i class="fa fa-solid fa-file"></i>
                        Notes</a></li>
                <li><a href="#"><i class="fa fa-regular fa-star"></i> Starred</a></li>
                <li><a href="#"><i class="fa fa-solid fa-share-from-square"></i> Shared with
                        me</a></li>
                <li><a href="#"><i class="fa fa-solid fa-box-archive"></i> Archive</a></li>
                <li class="link-wrapper"><a href="#"> <i class="icono fa-solid fa-caret-right text-secondary fa-xs">
                        </i><i class="bi bi-journal-bookmark-fill"></i> Notebooks</a></li>
                <li class="link-wrapper label"><a href="#"> <i
                            class=" icono fa-solid fa-caret-right text-secondary  fa-xs"> </i><i
                            class="fa fa-solid fa-tag"></i> Label</a></li>
            </ul>
        </nav>
    </aside>
</template>


<style scoped>
#second-sidebar {
    grid-area: second-sidebar;
    background-color: var(--color-bg-light);
    border: var(--border);
    border-width: 0 1px;
}

.closebtn {
    display: none;
}

.sidebar-upload {
    padding: 1rem;
}


ul {
    font-size: 0.75rem;
    padding: 0;
    margin: 0;
}

li {
    list-style: none;
    padding: 1rem 1.5625rem;
    border-left: 3px solid transparent;
}

a {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    text-decoration: none;
    color: var(--color-accent);
    font-weight: 600;
    font-size: 0.9375rem;
}

li i {
    color: var(--color-secondary);
}

li.active i,
li.active a {
    color: var(--color-primary);
}

li a .fa-caret-right {
    order: -1;
}

h4 {
    text-transform: uppercase;
    font-size: 0.875rem;
    font-weight: 700;
    color: var(--color-secondary);
    margin: 1rem 0 0 1rem;
}
</style>
