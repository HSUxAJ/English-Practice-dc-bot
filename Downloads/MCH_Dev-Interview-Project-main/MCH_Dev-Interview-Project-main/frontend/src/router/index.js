import { createRouter, createWebHashHistory } from "vue-router";
import Introduction from "../views/Introduction.vue";
import HistoricalWebsites from "../views/HistoricalWebsites.vue";

const routes = [
  { path: "/", name: "Introduction", component: Introduction },
  {
    path: "/historical-websites",
    name: "HistoricalWebsites",
    component: HistoricalWebsites,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
