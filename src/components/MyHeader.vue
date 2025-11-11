<script setup>
import { ref, onMounted, onUnmounted } from "vue";
import SearchBar from "./SearchBar.vue";
import UserProfile from "./UserProfile.vue";

const query = ref("");
const isLaptop = ref(window.innerWidth <= 1080);
const isMobile = ref(window.innerWidth <= 480);

function handleResize() {
  isLaptop.value = window.innerWidth <= 1080;
  isMobile.value = window.innerWidth <= 480;
}
onMounted(() => window.addEventListener("resize", handleResize));
onUnmounted(() => window.removeEventListener("resize", handleResize));
</script>

<template>
  <header class="flex">
    <div class="header-left flex">
      <div class="header-title flex" v-if="!isMobile">
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
  padding: 1rem 2rem;
  background: white;
  border-bottom: var(--border);
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 2rem;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 2rem;
  flex: 1;
}

.header-title {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.header-title h1 {
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
}

.header-actions button {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.user-menu {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  position: relative;
}

.user-menu img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.status-dot {
  width: 10px;
  height: 10px;
  background: #22c55e;
  border-radius: 50%;
  position: absolute;
  left: 30px;
  top: 30px;
  border: 2px solid white;
}

.user-info {
  display: flex;
  flex-direction: column;
}

.user-name {
  font-weight: 600;
  color: var(--color-accent);
  margin: 0;
  font-size: 0.875rem;
}

.user-email {
  color: var(--color-secondary);
  margin: 0;
  font-size: 0.75rem;
}

.dropdown {
  position: relative;
}

.dropbtn {
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.dropdown-content {
  display: none;
  position: absolute;
  right: 0;
  background-color: white;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  border-radius: 0.5rem;
  padding: 0.5rem;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown-content button {
  width: 100%;
  padding: 0.75rem;
  border: none;
  background: none;
  cursor: pointer;
  text-align: left;
  border-radius: 0.25rem;
}

.dropdown-content button:hover {
  background-color: var(--color-bg-light);
}

/* Responsive - ocultar botones en desktop, mostrar en dropdown */
@media (min-width: 768px) {
  .header-actions {
    display: flex;
  }
  .dropdown-content {
    display: none !important;
  }
}

@media (max-width: 767px) {
  .header-actions {
    display: none;
  }
  .dropdown:hover .dropdown-content {
    display: block;
  }
}
</style>
