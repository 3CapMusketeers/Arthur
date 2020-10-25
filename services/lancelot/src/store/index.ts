import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    tracks: []
  },
  getters: {
    tracks: state => {
      return state.tracks;
    }
  },
  mutations: {
    changeTracks(state, payload) {
      state.tracks = payload
    }
  },
  actions: {},
  modules: {}
});
