import { createApp } from "vue";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import App from "./App.vue";

// Importar iconos
import "primeicons/primeicons.css";
import "@fortawesome/fontawesome-free/css/all.css";

const app = createApp(App);
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});
app.mount("#app");
