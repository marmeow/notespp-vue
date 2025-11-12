<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import SearchBar from "./SearchBar.vue";
import UserProfile from "./UserProfile.vue";

const query = ref("");
const isLaptop = ref(window.innerWidth <= 1080);


function handleResize() {
  console.log("innerWidth:", window.innerWidth);
  isLaptop.value = window.innerWidth <= 1080;
}

onMounted(() => {
  handleResize(); // asegura que se calcule al cargar
  window.addEventListener("resize", handleResize);
});

onUnmounted(() => window.removeEventListener("resize", handleResize));
</script>

<template>
  <header class="flex">
    <div class="header-title-search flex">
      <div class="header-title flex">
        <i class="fa-solid fa-angles-left fa-xl text-secondary"></i>
        <h1>Note</h1>
      </div>
      <SearchBar />
    </div>

    <!-- Iconos solo en escritorio -->
    <div class="header-actions flex" v-if="!isLaptop">
      <button aria-label="Tasques">
        <i class="fa-solid fa-clipboard-check fa-xl text-secondary"></i>
      </button>
      <button aria-label="Notificacions">
        <i class="fa-solid fa-bell text-secondary fa-xl"></i>
      </button>
    </div>
    <UserProfile />
  </header>
</template>

<style scoped>
header {
  width: 100%;
  background: white;
  border-bottom: var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  grid-area: header;

}

.header-title-search {
  display: flex;
  align-items: center;
  gap: 2rem;
  flex: 1;
  padding: 1rem;
}

.header-title {
  display: flex;
  align-items: center;
  gap: 1rem;
}

h1 {
  margin: 0;
  color: var(--color-accent);
  font-size: 1.875rem;
}

.text-secondary {
  color: var(--color-secondary);
}

.p-input-icon-left {
  width: 100%;
}

.header-actions {
  display: flex;
  align-items: center;
  padding: 1rem;
  font-size: 1rem ;

}

button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
 
}


@media (max-width: 480px) {
  .header-title {
    display: none;
  }

  .header-title-search {
    padding: 1rem;
  }

}
</style>
