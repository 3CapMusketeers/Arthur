import Vue from "vue"
import store from "./store";
import router from "./router";
import App from "./App.vue";

//Packages
///Bootstrap
import {BootstrapVue, BootstrapVueIcons} from 'bootstrap-vue'

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);


// import 'bootstrap/dist/css/bootstrap.css';
// import 'bootstrap-vue/dist/bootstrap-vue.css';

import './assets/style.scss';

// Vue.component('main-comment', Comment)

new Vue({
  store,
  router: router,
  render: h => h(App)
}).$mount('#app');
