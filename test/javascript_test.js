import { createSSRApp } from "vue";
import App from "./App.vue";
import router from "./router";
import DynamicLink from "./components/logic/DynamicLink.vue"
import VueAxios from "vue-axios"
import axios from "axios"

import "./assets/css/main.css";

const app = createSSRApp(App);

app.component('DynamicLink', DynamicLink)

app.use(VueAxios, axios);

app.use(router);

app.mount("#app");

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
      children: [
        { path: '', component: HomeView, alias: ['/company'] },
      ],
    },]})
