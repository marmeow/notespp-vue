import { createApp } from "vue";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import App from "./App.vue";

// Importar iconos
import "bootstrap-icons/font/bootstrap-icons.css";
import "primeicons/primeicons.css";
import "@fortawesome/fontawesome-free/css/all.css";


import ToastService from 'primevue/toastservice'

const app = createApp(App);
app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
});
app.use(ToastService); 
app.mount("#app");
