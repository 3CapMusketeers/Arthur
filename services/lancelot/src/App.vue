<template>
  <div id="app" type="dark">
    <b-navbar toggleable="lg" type="dark" variant="primary">
      <b-navbar-brand href="#">Camelot</b-navbar-brand>
    </b-navbar>
    <router-view></router-view>
    <div class="col d-flex justify-content-center ">
      <div>
        <h5 class="text-center pb-2">Created for:</h5>
        <img src="./assets/spotify.png" height="50" width="175"/>
        <h6 class="text-center p-3">With <b-icon icon="heart-fill"></b-icon> in UPRM</h6>
      </div>
    </div>
  </div>
</template>
<script lang="ts">
import { Component, Vue } from "vue-property-decorator";

@Component({
  components: {}
})
export default class Login extends Vue {}
</script>
<style scoped type="scss">
</style>
