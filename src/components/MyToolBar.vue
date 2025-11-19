<script setup>
import MyButton from './MyButton.vue';

</script>


<template>

    <div class="tool-bar-menu">
        <div class="tools flex">
            <i class="fa-regular fa-star fa-lg text-secondary"></i>
            <div class="border-right">
                <i class="fa-solid fa-up-down-left-right fa-lg text-secondary"></i>
                <i class="fa-regular fa-clone fa-lg text-secondary"></i>
                <i class="pad-icon fa-regular fa-clone fa-lg text-secondary"></i>
            </div>
            <div class="border-left border-right">
                <i class="fa-solid fa-file-arrow-down fa-lg text-secondary"></i>
                <i class="pad-icon fa-solid fa-print fa-lg text-secondary"></i>
            </div>

            <i class=" border-left fa-solid fa-trash fa-lg text-secondary"></i>
        </div>
        <div class="share flex">
            <div class="share-stuff flex">
                <i class="fa-solid fa-users fa-lg text-primary"></i>
                <p class="users-shared"><span class="numbUsers">2</span> people</p>

            </div>
            <MyButton bg="var(--color-primary)" color="white" width="fit-content">
                <i class="fa fa-user"></i> <span class="share">Share</span>
            </MyButton>
        </div>
    </div>

    <div class="tool-bar-format flex">
        <div class="text-format border-right">
            <i class="fa-solid fa-text-height text-secondary"></i>
            <i class="fa-solid fa-bold text-secondary"></i>
            <i class="fa-solid fa-italic text-secondary"></i>
            <i class="fa-solid fa-strikethrough text-secondary"></i>
            <i class="fa-solid fa-underline text-secondary"></i>
        </div>
        <div class="border-right border-left list-format">
            <i class="fa-solid fa-list-ol text-secondary"></i>
            <i class="fa-solid fa-list-ul text-secondary"></i>
        </div>
        <div class="border-right border-left paragraph-format">
            <i class="fa-solid fa-align-justify text-secondary"></i>
        </div>
        <div class="border-left border-right extra-tools-format">
            <i class="fa-solid fa-list-check text-secondary"></i>
            <i class="fa-solid fa-terminal text-secondary"></i>
            <i class="fa-solid fa-quote-left text-secondary"></i>
            <i class="fa-solid fa-minus text-secondary"></i>
            <i class="bi bi-table text-secondary"></i>
        </div>
        <div class="border-left border-right text-format-decoration">
            <i class="fa-solid fa-highlighter text-secondary"></i>
            <i class="fa-solid fa-font text-secondary"></i>
        </div>
        <div class=" border-left border-right instert-images">
            <i class="fa-solid fa-image text-secondary"></i>
        </div>
        <div class="border-left undo-redo">
            <i class="fa-solid fa-rotate-left text-secondary"></i>
            <i class="fa-solid fa-rotate-right text-secondary"></i>
        </div>
    </div>


</template>


<style scoped>


.tool-bar-menu,
.tool-bar-format {
    border-bottom: var(--border);
    flex-shrink: 0;
    /* Evita que se compriman */
}


.tool-bar-menu {
    padding: 0.625rem 1.5625rem;
    display: grid;
    grid-template-columns: auto 16.25rem;
}

.tools i,
.tool-bar-format i {
    margin-right: 1.25rem;
    cursor: pointer;
}

.tools .fa-star {
    padding-right: 3.125rem;
}

.border-right {
    padding: 0.3125rem 0.625rem 0.3125rem 0px;
    border-right: var(--border);
}

.border-left {
    padding: 0.3125rem 0px 0.3125rem 1rem;
}

.share {
    justify-content: space-between;
}

.share .btn {
    background-color: var(--color-primary);
    color: white;
}

.share-stuff {
    font-size: 1.0625rem;
}

.share-stuff p {
    margin-left: 0.625rem;
    color: var(--color-accent);
    font-weight: 600;
}

.tool-bar-format {
    background-color: var(--color-bg-light);
    padding: 0.625rem 1.5625rem;
}




</style>