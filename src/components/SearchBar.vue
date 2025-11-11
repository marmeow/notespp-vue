<script setup></script>

<template>
  <div class="search-tool">
    <i class="pi pi-search"></i>
    <input type="text" v-model="input" placeholder="Search for anything..." />
  </div>
</template>

<style scoped>
div {
  display: flex;
}

input:focus {
  outline: none;
}

input::placeholder {
  opacity: 1;
  color: var(--color-secondary);
}

.pi {
  color: var(--color-secondary);
  font-size: 1.5rem;
  font-weight: bold;
  display: flex;
  align-items: center;
}

input {
  border: none;
  font-size: 1.125rem;
  margin-left: 1rem;
  color: #575757;
  width: 100%;
  background-color: white;
}
</style>
