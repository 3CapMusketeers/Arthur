import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Login from "@/views/Login.vue";
import Playlist from "@/views/Playlist.vue";
import NotFound from "@/views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/playlist",
    name: "Playlist",
    component: Playlist
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  { path: '*', component: NotFound },
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

export default router;

router.beforeEach((to, from, next) => {
  const publicPages = ['/spotifyCallback', '/', '/login', ];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('spotify_token');

  // trying to access a restricted page + not logged in
  // redirect to login page
  if (authRequired && !loggedIn) {
    next('/login');
  } else {
    next();
  }
});
