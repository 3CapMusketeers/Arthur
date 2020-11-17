import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
});

export default new Vuex.Store({
  state: {
    tracks: [],
    user: {
      username: "",
      token: "",
      isAuth: false
    },
  },
  getters: {
    tracks: state => {
      return state.tracks;
    },
    userToken: state => {
      return state.user.token;
    },
    username: state => {
      return state.user.username
    }
  },
  mutations: {
    changeTracks(state, payload) {
      state.tracks = payload;
    },
    login(state, payload) {
      state.isAuth = true;
      state.user.username = payload.username;
      state.user.token = payload.token;
    },
    logout(state) {
      state.isAuth = false;
      state.user.username = "";
      state.user.token = "";
    }

  },
  actions: {},
  modules: {},
  plugins: [vuexLocal.plugin],
});
