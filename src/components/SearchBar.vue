<script setup>
import IconField from 'primevue/iconfield';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
</script>

<template>
  <div class="search-tool flex">
    <IconField>
      <InputIcon class="pi pi-search"/>
      <InputText v-model="value1" placeholder="Search for anything..." size="large" />
    </IconField>
  </div>
</template>

<style scoped>

.p-inputtext.p-component {
  background-color: white;
  outline: none;
  border: none;
  box-shadow: none;
  color: var(--color-secondary);
  display: flex;
  align-items: center;
}

.pi-search {
  font-weight: bold;
  font-size: 1.250rem !important;
  color: var(--color-secondary);
}

@media (max-width: 480px) {
  .pi-search {
    font-size: 1.250rem;
  }

  input {
    margin-left: 0.250rem;
    font-size: 1.125rem;
  }
}
</style>
