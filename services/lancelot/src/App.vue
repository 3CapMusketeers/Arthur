<template>
  <div id="app" type="dark">
    <div id="main">
      <b-navbar toggleable="lg" type="dark" variant="primary">
        <b-navbar-brand href="/">Camelot</b-navbar-brand>
        <b-navbar-nav>
        <span v-if="isAuth" class="row">
          <b-nav-item href="#">{{ username }}</b-nav-item>
          <b-nav-item href="#" :to="{ name: 'Playlist' }">Playlist</b-nav-item>
          <b-nav-item href="#" @click="logout()">Logout</b-nav-item>
        </span>
          <span v-else class="row">
          <b-nav-item :to="{ name: 'Login' }"> Login</b-nav-item>

        </span>
        </b-navbar-nav>
      </b-navbar>
      <router-view></router-view>
      <div class="footer col d-flex justify-content-center ">
        <div>
          <h5 class="text-center pb-2">Created for:</h5>
          <img src="./assets/spotify.png" height="50" width="175"/>
          <h6 class="text-center p-3">With
            <b-icon icon="heart-fill"></b-icon>
            in UPRM
          </h6>
        </div>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import {Component, Vue} from "vue-property-decorator";

@Component({
  components: {},
  computed: {
    isAuth () {
      return this.$store.getters.authenticated;
    },
    username () {
      return this.$store.getters.username;
    }
  }
})
export default class Login extends Vue {
  logout() {
    this.$store.commit('logout');
  }
}
</script>
<style scoped type="scss">
</style>
